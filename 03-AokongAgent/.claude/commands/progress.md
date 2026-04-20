---
description: Progress tracking — milestone status, risk analysis, blocker identification
argument-hint: [project/milestone]
allowed-tools: Read, Write, Bash, Task
---

# /progress — 进度跟踪

跟踪产品项目进度，分析风险和阻塞项。

## 执行流程

1. 读取项目/里程碑状态信息
2. 分析进度偏差和风险
3. 输出进度报告

## 支持的操作

- **status** — 查看当前项目状态
- **risk** — 风险预警分析
- **report** — 生成进度报告

## 触发条件

当用户提到进度、里程碑、风险预警时自动使用。
