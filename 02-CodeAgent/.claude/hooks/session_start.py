#!/usr/bin/env python3
"""SessionStart hook — check workspace/input/code for new code files"""

import sys
import json
from pathlib import Path
from datetime import datetime, timedelta


def main():
    try:
        data = json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {}
    except (json.JSONDecodeError, ValueError):
        data = {}

    plugin_root = Path(__file__).resolve().parent.parent.parent.parent
    input_dir = plugin_root / "workspace" / "input" / "code"

    if not input_dir.exists():
        sys.exit(0)

    now = datetime.now()
    cutoff = now - timedelta(hours=24)
    new_files = []

    for f in input_dir.rglob("*"):
        if f.is_file() and not f.name.startswith("."):
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            if mtime > cutoff:
                rel = f.relative_to(input_dir.parent.parent)
                new_files.append(f"  - {rel}")

    if new_files:
        print(f"\n检测到 {len(new_files)} 个待审查代码文件：")
        for nf in new_files:
            print(nf)
        print("提示: 使用 /review full <file> 进行审查\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
