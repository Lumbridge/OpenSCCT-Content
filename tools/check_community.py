"""Validate the source-only public map catalogue and optionally its actual inputs and conversions."""

import argparse
import concurrent.futures
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
TYPES = {"Maps": {".sdc"}, "StaticMeshes": {".usx"}, "Textures": {".utx", ".utc"},
         "Sounds": {".uas", ".uax", ".mux", ".usxx"}, "Animations": {".ukx"}}
STOCK = set("aqu03 bnk11 clu04 dtk09 fac05 gar01 map12 mis02 mus08 orp06 war10 "
            "tme30 tme32 tme33 tsp20 tsp21 tsp22 tsp23 tsp29 entry lobby".split())


def require(ok, message):
    if not ok:
        raise ValueError(message)


def safe_path(text):
    require(isinstance(text, str) and text and all(part not in ("", ".", "..") for part in text.split("/"))
            and not re.search(r"[:\\\x00-\x1f]", text), f"invalid relative path {text!r}")
    return PurePosixPath(text)


def package(text, *, local=False):
    p = safe_path(text)
    script = local and p.parts[:2] == ("System", "_PC_") and p.suffix.lower() == ".u"
    require(len(p.parts) == 3 and (script or (p.parts[0] == "Packages" and
            p.suffix.lower() in TYPES.get(p.parts[1], set()))), f"unexpected package {p}")
    return p


def check_catalog(doc):
    require(doc.get("format") == "openscct.content" and doc.get("formatVersion") == 1 and doc.get("shared") == [],
            "expected a source-only map catalogue with an empty shared list")
    require(isinstance(doc.get("maps"), list), "missing map list")
    seen = set()
    for item in doc["maps"]:
        code = item["code"]
        require(re.fullmatch(r"[A-Za-z0-9_-]+", code) and code.lower() not in seen | STOCK, f"duplicate or reserved map {code}")
        seen.add(code.lower())
        require(item.get("category") == "community" and item.get("id") == "community/" + code and
                len(item.get("title", "").strip()) > 0 and item.get("version") and isinstance(item.get("modes"), list) and
                item["modes"] and re.fullmatch(r"[a-f0-9]{16}", item.get("contentHash", "")), f"bad identity for {code}")
        require(set(item) == {"code", "id", "category", "title", "version", "modes", "contentHash", "steamRecipe"},
                f"{code} must only contain source map fields")
        recipe = item["steamRecipe"]
        commit = recipe["commit"]
        require(re.fullmatch(r"[a-f0-9]{40}", commit) and recipe["credits"].strip() and
                recipe["files"] and recipe["steamFiles"], f"incomplete recipe for {code}")
        destinations, folder, maps = set(), None, []
        for file in recipe["files"]:
            dst = package(file["destination"])
            src = safe_path(file["path"])
            require(src.parts[0] == "community" and len(src.parts) == 5 and src.parts[2:] == dst.parts and
                    (folder is None or folder == src.parts[1]), f"{code} source is outside its map directory")
            folder = src.parts[1]
            require(dst.as_posix().lower() not in destinations and isinstance(file["size"], int) and file["size"] > 0 and
                    re.fullmatch(r"[a-f0-9]{64}", file["sha256"]), f"bad source descriptor for {code}: {src}")
            destinations.add(dst.as_posix().lower())
            if dst.parts[1] == "Maps":
                maps.append(dst.name.lower())
        require(maps == [code.lower() + ".sdc"], f"expected exactly the named map package for {code}")
        base = f"https://github.com/OpenSCCT/SCCT-Maps/blob/{commit}/community/{urllib.parse.quote(folder)}/"
        require(recipe["evidence"].startswith(base), f"unbound credit evidence for {code}")
        for dependency in recipe["steamFiles"]:
            path = package(dependency, local=True).as_posix().lower()
            require(path not in destinations, f"{code} overlaps a Steam prerequisite: {dependency}")
            destinations.add(path)
    return doc["maps"]


def checked_bytes(entry, data):
    require(len(data) == entry["size"] and hashlib.sha256(data).hexdigest() == entry["sha256"],
            f"size or digest mismatch: {entry['path']}")


def verify(map_entry, args):
    code, recipe = map_entry["code"], map_entry["steamRecipe"]
    source = recipe["files"]
    if args.steam:
        for entry in source:
            require(not (args.steam / entry["destination"]).exists(), f"{code} would replace an installed Steam file")
        for path in recipe["steamFiles"]:
            require((args.steam / path).is_file(), f"{code} needs missing Steam input {path}")
    if args.remote or args.sources:
        sums_path = "/".join(source[0]["path"].split("/")[:2]) + "/SHA256SUMS.txt"
        def read(path):
            if args.sources:
                return (args.sources / path).read_bytes()
            url = "https://raw.githubusercontent.com/OpenSCCT/SCCT-Maps/" + recipe["commit"] + "/" + urllib.parse.quote(path)
            with urllib.request.urlopen(url, timeout=75) as response:
                return response.read()
        upstream = dict(reversed(line.strip().split(None, 1)) for line in read(sums_path).decode("utf-8-sig").splitlines() if line.strip())
        for entry in source:
            require(upstream.get(entry["destination"]) == entry["sha256"], f"{code} upstream checksum mismatch: {entry['path']}")
            checked_bytes(entry, read(entry["path"]))
    if args.converted:
        paths = [root / "svmap" / code for root in args.converted if (root / "svmap" / code / "manifest.json").is_file()]
        require(len(paths) == 1, f"expected exactly one conversion for {code}")
        folder = paths[0]
        manifest = json.loads((folder / "manifest.json").read_text(encoding="utf8"))
        require(manifest["map"] == code and manifest["hashes"]["sim"][:16] == map_entry["contentHash"],
                f"unexpected converted simulation hash for {code}")
        from svmbuild import canonical
        files, groups = canonical.hash_map(folder)
        require(files == manifest["files"] and groups == manifest["hashes"],
                f"recomputed SVMap file or group hashes differ for {code}")
        audio = json.loads((folder / "audio/audio.json").read_text(encoding="utf8"))
        require(not any(audio["missing"].values()), f"{code} has unresolved audio")
    return code


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--catalog", type=Path, default=ROOT / "community.json")
    inputs = ap.add_mutually_exclusive_group()
    inputs.add_argument("--remote", action="store_true", help="verify immutable original mod files and their upstream checksums")
    inputs.add_argument("--sources", type=Path, help="local checkout or mirror of the pinned SCCT-Maps sources")
    ap.add_argument("--steam", type=Path, help="a clean Steam Versus folder")
    ap.add_argument("--converted", type=Path, action="append", help="conversion root with svmap/ (repeat as needed)")
    ap.add_argument("--converter", type=Path, help="OpenSCCT content/ directory containing svmbuild, for local SVMap hashing")
    args = ap.parse_args()
    if args.converter:
        sys.path.insert(0, str(args.converter.resolve()))
    if args.converted:
        try:
            from svmbuild import canonical
        except ImportError:
            ap.error("local validation needs the SVMap canonical hash implementation; supply --converter /path/to/OpenSCCT/content")
    items = check_catalog(json.loads(args.catalog.read_text(encoding="utf8")))
    with concurrent.futures.ThreadPoolExecutor(4) as pool:
        codes = list(pool.map(lambda item: verify(item, args), items))
    print(f"Verified {len(codes)} community recipes: " + ", ".join(codes))


if __name__ == "__main__":
    main()
