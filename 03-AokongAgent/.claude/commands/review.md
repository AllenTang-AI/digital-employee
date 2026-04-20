---
description: Requirements review — PRD analysis, requirement quality assessment, priority recommendation
argument-hint: [PRD document]
allowed-tools: Read, Write, Grep, Glob, Task
---

# /review — 需求评审

需求评审由 **requirements-reviewer** 子Agent 主导，参考 `skills/requirements-review` 中的检查清单。

## 执行流程

1. 加载 `skills/requirements-review` 中的评审检查清单
2. 调用 **requirements-reviewer** 子Agent审查 PRD
3. 输出评审报告，包含问题清单、优先级建议、缺失需求
4. 输出到 `workspace/output/`

## 支持的操作

- **prd** — 审查产品需求文档
- **backlog** — 审查需求池

## 触发条件

当用户提到需求评审、PRD、需求分析时自动使用。
