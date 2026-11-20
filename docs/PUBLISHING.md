# Publishing community maps

The active [community catalogue](../community.json) lists source recipes for the Godot and Unreal modernisations and OpenSCCT Editor. Each recipe pins the reviewed files and their SHA-256 digests to a specific revision and includes author credit and evidence for that selection. Verify the recipe against a clean Steam installation. Include only community-authored files with permission to distribute them. Retail package dependencies come from the player's installed game.

Use the [source review and verification guide](SOURCE-MAPS.md) to check a recipe before submitting it.

## Historical pack reproduction

The following procedure reproduces an older converted pack locally. It requires a matching OpenSCCT checkout, its converter dependencies, a local Chaos Theory Versus installation and the corresponding SCCT-Maps revision. All output stays under the ignored `staging/` directory.

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
- maps from compatible SVMap minor versions can share an index; it advertises the newest included minor.
  A publish containing different major versions is refused.
- each map's category and source come from where its `.sdc` came from: the install (category `stock`), or the
  SCCT-Maps map that brought it (`<maps root>/installed.json`)
- Entry and Lobby (the menu maps: the front end and the lobby load them) are packed only with `--menu-maps`, which
  the published index uses; they list no modes

`--maps AquaE,ShipD` packs only those; `--force` packs even unchanged content.

To prepare separate bot navigation downloads for the published maps, run:

```powershell
python tools\occ.py bot-nav --baker <path-to-svm-server> --build staging\build\main --build staging\build\recovered --jobs 4
```

Use the server executable from the game version that will consume the graphs. Local builds are optional. The tool
downloads the indexed simulation archive when it needs a missing revision. `--maps AquaE,ShipD` limits the bake.
This writes a navigation-only publish plan. The regular map archives and multiplayer hashes stay the same. Review
any failed maps in the plan, then use `publish --dry-run` to preview the index additions before publishing.

## 5. Inspect the historical pack

```powershell
python tools/occ.py publish --dry-run
python tools/occ.py verify
python tools/occ.py readme
```

The preview writes `staging/index.preview.json`. The archive table goes to `staging/historical-packs.md`. Existing releases and their historical index remain available to identify files from earlier installations.
