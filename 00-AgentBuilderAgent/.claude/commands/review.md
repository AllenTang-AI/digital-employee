---
description: 审查数字员工 — 检查结构是否符合 Claude 官方标准
argument-hint: [Agent目录]
allowed-tools: Read, Write, Bash, Glob, Grep, Task
---

# /review — 审查数字员工

由 **employee-architect** 子Agent 主导，参考 `skills/official-patterns` 中的质量检查清单。

## 执行流程

1. 读取目标 Agent 目录结构
2. 逐项检查质量检查清单
3. 输出审查报告，标注通过/不通过项
4. 给出修复建议

## 审查维度

- 目录结构是否完整
- plugin.json 是否填写完整
- CLAUDE.md 是否包含必需内容
- Commands 是否有 frontmatter + 一级标题
- Agents 是否有完整 frontmatter + 一级标题
- Skills 是否有 frontmatter + 一级标题
- 内容是否中文
- 权限是否配置
- Hooks 是否配置
- Workspace 目录是否创建

## 触发条件

当用户需要审查或验证现有数字员工时自动使用。
