---
description: Tech management — tech selection, architecture review, code quality, tech debt
argument-hint: [topic/area]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /tech — 技术管理

技术管理由 **tech-lead** 子Agent 主导。

## 执行流程

1. 明确技术管理主题和目标项目
2. 确认项目在 workspace 下是否有对应目录，如无则创建（含 00-references/ 和各输出目录）
3. 加载 `skills/tech-management` 中的方法论
4. 调用 **tech-lead** 子Agent进行分析
5. 输出技术方案、架构决策、代码质量报告
6. 输出到 `workspace/{项目名}/01-tech/`

## 支持的操作

- **selection** — 技术选型分析
- **adr** — 架构决策记录
- **quality** — 代码质量标准
- **debt** — 技术债务评估

## 触发条件

当用户提到技术选型、架构评审、代码质量、技术债时自动使用。
