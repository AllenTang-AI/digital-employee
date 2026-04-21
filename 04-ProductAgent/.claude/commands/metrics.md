---
description: Data metrics — KPI definition, data analysis, growth strategy
argument-hint: [product-name] [define|analyze|growth]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /metrics — 数据指标

数据指标是产品规划 **P5 排期指标** 阶段的指标定义部分。

## 执行流程

1. 确认当前操作的产品名称
2. 检查前置阶段是否已完成，提醒用户但可继续
3. 加载 `skills/product-planner` 中的 P5 检查清单和模板
4. 加载 `skills/data-metrics` 中的指标体系
5. 调用 **data-analyst** 子Agent进行数据分析
6. 输出到 `workspace/{产品名}/05-roadmap/`

## 支持的操作

- **define** — 定义核心指标体系 → `05-roadmap/核心指标体系.md`
- **analyze** — 数据分析（漏斗、留存、分群）
- **growth** — 增长策略（AARRR 模型）

## 触发条件

当用户提到数据分析、指标定义、增长策略、A/B 测试时自动使用。
