# MOSA/数字工程周报 2026-09-21

时间窗：2026-09-14 至 2026-09-20（北京时间 CST）
数据来源：Military Embedded Systems、Air & Space Forces Magazine、TWZ、Northrop Grumman、DroneShield、TechConnect、The Open Group 等

## 一、本期要点

1. **MOSA 峰会议程与主题演讲人公布**（9/22-24，马里兰 National Harbor）：三军与 OSW 高层出席，分技术集成／政策与战略／执行 MOSA 三条并行轨；含「SOSA、FACE、CMOSS 标准收敛」「数字工程作为 MOSA 的强制函数」等关键场次。
2. **SOCOM 发布 MOSA 强制性显示器招标预告**：技术应用项目办公室（TAPO）为旋翼机寻求商用大面积显示系统（LADS），明确要求采用 MOSA，显示定位为现役座舱显示架构中的端点。
3. **SOSA/VITA 生态产品密集落地**：Abaco Systems 推出对齐 VITA 90/VNX+ 的 VNX382（SOSA aligned VNX+ 模块）；Aitech 推出对齐 SOSA 技术标准的 U-C5300 3U VPX GPGPU 板卡。
4. **AFA 2026（9/14-16）主轴为自主系统、电子战、分布式作战与边缘算力**，其中 Aitech C165 6U VME 单板计算机明确以「不替换整个遗留架构即可提升能力」为卖点。
5. **模块化武器架构并行推进**：洛马在 AFA 公布 AGM-158 FLEX 模块化弹体概念（可拆换头锥＋可重构尾段，沿用现有产线）；Sentinel 完成整弹垂直装配，走向 2027 年飞行试验。
6. **开放架构从平台外延到效应器与供应链**：DroneShield 将其开放反无人机架构扩展到高功率激光效应器。
7. **数字工程侧聚焦变更影响面与追溯**：单次工程变更在 MOSA／FACE／软件定义架构下可波及多达 125 个互连工程制品。

## 二、政策与采办改革

本窗口（2026-09-14 至 09-20）未检索到 GAO、DOT&E、NDAA、DFARS、DoDI 5000 系列的窗口内新增文件或更新；也无新的国防部级 MOSA 政策文件发布。

2026-09-18 | MOSA 峰会主题演讲预告：9/22-24 马里兰 National Harbor，三军与战争部办公室（OSW）高层将分享 MOSA 优先级、国防现代化、互操作性与政府—产业协作的高层视角，重点在加速 MOSA 在国防企业级落地；演讲人含空军战斗机与先进飞机组合采办执行官 Timothy Helfrich 准将、陆军通用直升机项目办公室 Ryan C. Nesrsta 上校、海军部长助理办公室系统工程主管 Jason Thomas（后者亦是监控列表中海军 MOSA 基线期望备忘录的推动者）
https://militaryembedded.com/radar-ew/rugged-computing/mosa-summit-keynotes-will-highlight-strategy-and-path-forward-for-wide-mosa-adoption

## 三、军种动态

2026-09-17 | 美特战司令部（SOCOM）技术应用项目办公室（TAPO）就旋翼机商用大面积显示系统（LADS）发布来源征询（sources-sought，SAM.gov）：明确要求采用模块化开放系统方法（MOSA），以支撑互操作性、可复用性与未来增长；显示作为现役座舱显示架构中的端点，安全关键的视频处理与控制保持在显示外部，须提供确定性、有界时延的视频与符号呈现。征询内容包括尺寸与分辨率、亮度范围、夜视兼容性、SWaP、视频与符号接口、鉴定与认证状态，响应截止 10 月
https://militaryembedded.com/avionics/displays/mosa-based-large-area-cockpit-displays-sought-for-military-rotary-wing-aircraft

2026-09-16 | AFA 空天网大会（9/14-16）展场综述：主线为自主系统、电子战、分布式作战与边缘算力前推。Shield AI X-BAT（AI 驾驶垂直起降战斗机，面向制空、打击、压制敌防空、EW、ISR，可在 GPS/通信拒止环境由 Hivemind 自主软件编队控制）；Anduril Pulsar-L（紧凑软件定义 EW，融合软件定义无线电＋板载 GPU＋机器学习，用于探测、跟踪与电子攻击）；Mercury Systems 雷达仿真产品（测试抗干扰与欺骗）；Crystal Group RE4100 边缘计算系统与 RE2500 便携工作站；Curtiss-Wright DTS1 Nano 加固 NAS（可换存储＋双层静态加密＋边缘 AI）；Crystal Group／RackTop／RedData 联合方案侧重战术边缘涉密数据在断连降级网络下继续存储与处理；Aitech C165 6U VME 单板计算机以 11 代 Intel Core i7 保留既有 VME 形态，为在用系统提供算力、存储与网络安全性提升路径。总体指向「现代化越来越不是换单一平台，而是换其支撑技术栈」
https://militaryembedded.com/radar-ew/sensors/afa-show-floor-highlights-autonomy-ew-and-edge-computing-priorities

2026-09-15 | 美空军参谋长 Wilsbach 在 AFA 表示：在基地面临导弹与无人机攻击的背景下，点防御必须成为空军持久能力，并强调抗打击网络与韧性
https://militaryembedded.com/unmanned/payloads/point-defense-resilient-networks-key-to-air-force-operations-under-attack-wilsbach-says

2026-09-15 | DroneShield 的 DroneSentry-X Mk2 反无人机单元在既有 JIATF-401 合同下安装于美陆军步兵班组车辆（ISV）并获验收
https://militaryembedded.com/unmanned/counter-uas/c-uas-units-from-droneshield-accepted-for-us-infantry-vehicles

2026-09-14 | 诺格与美空军在范登堡空军基地完成 Sentinel（LGM-35A）洲际导弹以作战姿态整弹垂直装配，验证导弹设计与集成，是迈向 2027 年飞行试验的设计与适用性评估的重要一步；官方口径强调数字转型、数字加速与先进制造
https://news.northropgrumman.com/sentinel/us-air-force-and-northrop-grumman-assemble-inert-missile-progress-toward-sentinel-flight-testing

## 四、MOSA 标准与开放架构产品进展

2026-09-18 | BAE Systems 推出 Shadow EW 系列紧凑型电子战系统，面向小型空中平台：低 SWaP＋软件定义能力，支持态势感知、瞄准、欺骗、生存力与协同效应投送；采用商用微芯片计算，围绕开放架构标准设计，软件可现场升级以适配任务需求变化；面向高量产与快速平台集成，生产在爱荷华州 Cedar Rapids，软件与设计在新罕布什尔州 Nashua
https://militaryembedded.com/unmanned/test/compact-ew-systems-with-open-architecture-design-launched-by-bae-systems

2026-09-16 | Abaco Systems 发布 VNX382：对齐 VITA 90/VNX+ 标准，基于 NXP i.MX95 SoC，含 6 个支持 lockstep 的 Arm Cortex-A55 核、专用 Cortex-M7 安全域、板载 Arm Mali GPU 与集成 NPU（2 TOPS），可在本地执行目标检测、传感器融合、态势感知等边缘推理以降低时延与对外部算力的依赖；接口含支持 TSN 的 1GbE/10GbE、USB、CANbus；以 SOSA aligned VNX+ 模块（VITA 90.0 侧壁冷却／VITA 90.4 楔形锁紧）或夹层 SoM 形式供货
https://militaryembedded.com/unmanned/payloads/sosa-aligned-vnx-product-from-abaco-systems-debuts

2026-09-14 | Aitech 发布 3U VPX C530 与 U-C5300 通用图形处理（GPGPU）板卡，面向国防与航天的 AI 处理；其中 UC-5300 对齐 SOSA（传感器开放系统架构）技术标准
https://militaryembedded.com/unmanned/rugged-computing/rugged-ai-gpgpu-boards-introduced-by-aitech-for-defense-edge-computing

2026-09-14 | Aitech 发布 C165 加固 6U VME 单板计算机：基于 11 代 Intel Core i7-1185GRE（Iris Xe 图形），较上一代 Aitech VME 平台每瓦性能提升 2 倍、图形性能提升逾 2.5 倍；最多 32GB 带内 ECC LPDDR4X、最多 4TB 自加密 NVMe（支持快速擦除/安全擦除）；含 TPM 2.0、Secure Boot、Intel Boot Guard 的 AiSecure 网络安全框架；支持 PMC/XMC 夹层；与 C164/C163 引脚兼容，可使项目在不迁移新架构的前提下完成算力、存储与网络安全能力升级，缓解元器件停产问题
https://militaryembedded.com/unmanned/rugged-computing/aitech-introduces-new-c165-rugged-single-board-computer-to-help-defense-programs-build-and-modernize-fielded-vme-systems

2026-09-16 | 光互联成为高速网络演进方向（赞助稿）：高带宽传感器与边缘算力增长推动军用嵌入系统从电互联转向光互联，与 VITA/SOSA 相关的高速网络标准演进呼应
https://militaryembedded.com/radar-ew/signal-processing/high-speed-networking-is-driving-the-shift-to-optical-connectivity

2026-09-14 | DroneShield 宣布扩展其开放反无人机架构，纳入澳大利亚 AIM Defence 的 Fractl 高功率激光效应器，使其分层生态从 RF 感知、电子战、指挥控制延伸到定向能；公司定位为开放的软件主导反无人机平台提供方，允许客户按威胁与任务演进组合互补的传感器与效应器
https://militaryembedded.com/unmanned/counter-uas/high-power-laser-integrated-with-droneshield-counter-drone-architecture

2026-09-14 | Holt Integrated Circuits 发布新 MIL-STD-1553/1760 终端产品（行业产品动态）
https://militaryembedded.com/avionics/software/holt-introduces-new-mil-std-15531760-terminal

## 五、数字工程与工业基础

2026-09-16 | 工程智能（engineering intelligence）方法论述：以结构化需求管理、双向追溯、数字主线和 AI 辅助工程分析为基础。文章指出，随着国防项目采用 MOSA（如 FACE 技术标准）、数字工程与软件定义架构，单次工程变更（网络安全整改、元器件停产、需求变化）可波及多达 125 个互连工程制品——涵盖系统与软件需求、FPGA 逻辑、硬件接口、安全分析、网络安全控制、验证程序与认证证据；当这些关系以离散文档或电子表格维护时，团队耗时在定位受影响制品而非实施变更，导致集成延迟、回归测试不完整与配置不一致
https://militaryembedded.com/comms/encryption/streamlining-requirements-management-and-traceability-with-engineering-intelligence

2026-09-15 | 观点文章：软件定义平台下系统生存力越来越由软件开发阶段的软件质量、安全性与可验证性决定，而非仅由装甲、隐身、冗余等物理设计决定；强调以静态分析、自动化测试、结构代码覆盖率与需求追溯构成持续验证，作为软件保证的客观证据，并提升软件供应链完整性
https://militaryembedded.com/avionics/software/before-the-battlefield-there-is-the-codebase

2026-09-15 | 观点文章：低成本弹药的规模化本质是供应链问题而非工程问题——技术可行性已不再是瓶颈，制约因素转为工业化能力；make-vs-buy 的真正判据不是单价而是恢复时间（供应商中断后回到批产速率的速度），飞行关键旋转件的换源认证周期常长于合同交付窗口
https://militaryembedded.com/radar-ew/signal-processing/the-scaling-test-is-a-supply-chain-test

2026-09-16 | 观点文章：以英日意 GCAP 六代机项目为例论「战略自主的幻象」——现代国防能力是跨国界、跨层级的系统集成工程，GCAP 的数字生态包含 AI 任务系统、先进传感器、电子战、软件定义架构、数字工程环境与复杂供应网络；对一二级供应商可见性较强，但三级以下（小型软件供应商、元器件制造商、专业分包商）可见性明显退化，恰是运营、网络与地缘风险高发处
https://militaryembedded.com/unmanned/payloads/moving-beyond-the-illusion-of-strategic-autonomy

2026-09-16 | 洛马在 AFA 公布 AGM-158 FLEX 模块化弹体概念（基于 JASSM）：可拆卸头锥以换装不同传感器、可重构尾段以适配不同发射方式，支持面射、潜射、地射与空射构型；尺寸含 206 英寸超远距（同 JASSM-XR）与 168 英寸增程（同 JASSM-ER）；公司自投 3500 万美元，称客户需求为「有更多选项」，公司未回应空军是否已订购或项目阶段
https://www.airandspaceforces.com/lockheed-martin-modular-jassm-cruise-missile

2026-09-14 | SES 第 11、12、13 颗 O3b mPOWER 卫星由 Falcon 9 发射，第二代中轨通信星座按计划组网完成（与本主题弱相关，记录备查）
https://militaryembedded.com/comms/satellites/three-o3b-mpower-satellites-launched-to-complete-meo-constellation

## 六、中国开放架构动态

本窗口（2026-09-14 至 09-20）未检索到中国开放架构方向的窗口内新增官方发布或标准进展。「车路云一体化关键技术培训」（2026-09-11，中国汽车工程学会）已在上期收录，按时间窗规则不重复计入。

## 七、监控列表更新

检查日期统一更新为 2026-09-21，7 项均无状态变更（无新触发入库条件）：

- 美海军 MOSA 基线期望备忘录：无新进展；推动者 Jason Thomas 将于 9/22-24 MOSA 峰会作专题对话，下期重点关注
- CCA 采购阶段：无新合同或编制方案公告
- Air Force CCA 软件架构：无新发布
- 国防部长 MOSA 强制执行备忘录：无备忘录原文或实施细则
- 多源采购与 MOSA 工业基础改革：无新政策文件
- SOSA 2.0 正式发布：Edition 2.0 标准本身仍未发布；本周生态继续扩大（Abaco SOSA aligned VNX+ 模块 VNX382、Aitech U-C5300 SOSA 对齐 GPGPU 板卡）
- CMOSS 更新：本窗口无新增

## 八、近期峰会日历

2026-09-22 至 09-24 | MOSA Industry and Government Summit & Expo，马里兰 National Harbor（Gaylord 度假村）。三轨议程：技术集成／政策与战略／执行 MOSA。重点场次：
- A True MOSA 101（NAVAIR，航空组合采办执行官）
- 将 MOSA 原则应用于现有平台（Army）
- MOSA at Scale：为采办自由构建工业基础（MOSA Cadre）
- 标准收敛：SOSA、FACE、CMOSS 与开放架构的未来（Army）
- 数字工程作为 MOSA 的强制函数
- 作战部采办转型 MOSA——空军、海军、陆军交叉对话
- 与 Jason Thomas 炉边对话（海军 ASN(RDT&E)）
- 太空 MOSA：可互操作太空飞行航电新纪元（NASA）
https://events.techconnect.org/MOSA_2026/program

2026-10-07 至 10-08 | FACE 与 SOSA 联盟技术交流会议（TIM）
https://www.opengroup.org/content/future-airborne-capability-environment-face/events

2026-10-14 至 10-16 | AUSA 年度会议与展览，华盛顿特区
https://www.ausa.org/meetings

2026-10-21 至 10-23 | 2026 世界智能网联汽车大会，北京亦庄
