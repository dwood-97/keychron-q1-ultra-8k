# Keychron Launcher Export Format

This document records what is directly observable from the factory-reset export for this exact **Keychron Q1 Ultra 8K ANSI**.

It is intentionally descriptive rather than a claim of an official schema.

## Version distinction

- Device current version shown during physical validation: `V1.0.2`.
- Genuine factory export JSON field: `"version": "1.0.0"`.

The JSON field is part of the exported configuration format; it is not the
keyboard's firmware/device current version. Derived profiles retain the
factory export field, and validation compares candidate versions against that
factory baseline.

## Top-level structure

The captured export contains these keys:

```json
{
  "id": <integer>,
  "keymap": [<layer 0>, <layer 1>, <layer 2>, <layer 3>],
  "version": "1.0.0",
  "MD5": "<MD5 of compact serialized keymap array>",
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

Real-device validation established that `MD5` is not opaque device metadata and
is not a digest of the complete JSON file. The accepted value is the MD5 of the
compact JSON serialization of the `keymap` array:

```python
hashlib.md5(
  json.dumps(data["keymap"], separators=(",", ":")).encode("utf-8")
).hexdigest()
```

The factory keymap serializes to `10cfb8ae547419ff0c5257e0b8a01bac`, matching
its field. The modified Conservative profile serializes to
`918db7c7dcd71e0e1b7c04d19a11a8b3`; after replacing its stale factory MD5 with
that value, Keychron Launcher imported it successfully on a physical Q1 Ultra
8K in the user's V1.0.2 device environment. The accepted file's JSON
`"version"` remained `1.0.0`; these values describe different things. The earlier
stale-MD5 version was rejected as `Invalid Configuration`.

This formula is experimentally established for this export generation; Keychron
does not publish the serialization/checksum schema in the Launcher guides linked
from `SOURCES.md`. Repository SHA-256 files remain separate whole-file integrity
checks and must be refreshed whenever a generated JSON file changes.

## Editing policy

For this observed Q1 Ultra 8K generation:

1. Preserve the genuine Launcher keymap export untouched.
2. Make experiments on copies only.
3. Change the smallest possible set of assignments.
4. Recalculate `MD5` with `tools/update_checksum.py` after every keymap edit.
5. Validate, compare against the factory baseline, then import.
6. Leave `id`, export `version`, and undocumented `knob` encoding alone unless
   separately tested.
7. Never infer compatibility from a QMK/VIA export belonging to another model.

The validator checks that keycode values are non-negative integers, but does
not claim every integer is a valid assignment. Keychron has not published the
full device-specific value schema.
