---
name: document-conversion
description: 文档格式转换规则 — 何时用脚本 vs 原生 Read 工具、格式保留规范
---

# 文档转换技能 — document-conversion

## 何时用哪种方式

| 输入 | 输出 | 方式 |
|---|---|---|
| 图片 (png/jpg/bmp) | .docx | 直接用 Read 工具 — 你理解图片内容 |
| PDF | .docx | 直接用 Read 工具 — 提取并结构化内容 |
| Markdown | .docx | 使用脚本：`python3.13 scripts/doc_processor.py md2docx` |
| Markdown | .pdf | 使用脚本：`python3.13 scripts/doc_processor.py md2pdf` |
| Word (.docx) | .pdf | 使用脚本：`python3.13 scripts/doc_processor.py docx2pdf` |
| 任意文档 | 摘要 | 直接用 Read 工具 |
| 任意文档 | 提取内容 | 直接用 Read 工具 |

## 格式保留优先级

1. **标题层级** — # → 一级标题，## → 二级标题，依此类推
2. **列表** — 编号列表和要点列表必须保留
3. **表格** — 行列结构、合并单元格
4. **代码块** — 等宽字体、保留缩进
5. **引用块** — 缩进或样式区分
6. **图片** — 嵌入时附带说明文字

## 常见陷阱

- Markdown 的 `###` 在 Word 中映射为三级标题，可能显得太小 — 考虑用二级标题替代
- pandoc 生成的 PDF 可能丢失中文字体渲染 — 确保配置了字体回退
- Word 中的长表格可能跨页拆分不美观 — 添加分页提示
- PDF 中的代码块应使用易读的等宽字体（Courier New，10pt）
