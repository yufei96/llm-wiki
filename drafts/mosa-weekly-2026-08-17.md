# MOSA/数字工程周报 2026-08-17

**时间窗：2026-08-10 ~ 2026-08-16（北京时间）**
**生成时间：2026-08-17**

---

## 一、本期要点

1. **DOT&E 公开测试报告撤下网络**：五角大楼将独立测试办公室（DOT&E）的无密级年度武器测试报告从官网移除，转移至 CAC 受限环境（Extranet），官方称防止 AI 帮助对手汇编美军脆弱性画像——独立测试透明度显著倒退，国会与公众监督渠道收窄
2. **GVSETS 2026 召开**：第18届地面车辆系统工程与技术研讨会在 Novi 举行（8/11-13），MOSA Technical Track 聚焦 VNX+（VITA 90）新标准，Elma 现场演示 CMOSS CMFF 机箱并通过 SOSA plug fest 互操作验证
3. **Collins Aerospace 获 $472M CH-47 航电现代化合同**：强调开放、可复用的航电架构提升陆军航空平台通用性
4. **MQ-28 Ghost Bat 进军德国 CCA 市场**：波音与莱茵金属联合提案，数字孪生+模块化架构支撑德国有人-无人协同作战
5. **Leonardo DRS 软件升级扩展 SGT STOUT 反无人机能力**：不改硬件、纯软件方式击败 Group 1/2 小型无人机，验证模块化接口架构的演进价值

本周期为美国八月假期季，核心新闻密度中等，但 GVSETS 与 DOT&E 两条信息价值较高。

---

## 二、政策与采办改革

### DOT&E 年度报告撤下公开网站，转入 CAC 受限环境
2026-08-11 | 五角大楼将独立测试办公室（DOT&E）无密级年度武器测试报告从官网撤下，转至安全 DOT&E Extranet（仅授权人员经 CAC 访问）。DoD 称此举为主动强化作战安全态势，防止 AI 工具帮助外国对手将分散信息汇编成美军脆弱性画像。DOT&E 自1983年设立以来一直依法公布无密级年度报告，此变动实质切断国会与公众对武器测试的独立监督渠道，引发透明度担忧。（POGO 8/11 通讯确认报道日期）
URL: https://federalnewsnetwork.com/defense-news/2026/08/dod-pulls-independent-testing-offices-public-reports-from-its-website

---

## 三、军种动态

### Collins Aerospace 获 $472M 合同推进 CH-47 航电现代化
2026-08-11 | 美国陆军授予柯林斯宇航（RTX 旗下）最高 $472M 工程服务合同，支持 CH-47 支奴干机队现代化与保障。工作包括航电升级、应对元器件过时、强化航电架构；重点支撑陆军跨平台通用性目标——采用开放、可复用的航电架构跨多机型集成，简化新技术插入、降低集成复杂度与成本/进度风险。工作地点：Huntsville, AL 与 Cedar Rapids, IA。
URL: https://militaryembedded.com/avionics/computers/avionics-upgrades-to-support-us-army-chinook-helicopters-under-472-million-contract

### Leonardo DRS 以软件升级扩展 SGT STOUT 反无人机能力
2026-08-12 | Leonardo DRS 在美政府测试活动中演示 SGT STOUT 防空系统软件更新，使已列装数百套的系统无需新硬件即可对抗 Group 1/Group 2 小型无人机。SGT STOUT 任务设备包采用模块化接口，支持后续集成被动探测、AI 决策辅助、边缘计算与新效应器，架构面向编队级防空（集成感知、提示、交战）。体现"软件定义武器系统"与模块化开放架构的持续演进。
URL: https://militaryembedded.com/unmanned/counter-uas/counter-uas-software-upgrade-demonstrated-on-us-army-air-defense-system

### MQ-28 Ghost Bat 被提议作为德国 CCA 平台
2026-08-11 | 波音与莱茵金属联合宣布，提议 MQ-28 Ghost Bat 作为德国发展协同作战飞机（CCA）能力的平台（空地/空空任务）。莱茵金属将在德国建立系统集成能力（软件与任务集成）；波音还与罗德与施瓦茨、Diehl、HENSOLDT 构建德国工业网络。MQ-28 采用数字孪生支撑基于试飞数据的开发，模块化架构支持传感器、软件与任务配置灵活更换——CCA 国际扩散标志性进展。
URL: https://militaryembedded.com/unmanned/isr/mq-28-ghost-bat-drone-proposed-for-german-collaborative-combat-aircraft-plans

### GVSETS 2026 举行：MOSA Technical Track 聚焦 VNX+ 标准
2026-08-11~13 | 第18届 NDIA 地面车辆系统工程与技术研讨会（GVSETS）在密歇根 Novi 举行。MOSA 技术分组重点关注新 VNX+（VITA 90）标准用于 SWaP 受限可部署系统；现场设 UGV 演示赛道（8/11-12）与无人机竞速。陆军下一代地面车辆（NGCV/XM-30）开放架构是本届核心议题。
URL: https://ndia-mich.org/event/gvsets-symposium

---

## 四、MOSA 标准进展

### Elma 在 GVSETS 展示 MOSA 对齐 CMFF 机箱与 VNX+ 原型
2026-08-11 | Elma Electronic 在 GVSETS 现场演示模拟电子战应用：MOSA 对齐的集成式 CMFF（CMOSS Mounted Form Factor，C5ISR/EW 模块化开放标准套件之车载形态）机箱安装在 SAVE 兼容托盘上，满足 MOSA 要求；该单元近期参加 SOSA "plug fest" 互操作活动，与多家厂商插件卡成功互操作。同期展出两款 VNX+ 部署式任务计算原型。8/11 下午 Elma 系统产品总监 Mark Littlefield 在 MOSA 技术分组演讲"如何基于标准的 MOSA 应对 SWaP 受限可部署系统（VNX+）"。
URL: https://militaryembedded.com/radar-ew/rugged-computing/mosa-aligned-cmff-chassis-shown-by-elma-at-gvsets-2026

### TSN 时间敏感网络从实验室走向军用平台
2026-08-10 | Military Embedded Systems 报道：时间敏感网络（TSN）解决方案正从实验室迁移到军用平台，用于确定性以太网传输以支撑雷达/EW、无人机等实时任务。TSN 与 SOSA/CMOSS 开放标准组合是构建可互操作模块化航电/车辆电子架构的关键趋势。
URL: https://militaryembedded.com/radar-ew/signal-processing/time-sensitive-networking-tsn-solutions-moving-from-labs-to-military-platforms

### EIZO 发布 3U VPX 战术 AI 单板计算机
2026-08-14 | EIZO 推出面向战术边缘 AI/传感器工作负载的 3U VPX 单板计算机，符合开放标准（VPX 生态），支撑地面车辆与机载平台的模块化计算升级。
URL: https://militaryembedded.com/comms/vetronics/3u-vpx-single-board-computer-for-tactical-ai-processing-launched-by-eizo

---

## 五、中国开放架构动态

本周时间窗（8/10-8/16）内未检索到中国智能网联/车路云/军工开放架构的新增重大发布。近期背景参考（窗口外，供跟踪）：
- 工信部 8/4 公布《智能网联汽车 自动驾驶系统安全要求》（GB 44721—2026）强制性国标（7/30 批准，2027/7/1 实施）——L3/L4 安全准入基线，从"推荐"转"强制"
- 车路云一体化试点首批20城进入收官（2026年中），试点扩容至50城，粤港澳大湾区跨市互认
- 华为乾崑 ADS 5（4月发布）累计上车超170万辆，2026目标80+车型/300万台

---

## 六、监控列表更新（2026-08-17 检查）

| 监控项 | 状态 | 变化 |
|---|---|---|
| CCA采购阶段 | 🟢 已触发 | 无新进展；本周仅德国 CCA（MQ-28 提案）国际动态 |
| AF CCA软件架构 | 🟡 新增 | 无新进展 |
| MOSA强制执行备忘录 | 等待原文 | 无新进展 |
| 多源采购改革 | 等待细节 | 无新进展 |
| SOSA 2.0正式发布 | 等待发布 | 无新进展（Elma CMFF 通过 SOSA plug fest 互操作，生态活跃） |
| CMOSS更新 | 等待新版 | ⚠️ 新进展：GVSETS 上 CMFF 车载形态实装演示，CMOSS 地面形态生态推进 |

---

## 七、峰会日历

- **2026 Defense Standardization Program (DSP) Conference** —— 8/3-6 于 Tysons, VA 举行（已结束；主题"Strength through Standardization"，含 MOSA 标准化专题）https://www.dsp.dla.mil/2026DSPConference
- **MOSA Industry & Government Summit 2026**（TechConnect）—— 9/22-24 于 National Harbor, MD https://events.techconnect.org/MOSA_2026
- **MOSA Interoperability Standards for Space Systems 网络研讨会** —— 8/26（聚焦 MBSE 数字标准，SOSA/CMOSS 太空互操作）https://spacenews.com/webinar-on-mosa-interoperability-standards-for-space-systems-august-26-2026
- **SOSA Consortium 会员大会** —— 10/6-8 Aberdeen, MD；12/1-2（TBD）https://www.opengroup.org/sosa/events
- **MOSA for Defense & Warfare Summit 2027**（DSI）—— 2027 议程待公布 https://mosa.dsigroup.org

---

*来源优先级：官方/军种/权威媒体 > 行业媒体；所有条目均已核对发布日期在时间窗内。*