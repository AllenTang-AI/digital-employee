---
name: hookify-rules
description: Hooks 事件驱动配置规范 — 可用事件、格式、匹配规则、Python Hook 写法
---

# Hooks 配置规范 — hookify-rules

## 核心思路

从"手动敲命令"变成"事件触发自动干活"。

## 配置文件格式

`.claude/hooks/hooks.json`：

```json
{
  "description": "Hook 描述",
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          { "type": "command", "command": "python3.13 ${CLAUDE_PLUGIN_ROOT}/.claude/hooks/session_start.py", "timeout": 15 }
        ]
      }
    ]
  }
}
```

## 可用事件

| 事件 | 触发时机 | 典型用途 |
|---|---|---|
| `SessionStart` | 会话启动 | 检查待处理文件 |
| `Stop` | 会话正常结束 | 生成会话总结 |
| `StopFailure` | 会话异常结束 | 错误报告 |
| `UserPromptSubmit` | 用户发送消息 | 输入校验/路由 |
| `PreToolUse` | 工具执行前 | 安全检查/拦截 |
| `PostToolUse` | 工具执行后 | 自动处理产出 |
| `PostToolUseFailure` | 工具执行失败 | 降级处理 |
| `SubagentStart` | 子Agent启动 | 上下文注入 |
| `SubagentStop` | 子Agent结束 | 结果汇总 |
| `FileChanged` | 文件变化 | 文件监控 |
| `CwdChanged` | 工作目录变化 | 路径重新检查 |

## PreToolUse Matcher 格式

```json
{
  "PreToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [
        { "type": "command", "command": "echo '文件变更检测'" }
      ]
    }
  ]
}
```

## Python Hook 标准写法

```python
#!/usr/bin/env python3
"""Hook 脚本 — 从 stdin 读取 JSON 上下文，输出到 stdout"""

import sys
import json
from pathlib import Path

def main():
    # 读取上下文（可选）
    try:
        data = json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {}
    except (json.JSONDecodeError, ValueError):
        data = {}

    # 你的逻辑
    # ...

    # 输出信息（可选，会显示在终端）
    print("处理完成")

    # 必须 exit(0)，否则 Claude 认为 hook 失败
    sys.exit(0)

if __name__ == "__main__":
    main()
```

## 典型应用场景

| 触发事件 | 自动动作 |
|---|---|
| SessionStart | 检查 workspace/input/ 新增文件 |
| PostToolUse (Write) | 文件写完自动质检/格式化 |
| FileChanged | 监控目录变化自动处理 |

## 注意事项

- Hook 命令超时默认 10 秒，可根据需要调整
- Hook 脚本必须 `sys.exit(0)` 退出，非零退出码会被视为失败
- Hook 输出到 stdout 会显示在终端，stderr 会被记录但用户看不到
- `${CLAUDE_PLUGIN_ROOT}` 是插件安装目录的绝对路径
