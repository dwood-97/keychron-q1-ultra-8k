# Keychron Launcher Export Format

This document records what is directly observable from the factory-reset export for this exact **Keychron Q1 Ultra 8K ANSI**.

It is intentionally descriptive rather than a claim of an official schema.

## Top-level structure

The captured export contains these keys:

```json
{
  "id": <integer>,
  "keymap": [<layer 0>, <layer 1>, <layer 2>, <layer 3>],
  "version": "1.0.0",
  "MD5": "<opaque Keychron value>",
  "knob": [<layer 0>, <layer 1>, <layer 2>, <layer 3>]
}
```

Observed values in the factory baseline:

- `id`: `875827728`
- `version`: `1.0.0`
- keymap layers: `4`
- key entries per layer: `98, 98, 98, 98`

## Key entries

Each layer is an array of records shaped like:

```json
{"col": 0, "row": 0, "val": 41}
```

Observed meaning:

- `row` and `col` identify a matrix position.
- `val` is the encoded assignment used by Launcher/ZMK.
- Values must not be rewritten from guesswork.
- Physical gaps in the 75% layout also appear in the matrix data.

In the factory Fn layers, value `1` occurs extensively at keys displayed by Launcher as **Pass-through** / transparent. This is an observation from the captured config and Launcher UI, not a claim about every Keychron/ZMK export format.

## Knob entries

The factory export stores knob rotation separately from the key matrix:

```json
[
  {
    "left": "KC_VOLD",
    "right": "KC_VOLU"
  },
  {
    "left": "RGB_VAD",
    "right": "RGB_VAI"
  },
  {
    "left": "KC_VOLD",
    "right": "KC_VOLU"
  },
  {
    "left": "RGB_VAD",
    "right": "RGB_VAI"
  }
]
```

Factory behavior:

- Layers 0 and 2: volume down/up.
- Layers 1 and 3: RGB value/brightness down/up.

Knob **press** remains represented in the keymap matrix rather than in the `knob` rotation array.

## Integrity and the `MD5` field

The export contains:

```text
Keychron MD5 field: 10cfb8ae547419ff0c5257e0b8a01bac
MD5 of downloaded JSON bytes: 4e933e03dacdf3d61cd8bfa0d5c122b9
SHA-256 of downloaded JSON bytes: 123ac6b5d00e2f5454f097041eb1781c078031cdbc58427c80e78deebdbd78ab
```

Because the two MD5 values differ, this repository does not assume that Keychron's `MD5` field is a raw-file checksum.

The factory export is therefore preserved byte-for-byte, and `SHA256SUMS` is maintained independently by this repository.

## Editing policy

Until Keychron publishes a stable schema or we have validated round-trip behavior:

1. Preserve genuine Launcher exports untouched.
2. Make experiments on copies only.
3. Change the smallest possible set of assignments.
4. Compare candidate files against the factory baseline.
5. Validate JSON before import.
6. Keep the original Keychron metadata unless testing proves Launcher expects it to change.
7. Never infer compatibility from a QMK/VIA export belonging to another model.
