# Keychron Q1 Ultra 8K ANSI

Private configuration repository for a **Keychron Q1 Ultra 8K ANSI** used primarily on Windows for daily work and gaming, especially World of Warcraft.

## Hardware

- Keyboard: Keychron Q1 Ultra 8K ANSI
- Firmware family: ZMK
- Configuration UI: Keychron Launcher
- Primary OS: Windows
- Primary gaming use: World of Warcraft / WoW Forever
- Mouse: Logitech G502 Hero

## Layer model

The board's four factory layers are treated as:

| Layer | Purpose |
|---|---|
| 0 | macOS base |
| 1 | macOS Fn / secondary |
| 2 | Windows base |
| 3 | Windows Fn / secondary |

Windows customization should primarily target **Layers 2 and 3**. Layers 0 and 1 should remain usable as the Mac configuration unless there is a strong reason to change them.

## Repository layout

```text
.
├── README.md
├── CHANGELOG.md
├── .gitignore
├── docs/
│   ├── SOURCES.md
│   ├── HARDWARE.md
│   ├── LAYERS.md
│   ├── EXPORT_FORMAT.md
│   ├── GAMING.md
│   ├── MACROS.md
│   └── RESTORE.md
├── exports/
│   ├── factory/
│   ├── windows-default/
│   └── windows-wow/
└── tools/
    ├── compare_exports.py
    └── validate_json.py
```

## Profiles

### Factory

The untouched Keychron Launcher export captured immediately after a factory reset. Never hand-edit files in `exports/factory/`.

### Windows Daily Driver

A conservative Windows setup that keeps normal typing intact while improving media, navigation, screenshots, utility shortcuts, and Fn-layer behavior.

### Windows WoW

A gaming-oriented Windows profile built around Layers 2 and 3 and designed to complement a Logitech G502 Hero rather than duplicate the mouse bindings.

## Workflow

1. Connect the keyboard to Keychron Launcher.
2. Export the current factory-reset keymap and place the raw file in `exports/factory/`.
3. If Launcher exposes macro export separately, place that raw export there too.
4. Commit and tag the untouched baseline before making changes.
5. Build Windows changes on Layers 2 and 3.
6. Export each known-good configuration into its matching directory.
7. Validate JSON files with `tools/validate_json.py`.
8. Compare exports with `tools/compare_exports.py` before importing a new revision.

## Safety rules

- Do not represent a hand-written file as a genuine Launcher export.
- Do not import QMK/VIA layout JSON from another Keychron model into this keyboard.
- Do not flash custom firmware when Launcher can accomplish the desired change.
- Preserve a known-good factory export and recovery procedure.
- Keep WoW combat automation in normal WoW keybindings/macros; keyboard macros should be limited to harmless utility tasks.

## Current status

A genuine factory-reset Keychron Launcher export has been captured and preserved verbatim:

`exports/factory/Keymap-Keychron Q1 Ultra 8K ANSI-28-16-31.json`

The baseline contains four keymap layers and four layer-specific knob definitions. Its SHA-256 is recorded in `exports/factory/SHA256SUMS`.

The next phase is to design the first Windows/WoW revision from a **copy** of this baseline, changing Layers 2 and 3 only unless a specific Mac-side change is intentionally requested.

## WoW test profiles

Three generated profiles live under `exports/windows-wow/`:

- `conservative/` — six standalone F13–F18 inputs
- `balanced/` — Caps-driven Layer 3 plus standalone F19–F24 inputs
- `aggressive/` — Caps-driven full F13–F24 MMO layer

See `docs/PROFILES.md` for the design and test order.
