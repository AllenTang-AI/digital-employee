#!/usr/bin/env python3
"""邮件助手脚本 — 草稿生成、回复建议、润色、分类"""

import argparse
import sys
import os
from datetime import datetime


def draft(to_addr, subject, body, style="formal", output=None):
    """生成邮件草稿"""
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M")
    greeting = "您好，" if style == "formal" else "Hi,"
    closing = "此致敬礼" if style == "formal" else "Best regards"

    email_text = f"""收件人: {to_addr}
主题: {subject}
日期: {now}

{greeting}

{body}

{closing}
"""
    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(email_text)
        print(f"邮件草稿已保存到: {output}")
    else:
        print(email_text)


def reply(original_email, reply_style="professional"):
    """生成回复建议"""
    print("=== 原邮件 ===")
    print(original_email)
    print("\n=== 回复建议 ===")
    print("[LLM: 请根据以上原邮件内容，生成专业、得体的中文回复草稿]")
    print(f"风格: {reply_style}")


def polish(email_text):
    """润色邮件内容"""
    print("=== 待润色内容 ===")
    print(email_text)
    print("\n=== 润色后 ===")
    print("[LLM: 请对以上邮件内容进行润色，保持原意，提升表达的流畅度和专业性]")


def classify(email_text):
    """对邮件进行分类"""
    print("=== 待分类邮件 ===")
    print(email_text[:500])
    print("\n=== 分类 ===")
    print("[LLM: 请对以上邮件进行分类，包括: 优先级(高/中/低)、类型(通知/请求/汇报/投诉/其他)]")


def review(email_text):
    """邮件质检"""
    print("=== 待检查邮件 ===")
    print(email_text)
    print("\n=== 质检报告 ===")
    print("[LLM: 请对以上邮件进行中文质检，检查以下方面：")
    print("1. 语气是否得体、专业")
    print("2. 有没有错别字或语法问题")
    print("3. 格式是否规范（称呼、署名、日期）")
    print("4. 有没有遗漏的重要信息")
    print("5. 收件人/主题是否清晰")
    print("请逐条列出问题并给出修改建议。]")


def main():
    parser = argparse.ArgumentParser(description="邮件助手")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    # draft
    p_draft = subparsers.add_parser("draft")
    p_draft.add_argument("--to", required=True)
    p_draft.add_argument("--subject", required=True)
    p_draft.add_argument("--body", default="")
    p_draft.add_argument("--style", default="formal", choices=["formal", "casual"])
    p_draft.add_argument("--output")

    # reply
    p_reply = subparsers.add_parser("reply")
    p_reply.add_argument("--text", required=True)
    p_reply.add_argument("--style", default="professional")

    # polish
    p_polish = subparsers.add_parser("polish")
    p_polish.add_argument("--text", required=True)

    # classify
    p_classify = subparsers.add_parser("classify")
    p_classify.add_argument("--text", required=True)

    # review
    p_review = subparsers.add_parser("review")
    p_review.add_argument("--text", required=True)

    args = parser.parse_args()

    if args.operation == "draft":
        draft(args.to, args.subject, args.body, args.style, args.output)
    elif args.operation == "reply":
        reply(args.text, args.style)
    elif args.operation == "polish":
        polish(args.text)
    elif args.operation == "classify":
        classify(args.text)
    elif args.operation == "review":
        review(args.text)


if __name__ == "__main__":
    main()
