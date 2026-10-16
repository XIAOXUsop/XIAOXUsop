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
  维护约定：
  1. 每个精选项目小节必须包含 `验证于提交 `<短SHA>`（YYYY-MM-DD...）`，由 `scripts/check_profile.py` 自动校验。
  2. 所有测试数字、评测结果与已知限制必须与对应仓库默认分支的最新 README / CI 产物一致。
  3. 历史版本的缺陷复盘细节留在各仓库的 Release Notes / CHANGELOG，主页只呈现核心设计、最新验证基线与真实边界。
-->

### 🏦 [amlagent](https://github.com/XIAOXUsop/amlagent) — 商业银行智能反洗钱（AML）尽调 Agent 平台

`Java 21` `Spring Boot 3.5` `LangChain4j` `pgvector` `Redis Streams` `Vue 3` · CI 8 项 7 绿 · MIT

> 接收反洗钱预警工单后，可靠地调度 Agent 工作流，自动完成交易画像、股权穿透、制裁名单筛查、监管法规检索、风险研判与结构化报告生成；用**独立于大模型的确定性护栏**校验结论，高风险工单转人工复核、补充尽调（EDD）与可疑报告（STR）闭环。

- **可靠异步工作流** — Transactional Outbox（`PENDING → PUBLISHING → PUBLISHED` 原子抢占）+ Redis Streams 消费组，含版本化租约 + 心跳 fencing、指数退避重试、死信重放与崩溃超时接管
- **Snapshot First 与证据追溯** — 推理前一次性冻结客户、交易、股权、制裁、关联预警与法规快照（`sourceDigest`）；混合 RAG（PGVector 向量 + 中文词法 + 加权 RRF + 本地 bge 精排）要求关键结论绑定合法 `evidenceId`，并提供可回滚索引供应链与知识投毒隔离
- **安全护栏与业务闭环** — `risk_rule` 表驱动规则 DSL + Prompt 注入三层防护，一级制裁命中强制 `HIGH` 并转人工 `HOLD`；支持解释核验工作区、限时实名补充尽调（EDD）、可疑交易报告（STR）报送/退回补正、确定性风险优先 SLA 运营队列与 SHA-256 调查档案导出；另提供面向 ADMIN 的客户绑定只读流式 AI 小助
- **全链路可观测** — Prometheus 指标 + **OpenTelemetry GenAI 语义约定**追踪（`chat {模型}` span，涵盖 `gen_ai.usage.*` / `gen_ai.response.finish_reasons` 等标准属性；**span 只记元数据，绝不写入客户 prompt 或补全正文**）

**上手**（三步启动——`docker-compose.yml` 仅含基础设施，后端默认 Mock 模型，无需配置 API Key 即可离线体验完整链路）：

```bash
docker compose up -d                       # MySQL(3307) / PGVector(5433) / Redis(6379)，后台运行
cd backend  && ./mvnw spring-boot:run      # 后端(8080)，默认 Mock 模型，占一个终端
cd frontend && npm install && npm run dev  # 前端(5173)，浏览器打开即可登录，占另一个终端
```

**已验证的数据**（测试范围与复现方式见 [amlagent README](https://github.com/XIAOXUsop/amlagent#当前验证结果)）

| 评测项 | 结果 |
|---|---|
| RAG 法规检索 Recall@5 | **93.3%** → 接入本地 bge 精排 **100%**（MRR 95.6%，nDCG@5 96.7%，无答案拒答 100%） |
| DeepSeek 真实 Agent 风险准确率 | **44.4% → 100%**（9 条冻结合成 DEV 迭代基线；Guardrails 后 **77.8% → 100%**） |
| 一级制裁规则漏报 | **0 / 5**（100 条独立合成规则回归案例） |
| 自动化测试 | 后端单测 **1003/1004**（1003 通过、1 项真实模型评测默认跳过）· 集成回归 **43/44**（本机加载精排模型时 **44/44**）· 前端单测 **85/85** · Playwright E2E **8/8** · Python 脚本测试 **74** 项 |

> 验证于提交 `a961bdf`（2026-10-07）。测试条数由 `scripts/test_summary.py` 从 Surefire XML 与 Vitest JSON 实算并由 CI 对账；内置数据集标注为 `PENDING_DOMAIN_REVIEW` 合成数据，不等同生产准确率。CI 8 个 job 中 7 项通过，唯一失败项为 `Backend Dependency Vulnerability Scan` 检出的 15 条上游依赖告警（归并于 `spring-core`、`spring-security-core` 与 `pgvector`），由 `scripts/dependency-triage.json` 逐条跟踪复查，不通过调低阈值或加豁免掩盖。

### 🖥️ [Pi-desktop](https://github.com/XIAOXUsop/Pi-desktop) — 基于官方 Pi 的本地编程 Agent 桌面应用

`TypeScript` `Electron 44` `Pi SDK` `Node.js 24` · CI ✅ · MIT

> 打开本机代码库，通过对话完成代码阅读、文件编辑、受控命令执行与差异审阅；内置独立进程恢复、字节级文件检查点撤销，以及 `/plan` 和 `/goal` 工作流扩展。

- **独立执行进程与多模型接入** — Electron 渲染层开启严格上下文隔离与 CSP，Pi 执行层在独立 Worker 进程运行；内置 DeepSeek、OpenAI、Anthropic、智谱 GLM、Kimi、通义千问等 11 家提供方预设（1,262 个目录模型）及 OpenAI Chat / Responses、Anthropic Messages 自定义接入，密钥经 `safeStorage` 加密存储
- **字节级文件检查点与冲突保护** — 自动记录任务开始前的原始文件字节（保存在项目 `.agent/checkpoints/`），支持新建、修改、删除文件的差异预览、一键撤销与撤回撤销；若任务后发生人工编辑则自动识别冲突并阻止覆盖
- **崩溃恢复与子进程生命周期监督** — Worker 意外中断后保留未完成输出与持久运行状态，支持人工核实待确认工具后继续任务，**已确认的写操作或工具绝不自动重放**；子进程命令由 Supervisor 统一托管并在宿主退出时清理后代进程
- **工作流与资源体系** — 内置 `/plan`（只读探索 → 澄清问题 → 提交计划 → 确认后按原权限执行）与 `/goal`（带 token/轮次预算与独立验证回合的持续目标推进）扩展；支持本地、npm 与 Git 来源的扩展、技能、提示模板与主题管理

**上手**：在 [v0.1.4 Release](https://github.com/XIAOXUsop/Pi-desktop/releases/tag/v0.1.4) 下载 `Pi-desktop-Setup-0.1.4-x64.exe` 安装版或 `Pi-desktop-0.1.4-Windows-x64.zip` 免安装版（均内置 Node.js 24 与 npm 运行时，无需本地预装开发环境）。

> 验证于提交 `10e583b`（2026-10-16，69 项核心测试 + 145 项桌面与工作流测试共 **214 项**自动化测试通过，另有真实 Electron 窗口检查、移除系统 Node 后的独立打包运行时验证、旧版升级迁移测试及 DeepSeek 20 任务评测闭环）。当前 Windows 发行包未配置代码签名证书，文件检查点不恢复数据库或外部网络副作用。

### 🩺 [ai-plugin-doctor](https://github.com/XIAOXUsop/ai-plugin-doctor) — AI 插件跨客户端配置诊断与发行验收 CLI

`TypeScript` `MCP` `C# Native` `Windows x64` · CI ✅ · MIT

> 扫描 Codex CLI、Claude Code、Cursor 和 VS Code 的本地 MCP 配置，定位覆盖链与故障原因并执行受限修复；同时支持在隔离环境中驱动真实 Codex CLI 与 Claude Code 完成 `stdio` MCP 工具的发现、选择与调用验收。

- **四客户端配置扫描与受限修复** — 被动扫描无需模型密钥、不拉起外部服务，覆盖 24 类常见配置故障（语法错误、方言差异、缺失变量、作用域覆盖、同名冲突、脚本启动器等）与配对正常对照；支持保留注释与格式的 JSON/JSONC 原子修复（备份文件受 Windows `FileSecurity` Owner-Only ACL 保护）及 Codex TOML 手工补丁导出
- **E0–E4 分层证据与真实客户端闭环** — 通过透明 `stdio` 代理在隔离工作区启动真实 Codex CLI 与 Claude Code，分别采集 **E0 静态配置、E1 协议握手、E2 客户端发现、E3 模型任务调用与参数断言** 四层独立状态（E4 桌面体验单列人工签署），正负例与启动失败严格归因
- **防篡改报告与版本回归对比** — 生成本地 HTML/JSON 证据包并校验 `static.json`、`probe.json`、配置快照及各 trial 日志的 SHA-256（任何证据篡改或缺失均拒绝重生成报告）；`compare` 支持插件升级或 schema 变更前后的回归门禁（E2/E3 退化返回退出码 2），Windows Job Object 确保超时或中断时彻底回收后代进程树
- **可复现源码包交付** — `npm run package:source` 生成固定文件顺序、时间戳与权限的源码 ZIP 及 `SOURCE_MANIFEST.json`，Windows CI 自动执行解压、独立重建与清单完整性校验

**上手**：

```powershell
npm ci --ignore-scripts && npm run build
node dist/src/cli.js scan --workspace "D:\你的项目" --clients codex,claude,cursor,vscode --out runs/config-scan
```

> 验证于提交 `2eb1f14`（2026-10-16，Windows CI 与本地 **163 项**测试全部通过，覆盖 24 类故障与配对对照、金丝雀密钥零泄漏、Job Object 进程树清理、ACL 备份与报告防篡改校验）。自动化工具调用验收仅覆盖本地 `stdio` MCP；Streamable HTTP、OAuth 与 IDE 图形界面会话保留人工取证流程。

### 🛰️ [mcp-sentinel](https://github.com/XIAOXUsop/mcp-sentinel) — MCP 工具面安全扫描器与 Lockfile

`Java 21` `MCP` `Security` `SARIF 2.1.0` · CI ✅ · MIT

> 把 MCP 服务器的工具定义锁进版本库（`mcp-sentinel.lock.json`），让"工具描述或 schema 被悄悄改写"像代码变更一样出现在 PR diff 与 CI 门禁中。

- **语义规范化指纹** — 对 `required` / `enum` / `type` / `allOf` / `anyOf` / `oneOf` 等集合关键字排序去重并对数值归一化，保留 `prefixItems` 等顺序敏感结构，避免服务端集合迭代顺序不同造成误报
- **按 MCP 风险轴分级与兜底** — 将 **27 类**工具面变更分为 `DANGEROUS`（如描述改写、新增可选参数、未识别嵌套变更 `UNGRADED_SCHEMA_CHANGE`）、`BREAKING`（如新增必填参数）与 `INFO`；钉死"**指纹变化 ⇒ 至少一条变更**"不变量，防止嵌套 schema 投毒静默绕过
- **内容绑定的审批继承** — `--accept-changes` 将变更类型、工具名与变更后内容摘要写入基线并打印审批摘要（批准 Beta 不会自动放行后续改成的 Gamma）；静态风险发现不参与批准，无变更可批准时不改写文件时间戳
- **16 条离线静态规则与 Fail-Closed 门禁** — 规则执行前完成 Unicode NFKC 归一、零宽/双向控制字符剥离与西里尔/希腊同形字折叠；支持 `stdio` 与 `streamable-http`（连接超时与请求超时独立控制，显式拒收 `sse` 别名）；基线缺失或损坏一律以退出码 **5** 失败（仅在显式声明 `--risk-only` 时跳过漂移比对），输出通过官方 Schema 校验的 SARIF 2.1.0 报告

**上手**：下载 [mcp-sentinel.jar](https://github.com/XIAOXUsop/mcp-sentinel/releases/latest) → `java -jar mcp-sentinel.jar lock --config mcp.json`

> 验证于提交 `3fce373`（2026-09-25，**132 项**测试通过，含真实 `stdio` 子进程、本地 Streamable HTTP 端到端、SARIF 2.1.0 官方 Schema 校验及发版前双道预检闸；v0.5.6 可执行 JAR 已下载实跑核验）。本工具只做离线工具定义锁定与静态分析，不拦截运行时 `tools/call`。

### 🗜️ [ctxpress](https://github.com/XIAOXUsop/ctxpress) — Java Agent 上下文确定性压缩引擎

`Java 21` `Context Engineering` `BPE Tokenizer` · CI ✅ · MIT

> 在工具输出、应用日志、RAG 片段进入 LLM 之前，按给定的 token 预算执行**确定性、可审计、可逆**的抽取式压缩，不调用大模型、零增量推理成本。

- **严格预算契约** — 支持 `o200k_base` 等真实 BPE 词表硬预算（`strictBudget`）与启发式安全余量；内容放得下时零改动，受保护内容本身超预算或无结构可裁时分动作名如实上报 `overBudgetBy`，**绝不静默超标**（由 **6 类语料 × 10 档预算矩阵**在 CI 逐格守卫，遵守率 **100%**）
- **按体裁处理而非切字符串** — JSON 三档压缩（第一档纯文本扫描去空白逐字节无损，二/三档数组头尾采样与字符串截断并用 `BigDecimal` 精确保值）；LOG 按行折叠相邻重复、保留故障行并设 60% 保护占比降级闸门；TEXT 按句切分并做跨片段句子级去重
- **内容寻址可逆归档** — 被省略原文写入内存或跨进程追加式文件归档（`ORIG-<sha256前16位>`），归档引用嵌入压缩结果中供模型按需调用，命令行 `retrieve` 取回与原文**逐字节一致**
- **离线保真评测** — 命中保护规则的关键信息在任意预算下召回率 **100%**（朴素头截断在小预算下仅 33%）；日志、折叠、JSON、文本、数值五组路径保真证书均为 **0 处凭空生成**

**上手**：下载 [ctxpress.jar](https://github.com/XIAOXUsop/ctxpress/releases/latest) → `java -jar ctxpress.jar analyze --max-tokens 8000 app.log`（作为 Maven 库引用时按仓库说明从 Release 安装自包含 POM 的 `v0.4.4` JAR；Maven Central 发布工作流已就绪，待配置凭据）。

> 验证于提交 `daeb3a2`（2026-09-25，**104 项**离线测试通过：core 78 + tokenizer 11 + cli 15，v0.4.4 Release JAR 已下载实跑核对）。当前提供离线保真评测（关键信息召回 + 零幻觉证书），尚未包含调用真实大模型的下游任务准确率评测。

### 🔌 [desensitize-spring-boot-starter](https://github.com/XIAOXUsop/desensitize-spring-boot-starter) — 敏感数据防护 Spring Boot Starter

`Java 21` `Spring Boot 3` `Jackson` `HMAC-SHA256` `AES-GCM` · CI ✅ · MIT

> 两层能力：**① 接口返回值脱敏**（`@Sensitive` 注解，Jackson 序列化层不可逆掩码，业务零侵入）；**② 大模型输入输出脱敏**（可逆假名化，出站替换为确定性令牌、入站自动还原，让模型看得见上下文关联而看不见真实身份）。

- **展示态序列化脱敏** — 支持身份证、手机号、姓名、邮箱、银行卡、地址、IP、自定义保留位数及数值/字符/UUID 标量；通过 `BeanPostProcessor` 幂等注册到容器内所有 `ObjectMapper`（即使应用自定义了 `ObjectMapper` Bean 也不会静默失效）
- **128-bit 确定性假名化令牌** — `TYPE_v2_<32位十六进制>` 由 `HMAC-SHA256(密钥, 类型|版本|原文)` 生成（覆盖 15/18 位身份证、`+86`/连字符手机号、4 位分组银行卡）；不含原文、跨轮次稳定、无密钥不可伪造；碰撞时严格抛出 `TokenCollisionException`，绝不静默覆盖或混淆身份
- **会话级隔离与加密文件保险库** — `ScopedTokenVault` 支持按会话隔离映射、TTL 过期、`forget(scope)` 整体撤销（拒绝控制字符防前缀撞键）及不含原文的 `RestoreAudit` 回调；内置 `EncryptedFileTokenVault` 提供 AES-GCM 文件锁持久化、原子替换、64 MiB 上限保护与密钥轮换
- **模型调用装饰器与异常消毒** — `PseudonymizingChat` 封装"出站脱敏 → 模型调用 → 入站还原 → 异常消毒"闭环；当请求含敏感数据时自动清洗异常消息并剥离底层堆栈，防止 SDK 报错将客户明文打进日志

**上手**：下载 [desensitize-spring-boot-starter.jar](https://github.com/XIAOXUsop/desensitize-spring-boot-starter/releases/latest) 安装到本地 Maven 仓库，在 DTO 字段或 getter 上添加 `@Sensitive` 即可。

> 验证于提交 `b159feb`（2026-09-26，**115 项**单测与 `ApplicationContextRunner` 自动配置集成测试通过，测试条数由 CI 自动对账；v0.6.3 Release JAR 已下载实跑核验，内嵌 `jackson-bom` 显式钉在 `2.21.5`）。假名化不支持流式分片逐块还原（需在完整响应或分片边界还原）。

### 🛡️ [aml-compliance-checker](https://github.com/XIAOXUsop/aml-compliance-checker) — IDEA 敏感数据合规检查插件

`Kotlin` `IntelliJ Platform SDK` `PSI Static Analysis` · CI ✅ · Apache-2.0

> 在代码编写阶段检测注释与字符串字面量中的身份证号、银行卡号、手机号、邮箱明文，给出可解释的置信度与判定依据，并支持 `Alt+Enter` **一键替换为等长脱敏值**。

- **双信号可解释判定** — **信号一（值形态，高置信）**：18 位身份证过 ISO 7064 校验位、16–19 位银行卡过 Luhn 校验；**信号二（标识符语义，中置信）**：向上最多 3 层 PSI 提取变量/字段/参数名、方法调用名（如 `setIdCard(...)`）及成对实参键名（如 `Map.of("cardNo", ...)`），专门兜住校验位不合法的测试与 Mock 数据
- **跨语言 PSI 扫描与安全预览** — 覆盖 Java 及 XML（如 MyBatis Mapper 注释与属性值）中的 `PsiComment`（含 Javadoc）与 `PsiLiteralValue`；告警信息仅显示短预览（如 `110************531`），防止告警面板本身泄漏完整敏感值；`DesensitizeFix` 通过 `WriteCommandAction` 原地等长替换

**上手**：在 [Releases 页面](https://github.com/XIAOXUsop/aml-compliance-checker/releases/latest) 下载 `aml-compliance-checker-0.4.6.zip`，IDEA 中 `Settings → Plugins → ⚙ → Install Plugin from Disk` 即可。

> 验证于提交 `e561ef1`（2026-10-07，**58 项**测试通过：30 项纯逻辑测试 + 28 项真实 IntelliJ PSI 与 QuickFix fixture 测试；0.4.6 公开 Release ZIP 已通过文件名、包内 JAR、`plugin.xml` 版本与修复提交祖先校验）。静态检查不覆盖动态字符串拼接、`.properties`/`.json` 等非 PSI 字面量文件及运行时数据。

### 🌐 [letterpress](https://github.com/XIAOXUsop/letterpress) — 中文排版讲究、写给人和 AI 读的静态博客与知识编译系统

`Astro 7` `TypeScript` `Content Negotiation` `LLM Wiki` · CI ✅ · MIT

> 零配置起步，文章给人读，Markdown 给 AI 读；将中文 Web 排版规范、HTTP 内容协商与可验证的知识溯源编译进同一个纯静态站点。

- **面向 AI 的内容协商与增量同步** — 内置 Cloudflare Pages / Netlify / Vercel 边缘函数垫片响应 `Accept: text/markdown`（处理 Claude Code 无 q 值顺序偏好、通配符与 `q=0` 拒绝），同一页面较 HTML 节省 **57.9% / 55.3%** 估算 token（`o200k_base` 真实词表复算为 **60.8% / 58.0%**）；构建期确定性产出 `/content-manifest.json`（含 SHA-256 与 JSON Schema 2020-12 校验）与 `/content.ndjson` 流式全量导出，附带可断点恢复的参考同步器
- **讲究的中文排版与克制的前端负载** — 行高 `1.75`、行宽 `34em`（容器宽度稳定跟随字号）、原生 `text-autospace` 中西文间距、`line-break: strict`、禁用中文伪斜体；文章阅读页 **0 外链 JS**（首页仅 2.5 KB 内联；搜索页按需通过原生模块加载同源 Pagefind，无需 `unsafe-eval`，访问者实际加载 5 个 JS 共 gzip **93 KB**）
- **知识层断链阻断与版本化溯源** — `[[方括号]]` 双向链接基于 Markdown AST 精确排除代码块，断链或同名标题歧义直接阻断构建；知识页结论绑定带日期规范版本的 `sources` 与正文摘要 `review.contentDigest`，修改正文或来源版本后未重新复核即触发 `review-stale` 阻断构建，机器出口同步携带新鲜度状态；提供 `wiki:ask`、`wiki:impact`、`wiki:review` CLI

**上手**：`npm install && npm run dev` · 在线 Demo：[https://xiaoxusop.github.io/letterpress/](https://xiaoxusop.github.io/letterpress/)

> 验证于提交 `094abbd`（2026-10-02，**568 项**离线单测、**201 项**构建产物契约、**23 条**检索金标、**32 步**门禁编排及跨时区 **107 个文件**逐字节可复现构建通过）。公开 Demo 托管在 GitHub Pages 上，受平台限制不支持自定义响应头，因此同 URL 的 `Accept: text/markdown` 内容协商与 `/content.ndjson` 的 MIME 类型需部署至 Cloudflare Pages / Netlify / Vercel 之一才生效。

## 工程习惯

- **每个项目都配 CI + 单元测试 + 开源协议**，构建产物不进版本库
- **可复现优先**：评测结果落盘 JSON，数据集带冻结标识与版本要素；发布包固定构建时间戳或输出 SHA-256 校验清单
- **如实标注局限**：合成数据不等于生产准确率，调优集指标不等于泛化能力，平台与协议边界在文档首屏如实声明
- **产物可获取**：按项目形态提供最低门槛的交付方式——
  - **桌面安装包 / 免安装便携包**：`Pi-desktop`（Release 提供内置 Node/npm 运行时的 Windows `.exe` 安装程序、`.zip` 便携包与 `SHA256SUMS.txt`）
  - **单文件可执行 JAR**：`ctxpress`、`mcp-sentinel`（Release 直接下载，`java -jar` 即可运行）
  - **自包含 POM 的库 JAR**：`desensitize-spring-boot-starter`（Release 下载后两步安装至本地 Maven 仓库即可引用）
  - **IDE 插件包**：`aml-compliance-checker`（Release 提供经版本与结构校验的 `.zip` 插件包，`Install Plugin from Disk` 即装即用）
  - **确定性源码包 / 在线体验 / 离线全链路示例**：`ai-plugin-doctor`（提供带 `SOURCE_MANIFEST.json` 的可复现源码包）、`letterpress`（提供[线上 Demo](https://xiaoxusop.github.io/letterpress/) 与三平台边缘函数模板）、`amlagent`（Docker 基础设施 + Mock 模型离线可跑全栈闭环）、[fsc-examples](https://github.com/XIAOXUsop/fsc-examples)（零 API Key 离线可跑的 LangChain4j + MCP 金融合规示例集与双轨评测，MIT）

## GitHub 数据

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
