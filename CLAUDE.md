# AI Agent — 数字员工构建平台

## 定位

本项目是一个基于 Claude Code 插件体系的**数字员工构建平台**。

每个子目录（`NN-AgentName/`）代表一个独立的数字员工，遵循统一的插件规范：

```
NN-EmployeeName/
  .claude-plugin/plugin.json    ← 员工身份标识
  CLAUDE.md                     ← 角色定义 + 工作规则
  agents/                       ← 专职子Agent（并行工作者）
  skills/                       ← 领域知识（按需加载）
  .claude/commands/             ← 交互入口（斜杠命令）
  .claude/hooks/                ← 事件驱动自动化
  scripts/                      ← 工具脚本
  workspace/                    ← 输入/输出目录
```

## 现有数字员工

| 编号 | 名称 | 定位 | 服务对象 |
|---|---|---|---|
| **00-AgentBuilderAgent** | 构建顾问 | 创建/审查数字员工 | 平台管理 |
| **01-OfficeAgent** | 办公助理 | 文档处理、邮件、工作汇报 | 个人办公 |
| **02-CodeAgent** | 软件架构师 | 代码审查、统计、架构重构 | 开发团队 |
| **03-AokongAgent** | 产品经理 | 产品架构、原型设计、需求评审、进度跟踪、产品测试 | 无人机产品 |

## 新建数字员工规范

1. 编号前缀：`NN-` 按创建顺序递增
2. 遵循官方插件结构（见 `00-AgentBuilderAgent/skills/official-patterns/`）
3. 每个员工有明确的 `.claude-plugin/plugin.json` 标识
4. 至少定义 2 个子Agent + 1 个 skill
