# Skill 标准化规范

## 格式模板

每个 slash command 的 .md 文件应包含：

```markdown
# /命令名 — 一句话描述

调用 `scripts/xxx.py` 处理。

## 用法
/命令名 <操作> [参数]

## 支持的操作
- **操作1** — 描述
- **操作2** — 描述

## 示例
```
/命令名 操作1 --file xxx
```

## 执行
1. 步骤一
2. 步骤二
3. 步骤三
```

## 来源

`claude-plugins-official-main/plugins/skill-creator`
`claude-code-main-anthropic/plugins/plugin-dev/skills/command-development/`
