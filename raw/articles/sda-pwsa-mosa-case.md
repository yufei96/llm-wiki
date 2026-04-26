---
title: "太空发展局（SDA）增殖型作战人员太空架构（PWSA）MOSA实施"
source: "深度调研JSON结果"
date: 2026-04-26
type: research_data
---

# 太空发展局（SDA）增殖型作战人员太空架构（PWSA）MOSA实施

## 结构化调研数据

{
  "project_name": "太空发展局（SDA）增殖型作战人员太空架构（PWSA）MOSA实施",
  "service_branch": "美国太空军（U.S. Space Force），SDA为太空军直属报告单位",
  "start_year": 2019,
  "prime_contractor": "多家供应商竞争模式：传输层（Transport Layer）主要承包商包括Lockheed Martin、Northrop Grumman、York Space Systems等；跟踪层（Tracking Layer）主要承包商包括Lockheed Martin、Northrop Grumman、L3Harris、Rocket Lab等。SDA采用'工厂化'批量采购模式，避免单一主承包商垄断。",
  "program_status": "持续部署中。Tranche 0（28颗卫星）于2022年12月首次发射，2023年完成在轨演示。Tranche 1（126颗传输层+35颗跟踪层+12颗战术演示卫星）于2025年9月开始发射。Tranche 2和Tranche 3合同已授予。Tranche 3跟踪层4颗合同共约35亿美元（2025年12月）。SDA计划每两年发射一个新批次。",
  "mosa_standards_used": "SDA NEBULA标准（Network Established Beyond the Upper Limits of the Atmosphere）：SDA自定义的网络架构标准，v3.05（2024年11月版本）。SDA光学星间链路（OISL）标准（SDA-9100-0001-01）：定义卫星间激光通信的互操作参数。采用基于IP/MPLS的网络协议栈，遵循OSI参考架构。Link 16战术数据链接口标准。Ka波段射频通信标准。",
  "mosa_implementation_status": "全面实施中（Implementing）。PWSA是MOSA在太空域最大规模的应用案例。SDA通过标准化接口要求所有供应商的卫星必须兼容NEBULA网络标准和OISL标准，实现多供应商卫星的即插即用互操作。",
  "modular_architecture_description": "PWSA采用七层功能架构：1）传输层（Transport Layer）——全球LEO光学mesh网络骨干；2）跟踪层（Tracking Layer）——红外导弹预警/跟踪传感器；3）导航层（Navigation Layer）——GPS备份PNT能力；4）战场管理层（Battle Management Layer）——星上边缘计算；5）托管层（Custody Layer）——ISR目标跟踪（利用外部资产）；6）新兴能力层（Emerging Capabilities Layer）——灵活集成新技术；7）支持层（Support Layer）——地面站、发射服务等。各层通过标准化接口解耦，可独立更新迭代。",
  "interface_specifications": "SDA OISL标准（9100-0001-01）：定义光学星间链路参数，包括C波段1536.61nm波长、LHCP偏振、BER 10^-6至10^-9、调制解调延迟≤15ms。SDA NEBULA标准v3.03/v3.05：基于IP/MPLS的网络架构，定义网络层协议、QoS、OAM、Netconf管理等。Ka波段RF接口：用于上下行链路。Link 16战术数据链接口：用于与地面/空中/海上平台数据传输。",
  "compliance_certification": "所有PWSA供应商必须通过SDA NEBULA标准和OISL标准合规测试。SDA在合同中明确要求接口兼容性验证。Kepler Communications等公司已成功完成SDA标准兼容OISL在轨测试。",
  "brownfield_vs_greenfield": "绿地项目（Greenfield）。PWSA是全新架构，不基于现有卫星系统改造。",
  "acquisition_pathway": "其他交易权限（Other Transaction Authority, OTA）和快速采办。SDA以极快的采办速度著称——从合同授予到首次发射仅2.5年（Tranche 0）。",
  "contract_type": "其他交易权限（OTA）合同、固定价格合同。SDA采用大批量竞争性采购模式，Tranche 3跟踪层仅4份合同即达35亿美元。",
  "milestones": "2019年 SDA成立；2020年 SDA发布OISL标准；2022年12月 Tranche 0首批10颗卫星发射；2023年6月 Tranche 0第二批发射；2023年夏 Tranche 0在轨演示；2025年9月 Tranche 1首批21颗传输层卫星发射；2025年12月 Tranche 3跟踪层合同授予（35亿美元）；每偶数年9月计划新批次发射",
  "total_program_value": "Tranche 3跟踪层仅4份合同即35亿美元。传输层和跟踪层各批次累计合同金额[不确定]，但仅Tranche 1至Tranche 3的合同总额估计超过100亿美元。FY2026国会为Tranche 3传输层拨款5亿美元，为SDA整体拨款约12亿美元。",
  "osa_description": "PWSA是MOSA在太空域最大规模的应用。SDA通过自定义的NEBULA网络标准和OISL光学通信标准，建立了太空域的开放系统架构。所有供应商的卫星必须遵循相同的接口标准，实现多供应商、多批次卫星的互操作。这种架构使得：1）任何满足标准的供应商均可参与竞标；2）不同批次（Tranche）的卫星可互相通信；3）新能力可按'每两年一批次'的节奏快速插入；4）单颗卫星失效不影响整体网络（mesh网络自动路由）。SDA的MOSA策略本质上是将互联网的开放架构理念应用于太空军事通信网络。",
  "key_modular_subsystems": "1）光学通信终端（OCT）：标准化激光通信终端，所有卫星和地面/空中平台通用；2）传输层卫星平台：基于标准卫星总线，支持不同供应商制造；3）跟踪层红外传感器：模块化红外载荷，可独立于卫星平台升级；4）战场管理/指挥控制通信（BMC3）模块：星上边缘计算模块；5）Ka波段RF子系统：标准化上下行链路；6）Link 16战术数据链接口模块；7）地面段：操作中心、地面接入点（GEP）、云环境",
  "digital_engineering_integration": "SDA采用数字工程方法进行星座架构设计和仿真。通过模型化方法验证网络拓扑、链路预算和覆盖分析。多供应商之间的接口兼容性通过数字化验证工具确保。[不确定]SDA是否全面采用MBSE方法论未在公开资料中明确。",
  "cost_benefit_analysis": "SDA的采办模式本身就体现了MOSA的成本效益逻辑：通过标准化接口降低供应商门槛，通过批量采购降低单价，通过模块化设计降低升级成本。但根据GAO-25-106931，DOD政策不要求正式的MOSA成本效益分析。[不确定]SDA是否进行了正式的MOSA成本效益分析未确认。",
  "competition_effects": "MOSA架构极大促进了太空域供应商竞争。SDA通过NEBULA和OISL标准，使多家传统和新兴太空企业参与PWSA建设：Lockheed Martin、Northrop Grumman、L3Harris、York Space Systems、Rocket Lab、Umbra等。Tranche 3跟踪层4家供应商各获约8.75亿美元合同。Umbra等商业公司通过OISL标准集成，展示了MOSA对新兴供应商的开放效果。",
  "integration_challenges": "1）供应链问题：Tranche 0因供应链延迟从2022年9月推迟至12月发射；2）多供应商接口兼容性验证：不同供应商的OISL终端需要严格的互操作测试；3）在轨网络管理：数百颗卫星的mesh网络路由和管理复杂度高；4）地面段集成：需要与MDA、SSC等其他太空架构的地面系统互操作；5）国会对Space Force暂停Tranche 3资金的担忧引发稳定性问题。",
  "mosa_non_implementation_reasons": "不适用。PWSA是积极且大规模实施MOSA的项目。",
  "ip_data_rights_strategy": "SDA通过政府定义的开放标准（NEBULA、OISL）确保政府拥有关键接口标准的知识产权。供应商在卫星平台和载荷层面保有自身IP，但必须开放接口以符合SDA标准。[不确定]具体的技术数据权利条款在OTA合同中的安排未公开披露。",
  "peo_coordination": "SDA本身作为太空军直属单位，直接向太空军作战部长报告，具有独立于传统PEO结构的采办权限。SDA与MDA（导弹防御局）和SSC（太空系统司令部）在架构层面进行协调，共同构建国家太空防御架构。[不确定]SDA内部的MOSA跨项目/跨批次协调机制的具体细节未完全公开。",
  "gao_reports": "GAO-25-106931: DOD Needs Better Planning to Attain Benefits of Modular Open Systems Approaches (2025年1月) - https://www.gao.gov/assets/gao-25-106931.pdf（报告中Space Force Tranche 1 Tracking Layer被列为实施MOSA的项目）",
  "crs_reports": "[不确定]是否有专门针对SDA PWSA的CRS报告",
  "dod_directives": "DoDD 5000.01 国防采办系统; 10 USC 4401 MOSA法定要求; SDA NEBULA Standard v3.05; SDA OISL Standard 9100-0001-01",
  "contractor_documents": "SDA PWSA传输层概况（2024年5月）; SDA PWSA地面段概况（2024年10月）; SDA Tranche 1概况（2024年6月）",
  "ndaa_provisions": "2017 NDAA Sec 805 - 10 USC 4401; FY2026 NDAA为SDA Tranche 3传输层拨款5亿美元，为SDA整体拨款约12亿美元",
  "congressional_oversight": "国会积极监督SDA项目。FY2026拨款中，国会否决了Space Force暂停Tranche 3的提议，恢复并增加了约12亿美元资金。国会支持SDA的快速采办模式和MOSA架构策略。",
  "industry_feedback": "[不确定]行业对SDA NEBULA/OISL标准的正式反馈未公开。但多家商业太空公司（包括Umbra、Kepler等）积极申请集成SDA标准，表明行业对开放架构的接受度较高。",
  "allied_interoperability": "[不确定]PWSA是否计划与盟友太空架构互操作未在公开资料中明确。但基于标准IP协议栈的架构理论上有利于盟友集成。",
  "mosa_evolution_timeline": "2019年SDA成立 → 2020年发布OISL标准 → 2022年Tranche 0发射 → 2023年在轨演示 → 2024年NEBULA标准v3.03/v3.05发布 → 2025年Tranche 1发射 → 2025年Tranche 3合同授予 → 每两年持续迭代",
  "uncertain": [
    "total_program_value",
    "cost_benefit_analysis",
    "ip_data_rights_strategy",
    "digital_engineering_integration",
    "peo_coordination",
    "crs_reports",
    "industry_feedback",
    "allied_interoperability"
  ]
}