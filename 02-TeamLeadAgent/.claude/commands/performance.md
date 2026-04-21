---
description: Performance coaching — OKR alignment, 1v1, performance review, growth plan
argument-hint: [member/topic]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /performance — 绩效辅导

绩效辅导由 **performance-coach** 子Agent 主导。

## 执行流程

1. 明确绩效辅导主题和目标项目
2. 确认项目在 workspace 下是否有对应目录，如无则创建
3. 调用 **performance-coach** 子Agent进行分析
4. 输出 OKR 方案、1v1 提纲、绩效评估或成长计划
5. 输出到 `workspace/{项目名}/04-performance/`

## 支持的操作

- **okr** — OKR 制定和评审
- **1v1** — 1v1 沟通提纲
- **review** — 绩效评估
- **growth** — 个人成长计划

## 触发条件

当用户提到 OKR、1v1、绩效、成长计划时自动使用。
