#!/usr/bin/env python3
"""Make WASD pass through on Layer 3 for Caps-driven profiles."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from keymap_format import (
    FACTORY_EXPORT,
    keymap_md5,
    load_json,
    validate_export,
)


WASD_POSITIONS = ((2, 2), (3, 1), (3, 2), (3, 3))


def prepare(path: Path, baseline: dict) -> bool:
    try:
        data = load_json(path)
    except (OSError, ValueError) as exc:
        print(f"FAIL  {path}: {exc}")
        return False
    if path.resolve() == FACTORY_EXPORT.resolve():
        print(f"FAIL  {path}: the factory export is immutable")
        return False
    keymap = data.get("keymap") if isinstance(data, dict) else None
    if (
        not isinstance(keymap, list)
        or len(keymap) != 4
        or not isinstance(keymap[2], list)
        or not isinstance(keymap[3], list)
    ):
        print(f"FAIL  {path}: expected four valid Launcher keymap layers")
        return False

    caps = next(
        (
            entry
            for entry in keymap[2]
            if isinstance(entry, dict)
            and entry.get("row") == 3
            and entry.get("col") == 0
        ),
        None,
    )
    if not caps or caps.get("val") != 21027:
        print(f"FAIL  {path}: Layer 2 Caps Lock is not momentary Layer 3")
        return False

    layer_three = {
        (entry["row"], entry["col"]): entry
        for entry in keymap[3]
        if isinstance(entry, dict)
    }
    try:
        for position in WASD_POSITIONS:
            layer_three[position]["val"] = 1
    except (IndexError, KeyError) as exc:
        print(f"FAIL  {path}: incomplete Layer 3 matrix: {exc}")
        return False

    data["MD5"] = keymap_md5(data)
    errors = validate_export(data, baseline)
    if errors:
        for error in errors:
            print(f"FAIL  {path}: {error}")
        return False

    rendered = json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n"
    try:
        path.write_text(rendered, encoding="utf-8", newline="\n")
    except OSError as exc:
        print(f"FAIL  {path}: {exc}")
        return False
    print(f"UPDATED {path}: WASD transparent; MD5 {data['MD5']}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, metavar="FILE")
    args = parser.parse_args()
    try:
        baseline = load_json(FACTORY_EXPORT)
    except (OSError, ValueError) as exc:
        print(f"Cannot load factory export: {exc}", file=sys.stderr)
        return 2
    results = [prepare(path, baseline) for path in args.files]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())