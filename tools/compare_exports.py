#!/usr/bin/env python3
"""Pretty-print a unified diff between two JSON exports.

The script deliberately treats Launcher exports as opaque JSON. It does not
assume or rewrite a schema. That keeps it useful even if Keychron changes the
export structure in a future Launcher version.
"""

from __future__ import annotations

import difflib
import json
import sys
from pathlib import Path


def normalized_json(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    rendered = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
    return [line + "\n" for line in rendered.splitlines()]


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: compare_exports.py OLD.json NEW.json", file=sys.stderr)
        return 2

    old_path = Path(sys.argv[1])
    new_path = Path(sys.argv[2])

    try:
        old_lines = normalized_json(old_path)
        new_lines = normalized_json(new_path)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    diff = difflib.unified_diff(
        old_lines,
        new_lines,
        fromfile=str(old_path),
        tofile=str(new_path),
    )
    sys.stdout.writelines(diff)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
