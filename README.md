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

<!--
  ⚠️ 这一节里的**数字都会过期**，改之前先回各自仓库取一次真实值。
  2026-09-19 同步过一次，当时发现四处对不上（amlagent 后端单测 549→575、
  letterpress 单测 220→254、契约 104→194、token 节省 64.5%/66.5%→68.9%/70.2%）。

  2026-09-20 又同步一次，两处要改、其余对得上：
  · letterpress 单测 254 → **263**（另外三项数字各自与仓库里的一致）；
  · amlagent 原先写的「CI ✅」**不成立**——8 个 job 里 7 个绿，依赖扫描是红的，
    而且那是 17 条**真告警**（不是工具故障），如实写进正文了。
  这一轮还给每个项目的数字都加了一行「验证提交：<短 SHA>」——
  数据只引用**已经推送、且 CI 跑过**的提交，免得再出现"主页说绿、仓库其实红"。

  2026-09-21 再同步一次，三处要改：
  · amlagent 的依赖阻断 **17 → 15 条**（mysql-connector-j 的 2 条升级清除，
    **由扫描结果确认**，不是升级后的推断），验证提交跟到 `64ad3ce`；
    并补上"本机也完整跑通过一次"的记录（集成 44/44、E2E 8/8）；
  · mcp-sentinel 写清 v0.5.3 构建自 `02c18d4`、`17f3466` 只动 CI 配置
    （运行时代码与 Release 产物无变化）；
  · letterpress 补一句：对 Pages Demo 跑线上烟测本来就该红，
    那是已知限制不是部署事故。**「线上内容协商已验证」这句话仍然不写**——
    真实部署还没有（见下）。

  取数命令（都在对应仓库里跑）：

    amlagent      后端单测/集成/前端 → `python scripts/test_summary.py`（只读真实产物）
                  Playwright E2E     → CI 的 `Playwright E2E` job 日志里 "N passed"
    letterpress   单测               → `npm test`（README 徽章与「实测数据」表同步）
                  契约条数、token 节省 → `npm run verify`（脚本会自己打印；
                                         README 抄错它会红）
    desensitize   → `./mvnw -B verify` 的 "Tests run:" 合计
    mcp-sentinel  → `./mvnw -B verify` 的 "Tests run:" 合计
    IDEA 插件     → `./gradlew cleanTest test`，再数 build/test-results/test/*.xml

  两个注意：
  · letterpress 的数字**随内容页数浮动**，是这一节里最常过期的一处；
  · 别用"最近一次我记得的数"——2026-09-19 那次四处过期，就是那么来的。
-->

### 🏦 [amlagent](https://github.com/XIAOXUsop/amlagent) — 商业银行智能反洗钱（AML）尽调 Agent 平台

`Java 21` `Spring Boot 3` `LangChain4j` `pgvector` `Redis Streams` `Vue 3` · CI 8 项 7 绿 · MIT

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
| 测试 | 后端单测 **575/576**（575 通过、1 项真实模型评测默认跳过）· 集成回归 **43/44**（1 项四路检索 A/B 需本机加载精排模型，CI 上按前置条件跳过）· 前端 **85** · Playwright E2E **8/8** |

> 数据集标签为合成数据（`PENDING_DOMAIN_REVIEW`），不等同生产准确率——仓库 README 中已如实标注。
> 测试数字不手写：仓库里 `scripts/test_summary.py` 从 Surefire XML 与 Vitest JSON 现算，
> 再由 CI 的 `README Test Numbers` job 拿 README 与当次产物**逐格比对**，对不上就红。
> 上表与下面的 CI 状态验证于提交 `64ad3ce`（2026-09-21，8 个 job 全部跑完、没有一个是取消的）。

> **CI 的真实状态，不写「✅」两个字糊过去：8 个 job 里 7 个绿，
> `Backend Dependency Vulnerability Scan` 是红的。** 那是 **15 条真告警**，归并在
> `spring-core`（12，最高 9.8）、`spring-security-core`（2，最高 9.1）、
> `pgvector`（1）三个依赖上——**不是工具坏了**，而是这几条在 Spring Boot 3.5.x 线上
> **没有可取的补丁版**：修复线（6.2.20 / 6.5.12）上游还没发布，能绕开的 7.x 要先迁到
> Spring Boot 4。仓库 README 的「依赖安全」一节逐条写了受影响区间与处理原则；
> 门禁宁可一直红着，也没有为了变绿去加一条豁免。
>
> 其中 **mysql-connector-j 的 2 条已于 2026-09-21 清除**（17 → 15）：Oracle 把它的版本号
> 改成了年份制，`26.7.0` 才是修复版，而仓库里此前记的「没有可取的修复版」只查了 9.x 那条线。
> 这一条**是扫描结果确认的**，不是升级后的推断——同一次扫描的输出里那个包整条消失了。

> 集成回归 **43/44（1 项按前置条件跳过）、0 失败**（Playwright E2E 8/8）。
> **本机也完整跑通过一次**（2026-09-21，同一提交）：三个依赖容器起在 3307/5433/6379，
> 集成回归 **44/44**（本机装了精排模型，CI 上跳过的那项在这里真跑），
> 后端以 Mock 模型启动、不联网，E2E **8/8**——比 CI 多出来的那 1 项就是 44 与 43 的差。
> 本轮开始时集成回归是 19 项失败，逐簇查明是三个独立原因：服务端新增校验而测试夹具未同步、
> 法规语料的字节哈希被 Windows 的 CRLF 检出破坏、以及测试用本地时区而应用用 UTC。
> 都不是"测试发现了真问题"。

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

> 数字与 Release 验证于提交 `093e457`（2026-09-20，CI 与 v0.6.2 Release 均通过）。
> v0.6.2 的 jar 已下载核对：内嵌 POM **没有 `<parent>`**（装完不会再去解析一个没发布的父 POM），
> 且 `jackson-bom` 钉在 **2.21.5**——v0.6.1 的解析结果是 2.21.2，命中 5 条公告。

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

> **v0.4.4 请勿使用**：那个 tag 的产物——压缩包名与包内 `plugin.xml` 的 `<version>`——**都是 0.4.1**
> （发布工作流没把 tag 传给构建，取的是 `gradle.properties` 里从 0.4.1 起就没再动过的值）。
> 装了它的人在插件列表里看到的是 0.4.1，**无法据此确认自己装的是哪一版**。
> **v0.4.5 起版本号才真正等于 tag**，且发布流程会断言 zip 名 / 包内 jar 名 / `plugin.xml`
> 三处都等于 tag，不一致就拒绝上传。v0.4.4 的 Release 不删除、不覆盖，只在说明里指向 v0.4.5。
>
> 数字验证于提交 `446ec89`（2026-09-20，Build 通过）。

### 🌐 [letterpress](https://github.com/XIAOXUsop/letterpress) — 中文排版讲究、写给人和 AI 读的静态博客

`Astro 7` `TypeScript` `Content Negotiation` · CI ✅ · MIT

> 零配置就能跑，改一个文件就能上线；文章给人读，markdown 给 AI 读。
> 三个差异化点都对应「别人没做的一步」：

- **给 AI 读的 markdown**——Claude Code / Cursor / OpenCode 发 `Accept: text/markdown`，
  本项目用三个平台（Cloudflare / Netlify / Vercel）的边缘函数做内容协商，
  补上现有集成跳过的托管平台垫片；实测同一页面省 **68.9% / 70.2%** token
- **中文排版按中文的规矩**——行高 1.75、行宽 `34em`（同时满足中文 30–40 字
  与西文 45–75 字符）、`text-autospace` 中西文自动间距、中文不用斜体
- **知识层 lint 会拦构建**——`[[方括号]]` 互链的独立知识库，断链使构建中止，
  语义级检查留给 agent（AGENTS.md 约定）
- **文章阅读页无外链 JavaScript**（首页仅 2.4 KB 内联）· **263 项**单测 ·
  **194 项**端到端契约 · 对比度亮暗双模式有自动化测试
  （搜索页按需加载站内 Pagefind，那不算外链，但也别理解成"整站零 JS"）

> 数字验证于提交 `b8151d6`（2026-09-20，CI 与 GitHub Pages 部署均通过，263/194 在本地重跑过）。

**上手**：`npm install && npm run dev` —— 零配置、零数据库、零环境变量。

Demo：https://xiaoxusop.github.io/letterpress/ —— **该环境不支持内容协商**
（GitHub Pages 改不了响应头）。要 curl 验证 `Accept: text/markdown`，
需要部署到 Cloudflare Pages / Netlify / Vercel 之一，仓库已备好三者的垫片与部署说明，
但**目前尚未部署**，因此"内容协商可用"这句话暂时无法在公开环境直接验证。

> 对着这个 Demo 跑仓库里的线上烟测（`npm run verify:online`）会在协商那几项上报红
> ——**那是上面这条限制本身，不是部署事故**。同一个脚本会同时证明 Pages 能做到的部分是好的
> （`.md` 孪生文件的字节数与 SHA-256 与清单一致、清单本身、NDJSON 可逐行解析）。
> 2026-09-21 实测：7 项不通过，全部落在协商与 `content.ndjson` 的 MIME 上。

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
**请用 v0.4.3 或更新**：更早版本内嵌的 POM 带着一个没随 Release 发布的父 POM，
装完之后宿主工程会报 `Could not find artifact …:ctxpress-parent`，根本用不起来
（这条是照自己的文档亲手做了一遍才发现的）。
**v0.4.3 还修好了 `retrieve` 的「逐字节一致」**——v0.4.2 取回会比原文**多一个换行字节**
（277,282 → 277,283，SHA-256 对不上），**而「逐字节一致」当时就挂在 README 里，是错的**。
修完对**最终发布的那个 jar 实跑验证过**（2026-09-20 复核：270,000 字节往返，
sha256 一致、逐字节相同），CI 里也有一条逐字节契约守着。
发布配置（源码/Javadoc jar、签名、手动触发的发布工作流、POM 元数据）已全部就绪，
缺的只有 Sonatype 令牌与 GPG 私钥。
> 另外：报告里现在**一定会写明 token 数字的口径**（`heuristic` 还是 `o200k_base`），
> 因为同一份内容在两种口径下能差 60%；把预算当硬约束时必须显式传计数器。

> 数字与 Release 验证于提交 `07ff249`（2026-09-20，CI 与 v0.4.3 Release 均通过）。
> 上面的「逐字节一致」不是照着代码推的：**下载 v0.4.3 的 jar 实跑了一遍**——
> 270,000 字节的日志压完再取回，长度差 0、sha256 相同、逐字节相等。

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
  并明确静态风险发现不参与批准——它们描述的是工具面本身有问题，不是"和上次不一样"；
  没有变更可批准时**一个字节都不写**——否则 PR 里会多出一条只有时间戳的 diff，
  而基线 diff 正是这个工具唯一能被评审的东西
- **117 项测试**（含真实 stdio 子进程与本地 Streamable HTTP 服务器的端到端）
- **完全离线**（对比 snyk / cisco 的 MCP 扫描器需要云 API 或 LLM Key），
  且它们目前都不做基线漂移——互补而非替代

**上手**：下载 [mcp-sentinel.jar](https://github.com/XIAOXUsop/mcp-sentinel/releases/latest) → `java -jar mcp-sentinel.jar lock --config mcp.json`

> **v0.5.3 的 Release 构建自提交 `02c18d4`**（tag `v0.5.3` 就指向它）。这之后 master 上
> 只有一个提交 `17f3466`，而它**只改了 `.github/workflows/ci.yml`**——冒烟脚本的 classpath
> 分隔符写死了 `:`，而 Windows 上应该是 `;`。也就是说 **master 比 Release 新的部分里
> 没有任何运行时改动**，`17f3466` 只是让 CI 在 Windows 上也能跑对。
> 数字与 Release 验证于 `17f3466`（2026-09-21，CI 通过）；jar 已下载核对：
> 内嵌 POM 没有 `<parent>`，**实际打包进去的 jackson-databind 是 2.21.5**。

## 工程习惯

- **每个项目都配 CI + 单元测试 + 开源协议**，构建产物不进仓库
- **可复现优先**：评测结果落盘 JSON，数据集带冻结标识与版本要素
- **如实标注局限**：合成数据不等于生产准确率，调优集指标不等于泛化能力
- **产物可获取**：**能打包成「一个文件」的四个项目**——`ctxpress`、`mcp-sentinel`、
  `desensitize-spring-boot-starter`、`aml-compliance-checker`——都发 GitHub Release
  并附可直接运行的产物（可执行 jar / IDEA 插件 zip）。「下载就能用」比「clone 下来
  自己构建」的门槛低一个数量级。
  另外三个不是这个形态，也都有 tag、`clone` 即用：`amlagent` 是全栈应用
  （Docker + 前后端源码，没有"一个文件"可下）、`letterpress` 的产物是
  [线上 Demo](https://xiaoxusop.github.io/letterpress/)、`fsc-examples` 是示例集。
  <!-- 2026-09-19 核对：原文写的是「每个项目都发…并附可直接运行的产物」，
       而按 API 查，amlagent(2 个 release)/letterpress(1)/fsc-examples(1) 的
       assets 都是空的。改成分开写，免得访客十秒就查到反证。 -->

## GitHub 数据

<!--
  原先这里还有两张卡，来自 github-readme-stats 的公共实例：
      /api?username=XIAOXUsop&show_icons=true&theme=synthwave...
      /api/top-langs/?username=XIAOXUsop&layout=compact&theme=synthwave...

  2026-09-19 移除：该公共实例**整站 503**——不只是这两张卡，
  连它的裸首页、以及为其他用户（如 torvalds）生成的卡都返回 503，
  所以这是服务级故障，不是账号或参数的问题。而同一份主页上的
  streak-stats 与 capsule-render 都是 200，说明不是本机网络的问题。

  它对带宽/速率限制一向紧张，属于这一类的已知代价。而下面那张
  `github-metrics.svg` 是**本仓库自己的 Actions 生成并提交**的——
  不依赖任何第三方实例，覆盖面还更全。所以这两张不是「没了」，
  是被一张更可靠、信息更多的替代了。

  若将来该公共实例恢复、而你仍想要那两张紧凑卡：把上面的两行 src 加回
  `<p align="center">` 里即可（参数照抄注释即可复原）。
-->

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
