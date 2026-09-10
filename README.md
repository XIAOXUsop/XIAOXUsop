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

### 🏦 amlagent — 商业银行智能反洗钱（AML）尽调 Agent 平台

`Java 21` `Spring Boot 3` `LangChain4j` `pgvector` `Redis Streams` `Vue 3` · CI ✅ · MIT

> 接收反洗钱预警工单后，可靠地调度 Agent 工作流，自动完成交易画像、股权穿透、制裁名单筛查、
> 监管法规检索、风险研判与结构化报告生成；用**独立于大模型的护栏**校验结论，高风险工单转人工复核闭环。

- **可靠任务** — Transactional Outbox + Redis Streams，含幂等、重试、死信、租约 fencing、崩溃恢复
- **证据追溯** — 混合 RAG（向量 + 中文词法 + 加权 RRF + 精排），结论必须引用 `evidenceId`
- **安全护栏** — 配置化规则 DSL；Prompt 注入三层防护；一级制裁强制 HIGH 并转人工
- **可观测** — Prometheus / Grafana 指标，traceId 全链路透传

**已验证的数据**（详见仓库内评测报告）

| 评测项 | 结果 |
|---|---|
| RAG 法规检索 Recall@5 | **93.3%** → 接入 bge 精排 **100%**（nDCG@5 96.7%，无答案拒答 100%） |
| DeepSeek 真实 Agent 风险准确率 | **44.4% → 100%**（9 条冻结合成 DEV，多轮迭代基线） |
| 一级制裁规则漏报 | **0 / 5** |
| 测试 | 后端 242 项单测 · 22 项集成回归 · 前端 15 项 |

> 数据集标签为合成数据（`PENDING_DOMAIN_REVIEW`），不等同生产准确率——仓库 README 中已如实标注。

### 🔌 desensitize-spring-boot-starter — 注解式敏感数据脱敏

`Java 21` `Spring Boot 3` `Jackson` · CI ✅ · MIT

> 一个 `@Sensitive` 注解把脱敏下沉到 **Jackson 序列化层**，业务代码零侵入；
> 数据库里仍是原值，只在对外输出的那一刻掩码。

8 种内置脱敏类型 · 字段与 getter 均可标注 · 嵌套对象与集合自动生效 · 占位字符可配置
**19 项测试**，含 `ApplicationContextRunner` 自动配置集成测试

### 🛡️ aml-compliance-checker — IDEA 敏感数据合规插件

`Kotlin` `IntelliJ Platform SDK` · CI ✅ · Apache-2.0

> 在 Java 注释与字符串字面量中检出身份证 / 银行卡 / 手机号明文，**一键替换为等长脱敏值**。

身份证做 ISO 7064 MOD 11-2 校验位验证、银行卡做 Luhn 校验，订单流水号不会误报；
报警文案只显示短预览。**17 项测试**。

### 📚 fsc-examples — LangChain4j 金融合规示例集

`Java 21` `LangChain4j` `MCP` `JUnit 5` · CI ✅ · MIT

> 用 `AiServices` + `@Tool` + 法规 RAG 跑通一条 AML 尽调 Agent 链路，
> 给出**确定性护栏**与**双轨评测**（原始模型分 vs 护栏修正后分），
> 并通过 **MCP（Model Context Protocol）** 把同一套工具面开放给任意 MCP 客户端。

- **Agent 与 MCP 共用同一份工具实现**，不存在演示与生产两套逻辑
- 协议层有真实握手测试：把服务作为独立子进程拉起，走完
  `initialize → tools/list → tools/call` 全程 JSON-RPC
- Mock-first：无 API Key、无需联网即可全链路跑通，便于上手与进 CI

## 工程习惯

- **每个项目都配 CI + 单元测试 + 开源协议**，构建产物不进仓库
- **可复现优先**：评测结果落盘 JSON，数据集带冻结标识与版本要素
- **如实标注局限**：合成数据不等于生产准确率，调优集指标不等于泛化能力

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
