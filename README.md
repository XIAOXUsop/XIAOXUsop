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

**上手**：三步——`docker-compose.yml` 里只有基础设施，没有后端/前端镜像，
所以不存在"一条命令起全栈"。`docker compose up -d` 是后台的，后两步各占一个终端：

```bash
docker compose up -d                       # MySQL(3307) / PGVector(5433) / Redis(6379)，后台运行
cd backend  && ./mvnw spring-boot:run      # 后端(8080)，默认 Mock 模型，无需 API Key，占一个终端
cd frontend && npm install && npm run dev  # 前端(5173)，浏览器打开即可登录，占另一个终端
```

仓库 README 里另有端口表、就绪判断与 `docker compose down / down -v` 的清理方式。

**已验证的数据**（详见仓库内评测报告）

| 评测项 | 结果 |
|---|---|
| RAG 法规检索 Recall@5 | **93.3%** → 接入 bge 精排 **100%**（nDCG@5 96.7%，无答案拒答 100%） |
| DeepSeek 真实 Agent 风险准确率 | **44.4% → 100%**（9 条冻结合成 DEV，多轮迭代基线） |
| 一级制裁规则漏报 | **0 / 5** |
| 测试 | 后端单测 **548/549**（548 通过、1 项真实模型评测默认跳过）· 集成回归 **44/44** · 前端 **85** · Playwright E2E **8/8** |

> 数据集标签为合成数据（`PENDING_DOMAIN_REVIEW`），不等同生产准确率——仓库 README 中已如实标注。
> 测试数字不手写：仓库里 `scripts/test_summary.py` 从 Surefire XML 与 Vitest JSON 现算，
> 上表所列为最近一次本机验证（2026-09-18）。

> 集成回归 **44/44 全绿**（Playwright E2E 8/8）。本轮开始时它是 19 项失败，逐簇查明是
> 三个独立原因：服务端新增校验而测试夹具未同步、法规语料的字节哈希被 Windows 的
> CRLF 检出破坏、以及测试用本地时区而应用用 UTC。都不是"测试发现了真问题"。

### 🔌 [desensitize-spring-boot-starter](https://github.com/XIAOXUsop/desensitize-spring-boot-starter) — 敏感数据防护（脱敏 + 可逆假名化）

`Java 21` `Spring Boot 3` `Jackson` `HMAC` · CI ✅ · MIT

> 两层能力：**接口返回值脱敏**（`@Sensitive` 注解，Jackson 序列化层，业务零侵入），
> 以及 **大模型输入输出脱敏**——发送前把敏感值换成确定性令牌，收到回复后自动还原。

- 掩码解决不了大模型场景：它保留部分原文（仍是个人信息），且模型无法凭掩码
  在整段对话里认出"是同一个人"；确定性令牌两者都能解决
- 令牌 = `HMAC-SHA256(密钥, 类型|版本|原文)` 截断为 **128 bit**（`TYPE_v2_<32 位十六进制>`）：
  **不含原文、跨轮次稳定、无私钥不可伪造**。早先的 40 bit 在约 100 万条明文下就有约 50%
  碰撞概率，届时保险库会把两个真实身份混成一个人
- **令牌碰撞是硬失败**：同令牌不同原文直接抛异常并保留原映射，不覆盖也不静默沿用——
  两种"将就"都会把某人的数据还原成另一个人的，且没有任何外部症状
- **会话级保险库**：映射按 `VaultScope` 分表，会话结束 `forget(scope)` 整体撤销不波及其他会话；
  支持过期时间；还原可挂审计回调（**只给作用域与类型，不给原文**）。
  文档里也写明它**不**改变什么——令牌仍是确定性的，跨会话同串，那是跨轮次一致性的来源
- 未知令牌保持原样而非猜测性替换；默认关闭，缺密钥在**启动期失败**而不是产出弱令牌
- **模型调用装饰器**：出站脱敏 → 调用 → 入站还原 → **异常消毒**。
  模型 SDK 常把请求内容带进异常 message，这一层会消毒它，并在请求含敏感内容时
  不保留底层堆栈（堆栈最常被打印，挂上去等于把原文放进日志）。不支持流式，
  因为令牌可能被切成两半，逐块还原要么漏、要么吐出半个令牌
- **95 项测试**（含碰撞失败、v1/v2 版本解析、会话隔离与并发、装饰器异常路径、
  两组 `ApplicationContextRunner` 集成测试）

**上手**：下载 [jar](https://github.com/XIAOXUsop/desensitize-spring-boot-starter/releases/latest) 装进本地仓库，加 `@Sensitive` 注解即可，零配置。
（Maven Central 发布配置同样已就绪，只差凭据。）

### 🛡️ [aml-compliance-checker](https://github.com/XIAOXUsop/aml-compliance-checker) — IDEA 敏感数据合规插件

`Kotlin` `IntelliJ Platform SDK` · CI ✅ · Apache-2.0

> 检出 Java 注释与字符串字面量中的身份证 / 银行卡 / 手机号明文，
> **一键替换为等长脱敏值**；v0.3 起采用**双信号判定**并给出判定依据。

- **值形态**（高置信）：身份证过 ISO 7064 校验位、银行卡过 Luhn，值本身即可自证
- **标识符语义**（中置信）：变量名/字段名/键名暗示敏感语义且值形似时提示——
  专门兜住**校验位不合法的 mock 数据**，这类纯正则一律放过，却正是真实数据泄漏最常见的形态
- 每条告警写清判定依据，用户可自行分辨真泄漏与误报；无上下文时不猜测
- **扫描边界（不覆盖什么）**：动态拼接、外部资源文件、运行时数据、非 Java 语言都不在范围内。
  标识符语义是启发式（最多向上两层取具名祖先），不是完整语义分析
- **54 项测试**：28 项纯逻辑 + 26 项真实 IntelliJ fixture（加载 Java PSI 走完整 inspection
  与 QuickFix 流程、断言告警**区间**只覆盖敏感值、设置存取往返、`plugin.xml` 注册）

**上手**：下载 [zip](https://github.com/XIAOXUsop/aml-compliance-checker/releases/latest)，IDEA 里 `Install Plugin from Disk` 即可。

### 🌐 [letterpress](https://github.com/XIAOXUsop/letterpress) — 中文排版讲究、写给人和 AI 读的静态博客

`Astro 7` `TypeScript` `Content Negotiation` · CI ✅ · MIT

> 零配置就能跑，改一个文件就能上线；文章给人读，markdown 给 AI 读。
> 三个差异化点都对应「别人没做的一步」：

- **给 AI 读的 markdown**——Claude Code / Cursor / OpenCode 发 `Accept: text/markdown`，
  本项目用三个平台（Cloudflare / Netlify / Vercel）的边缘函数做内容协商，
  补上现有集成跳过的托管平台垫片；实测同一页面省 **64.5% / 66.5%** token
- **中文排版按中文的规矩**——行高 1.75、行宽 `34em`（同时满足中文 30–40 字
  与西文 45–75 字符）、`text-autospace` 中西文自动间距、中文不用斜体
- **知识层 lint 会拦构建**——`[[方括号]]` 互链的独立知识库，断链使构建中止，
  语义级检查留给 agent（AGENTS.md 约定）
- **文章阅读页无外链 JavaScript**（首页仅 2.4 KB 内联）· **220 项**单测 ·
  **104 项**端到端契约 · 对比度亮暗双模式有自动化测试
  （搜索页按需加载站内 Pagefind，那不算外链，但也别理解成"整站零 JS"）

**上手**：`npm install && npm run dev` —— 零配置、零数据库、零环境变量。

Demo：https://xiaoxusop.github.io/letterpress/ —— **该环境不支持内容协商**
（GitHub Pages 改不了响应头）。要 curl 验证 `Accept: text/markdown`，
需要部署到 Cloudflare Pages / Netlify / Vercel 之一，仓库已备好三者的垫片与部署说明，
但**目前尚未部署**，因此"内容协商可用"这句话暂时无法在公开环境直接验证。

### 🗜️ [ctxpress](https://github.com/XIAOXUsop/ctxpress) — Agent 上下文压缩引擎

`Java 21` `Context Engineering` · CI ✅ · MIT

> 在工具输出、日志、RAG 片段进入 LLM 之前，按你给出的 token 预算压缩它们——
> **确定性、可审计、可逆**。

- **输出 ≤ 你给的预算**，做不到时（只有受保护内容本身就超预算这一种情形）
  报告里显式给出 `overBudgetBy`，**绝不静默超标**。
  这条契约由一张 **6 类语料 × 10 档预算的矩阵**逐格断言，CI 当门禁跑：**遵守率 100%**
- **保真评测（离线，无模型）**：命中保护规则的关键信息**任何预算下召回 100%**
  （对照组朴素头截断在小预算下只有 33%）；6 个用例 **0 行凭空生成**——
  输出的每一行要么逐字来自输入、要么匹配已声明的省略标记文法
- **可逆**：压掉的原文进内容寻址归档，**归档引用被写进压缩内容本身**，
  读到这段内容的模型自己就知道有东西被省略、以及怎么要回来。
  命令行 `--archive` 写文件归档、`retrieve` 取回，**逐字节一致**
- **不调用模型**：同输入必然同输出（可写断言测试）、零增量成本、不会引入原文没有的事实

> **如实标注局限**：未受保护的关键信息召回与最朴素的均匀行采样相当（略低）——
> 差距来自省略标记的开销（一个标记约 7 token、一行日志约 11 token），
> 那是"可审计 + 可取回"的代价。另外尚无下游任务精度评测（GSM8K 那类需要真调模型、
> 要花钱，且对抽取式压缩器用错了指标）。仓库 README 中已如实标注。

**上手（命令行）**：下载 [ctxpress.jar](https://github.com/XIAOXUsop/ctxpress/releases/latest) → `java -jar ctxpress.jar analyze --max-tokens 8000 app.log`

**上手（当库用）**：`io.github.xiaoxusop:ctxpress-core` **尚未发布到 Maven Central**，
直接写坐标会解析失败。现在要用的方式是下载 Release 里的 jar 并
`mvn install:install-file` 装进本地仓库——仓库 README 给了可复制的两步命令。
发布配置（源码/Javadoc jar、签名、手动触发的发布工作流、POM 元数据）已全部就绪，
缺的只有 Sonatype 令牌与 GPG 私钥。
> 另外：报告里现在**一定会写明 token 数字的口径**（`heuristic` 还是 `o200k_base`），
> 因为同一份内容在两种口径下能差 60%；把预算当硬约束时必须显式传计数器。

### 🛰️ [mcp-sentinel](https://github.com/XIAOXUsop/mcp-sentinel) — MCP 工具面 lockfile

`Java 21` `MCP` `Security` · CI ✅ · MIT

> 把 MCP 服务器的工具定义锁下来、提交进版本库，让"配置被悄悄改了"像"代码被改了"
> 一样出现在 diff 与评审里。

- 针对 **rug pull**：名字与 schema 都不变、只悄悄改描述。扫描器每次拿到的都是当前版本，
  **没有历史对照就发现不了**——这不是"规则多少"的差别，而是"有没有基线"的差别
- **fail-closed**：`scan` 默认要求基线可用，缺失 / 损坏 / 版本不兼容一律退出 5，
  **不会退化成"只跑风险规则然后返回 0"**——一次漏拷的 lock 文件若表现为干净通过，
  门禁就把它最该守的东西放过去了。确实只要静态规则时用 `--risk-only` 显式声明
- **两种传输**：stdio（本地子进程）与 **Streamable HTTP**（远程端点）。
  请求头里的密钥用 `${环境变量名}` 引用，配置里不放明文；引用了不存在的变量
  在连接前就按配置错误失败，而不是发一个空头出去。换传输不改变任何一条检测语义
- 输出 **SARIF 2.1.0**，发现以行内注解出现在 PR 上；退出码可作 CI 门禁
  （0 通过 / 1 用法 / 2 连接 / 3 风险 / 4 未批准漂移 / 5 基线不可用 / 6 产物写入失败）
- 批准变更时打印**审批摘要**（批准了哪些工具、级别、前后摘要、基线新指纹），
  并明确静态风险发现不参与批准——它们描述的是工具面本身有问题，不是"和上次不一样"
- **107 项测试**（含真实 stdio 子进程与本地 Streamable HTTP 服务器的端到端）
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
