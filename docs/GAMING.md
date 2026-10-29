# Windows / WoW Design

## Goal

Build a Windows profile that is excellent for World of Warcraft without turning the keyboard into an awkward single-purpose device.

The keyboard should complement a Logitech G502 Hero, which already carries ten convenient combat inputs through five mouse buttons plus their Shift variants.

## Prime left-hand real estate

Preserve and prioritize:

```text
1 2 3 4 5
Q W E R T
A S D F G
Z X C V
Tab
Caps Lock
Shift
Ctrl
Alt
Space
```

Movement remains conventional `WASD` unless deliberately changed in-game.

## What We Know

Verified on the physical Q1 Ultra 8K with device Current Version V1.0.2. The
Launcher export JSON field is `"version":"1.0.0"`; these are distinct version
values.

- The corrected generated keymap imported successfully in Keychron Launcher.
- Launcher displayed the F13-F18 assignments correctly.
- Layer 3 retained its factory passthrough, wireless, and RGB behavior.
- OS-level event delivery and WoW Forever binding support were not established
	by that test.

Current Blizzard forum search results include WoW Forever player reports and
support requests explicitly asking for F13-F24 binding support. These are
first-party-hosted community reports, not a Blizzard statement of supported
inputs. No official WoW Forever keycode list was found. Treat F13-F24 as
unsupported for this project unless a direct in-game test or Blizzard release
confirms otherwise.

## Recommended Architecture

### Layer 2

Keep as the normal Windows base and gaming layer. Preserve ordinary typing,
WASD, and the familiar Windows layout.

### Layer 3

Keep factory utilities by default. For the current gaming experiment, use Caps
Lock as momentary Layer 3 and map six left-hand keys to shifted US-ANSI symbols:

| Held key | Layer 3 output |
|---|---|
| Caps + Q | `!` |
| Caps + E | `@` |
| Caps + R | `#` |
| Caps + F | `$` |
| Caps + V | `%` |
| Caps + C | `^` |

WASD remain transparent on Layer 3 so movement passes through while Caps is
held.

These symbol assignments are equivalent to Shift+1 through Shift+6; they are
not six independent HID usages. In WoW, they may therefore be recognized as the
same bindings as ordinary Shift+1 through Shift+6 and can collide with existing
bindings that already use those combinations. Treat this as a compatibility and
ergonomics experiment, not a guaranteed source of six additional unique inputs.

The factory Layer 3 has non-transparent Keychron-specific assignments at W/A/S/D.
Setting them transparent is required for movement while the layer is active and
replaces those four factory functions whenever either Caps or the normal Fn key
activates Layer 3.

Other Layer 3 positions retain their factory utility behavior.

## F13–F24 Experiment

The F13-F24 profiles remain useful for validating keymap generation and the
Launcher import path. Their keycodes were displayed on the keyboard, but current
WoW Forever community reports indicate that the client does not bind them. They
are experiments only and must not be presented as recommended WoW profiles.

## Hold/Tap strategy

Hold/Tap can create useful dual-purpose keys, but MMO gameplay is latency- and timing-sensitive.

Potential experiment:

```text
Caps Lock tap  -> Caps Lock
Caps Lock hold -> alternate layer or modifier
```

Only keep it if rapid taps, movement combinations and typing remain predictable. A clever layout is not worth accidental activations during combat.

## Snap Action

Treat Snap Action as optional. Do not enable it simply because the keyboard supports it. WoW generally benefits more from predictable simultaneous input than from FPS-oriented opposite-direction prioritization.

If tested, verify movement combinations such as:

- W + A
- W + D
- A + D transitions
- strafing while casting
- jumping while moving

## Validation Order

1. Regenerate `exports/experiments/wow-keypad-layer/Keymap-Q1-Ultra-8K-WoW-keypad-layer.json` with `python tools/build_wow_keypad_layer.py`.
2. Refresh that directory's `SHA256SUMS`, then import the regenerated JSON.
3. Confirm Caps is momentary Layer 3, Q/E/R/F/V/C show `! @ # $ % ^`, W/A/S/D are transparent, and knob press is Play/Pause.
4. In a Windows key-event tester, verify Caps+Q/E/R/F/V/C produces the intended shifted-key events.
5. In WoW Forever's key-binding UI, attempt to bind each symbol and note whether the client records it as `!`/`@`/etc. or as Shift+1/Shift+2/etc.
6. Test each binding in a safe area while moving with WASD and holding Caps.
7. Check specifically for conflicts with existing Shift+1 through Shift+6 bindings; rollback by importing the factory export if any base behavior is wrong.

Do not add Hold/Tap, macros, or multi-action automation to this profile yet. Promote
it only after physical and in-game validation.
