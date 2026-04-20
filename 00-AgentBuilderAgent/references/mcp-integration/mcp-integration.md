# MCP 集成邮件/通讯经验

## 思路

参考 slack / telegram 插件的 MCP 集成方式：

1. 用 MCP 协议连接外部服务（SMTP/IMAP 或 Gmail API）
2. 定义 4 个核心 tool：
   - `send_email` — 发邮件
   - `read_email` — 读邮件
   - `list_inbox` — 列收件箱
   - `search_email` — 搜邮件
3. 在 CLAUDE.md 里告诉 Agent 什么时候用这些工具

## 来源

`claude-plugins-official-main/external_plugins/slack`
`claude-plugins-official-main/external_plugins/telegram`
