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

## Factory reset

Use the current Q1 Ultra 8K model-specific Keychron instructions rather than relying on generic Keychron reset procedures. The official user guide is linked in `SOURCES.md`.

After any factory reset, export the fresh state before making additional changes if the baseline may differ due to a firmware update.

## Firmware warning

Do not flash custom firmware solely to restore a keymap. Prefer Launcher import/reset and official model-specific recovery steps first.
