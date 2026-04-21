---
description: Requirements management — PRD writing, backlog management, prioritization
argument-hint: [product-name] [write|review|prioritize|backlog]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /requirements — 需求管理

需求管理是产品规划 **P3 定好需求** 阶段。

## 执行流程

1. 确认当前操作的产品名称
2. 检查前置阶段（P1/P2）是否已完成，提醒用户但可继续
3. 加载 `skills/product-planner` 中的 P3 检查清单和模板
4. 加载 `skills/market-research` 中的用户调研方法（如需）
5. 调用 **requirements-manager** 子Agent撰写/评审 PRD
6. 输出到 `workspace/{产品名}/03-requirements/`

## 支持的操作

- **write** — 撰写 PRD 文档 → `03-requirements/PRD.md`
- **review** — 评审需求文档
- **prioritize** — 需求优先级排序（RICE/MoSCoW）→ `03-requirements/需求池.md`
- **backlog** — 需求池管理
- **brd** — 撰写 BRD → `03-requirements/BRD.md`
- **stories** — 撰写用户故事 → `03-requirements/用户故事.md`

## 触发条件

当用户提供需求描述、PRD 草稿或需要需求管理时自动使用。
