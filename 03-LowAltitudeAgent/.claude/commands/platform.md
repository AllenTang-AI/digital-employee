---
description: Platform architecture — system architecture, technology selection, interface design
argument-hint: [platform/scope]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /platform — 平台架构

平台架构由 **platform-architect** 子Agent 主导。

## 执行流程

1. 明确平台定位和建设范围
2. 确认项目在 workspace 下是否有对应目录，如无则创建
3. 加载 `skills/platform-architecture` 中的架构规范
4. 调用 **platform-architect** 子Agent进行架构设计
5. 输出系统架构、技术选型、接口设计
6. 输出到 `workspace/{项目名}/01-platform/`

## 支持的操作

- **design** — 设计平台架构
- **review** — 审查现有架构
- **compare** — 对比多个技术方案

## 触发条件

当用户提到平台架构、技术选型、系统分层、接口设计时自动使用。
