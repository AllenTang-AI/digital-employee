---
description: Product roadmap — version planning, milestone, commercialization
argument-hint: [product-name] [plan|milestone|commercialize]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /roadmap — 产品规划

产品规划是产品规划 **P5 排期指标** 阶段的版本规划部分。

## 执行流程

1. 确认当前操作的产品名称
2. 检查前置阶段（P4 原型）是否已完成，提醒用户但可继续
3. 加载 `skills/product-planner` 中的 P5 检查清单和模板
4. 调用 **product-strategist** 子Agent进行产品规划
5. 输出到 `workspace/{产品名}/05-roadmap/`

## 支持的操作

- **plan** — 制定版本规划 → `05-roadmap/版本规划.md`
- **milestone** — 里程碑规划 → `05-roadmap/里程碑.md`
- **commercialize** — 商业化策略

## 触发条件

当用户提到版本规划、产品路线图、里程碑、商业化时自动使用。
