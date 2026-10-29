#!/usr/bin/env python3
"""Validate Q1 Ultra 8K Launcher exports without modifying them."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from keymap_format import FACTORY_EXPORT, load_json, validate_export


def validate(path: Path, baseline: dict, allow_mac_changes: bool, allow_knob_changes: bool) -> bool:
    try:
        data = load_json(path)
        errors = validate_export(
            data,
            baseline,
            allow_mac_changes=allow_mac_changes,
            allow_knob_changes=allow_knob_changes,
        )
    except (OSError, ValueError) as exc:
        print(f"FAIL  {path}: {exc}")
        return False

    if errors:
        for error in errors:
            print(f"FAIL  {path}: {error}")
        return False
    print(f"OK    {path}: schema, matrix, baseline, and keymap MD5")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, metavar="FILE")
    parser.add_argument("--baseline", type=Path, default=FACTORY_EXPORT)
    parser.add_argument("--allow-mac-changes", action="store_true")
    parser.add_argument("--allow-knob-changes", action="store_true")
    args = parser.parse_args()

    try:
        baseline = load_json(args.baseline)
    except (OSError, ValueError) as exc:
        print(f"Cannot load baseline {args.baseline}: {exc}", file=sys.stderr)
        return 2
    results = [
        validate(path, baseline, args.allow_mac_changes, args.allow_knob_changes)
        for path in args.files
    ]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
