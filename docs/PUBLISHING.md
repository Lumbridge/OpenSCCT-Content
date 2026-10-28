# Publishing

How the packs are made and published. Everything runs on Windows from this repository's root; `staging/` (git
ignored) holds the inputs, the builds and the archives.

You need:

- an OpenSCCT checkout (its content builder `content/svmbuild`, Python 3.10 with `content/requirements.txt`, and
  `src/OpenScct.Maps` for the map downloader), at the commit of the release you are building for
- a Splinter Cell Chaos Theory install (its `Versus` folder); the first publish used the Steam copy
- the .NET 10 SDK and the GitHub CLI (`gh`, logged in with push access to this repository)
- optional: a checkout of [SCCT-Maps](https://github.com/Lumbridge/SCCT-Maps) at the catalogue commit, so its files
  are copied instead of downloaded (it is only read)

One builder version builds everything in a publish, so every map names the same shared pack hashes.

## 1. The builder

Export the OpenSCCT commit you build with, so work in progress in a checkout never leaks into a pack:

```powershell
$src = "staging\svmbuild-src"
git -C ..\SVM-Rewrite archive HEAD content re spec tools/scctpkg fixtures | tar -x -C $src
```

## 2. The maps (build inputs)

`tools/fetch-scct-maps` downloads SCCT-Maps maps with OpenSCCT's own code (`OpenScct.Maps`, the launcher's Maps
download): each map's files, the stock asset packs and every package a map imports, into a folder laid out like an
install. It skips maps whose codes the install already has.

```powershell
dotnet build tools\fetch-scct-maps -c Release -o staging\fetch-bin -p:OpenScctRepo=..\SVM-Rewrite
$commit = git -C ..\SCCT-Maps rev-parse HEAD     # or the SCCT-Maps commit to publish
$game = "D:\Games\Steam Games\steamapps\common\Splintercell Chaos Theory\Versus"
staging\fetch-bin\fetch-scct-maps.exe staging\inputs\scct-maps-catalog.json $commit `
  --root staging\inputs\main --game $game --local ..\SCCT-Maps --cache staging\cache\releases `
  --skip "recovered/Eden,recovered/Heliport 1.1,recovered/Sublabs"
```

Maps that share a code (a community map and its recovered rebuild) cannot be in one build, as the builder converts
one `svmap/<code>` per build. Fetch the second set into its own root:

```powershell
staging\fetch-bin\fetch-scct-maps.exe staging\inputs\cat-rec.json $commit --root staging\inputs\recovered `
  --game $game --local ..\SCCT-Maps --cache staging\cache\releases `
  --ids "recovered/Eden,recovered/Heliport 1.1,recovered/Sublabs"
```

The second build must still see every other file of the first: the shared audio pack is made from every sound
package in the install and the add-ons, so a build from a smaller add-on folder names a different `audio` hash and
`pack` refuses it. Overlay the second set on a copy of the first (only the clashing `.sdc` files differ):

```powershell
robocopy staging\inputs\main\game staging\inputs\rec-combined\game /E
robocopy staging\inputs\recovered\game staging\inputs\rec-combined\game /E
```

Build from `rec-combined\game`, but give `pack` the `recovered` root: its `installed.json` says which SCCT-Maps map
each `.sdc` came from.

## 3. Build

Run the full build once per maps root, with the same install and builder (the install wins over the add-ons):

```powershell
cd staging\svmbuild-src\content
$env:SVM_CONTENT = "..\..\build\main"
python -u -m svmbuild classes chars audio ui maps-catalog renderpack fx maps audio-map --maps all `
  --game $game --addons ..\..\inputs\main\game --out ..\..\build\main --jobs 12 --report ..\..\build\main-report.json
$env:SVM_CONTENT = "..\..\build\recovered"
python -u -m svmbuild classes chars audio ui maps-catalog renderpack fx maps audio-map --maps EDE64,HELI02,sub18 `
  --game $game --addons ..\..\inputs\rec-combined\game --out ..\..\build\recovered --jobs 12
```

Maps that fail to convert are simply absent from `svmap/`; the report (`--report`) says why.

## 4. Pack

```powershell
python tools\occ.py pack --install $game --catalog staging\inputs\scct-maps-catalog.json `
  --build staging\build\main=staging\inputs\main --build staging\build\recovered=staging\inputs\recovered `
  --openscct 0.8.25 --generator "svmbuild 0.8.25 (058d034)" --menu-maps
```

`pack` writes `staging/out/*.zip` and `staging/out/plan.json`:

- one `full` and one `sim` archive per map, one archive per shared pack (`core`, `chars`, `audio`, from the first
  build; every other build must have the same `classes` and `audio` hashes)
- a pack whose files are the same as the index's (`treeSha256` and `manifestSha256`) is skipped: only changed and
  new packs are written
- changed packs get the next version (maps `1.0.0` → `1.0.1`; shared `0.8.25.1` → `0.8.25.2`, or
  `<new OpenSCCT version>.1`)
- each map's category and source come from where its `.sdc` came from: the install (category `stock`), or the
  SCCT-Maps map that brought it (`<maps root>/installed.json`)
- Entry and Lobby (the menu maps: the front end and the lobby load them) are packed only with `--menu-maps`, which
  the published index uses; they list no modes

`--maps AquaE,ShipD` packs only those; `--force` packs even unchanged content.

## 5. Publish

```powershell
python tools\occ.py publish --dry-run     # writes staging\index.preview.json, uploads nothing
python tools\occ.py publish
```

`publish`:

1. creates the release `content-<yyyy.MM.dd>` (`-2`, `-3`, ... when that tag exists) with `gh release create`
2. uploads the plan's archives with `gh release upload` (20 at a time; an interrupted publish resumes with
   `--tag <tag>`, uploading only what is missing)
3. checks every asset is on the release with its size
4. rewrites `index.json`: the new packs with their absolute download URLs, sizes and sha256; unchanged packs keep
   their old entries (and URLs into older releases); maps sorted by category then code
5. regenerates the README tables, commits `index.json` and `README.md` and pushes (`--no-commit`, `--no-push`)

Release assets are limited to 2 GiB each; `pack` refuses a bigger archive.

## 6. Verify

```powershell
python tools\occ.py verify            # schema, ids, requires vs shared hashes, archives in staging\out
python tools\occ.py verify --remote   # also HEAD every URL and compare sizes
```

## Republishing

After an OpenSCCT release that changes the converter, or a new SCCT-Maps commit: steps 1 to 5 again with the new
commit and version. Only packs whose content changed are uploaded; the index points the rest at their old releases.
Never delete a release that the index still points at (`occ.py verify --remote` would fail).

`occ.py readme` regenerates the README tables from `index.json` by hand.
