# Hookify 经验

## 核心思路

从"手动敲命令"变成"文件一丢自动干活"。

## 实现方式

在 `.claude/settings.json` 中配置 hooks：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "detect_and_process_file.sh"
          }
        ]
      }
    ]
  }
}
```

## OfficeAgent 场景

| 触发事件 | 自动动作 |
|---|---|
| inbox/screenshots/ 下新增图片 | 自动 OCR 转 Word → output/docs/ |
| inbox/files/ 下新增 .md 文件 | 检查是否为大纲，是则自动转 PPT |
| inbox/data/ 下新增 .csv 文件 | 自动出统计摘要 |

## 来源

`claude-plugins-official-main/plugins/hookify`
