"""Build independent bot-navigation assets for the maps in the content index."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

PACK_PATH = "catalog/bot-nav.zip"


def identity(path: Path) -> tuple[int, str, int]:
    """Read the SVMNAV headers to pair the download with the exact map, format and activation mask."""
    sides = []
    with ZipFile(path) as archive:
        for side in ("spy", "merc"):
            with archive.open(f"{side}.svmnav") as graph:
                if graph.read(7) != b"\x06SVMNAV":
                    raise ValueError(f"{path}: invalid {side} navigation header")
                version = int.from_bytes(graph.read(4), "little")
                length = 0
                for shift in (0, 7, 14):
                    value = graph.read(1)[0]
                    length |= (value & 127) << shift
                    if value < 128:
                        break
                match = re.fullmatch(rb".+-([0-9a-f]{64})-m([0-9]{1,3})", graph.read(length))
                if not match or not version or int(match[2]) > 255:
                    raise ValueError(f"{path}: invalid {side} navigation identity")
                sides.append((version, match[1].decode("ascii"), int(match[2])))
    if sides[0] != sides[1]:
        raise ValueError(f"{path}: the two navigation graphs have different identities")
    return sides[0]


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest() if hasattr(hashlib, "file_digest") else _sha256(stream)


def _sha256(stream) -> str:
    digest = hashlib.sha256()
    for block in iter(lambda: stream.read(1 << 20), b""):
        digest.update(block)
    return digest.hexdigest()


def _manifest(path: Path) -> dict:
    return json.loads((path / "manifest.json").read_text(encoding="utf-8-sig"))


def _download_sim(map_entry: dict, target: Path) -> None:
    download = map_entry.get("sim", map_entry["full"])
    archive_path = target / ".source.zip"
    request = urllib.request.Request(download["url"], headers={"User-Agent": "OpenSCCT-Content"})
    try:
        try:
            with urllib.request.urlopen(request, timeout=60) as source, archive_path.open("wb") as file:
                shutil.copyfileobj(source, file)
        except urllib.error.URLError:
            asset = re.fullmatch(r"https://github\.com/Lumbridge/OpenSCCT-Content/releases/download/([^/]+)/([A-Za-z0-9._-]+\.zip)", download["url"])
            if asset is None or not shutil.which("gh"):
                raise
            subprocess.run(["gh", "release", "download", asset[1], "--repo", "Lumbridge/OpenSCCT-Content",
                            "--pattern", asset[2], "--output", str(archive_path), "--clobber"], check=True)
        if archive_path.stat().st_size != download["size"] or sha256(archive_path) != download["sha256"]:
            raise ValueError(f"{map_entry['id']}: source archive does not match the index")
        with ZipFile(archive_path) as archive:
            for member in archive.namelist():
                if not (member == "manifest.json" or member.startswith("sim/")) or member.endswith("/"):
                    continue
                path = PurePosixPath(member)
                if ".." in path.parts or "\\" in member or ":" in member:
                    raise ValueError(f"Unsafe source archive path: {member}")
                dest = target.joinpath(*path.parts)
                dest.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(member) as source, dest.open("wb") as file:
                    shutil.copyfileobj(source, file)
    finally:
        archive_path.unlink(missing_ok=True)


def bake(index: dict, builds: list[Path], baker: Path, work: Path, out: Path, jobs: int,
         only: set[str] | None = None) -> tuple[list[dict], list[dict]]:
    env = dict(os.environ)
    env.setdefault("SVM_AI_NAV_CACHE", str((work.parent / "bot-nav-cache").resolve()))
    sources = {}
    for build in builds:
        for manifest in (build / "svmap").glob("*/manifest.json"):
            folder = manifest.parent
            sources[(folder.name.casefold(), _manifest(folder)["hashes"]["sim"][:16])] = folder

    def one(entry: dict) -> dict:
        code = entry["code"]
        target = work / entry["category"] / entry["contentHash"] / code
        target.mkdir(parents=True, exist_ok=True)
        expected = entry["manifestSha256"]
        if not (target / "manifest.json").is_file() or not _manifest(target)["hashes"]["sim"].startswith(entry["contentHash"]):
            if source := sources.get((code.casefold(), entry["contentHash"])):
                shutil.copytree(source / "sim", target / "sim", dirs_exist_ok=True)
                shutil.copyfile(source / "manifest.json", target / "manifest.json")
            else:
                _download_sim(entry, target)
        sim_hash = _manifest(target)["hashes"]["sim"]
        if not sim_hash.startswith(entry["contentHash"]):
            raise ValueError("staged simulation differs from the published map")

        log = target.parent / (code + ".log")
        with log.open("w", encoding="utf-8") as output:
            result = subprocess.run([str(baker), "--priority", "below", "--bake-bot-nav", str(target)],
                                    env=env, stdout=output, stderr=subprocess.STDOUT, check=False)
        if result.returncode:
            raise ValueError(f"bake failed ({result.returncode}), see {log}")
        path = target / PACK_PATH
        version, built_hash, mask = identity(path)
        if built_hash != sim_hash:
            raise ValueError("generated navigation belongs to another map revision")
        name = f"bot-nav-{entry['category']}-{code}-{sim_hash[:16]}-v{version}.zip"
        dest = out / name
        temp = dest.with_suffix(".tmp")
        shutil.copyfile(path, temp)
        temp.replace(dest)
        return {"id": entry["id"], "manifestSha256": expected, "simHash": sim_hash,
                "formatVersion": version, "activationMask": mask,
                "archive": {"file": name, "size": dest.stat().st_size, "sha256": sha256(dest)}}

    out.mkdir(parents=True, exist_ok=True)
    selected = [m for m in index["maps"] if m.get("modes") and (only is None or m["code"].casefold() in only)]
    assets, failed = [], []
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        pending = {pool.submit(one, entry): entry["id"] for entry in selected}
        for future in as_completed(pending):
            name = pending[future]
            try:
                asset = future.result()
                assets.append(asset)
                print(f"{len(assets) + len(failed)}/{len(selected)} {name}: {asset['archive']['size'] / 2**20:.1f} MiB", flush=True)
            except Exception as error:
                failed.append({"id": name, "reason": str(error)})
                print(f"{len(assets) + len(failed)}/{len(selected)} {name}: {error}", flush=True)
    return sorted(assets, key=lambda m: m["id"]), sorted(failed, key=lambda m: m["id"])
