---
description: Code review using specialized agents — security, architecture, test coverage
argument-hint: [file/directory] [operation]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /review — 代码审查

代码审查采用 **多Agent并行** 模式，参考官方 code-review 和 pr-review-toolkit 插件。

## 执行流程

### Phase 1: 并行扫描

同时启动 3 个子Agent并行审查：

1. **security-scanner** — 安全检查：注入、XSS、越权、敏感数据
2. **architecture-reviewer** — 架构审查：模块划分、耦合度、设计模式
3. **test-analyzer** — 测试分析：覆盖率、边缘案例、反模式

### Phase 2: 汇总评分

综合 3 个Agent的结果，生成统一报告：
- 安全评级 + 架构评级 + 测试评级
- 按严重程度排序的问题列表
- 具体修复建议

### Phase 3: 输出

输出审查报告到 console 或 `workspace/output/code/`

## 支持的操作

- **quick** — 快速审查：只跑 security-scanner
- **full** — 完整审查：3个Agent并行 + 汇总
- **security** — 只跑 security-scanner
- **diff** — 审查 git diff 变更
- **report** — 生成完整审查报告

## 静态扫描补充

在Agent审查前，先运行 `python3.13 scripts/code_review.py` 进行规则扫描，结果一并汇总。

## 触发条件

当用户提到代码审查时自动使用。
