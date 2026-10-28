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
| Category | Maps | Download size | What |
| --- | ---: | ---: | --- |
| `stock` | 92 | 1.5 GB | Ubisoft's maps: the Steam install's retail set and the SCCT Versus 4.0 maps |
| `original` | 2 | 188.6 MB | New maps made for SCCT Versus (SCCT-Maps `release/`) |
| `community` | 56 | 742.3 MB | The community map pack |
| `enhanced` | 1 | 22.6 MB | Edited versions of existing maps |
| `recovered` | 5 | 121.9 MB | Existing maps rebuilt as editable maps |
| `ports` | 9 | 183.9 MB | Maps ported from other games |
| **All** | **165** | **2.7 GB** | |

| Shared pack | Version | Size | Contents |
| --- | --- | ---: | --- |
| `core` | 0.8.25.1 | 77.2 MB | classes.json, render, fx, ui, maps |
| `chars` | 0.8.25.1 | 339.0 MB | chars |
| `audio` | 0.8.25.1 | 74.5 MB | audio |

<details><summary>Every map</summary>

| Map | Code | Category | Version | Modes | Size |
| --- | --- | --- | --- | --- | ---: |
| [Aquarius](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-AQU03-1.0.0.zip) | `AQU03` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.6 MB |
| [Aquarius](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-AquaD-1.0.0.zip) | `AquaD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.6 MB |
| [Enhanced Aquarius](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-AquaE-1.0.0.zip) | `AquaE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.6 MB |
| [Enhanced Aquarius 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-AquaT-1.0.0.zip) | `AquaT` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.8 MB |
| [Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-BankD-1.0.0.zip) | `BankD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Phoenix's Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-BankP-1.0.0.zip) | `BankP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-BNK11-1.0.0.zip) | `BNK11` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.1 MB |
| [Enhanced Cinema](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-CineE-1.0.0.zip) | `CineE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 10.2 MB |
| [Enhanced Cinema Sabotage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-CineS-1.0.0.zip) | `CineS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.8 MB |
| [Ump Cinema](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-CineU-1.0.0.zip) | `CineU` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-CLU04-1.0.0.zip) | `CLU04` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 10.9 MB |
| [Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ClubD-1.0.0.zip) | `ClubD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.0 MB |
| [Enhanced Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ClubE-1.0.0.zip) | `ClubE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.0 MB |
| [Shadow House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ClubS-1.0.0.zip) | `ClubS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.5 MB |
| [Enhanced Club House 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ClubT-1.0.0.zip) | `ClubT` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.0 MB |
| [Snake Cpusa](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-CpusS-1.0.0.zip) | `CpusS` | stock | 1.0.0 | Story, Deathmatch, MercDeathmatch | 29.7 MB |
| [Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-DeftD-1.0.0.zip) | `DeftD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.0 MB |
| [Snake Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-DeftS-1.0.0.zip) | `DeftS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.9 MB |
| [Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-DTK09-1.0.0.zip) | `DTK09` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.6 MB |
| [Entry](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-Entry-1.0.0.zip) | `Entry` | stock | 1.0.0 | - | 10.8 MB |
| [Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-FAC05-1.0.0.zip) | `FAC05` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-FactD-1.0.0.zip) | `FactD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.5 MB |
| [Enhanced Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-FactE-1.0.0.zip) | `FactE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.5 MB |
| [Phoenix's Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-FactP-1.0.0.zip) | `FactP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Enhanced Factory 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-FactT-1.0.0.zip) | `FactT` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.5 MB |
| [Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-GAR01-1.0.0.zip) | `GAR01` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.5 MB |
| [Snake Ghost Town](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-GhosS-1.0.0.zip) | `GhosS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.6 MB |
| [Enhanced Krauser Lab](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-KrauE-1.0.0.zip) | `KrauE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.7 MB |
| [Ump Krauser Lab](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-KrauU-1.0.0.zip) | `KrauU` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.0 MB |
| [Lobby](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-Lobby-1.0.0.zip) | `Lobby` | stock | 1.0.0 | - | 10.8 MB |
| [River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-Map12-1.0.0.zip) | `Map12` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.7 MB |
| [Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MIS02-1.0.0.zip) | `MIS02` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.6 MB |
| [Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MissD-1.0.0.zip) | `MissD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.9 MB |
| [Enhanced Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MissE-1.0.0.zip) | `MissE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.9 MB |
| [Phoenix's Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MissP-1.0.0.zip) | `MissP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.1 MB |
| [Enhanced Mount Hospital](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MounE-1.0.0.zip) | `MounE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.6 MB |
| [Enh Mount Hospital Sabo](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MounS-1.0.0.zip) | `MounS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.0 MB |
| [Ump Mount Hospital](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MounU-1.0.0.zip) | `MounU` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.6 MB |
| [Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MUS08-1.0.0.zip) | `MUS08` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.3 MB |
| [Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MuseD-1.0.0.zip) | `MuseD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Enhanced Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MuseE-1.0.0.zip) | `MuseE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Museum 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-MuseT-1.0.0.zip) | `MuseT` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.1 MB |
| [Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ORP06-1.0.0.zip) | `ORP06` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.8 MB |
| [Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-OrphD-1.0.0.zip) | `OrphD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.3 MB |
| [Enhanced Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-OrphE-1.0.0.zip) | `OrphE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.3 MB |
| [Ps2 Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-OrphS-1.0.0.zip) | `OrphS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.8 MB |
| [Enhanced Orphanage 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-OrphT-1.0.0.zip) | `OrphT` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.3 MB |
| [Panama Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PanaD-1.0.0.zip) | `PanaD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.1 MB |
| [Snake Panama Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PanaS-1.0.0.zip) | `PanaS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.9 MB |
| [Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PolaD-1.0.0.zip) | `PolaD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [Enhanced Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PolaE-1.0.0.zip) | `PolaE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [Phoenix's Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PolaP-1.0.0.zip) | `PolaP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [Enhanced Polar Base 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PolaT-1.0.0.zip) | `PolaT` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [Prison](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PrisD-1.0.0.zip) | `PrisD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 88.4 MB |
| [Pyrocryptic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-PyroD-1.0.0.zip) | `PyroD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.4 MB |
| [River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-RiveD-1.0.0.zip) | `RiveD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.3 MB |
| [Enhanced River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-RiveE-1.0.0.zip) | `RiveE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.3 MB |
| [Phoenix's River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-RiveP-1.0.0.zip) | `RiveP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.3 MB |
| [Sanctuary](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SancD-1.0.0.zip) | `SancD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.3 MB |
| [Enhanced Sanctuary](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SancE-1.0.0.zip) | `SancE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.3 MB |
| [Enhanced Schermerhorn](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ScheE-1.0.0.zip) | `ScheE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.0 MB |
| [Ump Schermerhorn](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ScheU-1.0.0.zip) | `ScheU` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.3 MB |
| [Shadow Moses](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ShadD-1.0.0.zip) | `ShadD` | stock | 1.0.0 | Story, Deathmatch, MercDeathmatch | 20.9 MB |
| [Phoenix's Shadow Moses](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ShadP-1.0.0.zip) | `ShadP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.8 MB |
| [Skyscraper](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SkysD-1.0.0.zip) | `SkysD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.8 MB |
| [Phoenix's Skyscraper](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SkysP-1.0.0.zip) | `SkysP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 32.2 MB |
| [Snake Slaughterhouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SlauS-1.0.0.zip) | `SlauS` | stock | 1.0.0 | Story, Deathmatch, MercDeathmatch | 15.9 MB |
| [Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-StatD-1.0.0.zip) | `StatD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.2 MB |
| [Enhanced Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-StatE-1.0.0.zip) | `StatE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.2 MB |
| [Ps2 Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-StatS-1.0.0.zip) | `StatS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.4 MB |
| [Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SteeD-1.0.0.zip) | `SteeD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.9 MB |
| [Enhanced Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SteeE-1.0.0.zip) | `SteeE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.8 MB |
| [Phoenix's Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SteeP-1.0.0.zip) | `SteeP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.9 MB |
| [Enhanced Steel Squat 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-SteeT-1.0.0.zip) | `SteeT` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.0 MB |
| [Stronghold](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-StroD-1.0.0.zip) | `StroD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.3 MB |
| [Terminus](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TermD-1.0.0.zip) | `TermD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 41.8 MB |
| [TME30](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TME30-1.0.0.zip) | `TME30` | stock | 1.0.0 | MercDeathmatch | 13.6 MB |
| [TME32](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TME32-1.0.0.zip) | `TME32` | stock | 1.0.0 | Story, MercDeathmatch | 13.5 MB |
| [TME33](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TME33-1.0.0.zip) | `TME33` | stock | 1.0.0 | MercDeathmatch | 14.9 MB |
| [TSP20](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TSP20-1.0.0.zip) | `TSP20` | stock | 1.0.0 | MercDeathmatch | 7.4 MB |
| [TSP21](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TSP21-1.0.0.zip) | `TSP21` | stock | 1.0.0 | Story, MercDeathmatch | 6.8 MB |
| [TSP22](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TSP22-1.0.0.zip) | `TSP22` | stock | 1.0.0 | Story, MercDeathmatch | 7.2 MB |
| [TSP23](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TSP23-1.0.0.zip) | `TSP23` | stock | 1.0.0 | Story, MercDeathmatch | 7.3 MB |
| [Exam Tuto](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-TSP29-1.0.0.zip) | `TSP29` | stock | 1.0.0 | Story, MercDeathmatch | 8.4 MB |
| [Enhanced Vertigo Plaza](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-VertE-1.0.0.zip) | `VertE` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Ump Vertigo Plaza](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-VertU-1.0.0.zip) | `VertU` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.5 MB |
| [Enh Vertigo Plaza Extraction](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-VertX-1.0.0.zip) | `VertX` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.1 MB |
| [Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-WAR10-1.0.0.zip) | `WAR10` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.6 MB |
| [Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-WareD-1.0.0.zip) | `WareD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.9 MB |
| [Phoenix's Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-WareP-1.0.0.zip) | `WareP` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.5 MB |
| [Zioplex](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ZiopD-1.0.0.zip) | `ZiopD` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.7 MB |
| [Zioplex Sabotage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-ZiopS-1.0.0.zip) | `ZiopS` | stock | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.9 MB |
| [Moonlight Park](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/original-MoonD-1.0.0.zip) | `MoonD` | original | 1.0.0 | Story, Deathmatch, MercDeathmatch | 139.5 MB |
| [Shipment](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/original-ShipD-1.0.0.zip) | `ShipD` | original | 1.0.0 | Story, Deathmatch, MercDeathmatch | 49.1 MB |
| [Abandoned Bunker](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-ABK27-1.0.0.zip) | `ABK27` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 5.2 MB |
| [Argus Hq](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-AHQ06-1.0.0.zip) | `AHQ06` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 14.2 MB |
| [Executive Suites Beta](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-apar01-1.0.0.zip) | `apar01` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 12.5 MB |
| [Base Argus](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-ARG01-1.0.0.zip) | `ARG01` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.4 MB |
| [Athlon](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-ATH05-1.0.0.zip) | `ATH05` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 9.4 MB |
| [Bank Mixed](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-BNK11b-1.0.0.zip) | `BNK11b` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.1 MB |
| [Buddhist Temple V0.5](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-BuddhistTemple-1.0.0.zip) | `BuddhistTemple` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 4.6 MB |
| [1v1 Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-c1v1esl-1.0.0.zip) | `c1v1esl` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.8 MB |
| [Sanctuary](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-CHU01-1.0.0.zip) | `CHU01` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.6 MB |
| [Chemical Industries 1.2](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-CI-1.0.0.zip) | `CI` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 11.7 MB |
| [Pyrocryptic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-CRY01-1.0.0.zip) | `CRY01` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 28.2 MB |
| [Clarity Soft Inc.](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-CSI01-1.0.0.zip) | `CSI01` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 35.8 MB |
| [Cargoship_beta](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-CSP11-1.0.0.zip) | `CSP11` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 17.1 MB |
| [1on1 Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-D1vs1esl-1.0.0.zip) | `D1vs1esl` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 7.7 MB |
| [Museum Aftermath](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-DDMUS-1.0.0.zip) | `DDMUS` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 7.7 MB |
| [Dimmykron Estate](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-DIM01-1.0.0.zip) | `DIM01` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 3.3 MB |
| [Dm Contain Beta](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-dm_contain-1.0.0.zip) | `dm_contain` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 8.7 MB |
| [Dock](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-DOC14-1.0.0.zip) | `DOC14` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 10.9 MB |
| [Eden](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-EDE64-1.0.0.zip) | `EDE64` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.9 MB |
| [1 On 1 Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-G1v1esl-1.0.0.zip) | `G1v1esl` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 25.9 MB |
| [Heliport_1.1](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-HELI02-1.0.0.zip) | `HELI02` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 30.2 MB |
| [Horizon Corporation](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-Horizon-1.0.0.zip) | `Horizon` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.6 MB |
| [Hotel 57](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-Hotel2-1.0.0.zip) | `Hotel2` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.5 MB |
| [Lagerhaus](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-Lagerhaus-1.0.0.zip) | `Lagerhaus` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 8.1 MB |
| [1 On 1 Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-m1v1esl2-1.0.0.zip) | `m1v1esl2` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 6.2 MB |
| [Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-Map17-1.0.0.zip) | `Map17` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.9 MB |
| [Mount Hospital Mod](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-MHO05_MOD-1.0.0.zip) | `MHO05_MOD` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.8 MB |
| [Museum Classic (n)](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-MUS08b-1.0.0.zip) | `MUS08b` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.3 MB |
| [Club House Vs Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-museumvsclubhouse-1.0.0.zip) | `museumvsclubhouse` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.2 MB |
| [Island](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-new-island-1.0.0.zip) | `new-island` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 8.5 MB |
| [Artillery Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-NNY02-1.0.0.zip) | `NNY02` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 6.0 MB |
| [Offshore Oilrig](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-OIL33-1.0.0.zip) | `OIL33` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.4 MB |
| [Outpost](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-OUT55-1.0.0.zip) | `OUT55` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 9.5 MB |
| [Panama Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-panama02-1.0.0.zip) | `panama02` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.1 MB |
| [**base Secrete De Red_flash**](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-RED1-1.0.0.zip) | `RED1` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.5 MB |
| [Rocamadour](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-rocamadour-1.0.0.zip) | `rocamadour` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 12.2 MB |
| [Ump Schermerhorn](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-SCH04-1.0.0.zip) | `SCH04` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.9 MB |
| [School](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-SCL03_ED-1.0.0.zip) | `SCL03_ED` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 7.6 MB |
| [Shadow Moses](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-SDM06-1.0.0.zip) | `SDM06` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 17.7 MB |
| [Ump Vertigo Plaza 2005](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-SKY08-1.0.0.zip) | `SKY08` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 10.6 MB |
| [Ump Vertigo Classic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-SKYMZ1-1.0.0.zip) | `SKYMZ1` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Spyscraper](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-spyscraper-1.0.0.zip) | `spyscraper` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 11.5 MB |
| [Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-SQU13-1.0.0.zip) | `SQU13` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.8 MB |
| [State Union](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-State02-1.0.0.zip) | `State02` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [[-- Station Orbitale --]](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-stationorb-1.0.0.zip) | `stationorb` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.2 MB |
| [Stockhouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-STH02-1.0.0.zip) | `STH02` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.8 MB |
| [Sublabs](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-sub18-1.0.0.zip) | `sub18` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.5 MB |
| [Tank Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-TAF06-1.0.0.zip) | `TAF06` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.9 MB |
| [Red Tower Corps.](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-tower1-1.0.0.zip) | `tower1` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 8.3 MB |
| [Ump Cinema](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-UMPCINC-1.0.0.zip) | `UMPCINC` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.5 MB |
| [Ump Krauser Lab](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-UMPKRA07-1.0.0.zip) | `UMPKRA07` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 7.8 MB |
| [Ump Hospital Classic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-UMPMHCLASSIC-1.0.0.zip) | `UMPMHCLASSIC` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.1 MB |
| [Suspect Dojo V.7](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-USDOJO-1.0.0.zip) | `USDOJO` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 1.5 MB |
| [Warehouse (smbp)](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-WAREXT-1.0.0.zip) | `WAREXT` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.6 MB |
| [Zioplex](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-ZCT03-1.0.0.zip) | `ZCT03` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.3 MB |
| [Ump Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-ZPB17-1.0.0.zip) | `ZPB17` | community | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.6 MB |
| [Oilrig2](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/enhanced-OffsE-1.0.0.zip) | `OffsE` | enhanced | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 22.6 MB |
| [Clarity Soft](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/recovered-ClarD-1.0.0.zip) | `ClarD` | recovered | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.9 MB |
| [Eden](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/recovered-EDE64-1.0.0.zip) | `EDE64` | recovered | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.5 MB |
| [Heliport_1.1](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/recovered-HELI02-1.0.0.zip) | `HELI02` | recovered | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 30.0 MB |
| [Offshore Oilrig](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/recovered-OffsD-1.0.0.zip) | `OffsD` | recovered | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.0 MB |
| [Sublabs](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/recovered-sub18-1.0.0.zip) | `sub18` | recovered | 1.0.0 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.4 MB |
| [Calypso Casino](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-CalyD-1.0.0.zip) | `CalyD` | ports | 1.0.0 | Story, Deathmatch, MercDeathmatch | 666.5 KB |
| [Blackwing](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_BLKG1-1.0.0.zip) | `SCDA_BLKG1` | ports | 1.0.0 | - | 19.2 MB |
| [Boss House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_BOSG2-1.0.0.zip) | `SCDA_BOSG2` | ports | 1.0.0 | - | 17.3 MB |
| [Dawn Waves](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_DWG-1.0.0.zip) | `SCDA_DWG` | ports | 1.0.0 | - | 22.5 MB |
| [Motorway 90](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_MOTG4-1.0.0.zip) | `SCDA_MOTG4` | ports | 1.0.0 | - | 31.8 MB |
| [Red Diamond](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_REDG6-1.0.0.zip) | `SCDA_REDG6` | ports | 1.0.0 | - | 19.8 MB |
| [Slaughterhouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_SLHG7-1.0.0.zip) | `SCDA_SLHG7` | ports | 1.0.0 | - | 27.1 MB |
| [Terminus](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_TERG5-1.0.0.zip) | `SCDA_TERG5` | ports | 1.0.0 | - | 22.1 MB |
| [USS Wisdom](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/ports-SCDA_USSG8-1.0.0.zip) | `SCDA_USSG8` | ports | 1.0.0 | - | 23.4 MB |

</details>

Index updated 2026-10-28T15:22:12Z.
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
