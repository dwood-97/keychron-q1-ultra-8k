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

## Recommended philosophy

### Layer 2

Keep as the normal Windows base and gaming layer.

Use standard letters/numbers wherever possible. The best gaming layout is one that does not require remembering a second keyboard just to type in chat.

### Layer 3

Use for secondary functions:

- media
- RGB
- wireless selection
- battery status
- screenshots
- Windows utilities
- infrequent navigation
- optional extra gaming keycodes

## F13–F24 strategy

Keychron Launcher visibly exposes higher function keycodes including F20–F24 in its Windows special-key section, and standard function keys include F13–F19.

These are promising for gaming because they are normally unused by Windows applications and therefore may avoid conflicts.

Before standardizing on them:

1. Assign one test key to `F13`.
2. Verify it in Keychron Launcher Key Test or an OS key tester.
3. Bind it directly in World of Warcraft.
4. Test modifiers such as Shift+F13 if relevant.
5. Repeat with the highest keycodes you intend to use.

Do not build the entire profile around F13–F24 until this test passes.

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

## Suggested first gaming iteration

Start conservative:

1. Keep Layer 2 nearly stock.
2. Keep the existing Fn access to Layer 3.
3. Test one or two spare physical keys with `F13`/`F14`.
4. Bind those in WoW and play normally.
5. Only then expand to additional extra keycodes or Hold/Tap behavior.

This keeps rollback trivial and lets ergonomics drive the design instead of theory.
