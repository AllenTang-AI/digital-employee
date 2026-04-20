# PDF/MD/DOCX 互转工具方案

## 核心思路

**Claude Code 内置多模态能力，直接读取图片/PDF/DOCX 文件，不需要 OCR 或解析脚本。**

官方做法：用 `Read` 工具直接读取文件 → Claude 理解内容 → 用 `Write` 工具输出目标格式。

## 当前实现（Claude 原生方式）

| 转换方向 | 方式 | 效果 |
|---|---|---|
| 图片 → 文字/docx | Read 图片 → Claude 识别内容 → Write docx | 高（视觉理解） |
| PDF → 文字/docx/md | Read PDF → Claude 提取内容 → Write | 高（直接读取） |
| DOCX → 文字/md/pdf | Read DOCX → Claude 提取内容 → Write | 高（直接读取） |
| MD → DOCX | Read MD → Claude 理解结构 → Write docx | 高（结构保留） |
| MD → PDF | Read MD → Claude 理解结构 → Write pdf（via pandoc） | 高 |
| 大纲 → PPT | Read 大纲 → Claude 理解结构 → python-pptx 生成 | 高 |

## 依赖

**轻量级依赖（仅用于格式生成，不用于内容理解）：**
- `pandoc`: md→pdf 最终渲染
- `python-docx`: 生成 .docx 文件
- `python-pptx`: 生成 .pptx 文件
- `openpyxl`: 生成 .xlsx 文件
- `markdown`: md 解析辅助

**不再需要：** pytesseract, pdfplumber, mammoth, weasyprint（Claude 原生替代）

## 使用方式

用户直接给文件，Claude 自动读取并转换：
```
"把这张截图转成 Word"          → Read 图片 → 写 docx
"把 PDF 转成 Markdown"         → Read PDF → 写 md
"把 Word 转成 PDF"             → Read docx → pandoc 生成 pdf
"把这个大纲做成 PPT"            → Read 大纲 → python-pptx 生成
```

## 环境要求

使用 conda Python 3.13 运行生成脚本：`python3.13 scripts/doc_processor.py <operation>`
