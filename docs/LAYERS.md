# Layer Reference

## Factory export verification

The genuine factory Launcher export confirms that the keymap contains exactly four layer arrays with 98 matrix entries each.

It also confirms the rotary definitions independently for all four layers:

| Layer | Counter-clockwise | Clockwise |
|---|---|---|
| 0 | `KC_VOLD` | `KC_VOLU` |
| 1 | `RGB_VAD` | `RGB_VAI` |
| 2 | `KC_VOLD` | `KC_VOLU` |
| 3 | `RGB_VAD` | `RGB_VAI` |

The Fn-layer export data uses value `1` extensively at positions shown as pass-through in Launcher. Physical gaps use `0` in the captured matrix. Do not generalize these numeric values to other boards without verification.

See `EXPORT_FORMAT.md` for the captured schema.


This document records the factory-reset layout as visible in Keychron Launcher v1.5.2.

## Layer 0 — macOS base

Purpose: normal macOS typing and media/system controls.

Notable factory assignments:

- Number/letter block: normal US ANSI typing layout.
- Bottom modifiers: `Ctrl`, `Opt`, `Cmd`, `Space`, `Cmd`, `Fn(1)`, `Ctrl`.
- Navigation column: `PgUp`, `PgDn`, `Home`.
- Arrow cluster: normal arrows.
- Knob press: `Mute`.
- Top row provides Mac-oriented display/media/system functions including screen brightness, Mission Control, Launchpad, keyboard brightness, previous/play/next, mute and volume.

## Layer 1 — macOS Fn / secondary

Purpose: macOS function layer, wireless controls, RGB controls and battery/status functions.

Notable factory assignments observed:

- Top row: `F1` through `F12`.
- Number row left side: `BTH1`, `BTH2`, `BTH3`, `2.4G`.
- RGB controls include toggle, mode +/-, brightness +/-, hue +/-, saturation +/-, effect speed +/-.
- Battery status is assigned on the lower-left letter region.
- Most unrelated keys are pass-through/transparent.
- Knob behavior is assigned to an RGB function.

## Layer 2 — Windows base

Purpose: normal Windows typing and the primary base layer for Windows gaming.

Factory layout observed:

```text
Esc  F1 F2 F3 F4  F5 F6 F7 F8  F9 F10 F11 F12  Del   [Knob: Mute]

`  1 2 3 4 5 6 7 8 9 0 - =  Backspace                 PgUp
Tab  Q W E R T Y U I O P [ ] \\                           PgDn
Caps  A S D F G H J K L ; '  Enter                       Home
Shift  Z X C V B N M , . /  Shift              Up
Ctrl  Win  Alt        Space        Alt  Fn(3)  Ctrl    Left Down Right
```

Notes:

- Layer 2 should remain immediately recognizable as a normal Windows keyboard.
- This is the main layer for any gaming-focused remaps.
- The factory Fn key enters Layer 3.

## Layer 3 — Windows Fn / secondary

Purpose: Windows secondary functions, wireless switching, media, RGB and system shortcuts.

Notable factory assignments observed:

- Top row includes screen brightness, Task, File, keyboard brightness, previous/play/next, mute and volume.
- Number row left side: `BTH1`, `BTH2`, `BTH3`, `2.4G`.
- RGB controls include toggle, mode +/-, brightness +/-, hue +/-, saturation +/-, effect speed +/-.
- Battery status is present on the lower-left letter region.
- Most unrelated keys are pass-through/transparent.
- Knob behavior is assigned to RGB control.

## Design rules for customization

1. Keep Layers 0 and 1 usable for macOS.
2. Put normal Windows typing and gaming-critical inputs on Layer 2.
3. Put secondary utility functions on Layer 3.
4. Prefer pass-through/transparent behavior for keys that do not need a Layer 3 override.
5. Avoid creating a layer dependency that makes normal recovery or typing difficult.
6. Document every deviation from factory here before creating a release/tag.

## Candidate Windows/WoW changes

Do not apply these blindly; treat them as design candidates to validate in-game:

- Consider `Caps Lock` as a dual-role key only if hold/tap timing proves reliable during combat.
- Consider assigning otherwise-unused Windows keycodes such as `F13`–`F24` to expendable physical positions if WoW recognizes them cleanly.
- Consider keeping the navigation column (`PgUp`, `PgDn`, `Home`) available for out-of-combat utility unless a gaming-specific need clearly outweighs it.
- Keep `WASD`, `1–5`, `Q`, `E`, `R`, `T`, `F`, `G`, `Z`, `X`, `C`, `V`, `Tab`, `Shift`, `Ctrl`, `Alt` directly usable on Layer 2.
