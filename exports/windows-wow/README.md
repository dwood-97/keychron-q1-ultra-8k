# Windows / WoW Experiments

These generated layouts are complete Launcher import files, but none is a
recommended production WoW Forever profile. They were built around F13-F24,
which the keyboard emits but current WoW Forever community reports say cannot
be bound.

| Profile | Experiment |
|---|---|
| `conservative/` | Six standalone F13-F18 outputs; physically imported successfully after checksum correction |
| `balanced/` | Caps-held Layer 3 plus F13-F24 outputs |
| `aggressive/` | Caps-held F13-F24 left-hand bank |

For the next game-input test, use the standard-keypad candidate under
`../experiments/wow-keypad-layer/`. Each modified keymap must have its `MD5`
recalculated with `tools/update_checksum.py`, then pass `tools/validate_json.py`.
The MD5 is calculated from compact serialized `keymap` JSON, not copied from the
factory export.
