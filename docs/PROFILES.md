# WoW profile design

## Goals

- Keep Layers 0/1 as Mac and Layers 2/3 as Windows.
- Preserve WASD movement in every profile.
- Treat generated profiles as experiments until imported and tested in-game.
- Preserve factory wireless shortcuts on Windows Layer 3 where practical.
- Make experimentation cheap: every profile is a complete importable keymap derived from factory.

## Profiles

### Conservative
Six underused physical controls become F13–F18. This profile successfully
imported after its MD5 was recalculated and proved the generated-import path.
WoW Forever does not currently appear to bind F13-F24; this is not a recommended
game profile.

### Balanced
Caps Lock becomes a momentary Layer 3 key. The added outputs are F13-F24 and
remain an importable Launcher experiment, not a recommended WoW profile.

### Aggressive
Caps Lock becomes a momentary Layer 3 key with a full F13-F24 bank. This is an
importable Launcher experiment only; the F13-F24 outputs are unsuitable unless
WoW Forever adds support.

### Standard-keypad layer experiment

`exports/experiments/wow-keypad-layer/` contains the next physical test. Caps
holds Layer 3; Caps+Q/E/R/F/Z/X emits Numpad 1-6, and WASD remains transparent.
This is the leading architecture to test, not yet a production profile.

## Testing

1. Import one profile.
2. Confirm the keymap visually and verify the standard keypad outputs in Windows.
3. Attempt to bind Numpad 1-6 in the current WoW Forever client.
4. Test movement and Caps+WASD combinations during gameplay.
5. Promote only after input recognition and ergonomics are confirmed; otherwise
	keep the candidate under experiments and roll back to the factory export.
