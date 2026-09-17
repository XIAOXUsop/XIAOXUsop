<p align="center">
  <img src="./assets/profile-hero-dark.svg#gh-dark-mode-only" width="100%" alt="XIAOXUsop — Java Backend, AI Applications, Agent Engineering" />
  <img src="./assets/profile-hero-light.svg#gh-light-mode-only" width="100%" alt="XIAOXUsop — Java Backend, AI Applications, Agent Engineering" />
</p>

<p align="center">
  <a href="https://github.com/XIAOXUsop/amlagent"><strong>旗舰项目</strong></a> ·
  <a href="https://github.com/XIAOXUsop/ctxpress">Agent 基础设施</a> ·
  <a href="https://github.com/XIAOXUsop/mcp-sentinel">MCP 安全</a> ·
  <a href="https://xiaoxusop.github.io/letterpress/">博客 / Demo</a>
</p>

## 关于我

专注 **Java 后端开发、AI 应用开发与 Agent 工程**，目前开放相关岗位机会。

我关注的不只是“把模型调用跑通”，而是如何让一个 AI 应用具备
**可评测、可追溯、可恢复、可观测**的工程属性：任务失败后能够恢复，模型结论能够找到证据，
效果能够通过固定数据集回归，关键链路能够被监控。

> **求职方向：** Java 后端 / AI 应用 / Agent 工程　　
> **项目特点：** 均提供源码、README、自动化测试与 CI；核心工具提供可下载 Release

## 30 秒速览

| 能力方向 | 我做过什么 | 可核验项目 |
|---|---|---|
| Java 后端 | 可靠异步任务、状态机、JWT/CSRF、双数据源、数据库迁移、SSE | [amlagent](https://github.com/XIAOXUsop/amlagent) |
| AI 应用 | LangChain4j 工具调用、混合 RAG、结构化输出、规则护栏、模型评测 | [amlagent](https://github.com/XIAOXUsop/amlagent) · [fsc-examples](https://github.com/XIAOXUsop/fsc-examples) |
| Agent 工程 | 上下文预算与恢复、MCP 工具面基线、证据链、人工复核闭环 | [ctxpress](https://github.com/XIAOXUsop/ctxpress) · [mcp-sentinel](https://github.com/XIAOXUsop/mcp-sentinel) |
| 工程质量 | 离线测试、集成测试、固定评测集、CI、Release、Prometheus / OTel | [所有公开仓库](https://github.com/XIAOXUsop?tab=repositories) |

## 代表项目

### 1. [amlagent](https://github.com/XIAOXUsop/amlagent) — AML 尽调 Agent 平台

`Java 21` `Spring Boot 3.5` `LangChain4j` `Redis Streams` `PostgreSQL / pgvector` `Vue 3`

接收反洗钱预警工单后，调度 Agent 完成交易画像、股权穿透、制裁筛查、法规检索、风险研判和报告生成；
模型结论经过独立规则护栏校验，高风险工单进入人工复核。

- **可靠任务：** Transactional Outbox + Redis Streams，覆盖幂等、重试、死信、租约 fencing 与崩溃恢复。
- **一致性：** 推理前通过 Snapshot First 冻结业务快照，工具与护栏读取同一版本数据。
- **证据闭环：** 向量 + 中文词法 + 加权 RRF + 精排，报告引用可回溯到法规 `evidenceId`。
- **安全与观测：** Prompt 注入分层防护；Prometheus 指标与 OpenTelemetry GenAI 追踪不记录提示词正文。

**验证证据：** 固定的 18 条 RAG DEV 中，无精排 Recall@5 为 **93.3%**，本地 bge 精排后为
**100%**；同时冷缓存 P95 从 **135ms** 增至 **671ms**。这里保留延迟代价，不只展示质量收益。
数据集仍是 `PENDING_DOMAIN_REVIEW`，这些数字是开发基线，**不代表真实银行生产准确率**。

[源码与运行说明](https://github.com/XIAOXUsop/amlagent) ·
[项目全景文档](https://github.com/XIAOXUsop/amlagent/blob/master/PROJECT-OVERVIEW.md) ·
[真实模型评测报告](https://github.com/XIAOXUsop/amlagent/blob/master/DeepSeek真实Agent评测报告-二轮对比.md)

### 2. [ctxpress](https://github.com/XIAOXUsop/ctxpress) — Agent 上下文压缩引擎

`Java 21` `Maven Multi-module` `CLI` `Context Engineering` `Content-addressed Archive`

在日志、工具输出和 RAG 片段进入模型前，按 token 预算进行**确定性、可审计、可恢复**的压缩，
不调用模型，同一输入与策略得到同一结果。

- **预算契约：** 输出不静默超过预算；保护内容本身超限时显式报告 `overBudgetBy`。
- **保真：** 命中保护规则的信息在当前离线评测各预算下召回 **100%**；小预算头截断对照组为 33%。
- **可恢复：** 被省略原文进入内容寻址归档，压缩结果携带引用，取回时逐字节一致。
- **可验证：** 84 项离线测试；6 个保真用例中，输出共 **0 行凭空生成**。

这些结果只说明仓库中声明的语料与保护规则；项目尚未宣称能提升任意下游模型任务的准确率。

[源码与评测方法](https://github.com/XIAOXUsop/ctxpress) ·
[下载 Release](https://github.com/XIAOXUsop/ctxpress/releases/latest)

### 3. [mcp-sentinel](https://github.com/XIAOXUsop/mcp-sentinel) — MCP 工具面 lockfile

`Java 21` `MCP SDK` `JSON Schema` `SARIF 2.1.0` `CI Security Gate`

把 MCP Server 暴露的工具名称、描述和 schema 锁定为版本化基线，让静默配置变化像代码变化一样进入
diff、评审和 CI。

- **基线漂移：** 识别工具新增/删除、描述变化、schema 收放宽以及工具影子等风险。
- **面向 rug pull：** 即使工具名称与参数没变，只修改描述，也能与历史基线进行比较。
- **CI 集成：** 输出 SARIF 2.1.0 和稳定退出码，可在 GitHub PR 中展示定位结果。
- **离线验证：** 不依赖云扫描 API 或 LLM Key，当前包含 84 项测试。

它是工具面变更检测器，不把自己包装成能够识别所有恶意 MCP Server 的万能扫描器。

[源码与威胁模型](https://github.com/XIAOXUsop/mcp-sentinel) ·
[下载 Release](https://github.com/XIAOXUsop/mcp-sentinel/releases/latest)

## 其他可运行项目

| 项目 | 解决的问题 | 工程证据 |
|---|---|---|
| [desensitize-spring-boot-starter](https://github.com/XIAOXUsop/desensitize-spring-boot-starter) | Jackson 序列化层注解式脱敏；LLM 输入输出的 HMAC 确定性假名化与还原 | 8 种脱敏类型、35 项测试、自动配置集成测试、可下载 JAR |
| [aml-compliance-checker](https://github.com/XIAOXUsop/aml-compliance-checker) | 在 IDEA 中发现注释/字符串里的身份证、银行卡等明文，并提供 QuickFix | Kotlin + PSI、值形态与标识符语义双信号、可下载插件 ZIP |
| [letterpress](https://github.com/XIAOXUsop/letterpress) | 面向人和 AI 双读的静态博客：HTML/Markdown 内容协商 + Wiki 构建检查 | 215 项单测、102 项产物契约、[在线 Demo](https://xiaoxusop.github.io/letterpress/) |

## 技术能力

| 方向 | 实际使用的技术 | 主要落点 |
|---|---|---|
| Java 后端 | Java 21、Spring Boot 3、Maven、JPA、JWT、SSE | amlagent、desensitize starter |
| 数据与异步 | MySQL、PostgreSQL / pgvector、Redis Streams、Flyway | amlagent |
| AI / Agent | LangChain4j、Tool Calling、RAG、结构化输出、Guardrails、Eval | amlagent、fsc-examples |
| Agent 工具 | MCP、上下文压缩、内容寻址归档、SARIF | ctxpress、mcp-sentinel |
| 可观测与交付 | Docker Compose、Prometheus、OpenTelemetry、GitHub Actions | amlagent、各项目 CI |
| 前端与内容 | Vue 3、TypeScript、Astro | amlagent frontend、letterpress |

## 我的工程方法

- **先定义失败条件：** 超预算、无证据、模型输出无效、任务重复消费，都应有显式结果而不是静默兜底。
- **区分模型能力与系统能力：** 原始模型结果、规则修正结果、端到端任务结果分别计分。
- **保留版本与证据：** 数据集哈希、Prompt 版本、规则版本、快照摘要进入报告或执行记录。
- **承认边界：** 合成数据不等于生产数据，DEV 调优结果不等于泛化能力，本地延迟不等于线上 SLA。
- **让项目能被运行：** 优先提供 Mock / 离线路径、Maven Wrapper、Docker Compose、CI 和 Release。

更详细的主页取舍、证据来源和维护规则见 [design.md](./design.md)。

## GitHub Activity

<p align="center">
  <img src="./github-metrics.svg" width="100%" alt="XIAOXUsop GitHub activity metrics" />
</p>

## 联系

- GitHub：[@XIAOXUsop](https://github.com/XIAOXUsop)
- 项目与技术讨论：可在对应仓库提交 Issue

如果你的团队正在招聘 **Java 后端、AI 应用或 Agent 工程方向**的岗位，欢迎通过 GitHub 与我联系。
