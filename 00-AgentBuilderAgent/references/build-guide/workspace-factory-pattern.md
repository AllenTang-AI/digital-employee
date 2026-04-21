# 数字员工工作目录规范 — Workspace Factory Pattern

## 核心原则

所有数字员工的 workspace 采用**工厂模式**：第一层按项目/任务组织，第二层是标准化的编号目录。

```
{Agent}/workspace/
  {项目或任务名称}/          ← 第一层：项目/任务维度
    00-references/           ← 输入（参考材料、代码、文档）
    01-{职责域1}/            ← 输出：职责域1
    02-{职责域2}/            ← 输出：职责域2
    03-{职责域3}/            ← 输出：职责域3
    ...
```

## 标准模板

### 1. OfficeAgent（办公助理）

```
workspace/
  {任务名称}/
    00-references/   ← 输入（待处理文档、原邮件、汇报素材）
    01-docs/         ← 文档处理输出
    02-emails/       ← 邮件沟通输出
    03-reports/      ← 工作汇报输出
```

### 2. TeamLeadAgent（研发团队 Leader）

```
workspace/
  {项目或团队名称}/
    00-references/   ← 输入（外部项目代码、技术文档、会议记录）
    01-tech/         ← 技术管理（技术方案、ADR、代码审查报告、技术债清单）
    02-delivery/     ← 项目交付（迭代计划、进度报告、复盘）
    03-team/         ← 团队建设（人才画像、面试评估、文化文档）
    04-performance/  ← 绩效辅导（OKR、1v1 提纲、绩效评估、IDP）
    05-efficiency/   ← 工程效能（效能指标、流程优化）
```

### 3. LowAltitudeAgent（低空经济）

```
workspace/
  {平台或区域名称}/
    00-references/   ← 输入（行业资料、竞品文档、政策文件）
    01-platform/     ← 平台架构
    02-product/      ← 产品设计
    03-construction/ ← 建设方案
    04-operations/   ← 运营策略
```

### 4. ProductAgent（B/G端产品经理）

```
workspace/
  {产品名称}/
    .product-info.json  ← 产品元信息（名称、阶段、创建时间、已完成阶段、关键决策）
    00-reference/       ← 参考文档（行业资料、历史文档、竞品资料）
    01-market/          ← P1 市场分析
    02-strategy/        ← P2 产品策略
    03-requirements/    ← P3 需求定义
    04-prototype/       ← P4 原型设计
    05-roadmap/         ← P5 排期指标
```

## 新建 Agent 的 workspace 设计规范

1. **第一层：项目/任务维度** — 使用者可以并行管理多个项目/任务，互不干扰
2. **00 固定为 references/reference** — 输入统一放在最前面
3. **01-05 编号与职责域一一对应** — 编号即顺序，小白能理解
4. **只有一级子目录** — 二级三级由使用者自行创建，不预设结构
5. **commands 中的输出路径使用 `{项目名}/` 变量** — 动态指向当前项目
6. **CLAUDE.md 中明确说明** — 当用户触发某个命令时，自动创建项目目录结构

## CLAUDE.md 工作目录描述模板

```markdown
## 工作目录

按**{项目/任务}**组织，每个{项目/任务}在 `workspace/` 下有独立目录：

```
workspace/
  {项目或任务名称}/
    00-references/   ← 输入（{输入类型}）
    01-{职责域1}/    ← {职责域1描述}
    02-{职责域2}/    ← {职责域2描述}
    ...
```

当用户提出{触发场景}时，自动创建对应{项目/任务}目录结构。输入放入 `00-references/`，输出保存到对应编号目录。二级目录由使用者自行创建。
```

## Command 执行流程模板

```markdown
## 执行流程

1. 明确{主题}和目标{项目/任务}
2. 确认{项目/任务}在 workspace 下是否有对应目录，如无则创建（含 00-references/ 和各输出目录）
3. 加载 `skills/{skill-name}` 中的{方法论}
4. 调用 **{agent-name}** 子Agent进行{分析}
5. 输出{产出物}
6. 输出到 `workspace/{项目名}/{编号}-{职责域}/`
```

## 注意事项

- ProductAgent 是特例，包含 `.product-info.json` 状态文件和 5 阶段流程
- OfficeAgent 的第一层叫"任务"而非"项目"，更贴合办公场景
- TeamLeadAgent 的第一层叫"项目或团队名称"，可以审查外部项目代码
- LowAltitudeAgent 的第一层叫"平台或区域名称"，对应低空经济建设场景
- 所有编号从 00 开始，00 固定为输入，01-05 为输出
