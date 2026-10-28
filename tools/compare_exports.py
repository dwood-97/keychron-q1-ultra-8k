#!/usr/bin/env python3
"""Show Launcher export changes by layer and physical key."""

from __future__ import annotations

import sys
from pathlib import Path

from keymap_format import POSITION_LABELS, keycode_name, load_json


def keyed_layer(layer: list[dict]) -> dict[tuple[int, int], int]:
    return {(entry["row"], entry["col"]): entry["val"] for entry in layer}


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: compare_exports.py OLD.json NEW.json", file=sys.stderr)
        return 2

    old_path, new_path = (Path(arg) for arg in sys.argv[1:])
    try:
        old_data = load_json(old_path)
        new_data = load_json(new_path)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not isinstance(old_data, dict) or not isinstance(new_data, dict):
        print("Error: both files must contain JSON objects", file=sys.stderr)
        return 1
    if not isinstance(old_data.get("keymap"), list) or not isinstance(
        new_data.get("keymap"), list
    ):
        print("Error: both files must contain a keymap array", file=sys.stderr)
        return 1

    differences = 0
    old_layers = old_data["keymap"]
    new_layers = new_data["keymap"]
    for layer_number in range(max(len(old_layers), len(new_layers))):
        if layer_number >= len(old_layers) or layer_number >= len(new_layers):
            print(f"Layer {layer_number}: layer missing from one export")
            differences += 1
            continue
        old_layer = keyed_layer(old_layers[layer_number])
        new_layer = keyed_layer(new_layers[layer_number])
        layer_changes = []
        for position in sorted(old_layer.keys() | new_layer.keys()):
            old_value = old_layer.get(position)
            new_value = new_layer.get(position)
            if old_value == new_value:
                continue
            row, col = position
            label = POSITION_LABELS.get(position, f"Matrix r{row}c{col}")
            old_name = "<missing>" if old_value is None else keycode_name(old_value)
            new_name = "<missing>" if new_value is None else keycode_name(new_value)
            layer_changes.append(f"{label}: {old_name} -> {new_name}")
        if layer_changes:
            print(f"Layer {layer_number}")
            for change in layer_changes:
                print(change)
                differences += 1

    for field in sorted((old_data.keys() | new_data.keys()) - {"keymap", "MD5"}):
        if old_data.get(field) != new_data.get(field):
            print(f"{field}: {old_data.get(field)!r} -> {new_data.get(field)!r}")
            differences += 1
    if not differences:
        print("No differences.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())