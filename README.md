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
| `original` | 2 | 188.8 MB | New maps made for SCCT Versus (SCCT-Maps `release/`) |
| `community` | 56 | 754.6 MB | The community map pack |
| `enhanced` | 1 | 22.8 MB | Edited versions of existing maps |
| `recovered` | 5 | 124.8 MB | Existing maps rebuilt as editable maps |
| `ports` | 9 | 183.9 MB | Maps ported from other games |
| **All** | **165** | **2.8 GB** | |

| Shared pack | Version | Size | Contents |
| --- | --- | ---: | --- |
| `core` | 0.8.33.1 | 77.2 MB | classes.json, render, fx, ui, maps |
| `chars` | 0.8.25.1 | 339.0 MB | chars |
| `audio` | 0.8.25.1 | 74.5 MB | audio |

<details><summary>Every map</summary>

| Map | Code | Category | Version | Modes | Size |
| --- | --- | --- | --- | --- | ---: |
| [Aquarius](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-AQU03-1.0.1.zip) | `AQU03` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.2 MB |
| [Aquarius](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-AquaD-1.0.1.zip) | `AquaD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.2 MB |
| [Enhanced Aquarius](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-AquaE-1.0.1.zip) | `AquaE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.2 MB |
| [Enhanced Aquarius 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-AquaT-1.0.1.zip) | `AquaT` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.3 MB |
| [Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-BankD-1.0.1.zip) | `BankD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Phoenix's Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-BankP-1.0.1.zip) | `BankP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-BNK11-1.0.1.zip) | `BNK11` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.1 MB |
| [Enhanced Cinema](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-CineE-1.0.1.zip) | `CineE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 10.2 MB |
| [Enhanced Cinema Sabotage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-CineS-1.0.1.zip) | `CineS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.8 MB |
| [Ump Cinema](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-CineU-1.0.1.zip) | `CineU` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-CLU04-1.0.1.zip) | `CLU04` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.5 MB |
| [Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ClubD-1.0.1.zip) | `ClubD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.5 MB |
| [Enhanced Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ClubE-1.0.1.zip) | `ClubE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.5 MB |
| [Shadow House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ClubS-1.0.1.zip) | `ClubS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.1 MB |
| [Enhanced Club House 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ClubT-1.0.1.zip) | `ClubT` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.6 MB |
| [Snake Cpusa](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-CpusS-1.0.1.zip) | `CpusS` | stock | 1.0.1 | Story, Deathmatch, MercDeathmatch | 30.0 MB |
| [Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-DeftD-1.0.1.zip) | `DeftD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.0 MB |
| [Snake Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-DeftS-1.0.1.zip) | `DeftS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.9 MB |
| [Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-DTK09-1.0.1.zip) | `DTK09` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.6 MB |
| [Entry](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-Entry-1.0.0.zip) | `Entry` | stock | 1.0.0 | - | 10.8 MB |
| [Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-FAC05-1.0.1.zip) | `FAC05` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.7 MB |
| [Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-FactD-1.0.1.zip) | `FactD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.8 MB |
| [Enhanced Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-FactE-1.0.1.zip) | `FactE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.8 MB |
| [Phoenix's Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-FactP-1.0.1.zip) | `FactP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.7 MB |
| [Enhanced Factory 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-FactT-1.0.1.zip) | `FactT` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.8 MB |
| [Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-GAR01-1.0.1.zip) | `GAR01` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.8 MB |
| [Snake Ghost Town](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-GhosS-1.0.1.zip) | `GhosS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.7 MB |
| [Enhanced Krauser Lab](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-KrauE-1.0.1.zip) | `KrauE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.7 MB |
| [Ump Krauser Lab](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-KrauU-1.0.1.zip) | `KrauU` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.0 MB |
| [Lobby](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/stock-Lobby-1.0.0.zip) | `Lobby` | stock | 1.0.0 | - | 10.8 MB |
| [River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-Map12-1.0.1.zip) | `Map12` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.8 MB |
| [Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MIS02-1.0.1.zip) | `MIS02` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.3 MB |
| [Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MissD-1.0.1.zip) | `MissD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.6 MB |
| [Enhanced Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MissE-1.0.1.zip) | `MissE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.6 MB |
| [Phoenix's Missile Strike](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MissP-1.0.1.zip) | `MissP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.9 MB |
| [Enhanced Mount Hospital](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MounE-1.0.1.zip) | `MounE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.6 MB |
| [Enh Mount Hospital Sabo](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MounS-1.0.1.zip) | `MounS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.0 MB |
| [Ump Mount Hospital](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MounU-1.0.1.zip) | `MounU` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.6 MB |
| [Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MUS08-1.0.1.zip) | `MUS08` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.3 MB |
| [Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MuseD-1.0.1.zip) | `MuseD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Enhanced Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MuseE-1.0.1.zip) | `MuseE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Museum 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-MuseT-1.0.1.zip) | `MuseT` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.1 MB |
| [Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ORP06-1.0.1.zip) | `ORP06` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.2 MB |
| [Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-OrphD-1.0.1.zip) | `OrphD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.7 MB |
| [Enhanced Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-OrphE-1.0.1.zip) | `OrphE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.7 MB |
| [Ps2 Orphanage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-OrphS-1.0.1.zip) | `OrphS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.8 MB |
| [Enhanced Orphanage 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-OrphT-1.0.1.zip) | `OrphT` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 15.7 MB |
| [Panama Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PanaD-1.0.1.zip) | `PanaD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.1 MB |
| [Snake Panama Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PanaS-1.0.1.zip) | `PanaS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.9 MB |
| [Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PolaD-1.0.1.zip) | `PolaD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.4 MB |
| [Enhanced Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PolaE-1.0.1.zip) | `PolaE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.4 MB |
| [Phoenix's Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PolaP-1.0.1.zip) | `PolaP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.4 MB |
| [Enhanced Polar Base 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PolaT-1.0.1.zip) | `PolaT` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.4 MB |
| [Prison](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PrisD-1.0.1.zip) | `PrisD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 88.7 MB |
| [Pyrocryptic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-PyroD-1.0.1.zip) | `PyroD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.5 MB |
| [River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-RiveD-1.0.1.zip) | `RiveD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Enhanced River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-RiveE-1.0.1.zip) | `RiveE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Phoenix's River Mall](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-RiveP-1.0.1.zip) | `RiveP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Sanctuary](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SancD-1.0.1.zip) | `SancD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.3 MB |
| [Enhanced Sanctuary](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SancE-1.0.1.zip) | `SancE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.6 MB |
| [Enhanced Schermerhorn](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ScheE-1.0.1.zip) | `ScheE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.0 MB |
| [Ump Schermerhorn](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ScheU-1.0.1.zip) | `ScheU` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 17.3 MB |
| [Shadow Moses](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ShadD-1.0.1.zip) | `ShadD` | stock | 1.0.1 | Story, Deathmatch, MercDeathmatch | 21.1 MB |
| [Phoenix's Shadow Moses](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ShadP-1.0.1.zip) | `ShadP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.9 MB |
| [Skyscraper](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SkysD-1.0.1.zip) | `SkysD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.8 MB |
| [Phoenix's Skyscraper](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SkysP-1.0.1.zip) | `SkysP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 32.2 MB |
| [Snake Slaughterhouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SlauS-1.0.1.zip) | `SlauS` | stock | 1.0.1 | Story, Deathmatch, MercDeathmatch | 15.9 MB |
| [Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-StatD-1.0.1.zip) | `StatD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.5 MB |
| [Enhanced Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-StatE-1.0.1.zip) | `StatE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.5 MB |
| [Ps2 Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-StatS-1.0.1.zip) | `StatS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.6 MB |
| [Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SteeD-1.0.1.zip) | `SteeD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.4 MB |
| [Enhanced Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SteeE-1.0.1.zip) | `SteeE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.4 MB |
| [Phoenix's Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SteeP-1.0.1.zip) | `SteeP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.4 MB |
| [Enhanced Steel Squat 3v3](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-SteeT-1.0.1.zip) | `SteeT` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.5 MB |
| [Stronghold](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-StroD-1.0.1.zip) | `StroD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.4 MB |
| [Terminus](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TermD-1.0.1.zip) | `TermD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 41.8 MB |
| [TME30](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TME30-1.0.1.zip) | `TME30` | stock | 1.0.1 | MercDeathmatch | 14.1 MB |
| [TME32](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TME32-1.0.1.zip) | `TME32` | stock | 1.0.1 | Story, MercDeathmatch | 13.5 MB |
| [TME33](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TME33-1.0.1.zip) | `TME33` | stock | 1.0.1 | MercDeathmatch | 15.9 MB |
| [TSP20](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TSP20-1.0.1.zip) | `TSP20` | stock | 1.0.1 | MercDeathmatch | 8.0 MB |
| [TSP21](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TSP21-1.0.1.zip) | `TSP21` | stock | 1.0.1 | Story, MercDeathmatch | 7.2 MB |
| [TSP22](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TSP22-1.0.1.zip) | `TSP22` | stock | 1.0.1 | Story, MercDeathmatch | 7.2 MB |
| [TSP23](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TSP23-1.0.1.zip) | `TSP23` | stock | 1.0.1 | Story, MercDeathmatch | 7.4 MB |
| [Exam Tuto](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-TSP29-1.0.1.zip) | `TSP29` | stock | 1.0.1 | Story, MercDeathmatch | 8.6 MB |
| [Enhanced Vertigo Plaza](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-VertE-1.0.1.zip) | `VertE` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.9 MB |
| [Ump Vertigo Plaza](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-VertU-1.0.1.zip) | `VertU` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.5 MB |
| [Enh Vertigo Plaza Extraction](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-VertX-1.0.1.zip) | `VertX` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.1 MB |
| [Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-WAR10-1.0.1.zip) | `WAR10` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.6 MB |
| [Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-WareD-1.0.1.zip) | `WareD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.9 MB |
| [Phoenix's Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-WareP-1.0.1.zip) | `WareP` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.5 MB |
| [Zioplex](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ZiopD-1.0.1.zip) | `ZiopD` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.7 MB |
| [Zioplex Sabotage](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/stock-ZiopS-1.0.1.zip) | `ZiopS` | stock | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.9 MB |
| [Moonlight Park](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/original-MoonD-1.0.1.zip) | `MoonD` | original | 1.0.1 | Story, Deathmatch, MercDeathmatch | 139.6 MB |
| [Shipment](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/original-ShipD-1.0.1.zip) | `ShipD` | original | 1.0.1 | Story, Deathmatch, MercDeathmatch | 49.1 MB |
| [Abandoned Bunker](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-ABK27-1.0.1.zip) | `ABK27` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 5.3 MB |
| [Argus Hq](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-AHQ06-1.0.1.zip) | `AHQ06` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 15.1 MB |
| [Executive Suites Beta](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-apar01-1.0.1.zip) | `apar01` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 12.7 MB |
| [Base Argus](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-ARG01-1.0.1.zip) | `ARG01` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.5 MB |
| [Athlon](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-ATH05-1.0.1.zip) | `ATH05` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 9.6 MB |
| [Bank Mixed](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-BNK11b-1.0.1.zip) | `BNK11b` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.1 MB |
| [Buddhist Temple V0.5](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-BuddhistTemple-1.0.1.zip) | `BuddhistTemple` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 4.6 MB |
| [1v1 Club House](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-c1v1esl-1.0.1.zip) | `c1v1esl` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 10.3 MB |
| [Sanctuary](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-CHU01-1.0.1.zip) | `CHU01` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 16.6 MB |
| [Chemical Industries 1.2](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-CI-1.0.1.zip) | `CI` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 11.7 MB |
| [Pyrocryptic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-CRY01-1.0.1.zip) | `CRY01` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 28.3 MB |
| [Clarity Soft Inc.](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-CSI01-1.0.1.zip) | `CSI01` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 35.8 MB |
| [Cargoship_beta](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-CSP11-1.0.1.zip) | `CSP11` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 17.6 MB |
| [1on1 Deftech Belew](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-D1vs1esl-1.0.1.zip) | `D1vs1esl` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 7.7 MB |
| [Museum Aftermath](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-DDMUS-1.0.1.zip) | `DDMUS` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 7.7 MB |
| [Dimmykron Estate](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-DIM01-1.0.0.zip) | `DIM01` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 3.3 MB |
| [Dm Contain Beta](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-dm_contain-1.0.1.zip) | `dm_contain` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 8.7 MB |
| [Dock](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-DOC14-1.0.1.zip) | `DOC14` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 11.1 MB |
| [Eden](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-EDE64-1.0.1.zip) | `EDE64` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 24.6 MB |
| [1 On 1 Station](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-G1v1esl-1.0.1.zip) | `G1v1esl` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 27.2 MB |
| [Heliport_1.1](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-HELI02-1.0.1.zip) | `HELI02` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.4 MB |
| [Horizon Corporation](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-Horizon-1.0.1.zip) | `Horizon` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.7 MB |
| [Hotel 57](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-Hotel2-1.0.1.zip) | `Hotel2` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.7 MB |
| [Lagerhaus](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-Lagerhaus-1.0.1.zip) | `Lagerhaus` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 8.6 MB |
| [1 On 1 Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-m1v1esl2-1.0.1.zip) | `m1v1esl2` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 6.2 MB |
| [Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-Map17-1.0.1.zip) | `Map17` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [Mount Hospital Mod](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-MHO05_MOD-1.0.1.zip) | `MHO05_MOD` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.9 MB |
| [Museum Classic (n)](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-MUS08b-1.0.1.zip) | `MUS08b` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.4 MB |
| [Club House Vs Museum](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-museumvsclubhouse-1.0.1.zip) | `museumvsclubhouse` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.8 MB |
| [Island](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-new-island-1.0.1.zip) | `new-island` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 8.7 MB |
| [Artillery Warehouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-NNY02-1.0.1.zip) | `NNY02` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 6.2 MB |
| [Offshore Oilrig](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-OIL33-1.0.1.zip) | `OIL33` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.7 MB |
| [Outpost](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-OUT55-1.0.1.zip) | `OUT55` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 9.8 MB |
| [Panama Bank](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-panama02-1.0.1.zip) | `panama02` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 21.1 MB |
| [**base Secrete De Red_flash**](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-RED1-1.0.1.zip) | `RED1` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.8 MB |
| [Rocamadour](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-rocamadour-1.0.1.zip) | `rocamadour` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 12.2 MB |
| [Ump Schermerhorn](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-SCH04-1.0.1.zip) | `SCH04` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 19.9 MB |
| [School](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-SCL03_ED-1.0.1.zip) | `SCL03_ED` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 7.9 MB |
| [Shadow Moses](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-SDM06-1.0.1.zip) | `SDM06` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 17.9 MB |
| [Ump Vertigo Plaza 2005](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-SKY08-1.0.1.zip) | `SKY08` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 10.9 MB |
| [Ump Vertigo Classic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-SKYMZ1-1.0.1.zip) | `SKYMZ1` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.4 MB |
| [Spyscraper](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-spyscraper-1.0.1.zip) | `spyscraper` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 11.5 MB |
| [Steel Squat](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-SQU13-1.0.1.zip) | `SQU13` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 18.4 MB |
| [State Union](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-State02-1.0.1.zip) | `State02` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [[-- Station Orbitale --]](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-stationorb-1.0.1.zip) | `stationorb` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.2 MB |
| [Stockhouse](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-STH02-1.0.1.zip) | `STH02` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 22.2 MB |
| [Sublabs](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-sub18-1.0.1.zip) | `sub18` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.2 MB |
| [Tank Factory](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-TAF06-1.0.1.zip) | `TAF06` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.2 MB |
| [Red Tower Corps.](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-tower1-1.0.1.zip) | `tower1` | community | 1.0.1 | Story, Deathmatch, MercDeathmatch | 8.5 MB |
| [Ump Cinema](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-UMPCINC-1.0.1.zip) | `UMPCINC` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 12.5 MB |
| [Ump Krauser Lab](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-UMPKRA07-1.0.1.zip) | `UMPKRA07` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 7.8 MB |
| [Ump Hospital Classic](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-UMPMHCLASSIC-1.0.1.zip) | `UMPMHCLASSIC` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.1 MB |
| [Suspect Dojo V.7](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.28/community-USDOJO-1.0.0.zip) | `USDOJO` | community | 1.0.0 | Story, Deathmatch, MercDeathmatch | 1.5 MB |
| [Warehouse (smbp)](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-WAREXT-1.0.1.zip) | `WAREXT` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 11.6 MB |
| [Zioplex](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-ZCT03-1.0.1.zip) | `ZCT03` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 13.3 MB |
| [Ump Polar Base](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/community-ZPB17-1.0.1.zip) | `ZPB17` | community | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 9.8 MB |
| [Oilrig2](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/enhanced-OffsE-1.0.1.zip) | `OffsE` | enhanced | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 22.8 MB |
| [Clarity Soft](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/recovered-ClarD-1.0.1.zip) | `ClarD` | recovered | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 32.0 MB |
| [Eden](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/recovered-EDE64-1.0.1.zip) | `EDE64` | recovered | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 24.1 MB |
| [Heliport_1.1](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/recovered-HELI02-1.0.1.zip) | `HELI02` | recovered | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 31.3 MB |
| [Offshore Oilrig](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/recovered-OffsD-1.0.1.zip) | `OffsD` | recovered | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 23.2 MB |
| [Sublabs](https://github.com/Lumbridge/OpenSCCT-Content/releases/download/content-2026.10.29/recovered-sub18-1.0.1.zip) | `sub18` | recovered | 1.0.1 | Story, DiskHunt, Deathmatch, MercDeathmatch | 14.1 MB |
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

Index updated 2026-10-29T03:09:42Z.
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
