---
description: Product testing — test case generation, defect analysis, test report
argument-hint: [product/module] [operation]
allowed-tools: Read, Write, Grep, Glob, Bash, Task
---

# /test — 产品测试

产品测试由 **test-designer** 子Agent 主导，参考 `skills/testing-standards` 中的测试标准。

## 执行流程

1. 加载 `skills/testing-standards` 中的测试标准
2. 调用 **test-designer** 子Agent生成测试用例或分析缺陷
3. 输出测试报告
4. 输出到 `workspace/output/`

## 支持的操作

- **generate** — 生成测试用例
- **analyze** — 缺陷分析
- **report** — 生成测试报告

## 测试类别

| 类别 | 覆盖 | 优先级 |
|---|---|---|
| 功能测试 | 核心功能按规格运行 | P1 |
| 飞行测试 | 起降、悬停、航线、返航 | P0 |
| 安全测试 | 电子围栏、避障、应急程序 | P0 |
| 环境测试 | 温度、湿度、抗风、海拔 | P1 |
| 通信测试 | 距离、延迟、重连、抗干扰 | P1 |
| 电池测试 | 续航、充电循环、低电量行为 | P0 |

## 触发条件

当用户提到测试用例、缺陷分析、测试报告时自动使用。
