---
description: Team building — talent profile, interview, team culture, knowledge management
argument-hint: [topic/person]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /team — 团队建设

团队建设由 **team-builder** 子Agent 主导。

## 执行流程

1. 明确团队管理主题和目标项目
2. 确认项目在 workspace 下是否有对应目录，如无则创建
3. 加载 `skills/team-culture` 中的团队方法论
4. 调用 **team-builder** 子Agent进行分析
5. 输出人才画像、面试方案、文化文档
6. 输出到 `workspace/{项目名}/03-team/`

## 支持的操作

- **profile** — 人才画像
- **interview** — 面试方案
- **culture** — 团队文化建设
- **knowledge** — 知识管理

## 触发条件

当用户提到招聘、面试、团队文化、知识管理时自动使用。
