---
description: Operations strategy — operation model, data metrics, commercialization
argument-hint: [platform/scenario]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /operations — 运营策略

运营策略由 **operations-strategist** 子Agent 主导。

## 执行流程

1. 明确运营目标和场景
2. 确认项目在 workspace 下是否有对应目录，如无则创建
3. 加载 `skills/operations-strategy` 中的运营框架
4. 调用 **operations-strategist** 子Agent制定运营策略
5. 输出运营模式、数据指标、商业化方案
6. 输出到 `workspace/{项目名}/04-operations/`

## 支持的操作

- **model** — 运营模式设计
- **metrics** — 数据指标体系
- **revenue** — 商业化方案

## 触发条件

当用户提到运营模式、数据指标、商业化、增长策略时自动使用。
