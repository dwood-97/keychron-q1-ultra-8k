#!/usr/bin/env python3
"""Build the experimental Caps-held F7-F12 WoW input layer."""

from __future__ import annotations

import json
import sys

from keymap_format import FACTORY_EXPORT, ROOT, keymap_md5, load_json, validate_export


OUTPUT = (
    ROOT
    / "exports/experiments/wow-keypad-layer/Keymap-Q1-Ultra-8K-WoW-keypad-layer.json"
)
ASSIGNMENTS = {
    (0, 14, 2): 174,
    (3, 0, 2): 21027,
    (2, 1, 3): 64,
    (2, 2, 3): 1,
    (2, 3, 3): 65,
    (2, 4, 3): 66,
    (3, 1, 3): 1,
    (3, 2, 3): 1,
    (3, 3, 3): 1,
    (3, 4, 3): 67,
    (4, 5, 3): 68,
    (4, 4, 3): 69,
}


def main() -> int:
    try:
        data = load_json(FACTORY_EXPORT)
    except (OSError, ValueError) as exc:
        print(f"Cannot load factory export: {exc}", file=sys.stderr)
        return 1

    for (row, col, layer_number), value in ASSIGNMENTS.items():
        entries = {
            (entry["row"], entry["col"]): entry
            for entry in data["keymap"][layer_number]
        }
        if (row, col) not in entries:
            print(
                f"Factory export is missing matrix position r{row}c{col}",
                file=sys.stderr,
            )
            return 1
        entries[(row, col)]["val"] = value

    data["MD5"] = keymap_md5(data)
    errors = validate_export(data, load_json(FACTORY_EXPORT))
    if errors:
        for error in errors:
            print(f"FAIL  {error}", file=sys.stderr)
        return 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n"
    OUTPUT.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    print(f"MD5 {data['MD5']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
