#!/usr/bin/env python3
"""Verify or update the Launcher MD5 derived from a keymap array."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from keymap_format import FACTORY_EXPORT, keymap_md5, load_json


def update(path: Path, check_only: bool) -> bool:
    try:
        data = load_json(path)
    except (OSError, ValueError) as exc:
        print(f"FAIL  {path}: {exc}")
        return False

    if not isinstance(data, dict) or not isinstance(data.get("keymap"), list):
        print(f"FAIL  {path}: expected an object with a keymap array")
        return False
    if path.resolve() == FACTORY_EXPORT.resolve():
        print(f"FAIL  {path}: the factory export is immutable")
        return False

    expected = keymap_md5(data)
    current = data.get("MD5")
    if current == expected:
        print(f"OK    {path}: MD5 {expected}")
        return True
    if check_only:
        print(f"FAIL  {path}: stored MD5 {current!r}; expected {expected}")
        return False

    data["MD5"] = expected
    rendered = json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n"
    try:
        path.write_text(rendered, encoding="utf-8", newline="\n")
    except OSError as exc:
        print(f"FAIL  {path}: {exc}")
        return False
    print(f"UPDATED {path}: MD5 {expected}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, metavar="FILE")
    parser.add_argument(
        "--check",
        action="store_true",
        help="report stale checksums without modifying files",
    )
    args = parser.parse_args()
    results = [update(path, args.check) for path in args.files]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())