# Digital Employee — 数字员工构建平台

基于 Claude Code 插件体系的多 Agent 数字员工平台，每个子目录代表一个独立的数字员工。

## 数字员工

| 编号 | 名称 | 定位 | 服务对象 |
|---|---|---|---|
| **00-AgentBuilderAgent** | 构建顾问 | 创建/审查数字员工 | 平台管理 |
| **01-OfficeAgent** | 办公助理 | 文档处理、邮件、工作汇报 | 个人办公 |
| **02-CodeAgent** | 软件架构师 | 代码审查、统计、架构重构 | 开发团队 |
| **03-AokongAgent** | 产品经理 | 产品架构、需求评审、进度跟踪、产品测试 | 无人机产品 |

## 员工结构

```
NN-EmployeeName/
  .claude-plugin/plugin.json    ← 员工身份标识
  CLAUDE.md                     ← 角色定义 + 工作规则
  agents/                       ← 专职子Agent（并行工作者）
  skills/                       ← 领域知识（按需加载）
  .claude/commands/             ← 交互入口（斜杠命令）
  .claude/hooks/                ← 事件驱动自动化
  scripts/                      ← 工具脚本
  workspace/                    ← 输入/输出目录（不上传）
```

## 快速开始

1. **前置条件**：安装 [Claude Code](https://github.com/anthropics/claude-code)
2. **克隆仓库**：
   ```bash
   git clone https://github.com/AllenTang-AI/ai-agent-digital-employee.git
   ```
3. **进入目录使用对应员工**：
   ```bash
   cd "Digital Employee"/01-OfficeAgent   # 办公助理
   cd "Digital Employee"/02-CodeAgent     # 代码审查
   cd "Digital Employee"/03-AokongAgent   # 产品管理
   ```

## 新建数字员工

1. 按顺序分配编号（NN-），如 `04-NewAgent`
2. 参考 `00-AgentBuilderAgent/skills/official-patterns/` 中的规范
3. 定义 `.claude-plugin/plugin.json` 标识
4. 至少包含 2 个子Agent + 1 个 skill

详细指南见 [00-AgentBuilderAgent/CLAUDE.md](00-AgentBuilderAgent/CLAUDE.md)

## 许可证

MIT
