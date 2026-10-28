# Conservative WoW profile

Purpose: six-output experiment to verify that generated keymaps import and
higher function keycodes can be emitted by the keyboard. F13-F18 are not a
recommended WoW Forever binding strategy.

## Layer 2 changes

- Caps Lock → F13
- PgUp → F14
- PgDn → F15
- Home → F16
- Delete → F17
- Knob press → F18

Layers 0, 1 and 3 remain factory. Knob rotation remains factory (volume on Layer 2, RGB brightness on Layer 3).

This profile was successfully imported on a physical Q1 Ultra 8K in the user's
V1.0.2 environment after recalculating the MD5. Launcher displayed the six
assignments above. The accepted MD5 is derived from compact serialized `keymap`
JSON; it is not the factory value. Use `tools/validate_json.py` to check it.
