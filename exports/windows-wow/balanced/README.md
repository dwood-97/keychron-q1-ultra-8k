# Balanced WoW profile

Purpose: preserve the historical F13-F24 Caps-layer import experiment. Not a
recommended WoW Forever profile unless the client adds support for those keys.

## Layer 2 changes

- Caps Lock → momentary Layer 3 (`Fn(3)`)
- PgUp → F19
- PgDn → F20
- Home → F21
- Delete → F22
- Knob press → F23
- Grave/Tilde (`) → F24

## Layer 3 additions while holding Caps

- Caps + Q → F13
- Caps + E → F14
- Caps + R → F15
- Caps + F → F16
- Caps + Z → F17
- Caps + X → F18

W, A, S and D remain pass-through on Layer 3 so movement continues to work while Caps is held. Factory wireless shortcuts on Fn+1 through Fn+4 are also preserved.
W, A, S and D are explicitly transparent on Layer 3 so movement continues while
Caps is held. This replaces the four factory Layer 3 assignments on those keys
whenever Layer 3 is active. Factory wireless shortcuts on Fn+1 through Fn+4 are
preserved.

The Caps assignment uses keycode `21027`, copied from the factory Windows `Fn(3)` key rather than guessed.

This file is derived from the current factory export. Its MD5 must match the
compact serialized `keymap` array. Use `tools/update_checksum.py` after edits and
`tools/validate_json.py` before import. The layout remains experimental because
WoW Forever binding support for F13-F24 is not established.
