# Conservative WoW profile

Purpose: six-output experiment to verify that generated keymaps import.

## Layer 2 changes

- Caps Lock → F13
- PgUp → F14
- PgDn → F15
- Home → F16
- Delete → F17
- Knob press → F18

Layers 0, 1 and 3 remain factory. Knob rotation remains factory (volume on Layer 2, RGB brightness on Layer 3).

This profile was successfully imported on a physical Q1 Ultra 8K with device
Current Version V1.0.2 after recalculating the MD5. The Launcher export JSON
field remains `"version":"1.0.0"`; Launcher displayed the six assignments
above. The accepted MD5 is derived from compact serialized `keymap` JSON; it is
not the factory value. Use `tools/validate_json.py` to check it.
