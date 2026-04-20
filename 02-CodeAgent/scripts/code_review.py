#!/usr/bin/env python3
"""代码审查静态扫描 — 规则检查，深度审查由 Claude 完成"""

import argparse
import re
import sys
from pathlib import Path


SECURITY_PATTERNS = {
    "硬编码密钥": [r"password\s*=\s*['\"][^'\"]+['\"]", r"api_key\s*=\s*['\"][^'\"]+['\"]", r"secret\s*=\s*['\"][^'\"]+['\"]"],
    "SQL 拼接": [r"(execute|cursor\.execute)\(.*\+|f['\"].*(SELECT|INSERT|UPDATE|DELETE)"],
    "命令注入": [r"os\.system\(.*\+|subprocess\.(call|run|Popen)\(.*shell\s*=\s*True"],
    "XSS 风险": [r"\.innerHTML\s*=|document\.write\(|eval\("],
    "路径穿越": [r"open\(.*\+.*path|os\.path\.join\(request"],
    "敏感日志": [r"logging\.(info|debug|warn)\(.*password|logging\.(info|debug|warn)\(.*token"],
}

CODE_SMELLS = {
    "过长函数": (r"def\s+\w+\([^)]*\):\s*\n(?:[ \t]+.*\n){50,}", "建议拆分，单函数不超过 50 行"),
    "嵌套过深": (r"(?m)^(?:\s{8,})\S", "缩进超过 4 层，建议提取为独立函数"),
    "裸 except": (r"except\s*:", "应捕获具体异常类型"),
    "import *": (r"from\s+\S+\s+import\s+\*", "应显式导入所需名称"),
    "魔法数字": (r"(?<!\w)(?:[2-9]\d{2,})(?!\w)", "建议提取为命名常量"),
}


def scan_file(filepath, rules, label=""):
    results = []
    try:
        content = Path(filepath).read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return results

    lines = content.split("\n")
    for name, pattern in rules.items():
        if isinstance(pattern, str):
            pattern = [pattern]
        for pat in pattern:
            for i, line in enumerate(lines, 1):
                if re.search(pat, line, re.IGNORECASE):
                    results.append({
                        "file": filepath,
                        "line": i,
                        "rule": name,
                        "content": line.strip(),
                        "label": label,
                    })
    return results


def scan_target(target, rules, label="", extensions=None):
    src = Path(target)
    if extensions is None:
        extensions = {".py", ".js", ".ts", ".jsx", ".tsx", ".sh", ".html"}

    if src.is_file():
        return scan_file(src, rules, label)
    elif src.is_dir():
        results = []
        for ext in extensions:
            for f in src.rglob(f"*{ext}"):
                if any(x in str(f) for x in [".git", "node_modules", "venv", "__pycache__"]):
                    continue
                results.extend(scan_file(f, rules, label))
        return results
    return []


def print_results(results, output=None):
    if not results:
        msg = "未发现明显问题"
        print(msg)
        if output:
            Path(output).write_text(f"# 代码审查报告\n\n{msg}\n", encoding="utf-8")
        return

    by_label = {}
    for r in results:
        by_label.setdefault(r["label"], []).append(r)

    lines = [f"# 代码审查报告\n\n共发现 {len(results)} 个潜在问题：\n"]

    for label, items in sorted(by_label.items()):
        lines.append(f"\n## {label} ({len(items)} 项)\n")
        for item in items:
            lines.append(f"- **{item['file']}:{item['line']}** [{item['rule']}] `{item['content']}`")

    report = "\n".join(lines)
    print(report)

    if output:
        Path(output).write_text(report, encoding="utf-8")
        print(f"\n报告已保存: {output}")


def cmd_quick(args):
    results = []
    results.extend(scan_target(args.target, CODE_SMELLS, "代码异味"))
    results.extend(scan_target(args.target, SECURITY_PATTERNS, "安全风险"))
    print_results(results, args.output)


def cmd_full(args):
    print(f"[提示: 完整审查建议使用 Read 工具读取 {args.target}，Claude 会从架构、可维护性、性能等维度进行深度审查]")
    results = []
    results.extend(scan_target(args.target, CODE_SMELLS, "代码异味"))
    results.extend(scan_target(args.target, SECURITY_PATTERNS, "安全风险"))
    if results:
        print("\n--- 静态扫描结果 ---\n")
        print_results(results, args.output)


def cmd_security(args):
    results = scan_target(args.target, SECURITY_PATTERNS, "安全风险")
    print_results(results, args.output)


def cmd_test(args):
    src = Path(args.target)
    if src.is_file():
        test_files = list(src.parent.rglob("test_*.py")) + list(src.parent.rglob("*_test.py"))
    else:
        test_files = list(src.rglob("test_*.py")) + list(src.rglob("*_test.py"))

    source_files = list(src.rglob("*.py")) if src.is_dir() else [src]
    source_files = [f for f in source_files if not f.name.startswith("test_")]

    print(f"源文件: {len(source_files)} 个")
    print(f"测试文件: {len(test_files)} 个")
    if not test_files:
        print("\n警告: 未找到测试文件")
    else:
        for tf in test_files:
            print(f"  - {tf.relative_to(src.parent if src.is_file() else src)}")


def cmd_report(args):
    print("=== 完整审查报告 ===\n")
    cmd_full(args)


def cmd_diff(args):
    import subprocess
    result = subprocess.run(["git", "diff", "--stat"], capture_output=True, text=True)
    if result.returncode != 0:
        print("不在 git 仓库中，无法获取 diff")
        return
    print("当前 git 变更：\n")
    print(result.stdout)
    print("\n[提示: 请使用 Read 工具查看具体变更，Claude 会逐行审查]")


def main():
    parser = argparse.ArgumentParser(description="代码审查静态扫描")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    for op, func, help_text in [
        ("quick", cmd_quick, "快速审查"),
        ("full", cmd_full, "完整审查"),
        ("security", cmd_security, "安全审查"),
        ("test", cmd_test, "测试检查"),
        ("report", cmd_report, "审查报告"),
        ("diff", cmd_diff, "git diff 审查"),
    ]:
        p = subparsers.add_parser(op, help=help_text)
        if op != "diff":
            p.add_argument("target", help="目标文件或目录")
        p.add_argument("--output", help="输出报告路径（可选）")

    args = parser.parse_args()

    if args.operation == "quick":
        cmd_quick(args)
    elif args.operation == "full":
        cmd_full(args)
    elif args.operation == "security":
        cmd_security(args)
    elif args.operation == "test":
        cmd_test(args)
    elif args.operation == "report":
        cmd_report(args)
    elif args.operation == "diff":
        cmd_diff(args)


if __name__ == "__main__":
    main()
