# Source maps for the modernisations

The native OpenSCCT launchers use [community.json](../community.json) for optional map downloads. Each recipe names the original community mod files, pins them to a Git commit and checks their SHA-256. The builder reads the required Chaos Theory assets from the player's Steam installation. Both the Godot and Unreal modernisations use the resulting local map.

## Available recipes

The table records a successful local conversion against Steam app 13570, build 252084. Each result has simulation, collision, render and audio data. The map's simulation hash identifies the build that another player or server needs to join. Match play and visual parity across these maps still need separate testing.

| Map | Package | Source files | Steam prerequisites | Simulation hash |
| --- | --- | ---: | ---: | --- |
| [Buddhist Temple 0.5](https://github.com/OpenSCCT/SCCT-Maps/blob/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community/Buddhist%20Temple%200.5/README.md) | `BuddhistTemple` | 3 | 17 | `77b1acbd68535137` |
| [DimmyKron Estate](https://github.com/OpenSCCT/SCCT-Maps/blob/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community/DimmyKron%20Estate/README.md) | `DIM01` | 4 | 10 | `8b6503655fa31177` |
| [DM Contain Beta](https://github.com/OpenSCCT/SCCT-Maps/blob/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community/DM%20Contain%20Beta/README.md) | `dm_contain` | 3 | 30 | `802f836308e9e1f5` |
| [Executive Suites Beta](https://github.com/OpenSCCT/SCCT-Maps/blob/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community/Executive%20Suites%20Beta/README.md) | `apar01` | 4 | 28 | `0420dc3fea443682` |
| [Stockhouse](https://github.com/OpenSCCT/SCCT-Maps/blob/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community/Stockhouse/README.md) | `STH02` | 5 | 51 | `fd13fd7c326d88a0` |
| [SubLabs](https://github.com/OpenSCCT/SCCT-Maps/blob/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community/SubLabs/README.md) | `sub18` | 4 | 45 | `733036c3a5b28dd1` |
| [Suspect Dojo v.7](https://github.com/OpenSCCT/SCCT-Maps/blob/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community/Suspect%20Dojo%20v.7/README.md) | `USDOJO` | 4 | 13 | `f256c5f332a9c647` |

Suspect Dojo uses the stock Club House, Aquarius and Warehouse packages alongside four files from its own mod folder. SubLabs credits .red aka Red_SoN in the original map. The other packages retain their original credits. The converter records editor-only preview asset warnings for Suspect Dojo and Executive Suites. The published recipes have complete gameplay audio references.

## Original PC archive and eligibility

The original PC Map Manager has its own catalogue for the retail engine. Its map packages target that installation. The modernisations offer the reviewed recipes above. The audit below covers all 56 distinct map packages in the archive's pinned community directory, including packs historically grouped there with official DLC and retail variants. The original archive keeps more categories, such as Enhanced and ports. [PC Map Manager](https://github.com/OpenSCCT/SCCT-Map-Manager) · [Pinned map archive](https://github.com/OpenSCCT/SCCT-Maps/tree/a3c948c4bf6250cf471c3edee6e03ef62e63932c/community)

For a private local import, supply your own original mod files and their dependencies in an add-on folder with the original `Packages/` layout. In a configured OpenSCCT checkout, run the following from `content/` with `$steam` set to the local game's `Versus` folder. The report lists missing references for review.

```powershell
python -m svmbuild maps-catalog renderpack maps audio-map --game $steam --addons $ownedMod --maps $mapCode --out $privateOutput --report $report
```

| Archive map | Package | Modernisation status |
| --- | --- | --- |
| 1 on 1 Club House | `c1v1esl` | Variant of an original map. The source archive includes retail geometry or content. |
| 1 on 1 Deftech Belew | `D1vs1esl` | Variant of an original map. The source archive includes retail geometry or content. |
| 1 on 1 Museum | `m1v1esl2` | Variant of an original map. The source archive includes retail geometry or content. |
| 1 on 1 Station | `G1v1esl` | Variant of an original map. The source archive includes retail geometry or content. |
| Abandoned Bunker | `ABK27` | The map imports `STM_MER`, `TXT_MER`, `stm_spy`, absent from the tested Steam install. |
| Argus HQ | `AHQ06` | The map imports `SQU13_txt`, absent from the tested Steam install. |
| Artillery Warehouse | `NNY02` | The map imports `KRA07_Dedouble`, `Prison_STC`, `Prison_TEX`, absent from the tested Steam install. |
| Athlon | `ATH05` | The map imports `Amb_Squat`, `SQU13_STM`, `SQU13_txt`, absent from the tested Steam install. |
| Bank Mixed | `BNK11b` | Variant of an original map. The source archive includes retail geometry or content. |
| Base Argus | `ARG01` | The map imports `Amb_Egouts`, `KRA07_Dedouble`, `MHOsfx_xbox`, absent from the tested Steam install. |
| Base Secrete | `RED1` | The map imports `SQU13_STM`, `SQU13_txt`, absent from the tested Steam install. |
| Buddhist Temple 0.5 | `BuddhistTemple` | Available in the native launcher. |
| Cargoship Beta | `CSP11` | The map imports `SM_Egouts`, `SQU13_STM`, `SQU13_txt`, absent from the tested Steam install. |
| Chemical Industries 1.2 | `CI` | The map imports `Amb_Krauser`, `KRA07_Dedouble`, `MHOtex_xbox`, absent from the tested Steam install. |
| Clarity Soft Inc | `CSI01` | The map imports `Amb_Building`, `Amb_Ini`, `Amb_Krauser`, absent from the tested Steam install. |
| Club House vs Museum | `museumvsclubhouse` | Variant of an original map. The source archive includes retail geometry or content. |
| DimmyKron Estate | `DIM01` | Available in the native launcher. |
| DM Contain Beta | `dm_contain` | Available in the native launcher. |
| Dock | `DOC14` | The conversion has unresolved actor references for fish and mover logic. The pack also references Oilrig assets. |
| Eden | `EDE64` | The map imports `Amb_Building`, `Amb_Egouts`, `Amb_Mount`, absent from the tested Steam install. |
| Executive Suites Beta | `apar01` | Available in the native launcher. |
| Heliport 1.1 | `HELI02` | Heliport’s own source package imports the Steel Squat texture package `SQU13_txt`, which the tested Steam depot lacks. |
| Horizon Corporation | `Horizon` | The map imports `Amb_Krauser`, `Amb_Polarbase`, `KRA07_Dedouble`, absent from the tested Steam install. |
| Hotel 57 | `Hotel2` | The map imports `Amb_Ini`, `Prison_STC`, `STM_INI`, absent from the tested Steam install. |
| Island | `new-island` | Its `Amb_island.uax` is byte-identical to the archived Mount Hospital `Amb_Mount.uax`. Steam lacks the required stock package. |
| Lagerhaus | `Lagerhaus` | Its mesh package imports `Island`. The same Island mesh and texture files occur across multiple authored maps and their original source attribution is unresolved. |
| Mount Hospital MOD | `MHO05_MOD` | Variant of an original map. The source archive includes retail geometry or content. |
| Museum Aftermath | `DDMUS` | Variant of an original map. The source archive includes retail geometry or content. |
| Museum Classic (N) | `MUS08b` | Variant of an original map. The source archive includes retail geometry or content. |
| Offshore Oilrig | `OIL33` | The converted map still references missing presence triggers in its mover logic. |
| Outpost | `OUT55` | The map imports `Amb_Mount`, absent from the tested Steam install. |
| Panama Bank 2.0 | `panama02` | The map imports `Amb_Egouts`, `Amb_Krauser`, `SQU13_STM`, absent from the tested Steam install. |
| Polar Base | `Map17` | Official Polar Base content, outside the baseline Steam depot. |
| Pyrocryptic | `CRY01` | The source readme credits Timothy Wall (BooBerry.Ck). Two distinct Steam recordings use the same ambient stream ID, `Amb_Gare.gar_musicExplo`. The original bank choice remains unknown. |
| Red Tower Corps | `tower1` | The map imports `SQU13_STM`, `SQU13_txt`, `krauser_txt`, absent from the tested Steam install. |
| Rocamadour | `rocamadour` | The map imports `Amb_Squat`, `SM_SKY09`, `SQU13_STM`, absent from the tested Steam install. |
| Sanctuary | `CHU01` | The map imports `Amb_Mount`, `Amb_Polarbase`, `KRA07_Dedouble`, absent from the tested Steam install. |
| School | `SCL03_ED` | The map imports `krauser_stm`, `krauser_txt`, absent from the tested Steam install. |
| Shadow Moses | `SDM06` | Shadow Moses uses a location from Metal Gear Solid. The source assets need a separate provenance review. |
| SpyScraper | `spyscraper` | The map imports `Amb_Building`, `KRA07_Dedouble`, `Prison_STC`, absent from the tested Steam install. |
| State Union | `State02` | The map imports `Amb_Building`, `Amb_Krauser`, `Amb_Mount`, absent from the tested Steam install. |
| Station Orbitale | `stationorb` | The map imports `Map17_STM`, absent from the tested Steam install. |
| Steel Squat (English) | `SQU13` | Official Steel Squat content, outside the baseline Steam depot. |
| Stockhouse | `STH02` | Available in the native launcher. |
| SubLabs | `sub18` | Available in the native launcher. |
| Suspect Dojo v.7 | `USDOJO` | Available in the native launcher. |
| Tank Factory | `TAF06` | The map imports `Amb_Squat`, `SQU13_STM`, `SQU13_txt`, absent from the tested Steam install. |
| UMP Cinema | `UMPCINC` | Uses an original level or its packages from outside this Steam depot. |
| UMP Hospital | `UMPMHCLASSIC` | Uses an original level or its packages from outside this Steam depot. |
| UMP Krauser Lab | `UMPKRA07` | Uses an original level or its packages from outside this Steam depot. |
| UMP Polar Base | `ZPB17` | Uses an original level or its packages from outside this Steam depot. |
| UMP Schermerhorn 1.1 | `SCH04` | Uses an original level or its packages from outside this Steam depot. |
| UMP Vertigo Classic | `SKYMZ1` | Uses an original level or its packages from outside this Steam depot. |
| UMP Vertigo Plaza | `SKY08` | Uses an original level or its packages from outside this Steam depot. |
| Warehouse (SMBP) | `WAREXT` | Variant of an original map. The source archive includes retail geometry or content. |
| Zioplex | `ZCT03` | The map imports `Amb_Building`, `Amb_Krauser`, `Amb_Mount`, absent from the tested Steam install. |

## Reproduce the checks

From the root of this repository, run `python tools/check_community.py --remote`. CI downloads each declared source file at its pinned commit and compares its digest with the recipe and the original package's SHA256SUMS.txt. It also checks map IDs, file paths, allowed extensions, required local files and the absence of converted archives in the feed.

To repeat a local validation, pass `--steam` with a clean `Versus` directory, `--sources` with a local copy of the pinned source tree, `--converted` with the conversion output and `--converter` with the OpenSCCT checkout’s `content/` directory. Repeat `--converted` for additional output folders. The checker verifies all declared local prerequisites, every converted file and simulation hash, and the map audio references.
