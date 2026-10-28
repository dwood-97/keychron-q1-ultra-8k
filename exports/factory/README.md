# Factory Baseline

This directory contains the genuine Keychron Launcher keymap export captured after the keyboard was returned to factory defaults.

## Preserved export

`Keymap-Keychron Q1 Ultra 8K ANSI-28-16-31.json`

The file above is preserved **verbatim**. Do not hand-edit it.

## Integrity

SHA-256:

`123ac6b5d00e2f5454f097041eb1781c078031cdbc58427c80e78deebdbd78ab`

The export also contains a top-level Keychron field:

`"MD5": "10cfb8ae547419ff0c5257e0b8a01bac"`

That field does **not** equal the MD5 hash of the downloaded JSON file (`4e933e03dacdf3d61cd8bfa0d5c122b9`). Treat the Keychron field as opaque application metadata; do not recalculate or overwrite it unless official documentation establishes its semantics.

## Confirmed export structure

The factory export contains:

- `id`: `875827728`
- `version`: `1.0.0`
- `keymap`: 4 layers
- entries per layer: `98, 98, 98, 98`
- `knob`: 4 layer-specific rotary definitions

Known layer ownership:

| Layer | OS / role |
|---|---|
| 0 | macOS base |
| 1 | macOS Fn |
| 2 | Windows base |
| 3 | Windows Fn |

Factory knob rotation:

| Layer | Counter-clockwise | Clockwise |
|---|---|---|
| 0 | `KC_VOLD` | `KC_VOLU` |
| 1 | `RGB_VAD` | `RGB_VAI` |
| 2 | `KC_VOLD` | `KC_VOLU` |
| 3 | `RGB_VAD` | `RGB_VAI` |

## Restore

Use Keychron Launcher's **Import** function with the untouched export above.

See `../../docs/RESTORE.md` before importing or flashing anything.
