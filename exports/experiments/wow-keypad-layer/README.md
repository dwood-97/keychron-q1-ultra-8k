# WoW Forever F7-F12 Layer Experiment

Status: generated and structurally validated; awaiting physical import and in-game testing. This is not a production profile.

## Assignments

- Layer 2 knob press: Play/Pause.
- Layer 2 Caps Lock: momentary Layer 3.
- Layer 3 Q/E/R/F/V/C: F7/F8/F9/F10/F11/F12.
- Layer 3 W/A/S/D: transparent, so movement passes through while Caps is held.
- All other assignments and knob rotations: copied from the current factory export.
- Layers 0/1: unchanged.

The four WASD overrides replace non-transparent factory Layer 3 functions at
those positions while either Caps or the normal Fn key activates Layer 3.

F7-F12 are ordinary keyboard HID usages already understood by the existing
keymap tooling. Unlike the earlier shifted-symbol experiment, these assignments
do not depend on synthesizing Shift+number combinations. They are still not six
new globally unique keys: the physical F7-F12 keys generate the same inputs, so
WoW bindings can conflict with any existing use of those function keys.

## Build and Validate

From the repository root:

```powershell
python tools/build_wow_keypad_layer.py
python tools/update_checksum.py --check exports/experiments/wow-keypad-layer/Keymap-Q1-Ultra-8K-WoW-keypad-layer.json
python tools/validate_json.py exports/experiments/wow-keypad-layer/Keymap-Q1-Ultra-8K-WoW-keypad-layer.json
python tools/compare_exports.py exports/factory/Keymap-Keychron Q1 Ultra 8K ANSI-28-16-31.json exports/experiments/wow-keypad-layer/Keymap-Q1-Ultra-8K-WoW-keypad-layer.json
```

The builder copies the factory export, applies only the documented assignments,
recalculates the keymap MD5, validates the result, and writes the generated file.
Refresh this directory's `SHA256SUMS` whenever the generated JSON changes.

## Physical Test

1. Keep the genuine factory export available for rollback. Connect the keyboard to Keychron Launcher using the supported connection method.
2. Import `Keymap-Q1-Ultra-8K-WoW-keypad-layer.json` from this directory.
3. In Launcher, verify Layer 2 knob press is Play/Pause, Layer 2 Caps Lock is momentary Layer 3, and Layer 3 Q/E/R/F/V/C show F7-F12. Confirm W/A/S/D are passthrough and Layers 0/1 remain unchanged.
4. Check the knob press generates Play/Pause, then check Caps+Q/E/R/F/V/C produces F7/F8/F9/F10/F11/F12 in a local keyboard event tester or the game's key-binding screen.
5. In WoW Forever's key-binding screen, bind F7-F12 and test them in a safe area while holding Caps, including Caps+W/A/S/D movement combinations.
6. Check for conflicts with any existing F7-F12 bindings.
7. Stop if movement, typing, or any Windows function is affected unexpectedly. Restore the factory keymap through Launcher.

A successful Launcher import validates the file format and layer assignments only. It does not by itself establish that the layout is comfortable or conflict-free in WoW Forever. Do not promote this profile until real play confirms the ergonomics.
