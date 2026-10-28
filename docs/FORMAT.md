# Format

What a client reads from this repository and what it downloads. This is the contract OpenSCCT's game, launcher and
servers are written against (OpenSCCT `docs/CONTENT-PACKS.md` is the same contract seen from the game's side).

The repository's tree holds only the index and the tools that make it. The packs are GitHub Release assets, so git
history stays small and downloads have no LFS quota. Older releases stay: a host and its players can use the same
pack until the index moves on.

## The index

`index.json` on the `main` branch, fetched raw:
`https://raw.githubusercontent.com/Lumbridge/OpenSCCT-Content/main/index.json`. It is the only file a client reads
from the tree. `schema/index.schema.json` is its JSON Schema; `tools/occ.py verify` checks it.

```json
{
  "format": "openscct.content",
  "formatVersion": 1,
  "updated": "2026-10-28T20:00:00Z",
  "svmapFormat": "1.1",
  "shared": [
    {
      "id": "core",
      "title": "Shared game data",
      "version": "0.8.25.1",
      "contents": ["classes.json", "render", "fx", "ui", "maps"],
      "hashes": { "classes": "<sha256 of shared/classes.json>" },
      "treeSha256": "<sha256 of the pack's file list>",
      "generator": "svmbuild 0.8.25 (058d034)",
      "download": { "url": "https://github.com/Lumbridge/OpenSCCT-Content/releases/download/<tag>/shared-core-0.8.25.1.zip",
                    "size": 31457280, "sha256": "<sha256 of the zip>" }
    }
  ],
  "maps": [
    {
      "id": "stock/AquaE",
      "code": "AquaE",
      "title": "Enhanced Aquarius",
      "category": "stock",
      "version": "1.0.0",
      "modes": ["Story", "DiskHunt", "Deathmatch", "MercDeathmatch"],
      "contentHash": "66b2f44d79c6cf46",
      "manifestSha256": "<sha256 of the map's manifest.json>",
      "treeSha256": "<sha256 of the pack's file list>",
      "requires": [ { "pack": "audio", "sha256": "<sha256>" }, { "pack": "classes", "sha256": "<sha256>" } ],
      "source": { "kind": "repo", "repo": "Lumbridge/SCCT-Maps", "commit": "<40 hex>",
                  "path": "stock/Packages/Maps/AquaE.sdc", "sha256": "<sha256 of the .sdc>", "mapId": "stock/AquaE" },
      "generator": "svmbuild 0.8.25 (058d034)",
      "full": { "url": "https://github.com/.../stock-AquaE-1.0.0.zip", "size": 12345678, "sha256": "<sha256>" },
      "sim":  { "url": "https://github.com/.../stock-AquaE-1.0.0-sim.zip", "size": 1234567, "sha256": "<sha256>" }
    }
  ]
}
```

### Top level

- `format` is always `openscct.content`.
- `formatVersion` changes only when an old client could not read the index. A client skips an index with a newer
  version and says the game needs an update.
- `updated` is when the index was last published (UTC).
- `svmapFormat` is the `major.minor` of the svmap packs (OpenSCCT `spec/svmap`). A client that reads a different
  major skips every map and says so.
- Unknown fields are ignored everywhere. Missing optional fields: `title` falls back to `code`, `modes` to empty,
  `sim` to `full`.

### Shared packs

Shared packs install to `shared/<contents>` and are what a converted map needs from outside its own folder:

| id | contents | hashes |
| --- | --- | --- |
| `core` | `classes.json`, `render` (the render pack), `fx`, `ui`, `maps` (the map catalog and its images) | `classes`: sha256 of `classes.json` |
| `chars` | `chars` | none |
| `audio` | `audio` (the shared sound banks) | `audio`: sha256 of `audio/audio.json` |

- `hashes` are the values the maps' `requires` name (each manifest's `requires[].sha256`): a map that requires
  `classes` with a hash matches the `core` pack whose `hashes.classes` is that hash. Every map in one index requires
  hashes the same index's shared packs have (`occ.py verify` checks this).
- `version` is `<OpenSCCT version>.<n>`: the OpenSCCT build whose converter made it, and a number bumped on every
  republish with the same converter.
- `treeSha256` is the sha256 of the pack's file list (below); it changes exactly when a file in the pack changes.
- `download` is the archive: URL, size in bytes and sha256 of the ZIP.

### Maps

- `id` is `<category>/<code>`. Category is one of:

  | category | what |
  | --- | --- |
  | `stock` | Ubisoft's maps: the Steam install's retail set and the SCCT Versus 4.0 maps (SCCT-Maps `stock/`) |
  | `original` | New maps made for SCCT Versus (SCCT-Maps `release/`, newest version) |
  | `community` | The community map pack (SCCT-Maps `community/`) |
  | `enhanced` | Edited versions of existing maps (SCCT-Maps `enhanced/`) |
  | `recovered` | Existing maps rebuilt as editable maps (SCCT-Maps `recovered/`) |
  | `ports` | Maps ported from other games (SCCT-Maps `ports/` and its released ports) |

  The same code can appear in two categories (a community map and its recovered rebuild, `community/EDE64` and
  `recovered/EDE64`). Both install to `svmap/<code>/`, so a client installs one of them at a time.
- `code` is the map's package name. It is also the svmap folder name and the name the game's catalog uses.
- `title` is the manifest's title; when that is only the code, the shared catalog's name, then SCCT-Maps' name.
- `modes` are the modes the map plays, decided as OpenSCCT's `MapCatalog.ModesOf` does from `sim/gameplay.json`:
  Story, DiskHunt, Deathmatch, MercDeathmatch, then Extraction, Sabotage, Neutralization, in that order.
- `contentHash` is `MapCatalog.ContentHashOf`: the first 16 hex characters (lowercase) of the manifest's
  `hashes.sim`. This is what lobbies and the hub compare, so a client can tell whether its copy matches without
  downloading.
- `manifestSha256` is the sha256 of the map's `manifest.json` as it is in the archive.
- `treeSha256` is the sha256 of the pack's file list, catalog entry included.
- `requires` is the manifest's `requires`, copied.
- `source` is the original package the map was converted from:
  - `kind` `install`: the Steam install's `Packages/Maps/<code>.sdc` (`path` is relative to the Versus folder; no repo)
  - `kind` `repo`: a file of `repo` at `commit`, at `path`
  - `kind` `release`: a release asset of `repo`, `path` being `releases/download/<tag>/<name>`

  `sha256` is the .sdc's sha256 (the manifest's `source.original.sha256`); `mapId` is the SCCT-Maps catalogue id.
- `generator` is the converter that made the pack.
- `full` is everything the game needs to play the map. `sim` is `manifest.json` and `sim/` only, which is what a
  dedicated server or hub needs.
- `version` is the pack's version: SemVer, starting at 1.0.0, the patch number bumped for every republish of the same
  id.

The file list behind `treeSha256` is the archive's files as `<path>\t<sha256>\n` lines sorted by path (UTF-8), hashed
with sha256.

## Pack archives

Every pack is a ZIP (the only archive both .NET and Python read without extra libraries).

- Names: `shared-<id>-<version>.zip`, `<category>-<code>-<version>.zip` and `<category>-<code>-<version>-sim.zip`
  (characters other than letters, digits, `.`, `-` and `_` become `_`). Clients use the URL from the index, never a
  name they build.
- Map archives hold the map folder's contents at the root: `manifest.json`, `sim/`, `render/`, `audio/`, `ui/`, plus
  `catalog/` (below). Shared archives hold their `contents` at the root (`classes.json`, `render/...`).
- Files that are already compressed (`.png`, `.ogg`, `.jpg`) are stored. Everything else is deflated (level 9).
- Entries are sorted by path and have fixed timestamps (1980-01-01), so the same content gives the same archive.
- Paths use `/`, are relative, and never contain `..`, a drive letter or a leading `/`. A client refuses any archive
  that breaks this.
- After extracting a map, the client checks each extracted file against `manifest.json`'s `files` (sha256 and size).
  A `sim` archive holds only part of the files; the rest are allowed to be missing.

### A map's catalog entry

The game's map catalog (`shared/maps/catalog.json`, OpenSCCT docs/MAPS.md) names maps and holds their menu, briefing
and loading images. A downloaded map brings its own entry, so it shows correctly over a catalog built from the
player's install:

```
catalog/entry.json     { "code": "AquaE", "name": "Enhanced Aquarius",
                         "images": { "menu": "images/menu.png", "briefing": "images/briefing.png",
                                     "loading-spy": "images/loading-spy.png", "loading-merc": "images/loading-merc.png" } }
catalog/images/<kind>.png
```

`images` paths are relative to `catalog/`. Only the images the converter made are listed (a map without a menu
picture has no `menu`; `images` can be empty). The catalog entry is in `full` archives only.

## Where packs install

| Who | Root | Layout |
| --- | --- | --- |
| Game (launcher install) | `%LOCALAPPDATA%\OpenSCCT\packs` | `svmap/<code>/`, `shared/`, `installed.json`, `downloads/` |
| Dedicated server / hub | `<server>/packs` (or `--content-packs <dir>`) | the same |

The game searches its maps in this order: content converted from the player's install (`<content>/svmap`),
downloaded packs (`<packs>/svmap`), the maps shipped with the build (`<exe>/maps`). A converted map of the same code
wins, so a player's own conversion is never overwritten. Shared content works the same way: `<content>/shared` when
the player converted their install, else `<packs>/shared`.
