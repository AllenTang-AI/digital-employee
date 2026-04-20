#!/usr/bin/env python3
"""SessionStart hook — check workspace/input for new files"""

import sys
import json
from pathlib import Path
from datetime import datetime, timedelta


def main():
    try:
        json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {}
    except (json.JSONDecodeError, ValueError):
        pass

    plugin_root = Path(__file__).resolve().parent.parent.parent.parent
    input_dir = plugin_root / "workspace" / "input"

    if not input_dir.exists():
        sys.exit(0)

    now = datetime.now()
    cutoff = now - timedelta(hours=24)
    new_files = []

    for f in input_dir.rglob("*"):
        if f.is_file() and not f.name.startswith("."):
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            if mtime > cutoff:
                new_files.append(f"  - {f.relative_to(input_dir)}")

    if new_files:
        print(f"\n检测到 {len(new_files)} 个待处理产品文件：")
        for nf in new_files:
            print(nf)
        print()

    sys.exit(0)


if __name__ == "__main__":
    main()
