# WoW Forever Shifted-Symbol Layer Experiment

Status: generated and structurally validated; awaiting physical import and in-game testing. This is not a production profile.

## Assignments

- Layer 2 knob press: Play/Pause.
- Layer 2 Caps Lock: momentary Layer 3.
- Layer 3 Q/E/R/F/V/C: `!` / `@` / `#` / `$` / `%` / `^`.
- Layer 3 W/A/S/D: transparent, so movement passes through while Caps is held.
- All other assignments and knob rotations: copied from the current factory export.

The four WASD overrides replace non-transparent factory Layer 3 functions at
those positions while either Caps or the normal Fn key activates Layer 3.

The six symbol assignments use shifted US-ANSI number-row keycodes, equivalent
to Shift+1 through Shift+6. They are not six independent HID usages. In WoW,
this may therefore behave like normal Shift+1 through Shift+6 and can conflict
with existing bindings that use those combinations. Direct Launcher, Windows,
and WoW Forever testing is required before treating this as a useful extra bind
bank.

- Layers 0/1: unchanged.

## Build and Validate

From the repository root:

```powershell
python tools/build_wow_keypad_layer.py
python tools/validate_json.py exports/experiments/wow-keypad-layer/Keymap-Q1-Ultra-8K-WoW-keypad-layer.json
python tools/compare_exports.py exports/factory/Keymap-Keychron Q1 Ultra 8K ANSI-28-16-31.json exports/experiments/wow-keypad-layer/Keymap-Q1-Ultra-8K-WoW-keypad-layer.json
```

The builder copies the factory export, applies only the documented assignments,
recalculates the keymap MD5, validates the result, and writes the generated file.
After regeneration, refresh this directory's `SHA256SUMS` before committing the
new generated artifact.

## Physical Test

1. Keep the genuine factory export available for rollback. Connect the keyboard to Keychron Launcher using the supported connection method.
2. Import `Keymap-Q1-Ultra-8K-WoW-keypad-layer.json` from this directory.
3. In Launcher, verify Layer 2 knob press is Play/Pause, Layer 2 Caps Lock is momentary Layer 3, and Layer 3 Q/E/R/F/V/C show `! @ # $ % ^`. Confirm W/A/S/D are passthrough and Layers 0/1 remain unchanged.
4. Check the knob press generates Play/Pause, then check Caps+Q/E/R/F/V/C produces the intended shifted symbols in a local keyboard event tester or the game's key-binding screen.
5. In WoW Forever's key-binding screen, try each symbol individually and confirm how the client labels it. Test them in a safe area while holding Caps, including Caps+W/A/S/D movement combinations.
6. Specifically check for collisions with existing Shift+1 through Shift+6 bindings.
7. Stop if movement, typing, or any Windows function is affected unexpectedly. Restore the factory keymap through Launcher.

A successful Launcher import validates the file format and layer assignments only. It does not by itself establish that WoW Forever treats these shifted symbols as useful additional inputs. Do not promote this profile until the client accepts the inputs and real play confirms the ergonomics.
