---
description: Construction plan — implementation plan, infrastructure, deployment
argument-hint: [project/region]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /construction — 建设方案

建设方案由 **construction-planner** 子Agent 主导。

## 执行流程

1. 明确建设项目和目标
2. 确认项目在 workspace 下是否有对应目录，如无则创建
3. 加载 `skills/construction-standard` 中的建设标准
4. 调用 **construction-planner** 子Agent制定建设方案
5. 输出实施计划、基础设施规划、投资估算
6. 输出到 `workspace/{项目名}/03-construction/`

## 支持的操作

- **plan** — 制定建设方案
- **estimate** — 投资估算
- **schedule** — 实施计划

## 触发条件

当用户提到建设方案、实施计划、投资估算、验收标准时自动使用。
