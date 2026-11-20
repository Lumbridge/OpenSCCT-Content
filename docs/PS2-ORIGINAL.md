# Original PS2 Versus collection

Fourteen original PlayStation 2 Versus levels are delivered as separate OpenSCCT
packs, including both tutorials. Package codes and display names end in `P`
(`ORP14P`, **Orphanage P**), so existing maps retain their identities.

The native Enhanced/Reloaded packages, original disc input hashes, objective
asset provenance and independent audit reports are documented in
[SCCT-Maps](https://github.com/OpenSCCT/SCCT-Maps/tree/main/ports/chaos-theory-ps2).
The source metadata and converter release are independent of the native release.

## Runtime and validation gate

Use **OpenSCCT 0.8.160 or newer** for the current collection. Version 0.8.157
fixed normal map-picker access; 0.8.158 adds the source-verified vial reset and
right thigh attachment corrections used by the 1.0.1 update. Version 0.8.160
consumes the explicit PS2 world trace and additive material metadata in 1.0.2.

The immutable v1 maps and converter were built and gameplay-tested against
0.8.156, source commit `6ea666373e28220413474cc98b4208901fd47c8b`. That historical
provenance is unchanged. Real standing/crouched pickup and a computer interaction
with the original90-unit use endpoint pass. The content index retains its
existing format; native Enhanced/Reloaded validation is tracked separately.

Source/serialization/pixel/geometry/animation audits pass. The real OpenSCCT
client/server objective smoke passes on DTK02P, including the separate vial,
console animations and panner, replicated alarm, modem, destruction particles and
carried-vial binding. All fourteen maps pass live load/render captures. The
native v1 release separately passed its recorded menu/match checks. These checks
do not claim fourteen completed matches.

## Version 1.0.1

Eleven changed packs receive version 1.0.1. Cinema and both tutorials keep their
byte-identical 1.0.0 packs and catalog entries. All fourteen IDs and P-suffixed
names remain stable, and no shared pack is repacked.

The update preserves the original vial mesh through initialization and reset,
and uses the source right thigh attachment for carrying. Source-backed Station
Neutralization completes through normal Use without carrying a vial; Extraction
retains pickup, carrying and delivery. These are separate original modes.

Six converted source SDCs replace 62 reviewed player-facing fields with original
English disc text or recorded literal translations where the localization cook
differs. Actor IDs, tags, events and script keys are unchanged. The other eight
source SDCs and all preview images remain unchanged.

The revised runtime passes its recorded input, reset, visual and network checks.
The independent content audit preserves geometry, lighting, render, audio,
collision, traversal and UI data. These checks do not claim fourteen completed
matches. The source revision and converter are recorded separately from the
immutable 1.0.0 source/archive history. Native Enhanced/Reloaded console work is
a separate Neutralization-only revision and does not change OpenSCCT's modes.

## Version 1.0.2

All fourteen packs receive version 1.0.2 with explicit
`LevelInfo.bPS2WorldGeometryTrace` metadata. The original PS2 native world-mesh
predicate accepts level geometry without the additional PC pawn/block-players
gate. Mount Hospital's staircase beneath the Rooms 200 / Lift signs already
had collision geometry; this update retains the original flags and selects
the source trace rule. Runtime defaults for PC maps stay unchanged.

Only Mount Hospital has render payload changes: three existing beam colour
accessors recover the cooked GS vertex colours, and one proved material gets
its original normal-view fixed additive coefficient, 80/128. Positions,
indices, normals, UVs, instances, collision, audio and catalogue pictures are
unchanged. A broad white rectangle becomes a faded shaft in Standard and Fast;
a substantial saturated central patch remains unresolved. This update does not
fully resolve the Hospital lighting report. No captured original PS2 frame
was used to claim pixel parity.

OpenSCCT 0.8.160 also fixes pre-bind script collision overrides, which prevented
Deftech's logical modem-placement volumes from remaining nonblocking; preserves
reliable hack message order; and faces PS2 console interactions toward the
case rather than their forward-offset touch cylinders. Recorded rendered
authority/client checks cover both lifts, all three standing exit routes,
Hospital stair ascent/descent and close console use. Original team restrictions,
hack requirements and encroachment retries are preserved. Crouched continuous
pressure at one grazing exit edge can retrigger the original retry response;
back-off, wait and reapproach crossed all three routes in the focused headless
check. The native encroachment caller remains unverified.

Cinema's eight authored panels were profiled with normal approach/hack input,
third-person camera and audio simulation at 2560x1440 on an RTX 4070 SUPER in
both renderers. Occasional hitches were recorded, but the reported sustained
collapse was not reproduced. There is no speculative Cinema performance fix.
The report concerns Fast; the exact triggering panel and reporting hardware
remain unconfirmed.
These checks use separate replicated authority/client worlds in one process,
not separate-machine internet sessions or fourteen completed matches.

The indexed source SDCs are unchanged. The new
[converter source bundle](https://github.com/OpenSCCT/OpenSCCT-Content/releases/download/content-2026.11.16/SCCT-PS2-OpenSCCT-converter-source-v1.0.2.zip)
and its
[manifest](https://github.com/OpenSCCT/OpenSCCT-Content/releases/download/content-2026.11.16/SCCT-PS2-OpenSCCT-converter-source-v1.0.2.manifest.json)
document the bounded frozen-baseline staging procedure. A fresh full GLB export
is not claimed byte-identical. The index generator records this manifest's
SHA-256 and the exact supported runtime commit. All 165 unrelated map entries,
the three shared packs, PS2 source origins, names, modes and catalogue payloads
are preserved.

## Hospital version 1.0.3

Mount Hospital P receives a render-only correction for the remaining bright
patch. The original PS2 packet builder and draw caller select each actor's
nonempty lighting instance before the mesh's base vertex-colour stream.
The previous conversion selected the brighter base stream instead.

The seven beam actors now retain their seven distinct original per-instance
streams, with 176 colours each. The source-black rim and interior layers stay
black. The shared geometry, UVs, positions, material gain and glow settings are
unchanged. Fixed-camera Standard and Fast captures show the shaft and readable
wall signs without the saturated patch. All seven instances were checked from
two views in each renderer.

The correction is grounded in the shipped PS2 ELF and original colour arrays.
Recorded original PS2 gameplay was inspected as a visual reference; an exactly
matched original framebuffer capture was not available, so pixel parity and
the original PS2 glow algorithm are not claimed.

Only Hospital's full/simulation archive manifests advance to 1.0.3. Its actual
simulation payload and multiplayer content hash remain unchanged. The other
178 indexed maps, existing shared packs, source SDC, objectives, collision,
audio, UI and catalogue pictures are preserved. OpenSCCT 0.8.160 remains the
supported runtime; a new runtime download is unnecessary.

The [1.0.3 converter source bundle](https://github.com/OpenSCCT/OpenSCCT-Content/releases/download/content-2026.11.16-2/SCCT-PS2-OpenSCCT-converter-source-v1.0.3.zip)
and [manifest](https://github.com/OpenSCCT/OpenSCCT-Content/releases/download/content-2026.11.16-2/SCCT-PS2-OpenSCCT-converter-source-v1.0.3.manifest.json)
retain the earlier source snapshot and add the explicit per-actor override,
synthetic regression tests and a bounded reproduction procedure over the
immutable 1.0.2 pack. Fresh full-export byte identity is not claimed.

## Prepared inputs

The reviewable local staging plan is `staging/ps2-original/inputs.json` (git
ignored), generated from the conversion workspace's `work/ps2-build` and frozen
native release plan. It records every source map SHA-256, canonical SVMap
manifest hash, existing shared requirements and current runtime release.

Each map includes its own PS2 assets and original objective overlay. The original
UI contributes 50 preview/loading images to the per-map catalogue entries.

Reuse the three existing indexed shared packs unchanged:

| Pack | Existing version | Role |
| --- | --- | --- |
| `core` | `0.8.91.1` | Existing shared classes and game data |
| `chars` | `0.8.152.1` | Existing character pack |
| `audio` | `0.8.152.1` | Existing shared audio |

The PS2 build names the existing `classes` and `audio` hash anchors. Its partial
`shared/` folder is not a replacement for a complete shared build. The installed
shared tree can contain local additions and must not be repacked as a new shared
release for this collection.

The prepared `prepare_occ_staging.py` wrapper calls the repository's existing
`occ.cmd_pack` for map archives only, leaving `plan.shared` empty and the existing
index untouched. It verifies native source bytes with raw SHA-256, SVMap files
with `svmbuild.canonical.hash_map`, and all `requires` against the existing index.
It also supplies the P-suffix titles and original UI images to per-map catalogue
entries without modifying a shared pack.

## Local staging procedure

1. Complete the final native and OpenSCCT actual-input validation receipts and
   publish the exact supported runtime first (0.8.158 for version 1.0.1).
2. Review and commit the SCCT-Maps source metadata. Record that exact commit;
   a pre-conversion commit or all-zero placeholder is not a valid origin.
3. Rerun the wrapper's default preflight against the final files. It writes only
   reviewable staging metadata and creates no archives.
4. Run the wrapper with `--pack`, the real `--source-commit`, builder version and
   `--generator` identifying the reviewed builder/adapter commit. This creates
   the fourteen full and fourteen simulation ZIPs locally. The wrapper refuses
   source mismatches, changed requirements or invalid SVMap hashes.
5. Review `staging/out/plan.json`: fourteen maps, zero skipped maps, no shared
   archives, exact source commit and expected titles/images. Use the ordinary
   `occ.py publish --dry-run` workflow to inspect `index.preview.json`.
6. Publish after the validation and release checks pass. Check that all existing
   shared entries and their hashes remain identical. Publication is authorized;
   these are verification gates, not an additional permission request.

The OpenSCCT release uses an immutable fourteen-map freeze. Later native
endpoint fixes cannot change these pack inputs or their source-origin hashes.

## Objective fidelity

OpenSCCT restores the green vial, original animated computer proxy and recovered
sabotage modem. Forty-one recovered objective objects include two static meshes
with matching attributed geometry/winding and thirteen textures with exact PS2
decoded RGBA pixels. The retained original PS2-authored computer asset has
matching bounds, eighteen bind bones and all seventy-two animation tracks; exact
equivalence of its cooked PS2 GPU vertices is not established.

Four authored zero quaternion tracks become unit identity rotations for glTF,
as proved by the PS2 native matrix code. Their zero positions are preserved;
other rotations, all positions and all key times pass the fourteen-map audit.

The modem active beep is the same-class retail compatibility alias
`Armes_impacts.Armes.ProxMine_ACTI_1`, rather than a claim of exact PS2 PCM. Its
destruction sound uses recovered PS2 PCM. The native PC ports retain their
compatible PC objective flow; the OpenSCCT profile carries the original PS2
presentation and source behavior adaptations.
