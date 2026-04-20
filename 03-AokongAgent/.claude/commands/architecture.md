---
description: Product architecture — system design, module decomposition, technology selection
argument-hint: [product/module]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /architecture — 产品架构

产品架构由 **product-architect** 子Agent 主导。

## 执行流程

1. 理解产品需求（PRD、产品愿景、用户场景）
2. 调用 **product-architect** 子Agent进行架构设计
3. 输出架构方案，包含模块拆分、技术选型、接口定义
4. 输出到 `workspace/output/`

## 支持的操作

- **design** — 设计产品架构
- **review** — 审查现有架构
- **compare** — 对比多个架构方案

## 触发条件

当用户提到产品架构、系统设计、模块拆分时自动使用。
