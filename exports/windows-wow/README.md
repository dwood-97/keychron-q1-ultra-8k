# Windows / WoW profiles

All profiles are derived from the pristine factory Launcher export.

| Profile | Strategy | Extra WoW inputs |
|---|---|---:|
| `conservative/` | Standalone underused keys only | 6 |
| `balanced/` | Caps momentary Layer 3 + standalone keys | 12 |
| `aggressive/` | Caps momentary Layer 3 with full F13–F24 left-hand bank | 12 |

Recommended test order: conservative → balanced → aggressive. Importing another profile is the rollback mechanism; the untouched factory export remains in `../factory/`.

The `MD5` field from the factory export is preserved in each derived keymap because it appears to be device/definition metadata rather than a raw file checksum. Treat the first import of each generated profile as a validation test in Keychron Launcher.
