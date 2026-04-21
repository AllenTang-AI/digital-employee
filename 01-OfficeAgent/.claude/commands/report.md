---
description: Work reports — weekly summaries, progress reports, quarterly reviews, briefing materials
argument-hint: [operation]
allowed-tools: Read, Write, Edit, Bash, Task, TodoWrite
---

# /report — 工作汇报

工作汇报由 **report-writer** 子Agent主导，按报告类型选择模板生成。

## 执行流程

1. 识别报告类型：weekly/progress/quarterly/briefing/outline2ppt
2. 确认任务在 workspace 下是否有对应目录，如无则创建
3. 引导用户提供输入（要点/数据/里程碑）
4. 调用 **report-writer** 子Agent生成结构化报告
5. 输出到 `workspace/{任务名}/03-reports/`
5. 如需 PPT，调用 `python3.13 scripts/outline_to_ppt.py`

## 支持的报告类型

| 类型 | 结构 | 适用场景 |
|---|---|---|
| weekly | 本周完成/进行中/风险/下周计划 | 团队周报 |
| progress | 概况/里程碑/KPI/风险建议 | 项目进度 |
| quarterly | OKR完成/成果/教训/下季规划 | 季度总结 |
| briefing | 核心结论(3条)/关键数据/需决策 | 向上汇报 |
| outline2ppt | 大纲→幻灯片 | 从大纲生成PPT |

## 触发条件

当用户提到汇报、总结、周报时自动使用。
