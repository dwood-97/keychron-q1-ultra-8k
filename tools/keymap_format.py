#!/usr/bin/env python3
"""Shared schema checks and labels for Q1 Ultra 8K Launcher exports."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
FACTORY_EXPORT = ROOT / "exports/factory/Keymap-Keychron Q1 Ultra 8K ANSI-28-16-31.json"
EXPECTED_ID = 875827728
EXPECTED_VERSION = "1.0.0"
EXPECTED_LAYER_COUNT = 4
EXPECTED_ENTRIES_PER_LAYER = 98
WASD_POSITIONS = {
    (2, 2): "W",
    (3, 1): "A",
    (3, 2): "S",
    (3, 3): "D",
}

POSITION_LABELS = {
    (0, 0): "Esc", (0, 13): "Delete", (0, 14): "Knob press",
    (1, 0): "Grave", (1, 11): "Minus", (1, 12): "Equal",
    (1, 13): "Backspace", (1, 14): "PgUp",
    (2, 0): "Tab", (2, 11): "Left bracket", (2, 12): "Right bracket",
    (2, 13): "Backslash", (2, 14): "PgDn",
    (3, 0): "Caps Lock", (3, 10): "Semicolon", (3, 11): "Apostrophe",
    (3, 12): "Enter", (3, 13): "Home",
    (4, 0): "Left Shift", (4, 13): "Right Shift", (4, 14): "Up",
    (5, 0): "Left Ctrl", (5, 1): "Left Win", (5, 2): "Left Alt",
    (5, 6): "Space", (5, 9): "Right Alt", (5, 10): "Fn (Layer 3)",
    (5, 11): "Right Ctrl", (5, 12): "Left", (5, 13): "Down", (5, 14): "Right",
}
POSITION_LABELS.update({(0, col): f"F{col}" for col in range(1, 13)})
POSITION_LABELS.update({(1, col): str(col) for col in range(1, 10)})
POSITION_LABELS[(1, 10)] = "0"
POSITION_LABELS.update(dict(zip(((2, col) for col in range(1, 11)), "QWERTYUIOP")))
POSITION_LABELS.update(dict(zip(((3, col) for col in range(1, 10)), "ASDFGHJKL")))
POSITION_LABELS.update(dict(zip(((4, col) for col in range(2, 12)), "ZXCVBNM,./")))

HID_KEY_NAMES = {
    **{value: chr(ord("A") + value - 4) for value in range(4, 30)},
    **{value: str(value - 29) for value in range(30, 39)},
    39: "0", 40: "Enter", 41: "Esc", 42: "Backspace", 43: "Tab", 44: "Space",
    45: "Minus", 46: "Equal", 47: "Left bracket", 48: "Right bracket",
    49: "Backslash", 51: "Semicolon", 52: "Apostrophe", 53: "Grave",
    54: "Comma", 55: "Period", 56: "Slash", 57: "Caps Lock",
    **{value: f"F{value - 57}" for value in range(58, 70)},
    73: "Insert", 74: "Home", 75: "PgUp", 76: "Delete", 77: "End",
    78: "PgDn", 79: "Right", 80: "Left", 81: "Down", 82: "Up", 83: "Num Lock",
    84: "Numpad divide", 85: "Numpad multiply", 86: "Numpad minus",
    87: "Numpad plus", 88: "Numpad Enter",
    **{value: f"Numpad {value - 88}" for value in range(89, 99)},
    99: "Numpad decimal", 100: "Non-US backslash", 101: "Application",
    102: "Power", 103: "Numpad equal", 168: "Mute",
    **{value: f"F{value - 91}" for value in range(104, 116)},
    224: "Left Ctrl", 225: "Left Shift", 226: "Left Alt", 227: "Left Win",
    228: "Right Ctrl", 229: "Right Shift", 230: "Right Alt", 231: "Right Win",
    0: "None", 1: "Transparent", 21027: "Momentary Layer 3",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def keymap_md5(data: dict[str, Any]) -> str:
    payload = json.dumps(data["keymap"], separators=(",", ":")).encode("utf-8")
    return hashlib.md5(payload).hexdigest()


def keycode_name(value: int) -> str:
    return HID_KEY_NAMES.get(value, f"Keycode {value}")


def validate_export(
    data: Any,
    baseline: dict[str, Any],
    allow_mac_changes: bool = False,
    allow_knob_changes: bool = False,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["root must be a JSON object"]

    required_fields = {"id", "keymap", "version", "MD5", "knob"}
    missing = required_fields - data.keys()
    if missing:
        errors.append(f"missing root fields: {', '.join(sorted(missing))}")
    if data.get("id") != EXPECTED_ID:
        errors.append(f"id must be {EXPECTED_ID} for this Q1 Ultra 8K export")
    if data.get("version") != EXPECTED_VERSION:
        errors.append(f"version must be {EXPECTED_VERSION} for this baseline")

    keymap = data.get("keymap")
    baseline_keymap = baseline.get("keymap")
    if not isinstance(keymap, list) or len(keymap) != EXPECTED_LAYER_COUNT:
        errors.append(f"keymap must contain exactly {EXPECTED_LAYER_COUNT} layers")
    elif not isinstance(baseline_keymap, list) or len(baseline_keymap) != EXPECTED_LAYER_COUNT:
        errors.append("factory baseline has an invalid keymap layer count")
    else:
        expected_positions = {
            (entry.get("row"), entry.get("col"))
            for entry in baseline_keymap[0]
            if isinstance(entry, dict)
        }
        for layer_number, layer in enumerate(keymap):
            if not isinstance(layer, list):
                errors.append(f"layer {layer_number} must be an array")
                continue
            if len(layer) != EXPECTED_ENTRIES_PER_LAYER:
                errors.append(f"layer {layer_number} must have {EXPECTED_ENTRIES_PER_LAYER} entries")
            positions = []
            for entry_index, entry in enumerate(layer):
                if not isinstance(entry, dict) or not {"row", "col", "val"} <= entry.keys():
                    errors.append(f"layer {layer_number} entry {entry_index} must have row, col, and val")
                    continue
                row, col, value = entry["row"], entry["col"], entry["val"]
                if (
                    not isinstance(row, int) or isinstance(row, bool)
                    or not isinstance(col, int) or isinstance(col, bool)
                ):
                    errors.append(f"layer {layer_number} entry {entry_index} has non-integer row/col")
                    continue
                positions.append((row, col))
                if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                    errors.append(f"layer {layer_number} entry {entry_index} has malformed keycode value")
            if len(positions) == len(layer):
                if len(set(positions)) != len(positions):
                    errors.append(f"layer {layer_number} has duplicate matrix positions")
                actual = set(positions)
                if expected_positions - actual:
                    errors.append(f"layer {layer_number} is missing matrix positions")
                if actual - expected_positions:
                    errors.append(f"layer {layer_number} has unexpected matrix positions")
        if not allow_mac_changes and keymap[:2] != baseline_keymap[:2]:
            errors.append("Mac layers 0/1 differ from the factory baseline")
        if isinstance(keymap[2], list) and isinstance(keymap[3], list):
            caps_entry = next(
                (
                    entry
                    for entry in keymap[2]
                    if isinstance(entry, dict)
                    and entry.get("row") == 3
                    and entry.get("col") == 0
                ),
                None,
            )
            if caps_entry and caps_entry.get("val") == 21027:
                layer_three = {
                    (entry.get("row"), entry.get("col")): entry
                    for entry in keymap[3]
                    if isinstance(entry, dict)
                }
                for position, key_name in WASD_POSITIONS.items():
                    if layer_three.get(position, {}).get("val") != 1:
                        errors.append(
                            f"Caps momentary Layer 3 requires {key_name} to be transparent"
                        )

    knob = data.get("knob")
    if not isinstance(knob, list) or len(knob) != EXPECTED_LAYER_COUNT:
        errors.append(f"knob must contain exactly {EXPECTED_LAYER_COUNT} layer entries")
    else:
        for layer_number, layer_knob in enumerate(knob):
            if (
                not isinstance(layer_knob, dict)
                or not isinstance(layer_knob.get("left"), str)
                or not isinstance(layer_knob.get("right"), str)
            ):
                errors.append(f"knob layer {layer_number} must have string left/right fields")
        if not allow_knob_changes and knob != baseline.get("knob"):
            errors.append("knob assignments differ from the factory baseline")

    if isinstance(keymap, list):
        expected_md5 = keymap_md5(data)
        if data.get("MD5") != expected_md5:
            errors.append(f"MD5 mismatch: stored {data.get('MD5')!r}; keymap digest is {expected_md5}")
    return errors