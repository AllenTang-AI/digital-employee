---
name: doc-conversion-patterns
description: 文档格式转换最佳实践 — 图片/PDF/MD/DOCX 互转方案、工具选择、常见陷阱
---

# 文档转换方案 — doc-conversion-patterns

## 核心思路

Claude Code 内置多模态能力，直接读取图片/PDF/DOCX 文件，不需要 OCR 或解析脚本。

**官方做法**：用 `Read` 工具直接读取 → Claude 理解内容 → 用 `Write` 工具输出目标格式。

## 转换矩阵

| 转换方向 | 方式 | 效果 |
|---|---|---|
| 图片 → .docx | Read 图片 → Claude 理解 → Write docx | 高（视觉理解） |
| PDF → .docx/.md | Read PDF → Claude 提取 → Write | 高（直接读取） |
| DOCX → .md/.pdf | Read DOCX → Claude 提取 → Write | 高（直接读取） |
| MD → DOCX | Read MD → Claude 理解结构 → Write docx | 高（结构保留） |
| MD → PDF | Read MD → pandoc 渲染 | 高（PDF 渲染质量好） |
| 大纲 → PPT | Read 大纲 → python-pptx 生成 | 高 |

## 依赖

轻量级依赖（仅用于格式生成，不用于内容理解）：
- `pandoc`: md→pdf 最终渲染
- `python-docx`: 生成 .docx 文件
- `python-pptx`: 生成 .pptx 文件
- `openpyxl`: 生成 .xlsx 文件

**不再需要**：pytesseract、pdfplumber、mammoth、weasyprint（Claude 原生替代）

## 格式保留优先级

1. 标题层级 — # → 一级，## → 二级
2. 列表 — 编号和要点列表
3. 表格 — 行列结构、合并单元格
4. 代码块 — 等宽字体、保留缩进
5. 引用块 — 缩进或样式区分
6. 图片 — 嵌入时附带说明

## 常见陷阱

- Markdown `###` 映射到 Word 三级标题可能太小 — 考虑用二级替代
- pandoc 生成 PDF 可能丢失中文字体 — 确保字体回退已配置
- Word 长表格跨页拆分不美观 — 添加分页提示
- PDF 代码块用 Courier New 10pt

## 环境要求

使用 conda Python 3.13 运行：`python3.13 scripts/doc_processor.py <operation>`
