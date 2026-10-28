#!/usr/bin/env python3
"""OpenSCCT-Content tools: pack converted content into release archives, publish them, verify the index.

Python 3.10+, standard library only. Run from anywhere; paths default to this repository.

    occ.py pack     --build <svmbuild out>[=<maps root>] ... --install <Versus folder>
    occ.py publish  [--dry-run] [--no-commit]
    occ.py verify   [--remote]
    occ.py readme

docs/PUBLISHING.md has the whole procedure, docs/FORMAT.md the formats.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX = REPO_ROOT / "index.json"
SCHEMA = REPO_ROOT / "schema" / "index.schema.json"
README = REPO_ROOT / "README.md"
STAGING = REPO_ROOT / "staging"
OUT = STAGING / "out"
PLAN = OUT / "plan.json"

GITHUB_REPO = "Lumbridge/OpenSCCT-Content"
SOURCE_REPO = "Lumbridge/SCCT-Maps"
INDEX_FORMAT = "openscct.content"
INDEX_FORMAT_VERSION = 1
ASSET_LIMIT = 2 * 1024 ** 3  # GitHub release assets: 2 GiB per file

CATEGORIES = ["stock", "original", "community", "enhanced", "recovered", "ports"]
CATEGORY_TITLES = {
    "stock": "Stock",
    "original": "Original",
    "community": "Community",
    "enhanced": "Enhanced",
    "recovered": "Recovered",
    "ports": "Ports",
}
CATEGORY_NOTES = {
    "stock": "Ubisoft's maps: the Steam install's retail set and the SCCT Versus 4.0 maps",
    "original": "New maps made for SCCT Versus (SCCT-Maps `release/`)",
    "community": "The community map pack",
    "enhanced": "Edited versions of existing maps",
    "recovered": "Existing maps rebuilt as editable maps",
    "ports": "Maps ported from other games",
}
# SCCT-Maps catalogue categories (OpenScct.Maps MapIndexParser) -> ours.
SCCT_MAPS_CATEGORY = {
    "stock": "stock", "original": "original", "community": "community",
    "enhanced": "enhanced", "recovered": "recovered", "ports": "ports",
}
# Not offered: the menu maps are part of the game's own menus, not maps to play.
MENU_MAPS = {"entry", "lobby"}

SHARED_PACKS = [
    # id, title, contents (relative to shared/), hashes the maps' requires name: pack -> file under shared/
    ("core", "Shared game data", ["classes.json", "render", "fx", "ui", "maps"], {"classes": "classes.json"}),
    ("chars", "Characters", ["chars"], {}),
    ("audio", "Shared sound banks", ["audio"], {"audio": "audio/audio.json"}),
]

STORED_EXT = {".png", ".ogg", ".jpg", ".jpeg"}
ZIP_TIME = (1980, 1, 1, 0, 0, 0)

MODE_ORDER = ["Story", "DiskHunt", "Deathmatch", "MercDeathmatch", "Extraction", "Sabotage", "Neutralization"]
# EGameMode values (OpenScct.Core Core.Enums.g.cs).
GM = {"Extraction": 1, "Sabotage": 2, "Neutralization": 3, "DiskHunt": 4, "Story": 5, "Deathmatch": 6,
      "MercDeathmatch": 7}
IMAGE_KINDS = ["menu", "briefing", "loading-spy", "loading-merc"]


# ---- small helpers ---------------------------------------------------------------------------------------------

def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(path: Path) -> str:
    size = path.stat().st_size
    h = hashlib.sha1(f"blob {size}\0".encode())
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_json(path: Path):
    with open(path, "rb") as f:
        data = f.read()
    if data.startswith(b"\xef\xbb\xbf"):
        data = data[3:]
    return json.loads(data.decode("utf-8"))


def dump_json(obj) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, path)


def load_index() -> dict:
    if INDEX.is_file():
        return load_json(INDEX)
    return {"format": INDEX_FORMAT, "formatVersion": INDEX_FORMAT_VERSION, "updated": None, "svmapFormat": None,
            "shared": [], "maps": []}


def bump(version: str | None, base: str = "1.0.0") -> str:
    """The next version after `version` (last number + 1), or `base` for a new pack."""
    if not version:
        return base
    parts = version.split(".")
    parts[-1] = str(int(parts[-1]) + 1)
    return ".".join(parts)


def safe_rel(rel: str) -> str:
    """A relative archive path with '/', refusing '..', drive letters and leading '/'."""
    rel = rel.replace("\\", "/")
    if not rel or rel.startswith("/") or re.match(r"^[A-Za-z]:", rel) or any(p in ("", ".", "..") for p in rel.split("/")):
        raise ValueError(f"bad archive path: {rel!r}")
    return rel


def tree_hash(rows: list[tuple[str, str]]) -> str:
    """sha256 over sorted 'path\\tsha256\\n' lines: changes when any file of a pack changes."""
    text = "".join(f"{p}\t{h}\n" for p, h in sorted(rows))
    return sha256_bytes(text.encode("utf-8"))


def asset_name(text: str) -> str:
    """A release asset file name: letters, digits, '.', '-' and '_' only."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", text)


# ---- deterministic zips ----------------------------------------------------------------------------------------

def write_zip(target: Path, entries: list[tuple[str, Path | bytes]]) -> None:
    """A zip with the entries sorted by path, fixed timestamps and attributes, stored for already compressed files
    (.png, .ogg, .jpg) and deflated at level 9 otherwise. The same inputs give the same bytes."""
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_name(target.name + ".tmp")
    seen = set()
    with zipfile.ZipFile(tmp, "w", allowZip64=True) as zf:
        for rel, src in sorted(entries, key=lambda e: e[0]):
            rel = safe_rel(rel)
            if rel.lower() in seen:
                raise ValueError(f"duplicate archive path: {rel}")
            seen.add(rel.lower())
            zi = zipfile.ZipInfo(rel, date_time=ZIP_TIME)
            zi.create_system = 0
            zi.external_attr = 0
            stored = Path(rel).suffix.lower() in STORED_EXT
            zi.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
            if not stored:
                zi._compresslevel = 9  # zipfile has no public per-entry level for open(); writestr uses this too
            size = len(src) if isinstance(src, bytes) else src.stat().st_size
            zi.file_size = size
            with zf.open(zi, "w", force_zip64=size > 0x7FFF0000) as dst:
                if isinstance(src, bytes):
                    dst.write(src)
                else:
                    with open(src, "rb") as f:
                        for block in iter(lambda: f.read(1 << 20), b""):
                            dst.write(block)
    os.replace(tmp, target)


def check_zip(path: Path) -> list[str]:
    """Problems with an archive's paths (the rules a client enforces)."""
    problems = []
    with zipfile.ZipFile(path) as zf:
        for n in zf.namelist():
            try:
                safe_rel(n)
            except ValueError as e:
                problems.append(str(e))
    return problems


# ---- reading a build -------------------------------------------------------------------------------------------

def mode_list(map_dir: Path) -> list[str]:
    """The modes a map plays, as OpenSCCT's MapCatalog.ModesOf decides them from sim/gameplay.json."""
    path = map_dir / "sim" / "gameplay.json"
    if not path.is_file():
        return []
    g = load_json(path)
    spy = merc = mdm = 0
    for a in g.get("actors") or []:
        cls = str(a.get("class") or "")
        if not cls.endswith("PlayerStart"):
            continue
        props = a.get("props") or {}
        if props.get("bMercDeathMatchStart") is True:
            mdm += 1
        elif props.get("TeamNumber") == 1:
            merc += 1
        else:
            spy += 1
    missions: dict[int, dict] = {}
    for m in g.get("missionTree") or []:
        gm = int(m.get("gameMode") or 0)
        missions.setdefault(gm, {
            "objectives": len(m.get("objectives") or []),
            "disks": len(m.get("triggers") or []),
        })
    settings = {int(v.get("GameModeId") or 0) for v in (g.get("mapSettings") or {}).values() if isinstance(v, dict)}
    out = []
    for name in MODE_ORDER:
        gm = GM[name]
        mission = missions.get(gm)
        if name in ("Extraction", "Sabotage", "Neutralization") and mission is None and gm not in settings:
            continue
        if name == "Story":
            ok = bool(mission and mission["objectives"] > 0)
        elif name == "DiskHunt":
            ok = bool(mission and mission["disks"] > 0)
        elif name == "Deathmatch":
            ok = spy > 0 and merc > 0
        elif name == "MercDeathmatch":
            ok = spy + merc + mdm > 0
        else:
            ok = bool(mission and mission["objectives"] > 0) and spy > 0 and merc > 0
        if ok:
            out.append(name)
    return out


def map_files(map_dir: Path) -> list[tuple[str, Path]]:
    rows = []
    for p in sorted(map_dir.rglob("*")):
        if p.is_file():
            rows.append((p.relative_to(map_dir).as_posix(), p))
    return rows


def catalog_entry(build: Path, code: str, name: str) -> tuple[bytes, list[tuple[str, Path]]]:
    """catalog/entry.json and catalog/images/*.png for a map, from the build's shared/maps."""
    images_dir = None
    cat_path = build / "shared" / "maps" / "catalog.json"
    images = {}
    files = []
    if cat_path.is_file():
        cat = load_json(cat_path)
        entry = None
        for k, v in (cat.get("images") or {}).items():
            if k.lower() == code.lower():
                entry = v
                break
        if entry:
            for kind in IMAGE_KINDS:
                rel = entry.get(kind)
                if not rel:
                    continue
                src = build / "shared" / "maps" / rel
                if src.is_file():
                    images[kind] = f"images/{kind}.png"
                    files.append((f"catalog/images/{kind}.png", src))
        if images_dir is None:
            folder = build / "shared" / "maps" / "images" / code
            if folder.is_dir() and not images:
                for kind in IMAGE_KINDS:
                    src = folder / f"{kind}.png"
                    if src.is_file():
                        images[kind] = f"images/{kind}.png"
                        files.append((f"catalog/images/{kind}.png", src))
    doc = {"code": code, "name": name, "images": images}
    return (json.dumps(doc, indent=2, ensure_ascii=False) + "\n").encode("utf-8"), files


def title_case(upper: str) -> str:
    """MapCatalog.TitleCase: each word capitalised (ENHANCED ORPHANAGE 3V3 -> Enhanced Orphanage 3v3)."""
    return " ".join(w[:1].upper() + w[1:].lower() for w in upper.split(" ") if w)


def map_title(build: Path, map_dir: Path, code: str, manifest: dict, scct_maps_name: str | None) -> str:
    """The name the game shows (MapCatalog.FolderEntry): the shared catalog's name, else SMapSettings.MapName in title
    case, else the manifest's title; then SCCT-Maps' name; then the code."""
    name = shared_catalog_name(build, code)
    if name:
        return name
    info = map_dir / "ui" / "mapinfo.json"
    if info.is_file():
        map_name = str(load_json(info).get("MapName") or "").strip()
        if map_name and map_name != "None":
            return title_case(map_name)
    title = str(manifest.get("title") or "").strip()
    if title and title.lower() not in (code.lower(), "untitled"):
        return title
    return scct_maps_name or code


def shared_catalog_name(build: Path, code: str) -> str | None:
    cat_path = build / "shared" / "maps" / "catalog.json"
    if not cat_path.is_file():
        return None
    for k, v in (load_json(cat_path).get("names") or {}).items():
        if k.lower() == code.lower() and v:
            return str(v)
    return None


class Origins:
    """Where each map file came from: the install, or a map of the SCCT-Maps catalogue downloaded into a maps root
    (OpenScct.Maps MapLibrary's installed.json)."""

    def __init__(self, install: Path | None, roots: list[Path], catalog: dict | None):
        self.install = install
        self.by_root: dict[str, dict[str, dict]] = {}
        self.catalog = {m["Id"]: m for m in (catalog or {}).get("Maps", [])}
        self.commit = (catalog or {}).get("Commit")
        for root in roots:
            table: dict[str, dict] = {}
            manifest = root / "installed.json"
            if manifest.is_file():
                for m in load_json(manifest):
                    m = {k[:1].upper() + k[1:]: v for k, v in m.items()}  # installed.json is camelCase
                    codes = [c.lower() for c in m.get("Codes", [])]
                    for f in m.get("Files", []):
                        dest = f.get("path") or f.get("Destination")
                        if dest and dest.lower().startswith("packages/maps/") and dest.lower().endswith(".sdc"):
                            code = Path(dest).stem.lower()
                            if code in codes:
                                table[code] = {"map": m, "file": f}
            self.by_root[str(root)] = table

    def find(self, code: str, root: Path | None, original_sha256: str) -> dict:
        """{category, sourceName, source{...}} for a converted map."""
        if self.install is not None:
            p = self.install / "Packages" / "Maps" / f"{code}.sdc"
            if p.is_file() and sha256_file(p) == original_sha256:
                return {"category": "stock", "name": None,
                        "source": {"kind": "install", "path": f"Packages/Maps/{p.name}", "sha256": original_sha256}}
        if root is not None:
            hit = self.by_root.get(str(root), {}).get(code.lower())
            if hit:
                m, f = hit["map"], hit["file"]
                cat = SCCT_MAPS_CATEGORY.get(str(m.get("Category", "")).lower())
                if cat is None:
                    raise ValueError(f"{code}: unknown SCCT-Maps category {m.get('Category')!r}")
                src = f.get("source") or f.get("Source")
                source = {"kind": "repo", "repo": SOURCE_REPO, "commit": m.get("Commit") or self.commit,
                          "path": src, "sha256": original_sha256, "mapId": m.get("Id")}
                if src and src.startswith("releases/download/"):
                    source["kind"] = "release"
                return {"category": cat, "name": m.get("Name"), "source": source}
        raise ValueError(f"{code}: not in the install and not in a downloaded maps root")


# ---- pack ------------------------------------------------------------------------------------------------------

def cmd_pack(args) -> None:
    index = load_index()
    old_maps = {m["id"]: m for m in index.get("maps", [])}
    old_shared = {s["id"]: s for s in index.get("shared", [])}
    builds: list[tuple[Path, Path | None]] = []
    for spec in args.build:
        build, _, root = spec.partition("=")
        builds.append((Path(build).resolve(), Path(root).resolve() if root else None))
    for b, _ in builds:
        if not (b / "svmap").is_dir() or not (b / "shared").is_dir():
            die(f"{b} is not a svmbuild output folder (svmap/ and shared/)")
    catalog = load_json(Path(args.catalog)) if args.catalog else None
    origins = Origins(Path(args.install) if args.install else None, [r for _, r in builds if r], catalog)
    OUT.mkdir(parents=True, exist_ok=True)
    only = {c.lower() for c in args.maps.split(",")} if args.maps else None
    plan = {"created": _now(), "openscct": args.openscct, "generator": args.generator, "shared": [], "maps": [],
            "skipped": [], "unchanged": []}

    # Shared packs: from the first build; every other build must name the same requires hashes.
    first = builds[0][0]
    for pid, title, contents, hash_files in SHARED_PACKS:
        hashes = {k: sha256_file(first / "shared" / rel) for k, rel in hash_files.items()}
        for b, _ in builds[1:]:
            for k, rel in hash_files.items():
                other = sha256_file(b / "shared" / rel)
                if other != hashes[k]:
                    die(f"{b}: shared {rel} differs from {first}'s ({other[:12]} vs {hashes[k][:12]}); build every "
                        "folder from the same install and builder")
        entries: list[tuple[str, Path]] = []
        for c in contents:
            p = first / "shared" / c
            if p.is_file():
                entries.append((c, p))
            elif p.is_dir():
                entries += [(f"{c}/{q.relative_to(p).as_posix()}", q) for q in sorted(p.rglob("*")) if q.is_file()]
            else:
                die(f"{p} is missing")
        rows = [(rel, sha256_file(p)) for rel, p in entries]
        pack_sha = tree_hash(rows)
        old = old_shared.get(pid)
        if old and old.get("treeSha256") == pack_sha and not args.force:
            plan["unchanged"].append(pid)
            print(f"unchanged shared {pid} {old['version']}")
            continue
        base = f"{args.openscct}.1"
        version = base if not old or not old.get("version", "").startswith(args.openscct + ".") else bump(old["version"])
        name = f"shared-{pid}-{version}.zip"
        target = OUT / name
        print(f"pack shared {pid} {version}: {len(entries)} files")
        write_zip(target, entries)
        plan["shared"].append({
            "id": pid, "title": title, "version": version, "contents": contents, "hashes": hashes,
            "treeSha256": pack_sha, "files": len(entries), "generator": args.generator,
            "archive": {"file": name, "size": target.stat().st_size, "sha256": sha256_file(target)},
        })

    # Maps: every svmap folder of every build.
    seen_ids: dict[str, Path] = {}
    for build, root in builds:
        for map_dir in sorted((build / "svmap").iterdir(), key=lambda p: p.name.lower()):
            if not (map_dir / "manifest.json").is_file():
                continue
            code = map_dir.name
            if only is not None and code.lower() not in only:
                continue
            if code.lower() in MENU_MAPS and not args.menu_maps:
                continue
            manifest_bytes = (map_dir / "manifest.json").read_bytes()
            manifest = json.loads(manifest_bytes.decode("utf-8-sig"))
            if manifest.get("format") != "svmap":
                plan["skipped"].append({"code": code, "reason": "manifest is not svmap"})
                continue
            try:
                origin = origins.find(code, root, manifest["source"]["original"]["sha256"])
            except (ValueError, KeyError) as e:
                plan["skipped"].append({"code": code, "build": str(build), "reason": str(e)})
                print(f"skip {code}: {e}")
                continue
            mid = f"{origin['category']}/{code}"
            if mid in seen_ids:
                plan["skipped"].append({"code": code, "reason": f"{mid} also built in {seen_ids[mid]}"})
                continue
            seen_ids[mid] = build
            # Every listed file must be there with its size and hash.
            files = map_files(map_dir)
            on_disk = {rel: p for rel, p in files}
            bad = []
            for rel, meta in manifest.get("files", {}).items():
                p = on_disk.get(rel)
                if p is None or p.stat().st_size != meta["size"]:
                    bad.append(rel)
            if bad:
                plan["skipped"].append({"code": code, "reason": f"files missing or wrong size: {bad[:5]}"})
                print(f"skip {code}: {len(bad)} files missing or wrong size")
                continue
            title = map_title(build, map_dir, code, manifest, origin.get("name"))
            entry_json, cat_files = catalog_entry(build, code, title)
            listed = set(manifest.get("files", {}))
            rows = [(rel, manifest["files"][rel]["sha256"]) if rel in listed else (rel, sha256_file(p))
                    for rel, p in files]
            rows.append(("catalog/entry.json", sha256_bytes(entry_json)))
            rows += [(rel, sha256_file(p)) for rel, p in cat_files]
            pack_sha = tree_hash(rows)
            manifest_sha = sha256_bytes(manifest_bytes)
            old = old_maps.get(mid)
            if old and old.get("treeSha256") == pack_sha and old.get("manifestSha256") == manifest_sha and not args.force:
                plan["unchanged"].append(mid)
                continue
            version = bump(old.get("version") if old else None)
            stem = asset_name(f"{origin['category']}-{code}-{version}")
            full_entries: list[tuple[str, Path | bytes]] = list(files) + [("catalog/entry.json", entry_json)] + cat_files
            sim_entries: list[tuple[str, Path | bytes]] = [(rel, p) for rel, p in files
                                                           if rel == "manifest.json" or rel.startswith("sim/")]
            print(f"pack {mid} {version}: {len(full_entries)} files")
            full = OUT / f"{stem}.zip"
            sim = OUT / f"{stem}-sim.zip"
            write_zip(full, full_entries)
            write_zip(sim, sim_entries)
            for z in (full, sim):
                if z.stat().st_size >= ASSET_LIMIT:
                    die(f"{z.name} is over GitHub's 2 GiB asset limit")
            sim_hash = manifest["hashes"]["sim"].lower()
            fmt = str(manifest.get("formatVersion", ""))
            plan["maps"].append({
                "id": mid, "code": code, "title": title, "category": origin["category"], "version": version,
                "modes": [] if code.lower() in MENU_MAPS else mode_list(map_dir), "contentHash": sim_hash[:16], "manifestSha256": manifest_sha,
                "treeSha256": pack_sha, "svmapFormatVersion": fmt, "requires": manifest.get("requires", []),
                "source": origin["source"], "generator": args.generator,
                "unlisted": sorted(rel for rel, _ in files if rel != "manifest.json" and rel not in listed),
                "full": {"file": full.name, "size": full.stat().st_size, "sha256": sha256_file(full)},
                "sim": {"file": sim.name, "size": sim.stat().st_size, "sha256": sha256_file(sim)},
            })
    write_text(PLAN, dump_json(plan))
    total = sum(m["full"]["size"] + m["sim"]["size"] for m in plan["maps"]) + \
        sum(s["archive"]["size"] for s in plan["shared"])
    print(f"\n{len(plan['maps'])} maps and {len(plan['shared'])} shared packs packed ({total / 1e9:.2f} GB), "
          f"{len(plan['unchanged'])} unchanged, {len(plan['skipped'])} skipped. Plan: {PLAN}")


def _now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


# ---- publish ---------------------------------------------------------------------------------------------------

def gh(*args: str, check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["gh", *args], check=check, capture_output=capture, text=True)


def release_tag(date: str | None) -> str:
    base = "content-" + (date or _dt.datetime.now(_dt.timezone.utc).strftime("%Y.%m.%d"))
    existing = set(gh("release", "list", "--repo", GITHUB_REPO, "--limit", "1000", "--json", "tagName",
                      "--jq", ".[].tagName").stdout.split())
    if base not in existing:
        return base
    n = 2
    while f"{base}-{n}" in existing:
        n += 1
    return f"{base}-{n}"


def download_url(tag: str, name: str) -> str:
    return f"https://github.com/{GITHUB_REPO}/releases/download/{tag}/{name}"


def build_index(index: dict, plan: dict, tag: str) -> dict:
    shared = {s["id"]: s for s in index.get("shared", [])}
    for s in plan["shared"]:
        shared[s["id"]] = {
            "id": s["id"], "title": s["title"], "version": s["version"], "contents": s["contents"],
            "hashes": s["hashes"], "treeSha256": s["treeSha256"], "generator": s["generator"],
            "download": {"url": download_url(tag, s["archive"]["file"]), "size": s["archive"]["size"],
                         "sha256": s["archive"]["sha256"]},
        }
    order = {pid: i for i, (pid, *_rest) in enumerate(SHARED_PACKS)}
    maps = {m["id"]: m for m in index.get("maps", [])}
    for m in plan["maps"]:
        maps[m["id"]] = {
            "id": m["id"], "code": m["code"], "title": m["title"], "category": m["category"], "version": m["version"],
            "modes": m["modes"], "contentHash": m["contentHash"], "manifestSha256": m["manifestSha256"],
            "treeSha256": m["treeSha256"], "requires": m["requires"], "source": m["source"],
            "generator": m["generator"],
            "full": {"url": download_url(tag, m["full"]["file"]), "size": m["full"]["size"],
                     "sha256": m["full"]["sha256"]},
            "sim": {"url": download_url(tag, m["sim"]["file"]), "size": m["sim"]["size"],
                    "sha256": m["sim"]["sha256"]},
        }
    formats = {m["svmapFormatVersion"] for m in plan["maps"]}
    svmap = index.get("svmapFormat")
    if formats:
        majors = {".".join(f.split(".")[:2]) for f in formats}
        if len(majors) != 1:
            die(f"maps of several svmap formats in one publish: {sorted(formats)}")
        svmap = majors.pop()
    cat_order = {c: i for i, c in enumerate(CATEGORIES)}
    return {
        "format": INDEX_FORMAT,
        "formatVersion": INDEX_FORMAT_VERSION,
        "updated": _now(),
        "svmapFormat": svmap,
        "shared": sorted(shared.values(), key=lambda s: order.get(s["id"], 99)),
        "maps": sorted(maps.values(), key=lambda m: (cat_order.get(m["category"], 99), m["code"].lower(), m["id"])),
    }


def cmd_publish(args) -> None:
    if not PLAN.is_file():
        die("no staging/out/plan.json: run pack first")
    plan = load_json(PLAN)
    files = [s["archive"]["file"] for s in plan["shared"]] + \
        [m[k]["file"] for m in plan["maps"] for k in ("full", "sim")]
    if not files:
        print("nothing new to publish")
        return
    for name in files:
        p = OUT / name
        if not p.is_file():
            die(f"{p} is missing")
    tag = args.tag or release_tag(args.date)
    index = load_index()
    new_index = build_index(index, plan, tag)
    problems = validate_index(new_index)
    if problems:
        die("the new index is not valid:\n  " + "\n  ".join(problems))
    total = sum((OUT / f).stat().st_size for f in files)
    print(f"release {tag}: {len(files)} archives, {total / 1e9:.2f} GB")
    if args.dry_run:
        write_text(STAGING / "index.preview.json", dump_json(new_index))
        print(f"dry run: index written to {STAGING / 'index.preview.json'}")
        return

    existing = gh("release", "view", tag, "--repo", GITHUB_REPO, "--json", "assets", check=False)
    if existing.returncode != 0:
        notes = release_notes(plan, tag)
        notes_file = STAGING / f"notes-{tag}.md"
        write_text(notes_file, notes)
        gh("release", "create", tag, "--repo", GITHUB_REPO, "--title", tag, "--notes-file", str(notes_file),
           "--target", "main", "--latest")
        uploaded = {}
    else:
        uploaded = {a["name"]: a["size"] for a in json.loads(existing.stdout).get("assets", [])}
    pending = [f for f in files if uploaded.get(f) != (OUT / f).stat().st_size]
    for name in [f for f in files if f in uploaded and uploaded[f] != (OUT / f).stat().st_size]:
        gh("release", "delete-asset", tag, name, "--repo", GITHUB_REPO, "--yes")
    batch: list[str] = []
    batch_bytes = 0
    for i, name in enumerate(pending):
        batch.append(str(OUT / name))
        batch_bytes += (OUT / name).stat().st_size
        if len(batch) >= 20 or batch_bytes > 2_000_000_000 or i == len(pending) - 1:
            print(f"upload {i + 1}/{len(pending)} ({batch_bytes / 1e6:.0f} MB)", flush=True)
            for attempt in range(3):
                r = gh("release", "upload", tag, *batch, "--repo", GITHUB_REPO, "--clobber", check=False,
                       capture=False)
                if r.returncode == 0:
                    break
                print(f"upload failed (attempt {attempt + 1}), retrying", flush=True)
            else:
                die("upload failed; run publish again with --tag " + tag + " to resume")
            batch, batch_bytes = [], 0

    # Every asset must be there with its size before the index points at it.
    assets = {a["name"]: a["size"] for a in json.loads(
        gh("release", "view", tag, "--repo", GITHUB_REPO, "--json", "assets").stdout)["assets"]}
    missing = [f for f in files if assets.get(f) != (OUT / f).stat().st_size]
    if missing:
        die(f"{len(missing)} assets missing after upload, e.g. {missing[:3]}; run publish again with --tag {tag}")
    write_text(INDEX, dump_json(new_index))
    write_readme(new_index)
    write_text(STAGING / f"published-{tag}.json", dump_json({"tag": tag, "plan": plan}))
    print(f"index.json written ({len(new_index['maps'])} maps, {len(new_index['shared'])} shared packs)")
    if not args.no_commit:
        subprocess.run(["git", "-C", str(REPO_ROOT), "add", "index.json", "README.md"], check=True)
        subprocess.run(["git", "-C", str(REPO_ROOT), "commit", "-m",
                        f"Publish {tag}: {len(plan['maps'])} maps, {len(plan['shared'])} shared packs"], check=True)
        if not args.no_push:
            subprocess.run(["git", "-C", str(REPO_ROOT), "push"], check=True)


def release_notes(plan: dict, tag: str) -> str:
    lines = [f"OpenSCCT converted content, {tag}.", "",
             f"Built with {plan.get('generator') or 'svmbuild'}. The index on `main` (`index.json`) lists every pack "
             "with its download URL, size and sha256; OpenSCCT reads it to download maps.", ""]
    if plan["shared"]:
        lines.append("Shared packs: " + ", ".join(f"{s['id']} {s['version']}" for s in plan["shared"]))
        lines.append("")
    by_cat: dict[str, list[str]] = {}
    for m in plan["maps"]:
        by_cat.setdefault(m["category"], []).append(f"{m['code']} {m['version']}")
    for c in CATEGORIES:
        if c in by_cat:
            lines.append(f"{CATEGORY_TITLES[c]} ({len(by_cat[c])}): " + ", ".join(sorted(by_cat[c], key=str.lower)))
            lines.append("")
    lines.append("Stock content is Ubisoft's. OpenSCCT is a fan project, not affiliated with or endorsed by Ubisoft.")
    return "\n".join(lines) + "\n"


# ---- verify ----------------------------------------------------------------------------------------------------

def validate_schema(value, schema: dict, root: dict, path: str, problems: list[str]) -> None:
    """A JSON Schema subset: $ref (local), type, required, properties, additionalProperties (bool), items, enum,
    pattern, minimum, minItems, uniqueItems, const."""
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/"):
            problems.append(f"{path}: unsupported $ref {ref}")
            return
        target = root
        for part in ref[2:].split("/"):
            target = target[part]
        validate_schema(value, target, root, path, problems)
        return
    types = schema.get("type")
    if types is not None:
        names = types if isinstance(types, list) else [types]
        ok = False
        for t in names:
            if (t == "object" and isinstance(value, dict)) or (t == "array" and isinstance(value, list)) or \
                    (t == "string" and isinstance(value, str)) or (t == "null" and value is None) or \
                    (t == "boolean" and isinstance(value, bool)) or \
                    (t == "integer" and isinstance(value, int) and not isinstance(value, bool)) or \
                    (t == "number" and isinstance(value, (int, float)) and not isinstance(value, bool)):
                ok = True
        if not ok:
            problems.append(f"{path}: expected {types}")
            return
    if "const" in schema and value != schema["const"]:
        problems.append(f"{path}: must be {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        problems.append(f"{path}: {value!r} not one of {schema['enum']}")
    if isinstance(value, str) and "pattern" in schema and not re.search(schema["pattern"], value):
        problems.append(f"{path}: {value!r} does not match {schema['pattern']}")
    if isinstance(value, (int, float)) and "minimum" in schema and value < schema["minimum"]:
        problems.append(f"{path}: below {schema['minimum']}")
    if isinstance(value, dict):
        for k in schema.get("required", []):
            if k not in value:
                problems.append(f"{path}: missing {k}")
        props = schema.get("properties", {})
        for k, v in value.items():
            if k in props:
                validate_schema(v, props[k], root, f"{path}.{k}", problems)
            elif isinstance(schema.get("additionalProperties"), dict):
                validate_schema(v, schema["additionalProperties"], root, f"{path}.{k}", problems)
            elif schema.get("additionalProperties") is False:
                problems.append(f"{path}: unexpected {k}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            problems.append(f"{path}: fewer than {schema['minItems']} items")
        if schema.get("uniqueItems"):
            dumped = [json.dumps(v, sort_keys=True) for v in value]
            if len(set(dumped)) != len(dumped):
                problems.append(f"{path}: items are not unique")
        if "items" in schema:
            for i, v in enumerate(value):
                validate_schema(v, schema["items"], root, f"{path}[{i}]", problems)


def validate_index(index: dict) -> list[str]:
    schema = load_json(SCHEMA)
    problems: list[str] = []
    validate_schema(index, schema, schema, "$", problems)
    ids = [m.get("id") for m in index.get("maps", [])]
    if len(set(ids)) != len(ids):
        problems.append("$.maps: duplicate ids")
    for m in index.get("maps", []):
        if m.get("id") != f"{m.get('category')}/{m.get('code')}":
            problems.append(f"{m.get('id')}: id is not <category>/<code>")
    shared_hashes = {}
    for s in index.get("shared", []):
        for k, v in (s.get("hashes") or {}).items():
            shared_hashes[k] = v
    for m in index.get("maps", []):
        for r in m.get("requires", []):
            if shared_hashes.get(r.get("pack")) != r.get("sha256"):
                problems.append(f"{m.get('id')}: requires {r.get('pack')} {str(r.get('sha256'))[:12]}, "
                                "which no shared pack in the index has")
    return problems


def cmd_verify(args) -> None:
    index = load_json(INDEX)
    problems = validate_index(index)
    downloads = [(s["id"], s["download"]) for s in index["shared"]] + \
        [(m["id"] + " full", m["full"]) for m in index["maps"]] + \
        [(m["id"] + " sim", m["sim"]) for m in index["maps"] if "sim" in m]
    checked = 0
    for what, d in downloads:
        name = d["url"].rsplit("/", 1)[-1]
        local = OUT / name
        if local.is_file():
            checked += 1
            if local.stat().st_size != d["size"]:
                problems.append(f"{what}: {name} is {local.stat().st_size} bytes, index says {d['size']}")
            elif not args.quick and sha256_file(local) != d["sha256"]:
                problems.append(f"{what}: {name} sha256 differs from the index")
            elif not args.quick:
                problems += [f"{what}: {p}" for p in check_zip(local)]
    print(f"index: {len(index['shared'])} shared packs, {len(index['maps'])} maps; "
          f"{checked}/{len(downloads)} archives checked against staging/out")
    if args.remote:
        for i, (what, d) in enumerate(downloads):
            req = urllib.request.Request(d["url"], method="HEAD", headers={"User-Agent": "OpenSCCT-Content"})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    length = r.headers.get("Content-Length")
                    if length is not None and int(length) != d["size"]:
                        problems.append(f"{what}: remote size {length}, index says {d['size']}")
            except urllib.error.URLError as e:
                problems.append(f"{what}: {d['url']}: {e}")
        print(f"remote: {len(downloads)} URLs checked")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("ok")


# ---- readme ----------------------------------------------------------------------------------------------------

def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1000 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1000
    return str(n)


def readme_tables(index: dict) -> str:
    lines = ["| Category | Maps | Download size | What |", "| --- | ---: | ---: | --- |"]
    for c in CATEGORIES:
        maps = [m for m in index["maps"] if m["category"] == c]
        if not maps:
            continue
        size = sum(m["full"]["size"] for m in maps)
        lines.append(f"| `{c}` | {len(maps)} | {human(size)} | {CATEGORY_NOTES[c]} |")
    total = sum(m["full"]["size"] for m in index["maps"])
    lines.append(f"| **All** | **{len(index['maps'])}** | **{human(total)}** | |")
    lines += ["", "| Shared pack | Version | Size | Contents |", "| --- | --- | ---: | --- |"]
    for s in index["shared"]:
        lines.append(f"| `{s['id']}` | {s['version']} | {human(s['download']['size'])} | "
                     f"{', '.join(s['contents'])} |")
    lines += ["", "<details><summary>Every map</summary>", "",
              "| Map | Code | Category | Version | Modes | Size |", "| --- | --- | --- | --- | --- | ---: |"]
    for m in index["maps"]:
        title = m.get("title", m["code"]).replace("|", "\\|")
        lines.append(f"| [{title}]({m['full']['url']}) | `{m['code']}` | {m['category']} | {m['version']} | "
                     f"{', '.join(m.get('modes', [])) or '-'} | {human(m['full']['size'])} |")
    lines += ["", "</details>"]
    if index.get("updated"):
        lines += ["", f"Index updated {index['updated']}."]
    return "\n".join(lines)


def write_readme(index: dict) -> None:
    text = README.read_text(encoding="utf-8")
    start, end = "<!-- tables:start -->", "<!-- tables:end -->"
    if start not in text or end not in text:
        die("README.md has no <!-- tables:start --> / <!-- tables:end --> markers")
    head, rest = text.split(start, 1)
    _, tail = rest.split(end, 1)
    write_text(README, head + start + "\n" + readme_tables(index) + "\n" + end + tail)


def cmd_readme(args) -> None:
    write_readme(load_json(INDEX))
    print("README.md tables regenerated")


# ---- main ------------------------------------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="occ.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pack", help="pack a svmbuild output folder into staging/out")
    p.add_argument("--build", action="append", required=True,
                   help="svmbuild output folder, optionally =<maps root> (the OpenScct.Maps library root its "
                        "--addons came from: <root>/game was the addons folder). Repeat for several builds; the "
                        "first one's shared/ is packed.")
    p.add_argument("--install", help="the Versus install the builds read (--game): its maps are category stock")
    p.add_argument("--catalog", help="SCCT-Maps catalogue dump (tools/fetch-scct-maps output)")
    p.add_argument("--openscct", required=True, help="OpenSCCT version the builder came from, e.g. 0.8.25")
    p.add_argument("--generator", required=True, help="builder description, e.g. 'svmbuild 0.8.25 (058d034)'")
    p.add_argument("--maps", help="comma list of codes to pack (default: all)")
    p.add_argument("--menu-maps", action="store_true", help="also pack Entry and Lobby")
    p.add_argument("--force", action="store_true", help="pack even when the index has the same content")
    p.set_defaults(func=cmd_pack)

    p = sub.add_parser("publish", help="upload staging/out to a new release and rewrite index.json")
    p.add_argument("--tag", help="release tag (default content-<yyyy.MM.dd>[-n]); an existing tag resumes")
    p.add_argument("--date", help="date part of the tag, yyyy.MM.dd")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-commit", action="store_true")
    p.add_argument("--no-push", action="store_true")
    p.set_defaults(func=cmd_publish)

    p = sub.add_parser("verify", help="check index.json (and staging/out archives)")
    p.add_argument("--remote", action="store_true", help="HEAD every URL")
    p.add_argument("--quick", action="store_true", help="sizes only, no hashing")
    p.set_defaults(func=cmd_verify)

    p = sub.add_parser("readme", help="regenerate README.md tables from index.json")
    p.set_defaults(func=cmd_readme)

    args = ap.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
