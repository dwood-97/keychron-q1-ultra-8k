#!/usr/bin/env python3
"""Validate one or more JSON files without modifying them."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def validate(path: Path) -> bool:
    try:
        with path.open("r", encoding="utf-8") as handle:
            json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL  {path}: {exc}")
        return False

    print(f"OK    {path}")
    return True


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_json.py FILE [FILE ...]", file=sys.stderr)
        return 2

    paths = [Path(arg) for arg in sys.argv[1:]]
    return 0 if all(validate(path) for path in paths) else 1


if __name__ == "__main__":
    raise SystemExit(main())
