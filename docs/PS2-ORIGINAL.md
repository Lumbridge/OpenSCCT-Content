# Original PS2 Versus collection

Fourteen original PlayStation 2 Versus levels are delivered as separate OpenSCCT
packs, including both tutorials. Package codes and display names end in `P`
(`ORP14P`, **Orphanage P**), so existing maps retain their identities.

The native Enhanced/Reloaded packages, original disc input hashes, objective
asset provenance and independent audit reports are documented in
[SCCT-Maps](https://github.com/Lumbridge/SCCT-Maps/tree/main/ports/chaos-theory-ps2).
The source metadata and converter release are independent of the native release.

## Runtime and validation gate

Use **OpenSCCT 0.8.157 or newer**. Version 0.8.157 fixes the normal map picker's
mode filter so the fourteen P maps can be selected from the menu.

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

The original hack/open-before-pickup sequence and exact carried-vial attachment
are undergoing an additional source and runtime review. The v1 binding smoke
does not establish the complete sequence or clipping parity. Corrections and
English authored map labels will be delivered in a new version; the published
v1 map archives and converter remain immutable.

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
   publish the supported runtime first (0.8.157 or newer for the normal picker).
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
