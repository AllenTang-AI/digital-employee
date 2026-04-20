---
name: official-patterns
description: Claude 官方插件 5 层架构规范、子Agent声明、多Agent并行编排模式
---

# 官方插件架构模式 — official-patterns

## 5 层架构

每个官方插件从外到内逐层细化：

```
plugin/
  .claude-plugin/plugin.json    ← 第1层：身份证
  CLAUDE.md                     ← 第2层：岗位说明书
  commands/*.md                 ← 第3层：交互入口
  agents/*.md                   ← 第4层：专职子员工
  skills/*/SKILL.md             ← 第5层：参考资料
  hooks/hooks.json              ← 事件驱动
```

## 子Agent 声明规范

```yaml
---
name: security-scanner
description: 专注于安全漏洞扫描（可包含 <example> 块说明触发条件）
tools: Read, Grep, Bash, Glob
model: sonnet
color: red
---
```

关键：
- **tools** — 显式声明，限制权限
- **model** — sonnet/haiku/opus，按复杂度选
- **color** — 终端视觉标识
- **description** — 越具体越好

## 多Agent并行编排

官方 feature-dev 的 7 阶段：
```
Discovery → Codebase Exploration(并行) → Clarifying Questions → 
Architecture Design(并行) → Implementation → Quality Review(并行) → Summary
```

官方 pr-review-toolkit：
```
PR Review = security-scanner + code-reviewer + test-analyzer + 
            comment-analyzer + silent-failure-hunter → 汇总评分
```

## 渐进式加载（Skills）

- **CLAUDE.md** — 角色 + 规则（常驻上下文）
- **SKILL.md** — 领域知识（按需加载）
- **references/** — 大型参考文档（SKILL.md 中引用）

## 事件驱动（Hooks）

官方支持 20+ 种事件：`SessionStart`、`Stop`、`PreToolUse`、`PostToolUse`、`UserPromptSubmit`、`SubagentStop`、`FileChanged` 等。

当前实现 `SessionStart`：Agent 启动时检查 `workspace/input/` 待处理文件。

## 质量检查清单

- [ ] `.claude-plugin/plugin.json` 存在且填写完整
- [ ] `CLAUDE.md` 有可用命令表、子Agent列表、Skills列表、工作规则
- [ ] 每个 command 有 YAML frontmatter + `# /命令名 — 中文标题` 一级标题
- [ ] 每个 agent 有完整 frontmatter（name/description/tools/model/color）+ 一级标题
- [ ] 每个 skill 有 frontmatter（name/description）+ 一级标题
- [ ] 所有文件内容为中文（frontmatter 字段名除外）
- [ ] `.claude/settings.json` 权限已配置
- [ ] hooks 已配置（至少 SessionStart）
- [ ] workspace/input/ 和 output/ 已创建
