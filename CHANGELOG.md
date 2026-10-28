# Changelog


## Factory baseline milestone (untagged)

- Preserved the genuine factory-reset Keychron Launcher keymap export.
- Recorded SHA-256 integrity metadata.
- Documented the observed Launcher export structure.
- Verified four layer arrays and per-layer knob rotation behavior.
- Established the factory baseline from which Windows/WoW variants will be derived.

All notable configuration changes should be recorded here.

## Unreleased

### Added

- Initial repository structure.
- Documented Q1 Ultra 8K hardware and four-layer operating-system model.
- Added Windows/WoW design guidance.
- Added JSON validation and export comparison helpers.
- Added placeholders for genuine Keychron Launcher exports.

## Release status

The repository currently has no Git tags. After the factory-file integrity discrepancy is reconciled, tag the validated import tooling/profile-generation milestone as `v0.2.0-import-validated`. Do not tag a production WoW release until a profile is accepted by the current WoW Forever client and passes gameplay/ergonomics testing; use `v1.0.0-wow` for that later milestone.
## 2026-10-28 — Hardware validation

- First generated keymap imported on a physical Keychron Q1 Ultra 8K ANSI in the user's V1.0.0 environment.
- Launcher rejected the initial Conservative import as `Invalid Configuration` because the edited keymap retained a stale `MD5`.
- Recalculated `MD5` from compact serialized `keymap` JSON; the corrected Conservative export imported successfully.
- Confirmed Launcher displayed Caps Lock/F13, PgUp/F14, PgDn/F15, Home/F16, Delete/F17, and knob/F18; factory Layer 3 passthrough/wireless/RGB behavior remained intact.
- Reclassified F13-F24 layouts as import experiments pending WoW Forever support; added a Caps-held standard-keypad experiment for the next test.
- Added schema, matrix, Mac-layer, knob, and keymap-MD5 validation; checksum updater; board-aware comparison; and a keypad experiment builder.
