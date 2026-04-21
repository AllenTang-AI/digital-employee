---
description: Product design — functional modules, user roles, prototype design
argument-hint: [module/feature]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /product — 产品设计

产品设计由 **product-designer** 子Agent 主导。

## 执行流程

1. 明确目标用户和功能范围
2. 确认项目在 workspace 下是否有对应目录，如无则创建
3. 加载 `skills/product-design` 中的设计规范
4. 调用 **product-designer** 子Agent进行产品设计
5. 输出功能模块、用户角色、原型设计
6. 输出到 `workspace/{项目名}/02-product/`

## 支持的操作

- **modules** — 功能模块设计
- **persona** — 用户角色定义
- **prototype** — 原型设计

## 触发条件

当用户提到功能设计、用户角色、原型设计、信息架构时自动使用。
