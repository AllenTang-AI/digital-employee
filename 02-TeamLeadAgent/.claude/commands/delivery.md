---
description: Project delivery — requirement breakdown, scheduling, progress tracking, retrospective
argument-hint: [project/sprint]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /delivery — 项目交付

项目交付由 **delivery-manager** 子Agent 主导。

## 执行流程

1. 明确项目交付主题和目标项目
2. 确认项目在 workspace 下是否有对应目录，如无则创建
3. 加载 `skills/project-delivery` 中的交付方法
4. 调用 **delivery-manager** 子Agent进行分析
5. 输出需求拆解、排期方案、进度报告或复盘
6. 输出到 `workspace/{项目名}/02-delivery/`

## 支持的操作

- **breakdown** — 需求拆解
- **schedule** — 排期评估
- **track** — 进度跟踪
- **retro** — 复盘总结

## 触发条件

当用户提到需求拆解、排期、进度、复盘时自动使用。
