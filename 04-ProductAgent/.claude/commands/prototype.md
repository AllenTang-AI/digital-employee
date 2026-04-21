---
description: Product design — interaction prototype, information architecture, UX
argument-hint: [product-name] [ia|design|review]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /prototype — 产品设计

产品设计是产品规划 **P4 画好原型** 阶段。

## 执行流程

1. 确认当前操作的产品名称
2. 检查前置阶段（P3 PRD）是否已完成，提醒用户但可继续
3. 加载 `skills/product-planner` 中的 P4 检查清单和模板
4. 调用 **ux-designer** 子Agent进行信息架构和原型设计
5. 输出到 `workspace/{产品名}/04-prototype/`

## 支持的操作

- **ia** — 信息架构设计 → `04-prototype/信息架构.md`
- **design** — 页面原型和交互流程 → `04-prototype/交互原型.md`
- **review** — 评审现有设计
- **pages** — 页面清单 → `04-prototype/页面清单.md`

## 触发条件

当用户提到原型设计、交互流程、信息架构、用户体验时自动使用。
