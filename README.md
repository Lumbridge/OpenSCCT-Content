# OpenSCCT-Content

This repository describes the SVMap archive format and the catalogue for optional community-created maps. The [OpenSCCT launcher](https://github.com/OpenSCCT/OpenSCCT/releases/latest) builds the original game data from the player's installed Steam copy of Splinter Cell Chaos Theory. The Versus maps supplied with that copy form the starting roster for both modernisations and the editor.

## Find a map

- For **Modernisations**, use the map browser in [OpenSCCT Godot](https://master.lumbridge.co.uk/projects/godot), [OpenSCCT Unreal](https://master.lumbridge.co.uk/projects/unreal) or [OpenSCCT Editor](https://github.com/OpenSCCT/OpenSCCT-Editor). Optional public downloads are limited to community-created maps with reviewed assets. A map can reference stock assets already built on the player's computer.
- For the **Originals**, the [SCCT Maps collection](https://github.com/OpenSCCT/SCCT-Maps) and [SCCT Map Manager](https://github.com/OpenSCCT/SCCT-Map-Manager) serve the original PC Versus game. Its catalogue also includes recovered maps, Enhanced variants and ports.

## Contribute a map

Build an SVMap from your own project with the editor. The community catalogue identifies each map, its simulation content hash and a pinned source recipe. The recipe names the source revision and checksums for the reviewed files that the local converter may use. The simulation hash lets clients compare a map with a multiplayer host. Check that your map's models, textures, audio and other bundled assets may be redistributed before submitting it.

| File | Purpose |
| --- | --- |
| [Community catalogue](community.json) | Approved map sources and recipes for local conversion |
| [Historical archive index](index.json) | Map identities and pack formats used by older clients |
| [Schema](schema/index.schema.json) | Machine-readable catalogue format |
| [Format](docs/FORMAT.md) | Contents of full and simulation-only archives |
| [Publishing guide](docs/PUBLISHING.md) | Community recipe publication and the historical packing workflow |
| [Tools](tools) | Archive packing, verification and catalogue utilities |

<!-- tables:start -->
<!-- The release tools maintain this section from the approved community catalogue. -->
<!-- tables:end -->

## Historical releases

Earlier releases distributed converted retail content and shared libraries, including PS2 maps. The [PS2 collection notes](docs/PS2-ORIGINAL.md) record what those versions contained and tested. Splinter Cell and Chaos Theory belong to Ubisoft. Community maps belong to their creators.
