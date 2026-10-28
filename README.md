# OpenSCCT-Content

Game content for [OpenSCCT](https://github.com/Lumbridge/OpenSCCT), already converted to OpenSCCT's own formats:
maps (svmap packs) and the shared packs they need. With these a player, a dedicated server or the hub can download a
map and play it without running the converter.

The original game's maps, for Splinter Cell Chaos Theory Versus itself and the
[SCCT Map Manager](https://github.com/Lumbridge/SCCT-Map-Manager), are in [SCCT-Maps](https://github.com/Lumbridge/SCCT-Maps).
Everything here was converted from those files and from a retail install.

## What is here

The packs are ZIP archives attached to this repository's [releases](https://github.com/Lumbridge/OpenSCCT-Content/releases)
(`content-<date>`). The tree holds only:

| Path | What |
| --- | --- |
| [`index.json`](index.json) | Every pack: version, size, sha256, download URL, and for maps their category, modes and content hash |
| [`schema/index.schema.json`](schema/index.schema.json) | JSON Schema of the index |
| [`docs/FORMAT.md`](docs/FORMAT.md) | The index and archive formats (the contract the game reads) |
| [`docs/PUBLISHING.md`](docs/PUBLISHING.md) | How the packs are built and published |
| [`tools/`](tools) | `occ.py` (pack, publish, verify, readme; Python 3 standard library) and the map downloader the build uses |

<!-- tables:start -->
<!-- tables:end -->

## How the game uses it

OpenSCCT reads `index.json` from `main`
(`https://raw.githubusercontent.com/Lumbridge/OpenSCCT-Content/main/index.json`), downloads the archives it needs,
checks their sha256, and extracts them under its packs folder (`%LOCALAPPDATA%\OpenSCCT\packs`: `svmap/<code>/` and
`shared/`). A map's `full` archive is everything the game needs to play it; its `sim` archive (manifest and `sim/`
only) is all a dedicated server or the hub needs. Each map names the shared pack hashes it was converted against
(`requires`), and its `contentHash` is what lobbies compare, so a client can tell whether its copy matches a host's
without downloading anything.

Content a player converts from their own install always wins over a downloaded pack of the same map.

## Legal

The stock maps and the shared packs are converted from Ubisoft's Splinter Cell Chaos Theory and remain Ubisoft's.
Community, original, recovered, enhanced and ported maps belong to their authors (see each map's notes in
[SCCT-Maps](https://github.com/Lumbridge/SCCT-Maps)). OpenSCCT is a fan project; it is not affiliated with or endorsed
by Ubisoft.
