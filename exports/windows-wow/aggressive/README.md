# Aggressive WoW profile

Purpose: preserve the historical Caps-held F13-F24 import experiment. Not a
recommended WoW Forever profile unless the client adds support for those keys.

## Layer 2 change

- Caps Lock → momentary Layer 3 (`Fn(3)`)

## Layer 3 MMO bank

- Caps + Q → F13
- Caps + E → F14
- Caps + R → F15
- Caps + T → F16
- Caps + F → F17
- Caps + G → F18
- Caps + Z → F19
- Caps + X → F20
- Caps + C → F21
- Caps + V → F22
- Caps + B → F23
- Caps + N → F24

W, A, S and D intentionally remain pass-through so movement continues while Caps is held. Factory Fn+1 through Fn+4 wireless controls remain untouched.
W, A, S and D are explicitly transparent on Layer 3 so movement continues while
Caps is held. This replaces the four factory Layer 3 assignments on those keys
whenever Layer 3 is active. Factory Fn+1 through Fn+4 wireless controls remain
untouched.

The Caps assignment uses keycode `21027`, copied directly from the factory Windows `Fn(3)` key.

This file is derived from the current factory export. Its MD5 must match the
compact serialized `keymap` array. Use `tools/update_checksum.py` after edits and
`tools/validate_json.py` before import. The layout remains experimental because
WoW Forever binding support for F13-F24 is not established.
