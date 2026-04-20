# 如何从 Claude 官方学习构建数字员工

## 核心理念

Claude Code 不是一个简单的代码工具，而是一个**数字员工运行时框架**。每个插件就是一个数字员工，遵循统一的岗位说明书格式。

官方提供了 10+ 个成熟插件（feature-dev、code-review、pr-review-toolkit、skill-creator、hookify 等），完整展示了如何构建高质量的多Agent系统。

---

## 第一步：理解官方插件的 5 层架构

每个官方插件都有以下结构，从外到内逐层细化：

```
plugin/
  .claude-plugin/plugin.json    ← 第1层：身份证（我是谁）
  CLAUDE.md                     ← 第2层：岗位说明书（我做什么、规则是什么）
  commands/*.md                 ← 第3层：交互入口（你怎么跟我说话）
  agents/*.md                   ← 第4层：专职子员工（具体谁干活）
  skills/*/SKILL.md             ← 第5层：参考资料（按需加载的知识）
  hooks/hooks.json              ← 事件驱动自动化（监听器）
```

### 第1层：插件清单（身份证）

```json
{
  "name": "office-agent",
  "description": "个人办公自动化助手",
  "author": { "name": "Tangwei" }
}
```

- **作用**：唯一标识一个数字员工
- **关键字段**：`name`（必填）、`description`、`author`
- **扩展字段**：`version`、`dependencies`、`userConfig`、`channels`

### 第2层：CLAUDE.md（岗位说明书）

这是最重要的文件，定义了员工的完整人格。必须包含：
- **角色** — 我是谁、服务谁
- **可用命令** — 我能做什么（表格列出）
- **子Agent** — 我的手下有哪些专职人员
- **Skills** — 我有哪些参考资料
- **工作规则** — 我的行为准则（5-7条）
- **工作目录** — 我的输入输出在哪里

### 第3层：Commands（交互入口）

每个 command 是一个斜杠命令，用户从这里触发工作。关键格式：

```yaml
---
description: 一句话说明
argument-hint: [参数提示]
allowed-tools: 允许使用的工具列表
---

# /命令名 — 中文标题

中文描述 + 执行流程 + 支持操作 + 触发条件
```

**核心要点**：
- frontmatter 声明元数据（YAML 格式）
- 正文全是中文描述（你的数字员工用中文交互）
- 明确说明由哪个子Agent负责

### 第4层：Agents（专职子员工）

这是官方模式最有价值的部分。每个 agent 是一个专职子员工：

```yaml
---
name: 员工名称
description: 他能干什么（越具体越好，支持 <example> 块）
tools: Read, Write, Edit, Bash    # 显式声明可用工具
model: sonnet                      # sonnet / haiku / opus
color: blue                        # 终端中的视觉标识
---

# 中文标题 — agent名称

## 核心使命
...
## 工作方法
...
## 输出格式
...
```

**关键设计原则**：
1. **一个 agent 只做一件事** — 比如 security-scanner 只管安全，不管架构
2. **tools 显式声明** — 每个 agent 只能访问它需要的工具
3. **model 按复杂度选** — 简单任务用 haiku 省钱，复杂推理用 opus
4. **description 包含触发条件** — 让 Claude 知道什么时候调用这个 agent

### 第5层：Skills（按需加载知识）

不是所有内容都塞进 CLAUDE.md。大段知识放进 skills/，按需加载：

```
skills/
  code-review-standards/
    SKILL.md          # 审查标准（按需加载）
  refactoring-patterns/
    SKILL.md          # 重构模式参考
    reference.md      # 大型参考文档
```

```yaml
---
name: skill名称
description: 这份知识是什么（决定是否自动加载）
---

# 中文标题

具体内容...
```

**加载时机**：
- command 中引用了某个 skill
- agent 的 skills 列表中声明了
- Claude 根据 description 判断当前场景需要这份知识

---

## 第二步：本地化适配的关键决策

### 1. 语言策略

官方插件全是英文，因为面向全球开发者。你的数字员工用**中文**：
- CLAUDE.md — 中文
- commands/*.md — 中文
- agents/*.md — 一级标题中文 + 英文副标题
- skills/*.md — 中文
- 但 YAML frontmatter 的字段名保持英文（name/description/tools 是固定格式）

### 2. 权限策略

官方默认要求每个操作都确认。对数字员工来说这太慢：

```json
{
  "permissions": {
    "allow": ["Bash"]
  }
}
```

`.claude/settings.json` 中放行所有 Bash 权限。

### 3. 工作目录

官方插件没有统一的工作目录概念。你增加了 `workspace/input/` 和 `workspace/output/`，按任务分类：

```
workspace/
  input/           ← 用户放入待处理文件
  output/          ← Agent 产出文件
```

### 4. Hooks 事件驱动

官方 hookify 插件支持 20+ 种事件。你目前只需要：

```json
{
  "hooks": {
    "SessionStart": [
      { "type": "command", "command": "python3.13 .../session_start.py" }
    ]
  }
}
```

Agent 启动时自动检查 `workspace/input/` 有没有待处理文件。

### 5. 编号前缀

官方插件没有编号。你用 `NN-` 前缀管理多个员工：

```
00-knowledge/          ← 知识库
01-OfficeAgent/        ← 办公助理
02-CodeAgent/          ← 代码工程师
03-AokongAgent/        ← 产品管理专家
```

---

## 第三步：多Agent并行编排（核心能力）

这是官方最有价值的模式。以 feature-dev 插件为例：

```
用户触发 /feature-dev
  ↓
Phase 1: Discovery（主Agent）
  ↓
Phase 2: Codebase Exploration（2个 explorer 并行）
  ↓
Phase 3: Clarifying Questions（主Agent）
  ↓
Phase 4: Architecture Design（2个 architect 并行）
  ↓
Phase 5: Implementation（主Agent）
  ↓
Phase 6: Quality Review（reviewer Agent）
  ↓
Phase 7: Summary（主Agent）
```

你当前的 CodeAgent 就用了这个模式：

```
用户触发 /review full
  ↓
Phase 1: 并行启动 3 个子Agent
  ├─ security-scanner     → 安全报告
  ├─ architecture-reviewer → 架构报告
  └─ test-analyzer         → 测试报告
  ↓
Phase 2: 汇总评分
  ↓
Phase 3: 输出统一报告
```

---

## 第四步：新建数字员工的标准流程

### 1. 定义身份

```bash
mkdir -p NN-EmployeeName/{agents,skills,.claude/{commands,hooks},scripts,workspace/{input,output}}
```

### 2. 填写 .claude-plugin/plugin.json

```json
{
  "name": "employee-name",
  "description": "一句话描述这个员工的职责",
  "author": { "name": "Tangwei" }
}
```

### 3. 编写 CLAUDE.md

包含：角色、可用命令、子Agent列表、Skills列表、工作规则、工作目录。

### 4. 定义子Agent

至少 2 个，每个 agent 有明确的使命和输出格式。

### 5. 创建 Skills

至少 1 个，包含该领域的核心知识和检查清单。

### 6. 创建 Commands

每个 command 声明 allowed-tools，说明由哪个子Agent负责。

---

## 第五步：质量检查清单

新建或改造一个数字员工后，逐项检查：

- [ ] `.claude-plugin/plugin.json` 存在且 name/description 填写完整
- [ ] `CLAUDE.md` 有明确的可用命令表（表格格式）
- [ ] `CLAUDE.md` 列出了所有子Agent和Skills
- [ ] 每个 command 有 `# /命令名 — 中文标题` 一级标题
- [ ] 每个 command 有 `description` 和 `allowed-tools` frontmatter
- [ ] 每个 agent 有 `name`/`description`/`tools`/`model`/`color` frontmatter
- [ ] 每个 agent 有 `# 中文标题 — agent名称` 一级标题
- [ ] 每个 skill 有 `name`/`description` frontmatter
- [ ] 每个 skill 有 `# 中文标题` 一级标题
- [ ] 所有文件内容为中文（frontmatter 字段名除外）
- [ ] `.claude/settings.json` 权限已配置
- [ ] hooks 已配置（至少 SessionStart）
- [ ] workspace/input/ 和 output/ 目录已创建

---

## 实战案例对比

### 改造前（2024年初的水平）

```
OfficeAgent/
  CLAUDE.md          ← 所有规则和能力写在一个文件里
  commands/
    doc.md           ← 直接调用脚本，没有子Agent
```

问题：
- 所有内容常驻上下文，浪费 token
- 没有权限隔离（所有命令能用所有工具）
- 无法并行执行
- 无法按需加载知识

### 改造后（当前水平）

```
01-OfficeAgent/
  CLAUDE.md                    ← 角色 + 规则，不到 50 行
  .claude-plugin/plugin.json   ← 身份标识
  .claude/commands/            ← 3个入口，每个声明 allowed-tools
  .claude/hooks/               ← 事件驱动
  agents/                      ← 3个专职子Agent
  skills/                      ← 2份按需加载的知识
  scripts/                     ← 工具脚本
```

优势：
- CLAUDE.md 精简，token 消耗降低 70%
- 每个 agent 只能访问它需要的工具
- `/report` 触发时可以并行调用多个 agent
- Skills 只在需要时才加载到上下文
- 启动时自动检查待处理文件

---

## 后续演进方向

1. **MCP 集成** — 连接外部系统（GitHub/Jira/邮件/OA），让数字员工能读写真实数据
2. **Marketplace 分发** — 建立企业级 Marketplace，团队成员 `claude plugin install` 即可使用
3. **评估体系** — 参照 skill-creator 插件的 eval 机制，测试数字员工的质量
4. **更多员工** — 按业务需求创建 TeamAgent（团队管理）、ProductAgent（需求管理）、SupplyAgent（供应链）等
