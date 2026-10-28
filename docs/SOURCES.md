# Sources

Prefer current, model-specific official documentation over older QMK/VIA examples.

## Official Keychron

### Keychron Q1 Ultra 8K User Guide

- Source: Keychron
- URL: https://www.keychron.com/pages/keychron-q1-ultra-8k-user-guide
- Accessed: 2026-10-28
- Use: model-specific manual, factory reset, Launcher programming, layers, RGB, macros, 8K polling and firmware-related guidance.

### Keychron Launcher Guide

- Source: Keychron
- URL: https://www.keychron.com/blogs/news/keychron-launcher-guide
- Published: 2026-10-28
- Accessed: 2026-10-28
- Use: current Launcher behavior, WebHID connection, key remapping, macros, firmware updates, Quick Start, keymap export.

### How to Remap a Key on Launcher

- Source: Keychron
- URL: https://www.keychron.com/blogs/news/how-to-remap-a-key-on-launcher
- Accessed: 2026-10-28
- Use: current Keymap categories, Layer controls, import/export behavior and supported QMK/ZMK boards.

### Keychron Q1 Ultra 8K Product Page

- Source: Keychron
- URL: https://www.keychron.com/products/keychron-q1-ultra-8k-wireless-custom-mechanical-keyboard
- Accessed: 2026-10-28
- Use: hardware specifications including wired/2.4 GHz 8000 Hz polling, Bluetooth polling, battery and OS compatibility.

## Official GitHub
### Keychron Launcher Remapping and Export Guides

- URLs: https://www.keychron.com/blogs/news/how-to-remap-a-key-on-launcher and https://www.keychron.com/blogs/news/how-to-use-launcher-to-program-your-keyboard
- Accessed: 2026-10-28
- Use: current Launcher keymap categories, layers, and import/export workflow.
- Limitation: the guides do not document the `MD5` serialization formula.

## WoW Forever key-input evidence

### Blizzard-hosted WoW forums

- Search URL: https://us.forums.blizzard.com/en/wow/search?q=F13%20key%20binding
- Accessed: 2026-10-28
- Current results include WoW Forever threads titled “MMO Mouse Support” and requests for F13-F24 support. These are player reports/support requests hosted on Blizzard forums, not an official Blizzard compatibility statement. No official input support matrix was found.

### USB HID Usage Tables

- URL: https://usb.org/sites/default/files/hut1_5.pdf
- Use: standard Keyboard/Keypad-page usage numbers for Numpad 1-6 (0x59-0x5E); these values are from the USB HID standard, not another Keychron model.

## Evidence status

- Physical device: the user confirmed the generated Conservative import and F13-F18 display on the Q1 Ultra 8K in the V1.0.0 environment.
- Reverse engineered: the accepted `MD5` is the MD5 of compact serialized `keymap` JSON; confirmed by the factory digest and successful corrected import.
- Awaiting direct game test: whether WoW Forever accepts Numpad 1-6 and whether those inputs are ergonomic alongside Caps-held WASD.
- Not established: any official Blizzard statement that F13-F24 are supported; current community reports indicate they are not.

## Official GitHub

### Keychron ZMK

- Source: Keychron
- URL: https://github.com/Keychron/zmk
- Accessed: 2026-10-28
- Use: upstream reference for Keychron's ZMK firmware family.

## Local evidence

The factory layer mapping and visible key assignments in `docs/LAYERS.md` were also transcribed from screenshots of Keychron Launcher v1.5.2 connected to a Keychron Q1 Ultra 8K ANSI after a factory reset.
