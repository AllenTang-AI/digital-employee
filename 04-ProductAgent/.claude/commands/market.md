---
description: Market research — competitor analysis, market sizing, user research, business model
argument-hint: [product-name] [competitor|sizing|user|business]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /market — 市场分析

市场分析是产品规划 **P1 看清市场** 和 **P2 想清策略** 阶段。

## 执行流程

1. 确认当前操作的产品名称。如果 workspace 下没有对应产品目录，先引导用户创建（调用 `skills/product-planner` 中的产品初始化流程）
2. 加载 `skills/product-planner` 中的 P1/P2 检查清单和模板
3. 加载 `skills/market-research` 中的分析框架
4. 加载 `skills/product-strategy` 中的商业模式和产品定位模板（仅 P2）
5. 调用 **product-strategist** 子Agent进行分析
6. 输出到 `workspace/{产品名}/01-market/`（P1）或 `workspace/{产品名}/02-strategy/`（P2）

## 支持的操作

- **competitor** — 竞品分析 → `01-market/竞品分析.md`
- **sizing** — 市场规模测算（TAM/SAM/SOM）→ `01-market/市场规模.md`
- **user** — 用户调研分析 → `01-market/用户画像.md`
- **business** — 商业模式设计 → `02-strategy/商业模式.md` + `02-strategy/产品定位.md`

## 触发条件

当用户提到竞品分析、市场调研、用户调研、商业模式、产品定位时自动使用。
