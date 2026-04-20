# 参照 Claude Code 官方模式重构 Agent 经验总结

## 背景

初始版本的 Agent 只是简单的 `CLAUDE.md` + 几个脚本，所有能力都在一个文件里内联处理。参照官方插件（feature-dev、code-review、pr-review-toolkit、skill-creator、hookify）重构后，形成了完整的多层架构。

## 官方插件核心模式

### 1. 分层架构（5 层）

| 层级 | 文件 | 作用 | 类比 |
|---|---|---|---|
| **插件清单** | `.claude-plugin/plugin.json` | 名称、描述、作者 | package.json |
| **角色定义** | `CLAUDE.md` | 我是谁、能做什么、工作规则 | README + system prompt |
| **命令** | `.claude/commands/*.md` | 斜杠命令，用户触发入口 | CLI 命令 |
| **子Agent** | `agents/*.md` | 专项能力，带 `name/tools/model/color` frontmatter | 专职员工 |
| **技能** | `skills/*/SKILL.md` | 按需加载的知识，渐进式披露 | 参考资料 |
| **钩子** | `.claude/hooks/hooks.json` | 事件驱动自动化（SessionStart/Stop/PreToolUse 等） | 监听器 |

### 2. 子Agent 声明规范

```yaml
---
name: security-scanner
description: 专注于安全漏洞扫描
tools: Read, Grep, Bash, Glob
model: sonnet
color: red
---
```

关键点：
- **tools** — 显式声明可用工具，限制权限范围
- **model** — 可以为 sonnet/haiku/opus，不同 Agent 用不同模型控制成本
- **color** — 终端中的视觉标识
- **description** — 可以包含 `<example>` XML 块，说明何时触发

### 3. 多Agent并行编排

官方 `feature-dev` 插件的 7 阶段流程：
```
Discovery → Codebase Exploration(并行) → Clarifying Questions → 
Architecture Design(并行) → Implementation → Quality Review(并行) → Summary
```

官方 `pr-review-toolkit` 插件：
```
PR Review = security-scanner + code-reviewer + test-analyzer + 
            comment-analyzer + silent-failure-hunter → 汇总评分
```

我们的 Agent 借鉴了这个模式：
- `/review full` → 并行启动 security-scanner + architecture-reviewer + test-analyzer → 汇总

### 4. 渐进式加载（Skills）

不是所有内容都塞进 CLAUDE.md（会浪费 token），而是：
- **CLAUDE.md** — 角色定义 + 规则（常驻）
- **SKILL.md** — 领域知识（按需加载）
- **references/** — 大型参考文档（SKILL.md 中引用）

例如 `skills/code-review-standards/SKILL.md` 包含团队的审查标准，只有在 `/review` 时才加载。

### 5. 事件驱动（Hooks）

官方 hookify 插件支持 5 种事件：`SessionStart`、`Stop`、`PreToolUse`、`PostToolUse`、`UserPromptSubmit`。

我们实现了 `SessionStart` hook：Agent 启动时自动检查 `workspace/input/` 下是否有待处理文件。

## 重构前后对比

| 维度 | 重构前 | 重构后 |
|---|---|---|
| 结构 | CLAUDE.md + commands + scripts | + agents/ + skills/ + hooks/ + plugin.json |
| 命令执行 | 单Agent内联完成 | 多Agent并行 → 汇总评分 |
| 知识加载 | 所有内容常驻上下文 | skills/ 按需加载，节省 token |
| 自动化 | 需要手动调用 | hooks 事件驱动 |
| 权限控制 | 无 | commands 声明 allowed-tools |
| 插件标识 | 无 | .claude-plugin/plugin.json |

## 实战教训

### 做对了

1. **先读源码再动手** — 完整阅读了 5 个官方插件的每个文件，理解了完整的模式
2. **保持编号前缀** — `00-knowledge`、`01-OfficeAgent`、`02-CodeAgent` 的编号让目录有序
3. **每个 Agent 有明确边界** — OfficeAgent 做办公，CodeAgent 做代码，不交叉

### 需要改进（待做）

1. **MCP 集成** — 官方插件虽然没有内置 .mcp.json，但 MCP 是连接外部系统（GitHub/Jira/邮件）的关键路径
2. **Hookify 深度集成** — 目前只做了 SessionStart，可以扩展 PreToolUse（写文件自动质检）、PostToolUse（完成自动归档）
3. **测试/评估** — 官方 skill-creator 插件有完整的 eval 体系，我们的 Agent 没有测试

## 后续 Agent 扩展模板

新建 Agent 时，直接复制这个骨架：

```
NN-AgentName/
  CLAUDE.md                          # 角色 + 规则
  .claude-plugin/plugin.json         # 插件清单
  .claude/
    commands/                        # 斜杠命令
      <name>.md
    hooks/
      hooks.json                     # 事件监听
  agents/                            # 专项子Agent
    <name>.md
  skills/                            # 按需加载知识
    <skill-name>/
      SKILL.md
  scripts/                           # 工具脚本
  workspace/
    input/
    output/
```
