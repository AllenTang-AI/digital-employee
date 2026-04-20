---
description: Architecture refactoring — identify smells, suggest restructuring, generate roadmap
argument-hint: [file/directory] [operation]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /refactor — 架构重构

从架构维度识别问题并生成重构方案，参考 `skills/refactoring-patterns` 中的模式。

## 支持的操作

| 操作 | 输出 | 用途 |
|---|---|---|
| **smells** | 架构坏味道清单 | 循环依赖、紧耦合、职责不清 |
| **suggest** | 具体重构方案 | 模块拆分、层次划分、接口抽象 |
| **plan** | 分阶段重构路线图 | 优先级、风险、实施计划 |

## 执行流程

1. 加载 `skills/refactoring-patterns` 中的模式参考
2. 用 Read 工具分析项目结构和代码依赖
3. 调用 **architecture-reviewer** 子Agent识别问题
4. 生成重构方案，分阶段实施
5. 应用重构前先向用户确认

## 触发条件

当用户提到"重构"、"架构优化"、"代码拆分"、"模块调整"时自动使用。
