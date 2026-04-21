#!/usr/bin/env python3
"""SessionStart hook — print agent identity, check workspace for new files"""

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
    workspace_dir = plugin_root / "workspace"

    # Print agent identity
    plugin_json = plugin_root / ".claude-plugin" / "plugin.json"
    if plugin_json.exists():
        try:
            with open(plugin_json) as f:
                info = json.load(f)
            print(f"\n🤖 当前 Agent: {info.get('name', 'unknown')}")
            print(f"📍 工作目录: {workspace_dir}/\n")
        except Exception:
            pass

    # Check for new files in workspace (last 24 hours, skip .DS_Store)
    if not workspace_dir.exists():
        sys.exit(0)

    now = datetime.now()
    cutoff = now - timedelta(hours=24)
    new_files = []

    for f in workspace_dir.rglob("*"):
        if f.is_file() and not f.name.startswith("."):
            if "/.git/" in str(f):
                continue
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            if mtime > cutoff:
                rel = f.relative_to(workspace_dir)
                new_files.append(f"  - {rel}")

    if new_files:
        print(f"📁 检测到 {len(new_files)} 个新文件：")
        for nf in new_files:
            print(nf)
        print()

    sys.exit(0)


if __name__ == "__main__":
    main()
