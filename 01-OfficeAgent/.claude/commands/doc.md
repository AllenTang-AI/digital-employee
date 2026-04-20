---
description: Document processing — format conversion, content extraction, quality review
argument-hint: [file] [operation]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---
# /doc — 文档处理

文档处理采用 **Claude 原生 + 脚本生成** 双模式。

## 执行流程

1. 识别用户意图：格式转换、内容提取、文档质检
2. 调用 **doc-analyzer** 子Agent进行内容理解和格式分析
3. 需要格式生成时调用对应脚本（md2docx/md2pdf/docx2pdf）
4. 输出到 `workspace/output/docs/`

## 支持的操作

| 操作     | 输入       | 输出       | 实现                                |
| -------- | ---------- | ---------- | ----------------------------------- |
| img2docx | 图片       | .docx      | Read 图片 → 理解内容 → Write docx |
| md2docx  | Markdown   | .docx      | 脚本生成                            |
| md2pdf   | Markdown   | .pdf       | pandoc 渲染                         |
| docx2pdf | Word       | .pdf       | 脚本渲染                            |
| pdf2docx | PDF        | .docx      | Read PDF → 理解内容 → Write docx  |
| review   | 任意文档   | 质检报告   | Read + 检查                         |
| extract  | 任意文档   | 提取内容   | Read + 提取                         |
| merge    | 多个 .docx | 合并 .docx | 脚本合并                            |
| summary  | 任意文档   | 摘要       | Read + 生成                         |

## 脚本选择

- 图片/PDF/DOCX 内容理解：直接用 Read 工具，不需要脚本
- md → docx：`python3.13 scripts/doc_processor.py md2docx`
- md → pdf：`python3.13 scripts/doc_processor.py md2pdf`
- docx → pdf：`python3.13 scripts/doc_processor.py docx2pdf`
- 文档合并：`python3.13 scripts/doc_processor.py merge`

## 触发条件

当用户需要处理文档时自动使用。
