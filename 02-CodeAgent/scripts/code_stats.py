#!/usr/bin/env python3
"""代码统计工具 — 基于 git log 分析团队工作量"""

import argparse
import subprocess
import sys
from datetime import datetime, timedelta
from collections import defaultdict


def run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()


def get_repo_root():
    root = run("git rev-parse --show-toplevel")
    if not root:
        print("错误: 当前目录不是 git 仓库", file=sys.stderr)
        sys.exit(1)
    return root


def stats_daily(since=None, until=None):
    """每日工作量统计"""
    date_fmt = "--since=%s" % since if since else ""
    if until:
        date_fmt += " --until=%s" % until

    log_cmd = f"git log --pretty=format:'%h|%an|%ad|%s' --date=short {date_fmt}"
    lines = run(log_cmd)
    if not lines:
        print("此时间段内无提交记录")
        return

    by_date = defaultdict(lambda: {"commits": 0, "authors": set(), "files": 0, "added": 0, "removed": 0})

    for line in lines.split("\n"):
        if not line:
            continue
        parts = line.split("|", 3)
        if len(parts) < 4:
            continue
        h, author, date, _ = parts
        by_date[date]["commits"] += 1
        by_date[date]["authors"].add(author)

    # 统计每个 commit 的文件变更和行数
    for date in by_date:
        shortlog = run(f"git log --since={date} --until={date} --pretty=format: --numstat")
        if shortlog:
            for num_line in shortlog.split("\n"):
                if not num_line:
                    continue
                parts = num_line.split("\t")
                if len(parts) >= 2 and parts[0] != "-":
                    try:
                        by_date[date]["added"] += int(parts[0])
                        by_date[date]["removed"] += int(parts[1])
                        by_date[date]["files"] += 1
                    except ValueError:
                        pass

    print(f"\n{'日期':<12} {'提交数':>6} {'作者数':>6} {'文件变更':>8} {'新增行':>8} {'删除行':>8}")
    print("-" * 60)
    for date in sorted(by_date.keys()):
        d = by_date[date]
        print(f"{date:<12} {d['commits']:>6} {len(d['authors']):>6} {d['files']:>8} {d['added']:>8} {d['removed']:>8}")

    # 总计
    total = sum(d["commits"] for d in by_date.values())
    print(f"\n总计: {total} 次提交, {sum(d['files'] for d in by_date.values())} 个文件变更")
    print(f"新增 {sum(d['added'] for d in by_date.values())} 行, 删除 {sum(d['removed'] for d in by_date.values())} 行")


def stats_author():
    """开发者贡献统计"""
    log = run("git shortlog -sne --all")
    print(f"\n{'#':>4} {'提交数':>6} {'作者':<30}")
    print("-" * 45)
    for line in log.split("\n"):
        if not line:
            continue
        parts = line.strip().split("\t")
        if len(parts) != 2:
            continue
        count, author = parts
        print(f"{count:>4} 次提交    {author}")

    # 行数统计
    print("\n--- 代码行数 ---")
    log2 = run("git log --all --pretty=format:'%an' --numstat")
    by_author = defaultdict(lambda: {"added": 0, "removed": 0})
    current_author = None
    for line in log2.split("\n"):
        if not line:
            continue
        if "|" not in line and "\t" in line:
            parts = line.split("\t")
            if len(parts) >= 2 and parts[0] != "-":
                try:
                    by_author[current_author]["added"] += int(parts[0])
                    by_author[current_author]["removed"] += int(parts[1])
                except ValueError:
                    pass
        else:
            current_author = line.strip()

    for author, data in sorted(by_author.items(), key=lambda x: x[1]["added"] + x[1]["removed"], reverse=True):
        print(f"  {author}: +{data['added']} -{data['removed']}")


def stats_module(target=None):
    """按模块统计变更频次"""
    root = get_repo_root()
    log = run("git log --all --pretty=format: --name-only")
    module_counts = defaultdict(int)

    for line in log.split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split("/")
        if target:
            if line.startswith(target):
                module_counts[parts[0]] += 1
        else:
            module_counts[parts[0]] += 1

    print(f"\n{'模块':<30} {'变更次数':>8}")
    print("-" * 40)
    for mod, count in sorted(module_counts.items(), key=lambda x: -x[1]):
        print(f"{mod:<30} {count:>8}")


def stats_trend(days=30):
    """提交趋势"""
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    log = run(f"git log --since={since} --pretty=format:'%ad' --date=short")
    by_date = defaultdict(int)
    for line in log.split("\n"):
        if line:
            by_date[line] += 1

    # 补齐缺失日期
    start = datetime.now() - timedelta(days=days)
    print(f"\n近 {days} 天提交趋势:")
    for i in range(days, -1, -1):
        d = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        bar = "#" * by_date.get(d, 0)
        if bar:
            print(f"{d}  {bar} ({by_date[d]})")


def main():
    parser = argparse.ArgumentParser(description="代码统计工具")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    p_daily = subparsers.add_parser("daily", help="每日工作量")
    p_daily.add_argument("--since", help="起始日期 YYYY-MM-DD")
    p_daily.add_argument("--until", help="截止日期 YYYY-MM-DD")

    subparsers.add_parser("author", help="开发者贡献")
    p_module = subparsers.add_parser("module", help="模块变更")
    p_module.add_argument("target", nargs="?", help="指定模块路径")

    p_trend = subparsers.add_parser("trend", help="提交趋势")
    p_trend.add_argument("--days", type=int, default=30, help="天数（默认30）")

    args = parser.parse_args()

    if args.operation == "daily":
        stats_daily(args.since, args.until)
    elif args.operation == "author":
        stats_author()
    elif args.operation == "module":
        stats_module(args.target)
    elif args.operation == "trend":
        stats_trend(args.days)


if __name__ == "__main__":
    main()
