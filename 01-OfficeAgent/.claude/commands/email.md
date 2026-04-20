---
description: Email assistant — draft, reply, polish, review professional emails
argument-hint: [operation] [content]
allowed-tools: Read, Write, Edit, Task
---

# /email — 邮件助手

邮件处理由 **email-reviewer** 子Agent主导，参考 `skills/email-composition` 中的模式规范。

## 执行流程

1. 识别邮件类型：草稿、回复、润色、质检
2. 加载 `skills/email-composition` 中的模式参考
3. 调用 **email-reviewer** 子Agent生成/审查邮件
4. 输出到 console 或 `workspace/output/emails/`

## 支持的操作

- **draft** — 根据主题和要点生成邮件草稿
- **reply** — 根据原邮件生成回复建议
- **polish** — 润色已有邮件
- **review** — 邮件质检：语气、格式、遗漏检查

## 触发条件

当用户提到邮件相关需求时自动使用。
