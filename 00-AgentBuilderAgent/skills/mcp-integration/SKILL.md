---
name: mcp-integration
description: MCP 集成模式 — 连接外部系统（邮件/GitHub/Jira/OA）的标准写法
---

# MCP 集成模式 — mcp-integration

## 思路

MCP（Model Context Protocol）让数字员工能读写外部系统，而不只是处理本地文件。

## 标准架构

1. 用 MCP 协议连接外部服务（SMTP/IMAP/Gmail API、GitHub API、Jira API）
2. 在 `.mcp.json` 中定义 MCP Server
3. 在 CLAUDE.md 中告诉 Agent 有哪些工具可用、什么时候用

## 配置格式

`.mcp.json`：

```json
{
  "mcpServers": {
    "email": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-email"],
      "env": {
        "GMAIL_CREDENTIALS": "/path/to/credentials.json"
      }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## 典型 MCP 工具

### 邮件系统
| Tool | 功能 |
|---|---|
| `send_email` | 发送邮件 |
| `read_email` | 读取邮件 |
| `list_inbox` | 列出收件箱 |
| `search_email` | 搜索邮件 |

### GitHub
| Tool | 功能 |
|---|---|
| `list_prs` | 列出 PR |
| `get_diff` | 获取代码差异 |
| `add_comment` | 添加评论 |
| `approve_pr` | 批准 PR |

### Jira
| Tool | 功能 |
|---|---|
| `get_issue` | 获取问题详情 |
| `create_issue` | 创建问题 |
| `update_status` | 更新状态 |
| `search_issues` | 搜索问题 |

## OfficeAgent 集成建议

| 外部系统 | MCP Server | 用途 |
|---|---|---|
| Gmail/Outlook | mcp-email | 实际收发邮件 |
| GitHub | mcp-github | PR 审查、diff 获取 |
| Jira | mcp-jira | 需求跟踪、迭代管理 |
| 飞书 | 自建 | 消息通知、文档协作 |
| OA 系统 | 自建 | 审批流程、考勤 |

## 安全注意

- MCP Server 的凭证（token、password）存入系统 keychain，不要硬编码
- `.mcp.json` 中敏感字段使用环境变量引用 `${VAR_NAME}`
- 确保 MCP Server 运行在本地，不要暴露到公网

## 参考来源

- `claude-plugins-official-main/external_plugins/slack`
- `claude-plugins-official-main/external_plugins/telegram`
