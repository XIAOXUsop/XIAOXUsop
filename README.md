<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A9EFF,100:C9A961&height=200&section=header&text=XIAOXUsop&fontSize=50&fontAlignY=34&desc=Java%20%E5%90%8E%E7%AB%AF%20%C2%B7%20%E6%99%BA%E8%83%BD%20Agent%20%E5%BA%94%E7%94%A8%20%C2%B7%20%E8%87%AA%E7%A0%94%E6%8F%92%E4%BB%B6%E4%B8%8E%E5%B7%A5%E5%85%B7&descSize=17&descAlignY=54&anim=fade" alt="header"/>
</div>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&pause=1200&color=4A9EFF&center=true&vCenter=true&width=600&lines=%E4%B8%8D%E6%BB%A1%E8%B6%B3%E4%BA%8E%E2%80%9C%E6%8A%8A%E6%A8%A1%E5%9E%8B%E8%B7%91%E9%80%9A%E2%80%9D%EF%BC%8C%E8%A6%81%E6%B1%82%E5%8F%AF%E8%AF%84%E6%B5%8B%E3%80%81%E5%8F%AF%E8%BF%BD%E6%BA%AF%E3%80%81%E5%8F%AF%E6%81%A2%E5%A4%8D;%E6%AF%8F%E4%B8%AA%E7%BB%93%E8%AE%BA%E9%83%BD%E8%A6%81%E6%9C%89%E6%95%B0%E6%8D%AE%E6%94%AF%E6%92%91" alt="typing"/>
</div>

## 我是谁

Java 后端开发，专注 **智能 Agent 应用工程化** 与 **自研工具 / 插件**。

我做事的判断标准不是"功能跑通了"，而是 **可评测、可追溯、可恢复、可观测**——
每条风险结论都要能引用到法规证据，每个性能数字都要能复现。

## 技术栈

<div align="center">

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=java,spring,mysql,redis,pg,docker,git,maven,linux,js,vue,ts&theme=dark" alt="skills"/>
</a>

</div>

## 精选项目

### 🏦 [amlagent](https://github.com/XIAOXUsop/amlagent) — 商业银行智能反洗钱（AML）尽调 Agent 平台

`Java 21` `Spring Boot 3` `LangChain4j` `pgvector` `Redis Streams` `Vue 3` · CI ✅ · MIT

> 接收反洗钱预警工单后，可靠地调度 Agent 工作流，自动完成交易画像、股权穿透、制裁名单筛查、
> 监管法规检索、风险研判与结构化报告生成；用**独立于大模型的护栏**校验结论，高风险工单转人工复核闭环。

- **可靠任务** — Transactional Outbox + Redis Streams，含幂等、重试、死信、租约 fencing、崩溃恢复
- **证据追溯** — 混合 RAG（向量 + 中文词法 + 加权 RRF + 精排），结论必须引用 `evidenceId`
- **安全护栏** — 配置化规则 DSL；Prompt 注入三层防护；一级制裁强制 HIGH 并转人工
- **可观测** — Prometheus 指标 + **OpenTelemetry GenAI 语义约定**追踪：span 按 `chat {模型}`
  命名，属性涵盖 `gen_ai.usage.*` / `gen_ai.response.finish_reasons` 等，
  接入任意 OTel 后端无需私有埋点；**span 只记元数据，绝不写入 prompt 或补全内容**

**上手**：`docker compose up` 一键起全栈（后端 + 前端 + MySQL + Redis + PGVector + Prometheus/Grafana）。

**已验证的数据**（详见仓库内评测报告）

| 评测项 | 结果 |
|---|---|
| RAG 法规检索 Recall@5 | **93.3%** → 接入 bge 精排 **100%**（nDCG@5 96.7%，无答案拒答 100%） |
| DeepSeek 真实 Agent 风险准确率 | **44.4% → 100%**（9 条冻结合成 DEV，多轮迭代基线） |
| 一级制裁规则漏报 | **0 / 5** |
| 测试 | 后端 242 项单测 · 22 项集成回归 · 前端 15 项 |

> 数据集标签为合成数据（`PENDING_DOMAIN_REVIEW`），不等同生产准确率——仓库 README 中已如实标注。

### 🔌 [desensitize-spring-boot-starter](https://github.com/XIAOXUsop/desensitize-spring-boot-starter) — 敏感数据防护（脱敏 + 可逆假名化）

`Java 21` `Spring Boot 3` `Jackson` `HMAC` · CI ✅ · MIT

> 两层能力：**接口返回值脱敏**（`@Sensitive` 注解，Jackson 序列化层，业务零侵入），
> 以及 **大模型输入输出脱敏**——发送前把敏感值换成确定性令牌，收到回复后自动还原。

- 掩码解决不了大模型场景：它保留部分原文（仍是个人信息），且模型无法凭掩码
  在整段对话里认出"是同一个人"；确定性令牌两者都能解决
- 令牌 = `HMAC-SHA256(密钥, 类型|原文)` 截断：**不含原文、跨轮次稳定、无私钥不可伪造**
- 未知令牌保持原样而非猜测性替换；默认关闭，缺密钥在**启动期失败**而不是产出弱令牌
- **35 项测试**（含两组 `ApplicationContextRunner` 自动配置集成测试）

**上手**：下载 [jar](https://github.com/XIAOXUsop/desensitize-spring-boot-starter/releases/latest) 装进本地仓库，加 `@Sensitive` 注解即可，零配置。

### 🛡️ [aml-compliance-checker](https://github.com/XIAOXUsop/aml-compliance-checker) — IDEA 敏感数据合规插件

`Kotlin` `IntelliJ Platform SDK` · CI ✅ · Apache-2.0

> 检出代码中的身份证 / 银行卡 / 手机号明文，**一键替换为等长脱敏值**；
> v0.3 起采用**双信号判定**并给出判定依据。

- **值形态**（高置信）：身份证过 ISO 7064 校验位、银行卡过 Luhn，值本身即可自证
- **标识符语义**（中置信）：变量名/字段名/键名暗示敏感语义且值形似时提示——
  专门兜住**校验位不合法的 mock 数据**，这类纯正则一律放过，却正是真实数据泄漏最常见的形态
- 每条告警写清判定依据，用户可自行分辨真泄漏与误报；无上下文时不猜测
- **28 项测试**

**上手**：下载 [zip](https://github.com/XIAOXUsop/aml-compliance-checker/releases/latest)，IDEA 里 `Install Plugin from Disk` 即可。

### 📚 [fsc-examples](https://github.com/XIAOXUsop/fsc-examples) — LangChain4j 金融合规示例集

`Java 21` `LangChain4j` `MCP` `JUnit 5` · CI ✅ · MIT

> 用 `AiServices` + `@Tool` + 法规 RAG 跑通一条 AML 尽调 Agent 链路，
> 给出**确定性护栏**与**双轨评测**（原始模型分 vs 护栏修正后分），
> 并通过 **MCP（Model Context Protocol）** 把同一套工具面开放给任意 MCP 客户端。

- **Agent 与 MCP 共用同一份工具实现**，不存在演示与生产两套逻辑
- 协议层有真实握手测试：把服务作为独立子进程拉起，走完
  `initialize → tools/list → tools/call` 全程 JSON-RPC
- Mock-first：无 API Key、无需联网即可全链路跑通，便于上手与进 CI
- **14 项测试**（含双轨评测与 MCP 协议握手）

**上手**：`mvn -pl fsc-cases test` —— 无需 API Key、无需联网即可全链路跑通。

### 🗜️ [ctxpress](https://github.com/XIAOXUsop/ctxpress) — Agent 上下文压缩引擎

`Java 21` `Context Engineering` · CI ✅ · MIT

> 在工具输出、日志、RAG 片段进入 LLM 之前，按你给出的 token 预算压缩它们——
> **确定性、可审计、可逆**。

- **压缩量由预算决定，不是一个固定数字**：内容放得下时**完全不动**；
  只超出一点时只丢一点（同一份日志：给 60000 预算丢 6.7%，给 2000 才丢 96.5%）
- **可逆**：压掉的原文进内容寻址归档，且**归档引用被写进压缩内容本身**——
  读到这段内容的模型自己就知道有东西被省略、以及怎么要回来
- **不调用模型**：同输入必然同输出（可写断言测试）、零增量成本、不会引入原文没有的事实

**上手**：下载 [ctxpress.jar](https://github.com/XIAOXUsop/ctxpress/releases/latest) → `java -jar ctxpress.jar analyze --max-tokens 8000 app.log`

### 🛰️ [mcp-sentinel](https://github.com/XIAOXUsop/mcp-sentinel) — MCP 工具面 lockfile

`Java 21` `MCP` `Security` · CI ✅ · MIT

> 把 MCP 服务器的工具定义锁下来、提交进版本库，让"配置被悄悄改了"像"代码被改了"
> 一样出现在 diff 与评审里。

- 针对 **rug pull**：名字与 schema 都不变、只悄悄改描述。扫描器每次拿到的都是当前版本，
  **没有历史对照就发现不了**——这不是"规则多少"的差别，而是"有没有基线"的差别
- 输出 **SARIF 2.1.0**，发现以行内注解出现在 PR 上；退出码可作 CI 门禁
- **完全离线**（对比 snyk / cisco 的 MCP 扫描器需要云 API 或 LLM Key），
  且它们目前都不做基线漂移——互补而非替代

**上手**：下载 [mcp-sentinel.jar](https://github.com/XIAOXUsop/mcp-sentinel/releases/latest) → `java -jar mcp-sentinel.jar lock --config mcp.json`

## 工程习惯

- **每个项目都配 CI + 单元测试 + 开源协议**，构建产物不进仓库
- **可复现优先**：评测结果落盘 JSON，数据集带冻结标识与版本要素
- **如实标注局限**：合成数据不等于生产准确率，调优集指标不等于泛化能力
- **产物可获取**：每个项目都发 GitHub Release 并附可直接运行的产物——
  「下载就能用」比「clone 下来自己构建」的门槛低一个数量级

## GitHub 数据

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=XIAOXUsop&show_icons=true&theme=synthwave&hide_border=true&count_private=true" alt="GitHub Stats" height="165"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=XIAOXUsop&layout=compact&theme=synthwave&hide_border=true" alt="Top Languages" height="165"/>
</p>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=XIAOXUsop&locale=zh_CN&theme=synthwave&hide_border=true" alt="GitHub Streak"/>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/XIAOXUsop/XIAOXUsop/main/github-metrics.svg" alt="Metrics"/>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/XIAOXUsop/XIAOXUsop/output/github-contribution-grid-snake-dark.svg" alt="Snake animation"/>
</div>

## 联系

- GitHub: [@XIAOXUsop](https://github.com/XIAOXUsop)

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:C9A961,100:4A9EFF&height=100&section=footer" alt="footer"/>
</div>
