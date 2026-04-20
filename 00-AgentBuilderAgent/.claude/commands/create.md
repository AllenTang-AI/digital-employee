---
description: 创建数字员工 — 生成完整的 Claude Code 插件结构
argument-hint: [员工名称] [职责描述]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /create — 创建数字员工

由 **employee-architect** 子Agent 主导，参考 `skills/official-patterns` 中的架构规范。

## 执行流程

1. 了解用户需求：员工名称、职责、服务对象
2. 确定子Agent数量和职责
3. 确定需要的 Skills（官方模式、hookify、MCP 等）
4. 调用 **employee-architect** 子Agent生成完整结构
5. 输出到对应目录

## 需要用户提供的信息

- 员工编号（NN-）
- 员工名称
- 一句话职责描述
- 服务对象
- 核心能力（3-5个）
- 子Agent数量和职责

## 触发条件

当用户需要创建新的数字员工时自动使用。
