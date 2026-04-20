---
name: skill-structure
description: Skills 标准化格式 — SKILL.md 规范、渐进式加载、目录结构
---

# Skills 结构规范 — skill-structure

## 标准目录结构

```
skills/
  skill-name/
    SKILL.md           ← 必需：知识主体
    agents/            ← 可选：该 Skill 专用的子Agent
    scripts/           ← 可选：可执行脚本
    references/        ← 可选：大型参考文档（>300行放这里）
    assets/            ← 可选：模板、图标等静态资源
    evals/             ← 可选：测试用例
```

## SKILL.md 标准格式

```yaml
---
name: skill名称
description: 这份知识是什么（决定是否自动加载的关键）
when_to_use: 补充说明何时需要这份知识（可选）
argument-hint: [参数提示]（可选）
disable-model-invocation: true/false（可选）
allowed-tools: 工具列表（可选）
---

# 中文标题 — skill名称

具体内容...
```

## 渐进式加载原理

不是所有内容都塞进 CLAUDE.md，而是：

| 层级 | 加载时机 | 适合内容 |
|---|---|---|
| CLAUDE.md | 始终加载 | 角色、规则、命令表 |
| SKILL.md | 按需加载 | 领域知识、检查清单 |
| references/ | SKILL.md 引用 | 大型参考文档 |

## 编写规范

- **description 决定自动加载** — 描述越具体，Claude 越容易判断是否需要
- **SKILL.md 控制在 500 行以内** — 超过的内容放到 `references/` 目录
- **引用参考文件** — 在 SKILL.md 中用 `参考 [文件名](path)` 的方式引用
- **中文内容 + 英文字段名** — 正文中文，frontmatter 字段名英文

## 常见错误

- ❌ SKILL.md 超过 1000 行 — 应该拆分
- ❌ description 太模糊 — "各种知识" vs "代码审查标准和检查清单"
- ❌ 没有一级标题 — 文件第一行必须是 `# 标题`
- ❌ 内容全是英文 — 数字员工用中文交互，Skills 也应该是中文

## 参考来源

- `claude-plugins-official-main/plugins/skill-creator`
- `claude-code-main-anthropic/plugins/plugin-dev/skills/command-development/`
