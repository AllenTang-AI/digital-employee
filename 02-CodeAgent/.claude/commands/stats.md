---
description: Code statistics — daily workload, author contribution, module changes, trends
argument-hint: [operation] [parameters]
allowed-tools: Bash, Read, Write
---

# /stats — 代码统计

基于 git log 分析团队代码提交情况，生成每日工作量报告。

## 支持的操作

| 操作 | 输出 | 用途 |
|---|---|---|
| **daily** | 每日提交数、作者数、文件变更、新增/删除行数 | 每日工作量 |
| **author** | 各开发者提交数、代码行数贡献 | 个人贡献对比 |
| **module** | 各目录变更频次 | 热点模块识别 |
| **trend** | 近N天提交趋势图 | 团队活跃度 |
| **report** | 完整统计报告 | 管理层汇报 |

## 执行

1. 调用 `python3.13 scripts/code_stats.py <operation> <args>` 生成统计数据
2. 输出到 console 或指定文件

## 示例

```
/stats daily
/stats daily --since 2026-04-01
/stats author
/stats module src/
/stats trend --days 30
/stats report --output stats.md
```

## 触发条件

当用户提到代码统计、工作量、提交情况时自动使用。
