# Backup and Restore

## Preferred recovery path

The safest rollback is a genuine Keychron Launcher export from the factory-reset keyboard.

### Capture the factory baseline

1. Connect the Q1 Ultra 8K to Keychron Launcher.
2. Open **Keymap**.
3. Click **Export**.
4. Save the resulting file unchanged in `exports/factory/`.
5. If macros are exported separately, export them too and place the raw file in `exports/factory/`.
6. Record firmware/Launcher versions in `exports/factory/README.md`.
7. Commit the baseline.
8. Tag that commit `v0.1.0-factory`.

## Restore from a saved export

1. Connect the keyboard to Keychron Launcher using the connection method supported by the current firmware/Launcher version.
2. Open **Keymap**.
3. Click **Import**.
4. Select the known-good export.
5. Verify all four layers before closing Launcher.
6. Test modifiers, Fn behavior, arrows, knob, wireless switching and typing.
## Generate and verify a modified export

For a generated profile, work only on a copy of the factory export. From the
repository root, run:

```powershell
python tools/update_checksum.py path\to\profile.json
python tools/validate_json.py path\to\profile.json
python tools/compare_exports.py "exports/factory/Keymap-Keychron Q1 Ultra 8K ANSI-28-16-31.json" path\to\profile.json
```

The updater recalculates top-level `MD5` from compact serialized `keymap` JSON.
For a Caps-to-Layer-3 experiment, run `python tools/prepare_caps_layer.py FILE`
first to make W/A/S/D transparent and refresh its MD5. This intentionally
replaces the factory Layer 3 functions at those positions.
The validator rejects stale checksums and checks this board's expected metadata,
layer/matrix dimensions, duplicate or missing matrix positions, non-negative
integer keycode values, unchanged Mac layers, and unchanged knob rotation by
default. The comparison prints changed physical-key labels. These checks do not
prove every numeric keycode is meaningful to undocumented firmware; a passing
file still requires Launcher and device testing.

The current next-test candidate and exact physical/gameplay procedure are in
`../exports/experiments/wow-keypad-layer/README.md`.

## Factory reset

Use the current Q1 Ultra 8K model-specific Keychron instructions rather than relying on generic Keychron reset procedures. The official user guide is linked in `SOURCES.md`.

After any factory reset, export the fresh state before making additional changes if the baseline may differ due to a firmware update.

## Firmware warning

Do not flash custom firmware solely to restore a keymap. Prefer Launcher import/reset and official model-specific recovery steps first.


## Known-good factory file

The current known-good factory baseline is:

`exports/factory/Keymap-Keychron Q1 Ultra 8K ANSI-28-16-31.json`

Before importing, you can verify its SHA-256 against `exports/factory/SHA256SUMS`.

Do not replace this file with an edited version.
