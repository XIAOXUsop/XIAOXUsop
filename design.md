# GitHub 技术主页改造方案

> 适用目标：面向 Java 后端开发、AI 应用开发和 Agent 开发岗位展示可核验的技术能力；不公开年龄、学校、年级等个人背景。
>
> 本方案同时是本仓库 README 改造的内容规范、视觉规范和真实性清单。主页不是“技能大全”，而是一份可以被招聘方快速核验的工程作品索引。

## 1. 改造目标

### 1.1 主页要解决的三个问题

招聘方进入 GitHub 后，通常不会从头阅读一篇很长的自我介绍。新版主页需要在不同时间预算下回答不同问题：

| 阅读时间 | 必须回答的问题 | 页面承载位置 |
|---|---|---|
| 10 秒 | 技术方向是什么？希望承担什么工作？ | 首屏头图、方向说明、岗位方向 |
| 30 秒 | 你真正做过哪些项目？最强的三个是什么？ | “30 秒速览”和三个旗舰项目 |
| 2 分钟 | 项目是否有工程深度、测试和可复现证据？ | 项目证据、验证数据、仓库链接 |
| 5 分钟以上 | 代码质量如何？是否知道系统边界？ | 各项目 README、测试、设计文档、评测报告 |

### 1.2 目标形象

主页最终要建立的技术定位不是宽泛的“会 Java、Vue、AI”，而是：

> 以 Java 后端为基础，能够把 AI/Agent 原型做成可测试、可追溯、可恢复系统的开发者。

主品牌关键词：

- Java Backend
- AI Applications
- Agent Engineering
- Evaluable
- Traceable
- Recoverable
- Observable

### 1.3 成功标准

改造完成后应满足：

1. 首屏直接写明技术方向和开放机会，不公开年龄、学校、年级等个人信息。
2. 首屏不出现无法核验的“大规模生产”“企业落地”“服务百万用户”等表述。
3. 三个旗舰项目分别证明完整系统能力、Agent 基础设施能力和安全工具能力。
4. 每个关键结论都能点进仓库找到代码、测试或报告。
5. README 控制在可快速扫描的长度，详细设计留在各项目仓库。
6. 不依赖大量第三方动态图片服务，避免加载失败和模板感。
7. 明暗主题下都保持可读。

## 2. 真实性原则

### 2.1 可以写的内容

- 仓库中已经实现的功能。
- 已经存在的 CI、测试、Release、设计文档和评测报告。
- 有明确测试集、环境、时间和边界说明的实验数字。
- “开放相关岗位机会”这类不暴露个人背景的当前状态。
- “熟悉/使用”某项技术，但前提是它确实出现在项目中。

### 2.2 不写的内容

- 未发生的实习、工作经历、奖项、竞赛名次和用户量。
- 把合成 DEV 数据上的准确率写成生产准确率。
- 把本地演示系统写成真实银行生产系统。
- 把“项目使用过”升级成“精通”。
- 无法稳定复现或项目 README 已不再支持的旧数字。
- 与项目无关、只为堆关键词添加的技术图标。

### 2.3 用词规范

| 避免 | 推荐 |
|---|---|
| 企业级落地 | 按企业系统关注点设计 / 企业级工程实践演示 |
| 精通 Java | 以 Java 21 / Spring Boot 3 完成多个可运行项目 |
| 生产可用 | 提供测试、CI、离线演示和 Release；生产化仍需真实数据与领域评审 |
| 模型准确率 100% | 9 条冻结合成 DEV 上达到 100%，可能过拟合，不代表生产效果 |
| 零误报 | 在当前测试集/规则边界内通过；不扩展为真实世界保证 |

## 3. 已核验的内容资产

下面是主页可以依赖的证据账本。实际 README 只选取少量高价值证据，避免变成数据墙。

### 3.1 amlagent

定位：商业银行 AML 尽调 Agent 平台，是完整度最高的旗舰项目。

已核验能力：

- Java 21、Spring Boot 3.5、LangChain4j、Vue 3。
- Transactional Outbox + Redis Streams 任务链路。
- Snapshot First 冻结业务快照。
- 混合 RAG、证据 ID、Guardrails、人审闭环。
- Prometheus 与 OpenTelemetry GenAI 追踪。
- Docker Compose 离线 Mock 演示。

可引用数据：

- RAG 固定 DEV：无精排 Recall@5 93.3%，本地 bge 精排后 100%。
- 精排的本机冷缓存 P95 从 135ms 增至 671ms，主页应同时保留质量收益与延迟代价。
- 9 条冻结合成 DEV 的模型结果属于调优基线，必须带“合成 DEV / 不代表生产准确率”限定。

主页使用策略：

- 重点证明后端可靠性、Agent 工程化和证据闭环。
- 不在主页重复完整工作流、API 表和所有测试数字。
- 使用“可运行的工程项目/演示平台”，不使用“真实银行生产平台”。

### 3.2 ctxpress

定位：Agent 上下文压缩引擎，证明可以把共性问题抽象成独立工具。

已核验能力：

- Java 21、多模块 Maven、命令行工具。
- 按 token 预算做确定性压缩。
- 压缩内容带归档引用，可逐字节恢复。
- 完全离线，不调用模型。
- 84 项离线测试。

可引用数据：

- 命中保护规则的关键信息在当前保真评测各预算下召回 100%。
- 对照组在小预算下为 33%。
- 6 个评测用例共 0 行凭空生成。

边界：

- 结果只适用于仓库中声明的离线评测语料和保护规则。
- 尚无下游真实模型任务精度评测，不在主页暗示其能自动提升所有 Agent 准确率。

### 3.3 mcp-sentinel

定位：MCP 工具面 lockfile 与安全扫描器，证明对新兴 Agent 生态安全问题的理解。

已核验能力：

- 对 MCP 工具名称、描述和 schema 建立基线并检测漂移。
- 检测工具影子、危险描述、schema 变化等风险。
- 输出 SARIF 2.1.0，可接入 CI。
- 完全离线。
- 84 项测试。

主页使用策略：

- 强调“历史基线让静默变化进入 diff 和评审”。
- 不宣传成能够发现所有恶意 MCP Server 的通用安全产品。

### 3.4 desensitize-spring-boot-starter

定位：数据安全方向的 Spring Boot 组件。

已核验能力：

- Jackson 序列化层注解式脱敏。
- 8 种内置脱敏类型。
- 面向 LLM 输入输出的 HMAC 确定性假名化与还原。
- 35 项测试，包含自动配置集成测试。

### 3.5 aml-compliance-checker

定位：把数据安全检查前移到编码阶段的 IntelliJ IDEA 插件。

已核验能力：

- Kotlin + IntelliJ Platform SDK。
- 对身份证、银行卡、手机号等进行值形态与标识符语义双信号检测。
- 支持 QuickFix 脱敏。
- 当前项目 README 标注 MIT；旧 Profile 中的 Apache-2.0 不再沿用。

注意：旧 Profile 中“28 项测试”的数字未在当前项目 README 中找到稳定证据，因此新版主页不展示这一数字。

### 3.6 letterpress

定位：静态博客与知识层项目，证明前端交付、内容工程和面向 Agent 的 Web 设计能力。

已核验能力：

- Astro 7 + TypeScript。
- HTML/Markdown 内容协商。
- Wiki 双向/显式链接与断链构建门禁。
- 215 项单元测试、102 项端到端契约。
- 示例页面中 Markdown 相对 HTML 的 token 节省为 64.6% / 66.5%。

主页使用策略：作为扩展项目，不与 Java/Agent 三个旗舰项目争夺首屏。

## 4. 信息架构

新版 README 按以下顺序组织：

1. 自有明暗主题头图。
2. 技术定位：Java 后端、AI 应用与 Agent 工程。
3. 求职方向：Java 后端、AI 应用、Agent 工程。
4. 30 秒速览：能力、证据、对应仓库。
5. 三个旗舰项目。
6. 三个扩展工具/项目。
7. 技术能力矩阵。
8. 工程方法与真实性边界。
9. GitHub 活动。
10. 联系方式。

该顺序遵循“方向 → 证据 → 深度 → 广度 → 联系”，不再遵循“技术栈 → 六篇长项目介绍 → 一堆统计卡”的模板结构。

## 5. 首屏设计

### 5.1 头图

使用仓库内静态 SVG，不再依赖 capsule-render：

- `assets/profile-hero-dark.svg`
- `assets/profile-hero-light.svg`

头图内容：

- XIAOXUsop
- Java Backend · AI Applications · Agent Engineering
- Evaluable · Traceable · Recoverable · Observable
- Java 21 / Spring Boot / LangChain4j 三个主要技术标签
- 抽象的任务流、证据、护栏和检查点图形

头图不写：

- 公司名称。
- 工作年限。
- 虚构奖项。
- 无法证明的“专家”“架构师”等头衔。

### 5.2 定位文案

推荐正文：

> 专注 Java 后端开发、AI 应用开发与 Agent 工程，目前开放相关岗位机会。
>
> 我关注的不只是“把模型调用跑通”，而是如何让一个 AI 应用具备可评测、可追溯、可恢复和可观测的工程属性。

该表述只展示技术方向和机会状态，不披露年龄、学校、年级，也不制造资历错觉。

### 5.3 首屏入口

保留四个直接入口：

- Flagship Project：amlagent
- Agent Infrastructure：ctxpress
- MCP Security：mcp-sentinel
- Blog / Demo：letterpress

暂不添加邮箱和简历下载按钮，因为仓库没有公开且经用户确认的邮箱/简历 URL。后续获得准确信息后再添加。

## 6. 项目展示规范

### 6.1 旗舰项目模板

每个旗舰项目最多包含：

1. 项目名 + 一句话定位。
2. 4–6 个真实技术标签。
3. 三个最重要的工程亮点。
4. 一个“可核验证据”段落。
5. 源码、Release、文档/报告入口。

禁止把仓库 README 原文整段复制到主页。

### 6.2 三个旗舰项目的招聘信号

| 项目 | 对 Java 后端岗位证明什么 | 对 AI/Agent 岗位证明什么 |
|---|---|---|
| amlagent | 状态机、可靠消息、数据一致性、认证、可观测 | 工具调用、RAG、评测、Guardrails、人审闭环 |
| ctxpress | API/契约设计、多模块工程、CLI、测试 | 上下文预算、保真、归档恢复、确定性处理 |
| mcp-sentinel | schema、差异检测、CLI、CI/SARIF | MCP 工具治理、Agent 工具面安全、基线漂移 |

### 6.3 扩展项目

使用表格或短列表，每个项目一至两行：

- desensitize-spring-boot-starter
- aml-compliance-checker
- letterpress

它们用于证明技术广度，不重复详细设计。

## 7. 技术栈表达方式

删除只展示图标的技能墙，改成“技术 + 在哪里使用”的能力矩阵：

| 方向 | 技术 | 证据项目 |
|---|---|---|
| Java 后端 | Java 21、Spring Boot 3、Maven、JPA、JWT | amlagent、starter |
| 数据与异步 | MySQL、PostgreSQL/pgvector、Redis Streams、Flyway | amlagent |
| AI/Agent | LangChain4j、工具调用、RAG、结构化输出、Guardrails、评测 | amlagent、fsc-examples |
| Agent 工具 | MCP、上下文压缩、SARIF、内容寻址归档 | ctxpress、mcp-sentinel |
| 可观测与交付 | Docker Compose、Prometheus、OpenTelemetry、GitHub Actions | amlagent、各项目 CI |
| 前端与内容 | Vue 3、TypeScript、Astro | amlagent frontend、letterpress |

这样可以避免图标墙无法区分“听说过”和“在项目中实际使用”。

## 8. 视觉规范

### 8.1 色彩

- 主色：`#4A9EFF`，表示技术与信息流。
- 强调色：`#C9A961`，表示证据、检查点和可信结果。
- 深色背景：`#0D1117` / `#161B22`。
- 浅色背景：`#F6F8FA` / `#FFFFFF`。
- 正文辅助色遵循 GitHub 明暗主题的常见对比度。

### 8.2 图形语言

- 圆角矩形：系统组件。
- 连线和脉冲点：任务流。
- 金色检查点：评测、证据或护栏。
- 等宽字体：技术标签。
- 避免霓虹、夸张波浪和大面积 Emoji。

### 8.3 动态内容

保留一张仓库自生成的 `github-metrics.svg`；移除：

- 第三方 GitHub Stats 卡。
- Top Languages 卡。
- Streak 卡。
- Contribution Snake。
- 动态打字机。

理由：这些组件大量重复 GitHub 页面已有信息，且第三方服务失败会破坏首屏。提交次数和语言比例也不能直接证明工程能力。

## 9. GitHub 固定仓库方案

GitHub 最多固定六项，推荐顺序：

1. `amlagent`
2. `ctxpress`
3. `mcp-sentinel`
4. `desensitize-spring-boot-starter`
5. `letterpress`
6. `aml-compliance-checker`

`fsc-examples` 保留为学习/示例项目，但因其主题与 amlagent 重叠，不占有限的固定位置。

固定仓库的 About 描述应做到：问题 + 核心差异 + 主要技术，而不是只列技术名。

## 10. GitHub Activity 方案

保留 `lowlighter/metrics`，但收缩为与求职有关的信息：

- repositories
- activity
- isocalendar
- languages（限制数量）

移除 habits、traffic、stargazers 等容易制造噪音或需要额外解释的插件。Metrics 是辅助证据，不能排在项目之前。

删除不再使用的 Snake workflow，减少无意义的定时任务和 output 分支更新。

## 11. 招聘方核验路径

### Java 后端招聘方

推荐浏览顺序：

1. amlagent 的可靠任务、状态机、认证和数据库设计。
2. desensitize starter 的自动配置与测试。
3. ctxpress 的契约设计和多模块 Maven 结构。

### AI 应用招聘方

推荐浏览顺序：

1. amlagent 的 Agent、RAG、证据链和评测报告。
2. ctxpress 的上下文工程与保真评测。
3. letterpress 的 HTML/Markdown 内容协商。

### Agent 工程招聘方

推荐浏览顺序：

1. amlagent 的工具调用、Guardrails、人审闭环。
2. mcp-sentinel 的 MCP 工具面基线。
3. ctxpress 的预算契约、归档引用与恢复。

## 12. 实施清单

本轮直接实施：

- [x] 新建本设计文档。
- [x] 重写 Profile README 的信息架构。
- [x] 明确技术方向和开放机会，同时隐藏个人背景。
- [x] 将项目划分为三个旗舰项目和三个扩展项目。
- [x] 用能力矩阵替换技能图标墙。
- [x] 创建仓库自有明暗主题 SVG 头图。
- [x] 移除第三方头图、打字机、Stats、Streak 和 Snake。
- [x] 精简 Metrics workflow。
- [x] 删除不再使用的 Snake workflow。
- [x] 修正不稳定数字与许可证信息。

需要用户在 GitHub 页面手动完成：

- [ ] 按第 9 节重新排列六个固定仓库。
- [ ] 在 GitHub Profile Settings 中填写简短 Bio。
- [ ] 如愿意公开，提供招聘邮箱并加入主页联系区。
- [ ] 如有正式简历链接，再添加“下载简历”按钮。

推荐 Bio：

```text
Building reliable Java backends and Agent systems. Open to opportunities.
```

## 13. 验证清单

提交前检查：

1. README 中所有 GitHub 仓库链接可访问。
2. SVG 不引用外部字体或远程资源。
3. 明暗主题 SVG 均能独立打开。
4. README 不含旧的 capsule-render、typing-svg、streak-stats、github-readme-stats 和 Snake 引用。
5. 所有数据在对应项目 README 中有来源。
6. Markdown 表格在窄屏下仍可读。
7. 页面首屏不披露年龄、学校、年级，也不虚构工作经验或资历。
8. `git diff --check` 无空白错误。

## 14. 后续维护规则

- 每月或重要版本发布后更新一次，而不是每天追逐装饰组件。
- 项目数据变化时先更新项目 README，再同步 Profile 的摘要。
- 新项目只有满足“可运行 + README + 测试/验证 + 明确差异”后才进入主页。
- 三个旗舰位置保持稀缺；新增项目必须替换，而不是无限追加。
- 如果获得真实实习、比赛、开源贡献或用户反馈，再添加对应章节，并链接可核验证据。
- 机会状态变化后，只需更新“开放相关岗位机会”文案，不需要重做整套信息架构。
