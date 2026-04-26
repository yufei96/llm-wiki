---
title: "持久高能激光（E-HEL）定向能武器MOSA"
source: "深度调研JSON结果"
date: 2026-04-26
type: research_data
---

# 持久高能激光（E-HEL）定向能武器MOSA

## 结构化调研数据

{
  "item_type": "case_study",
  "project_name": "持久高能激光（E-HEL）定向能武器MOSA",
  "service_branch": "美国陆军",
  "start_year": "2024",
  "prime_contractor": "HII Mission Technologies（2025年3月获得开发合同）",
  "program_status": "原型开发阶段。陆军快速能力与关键技术办公室（RCCTO）定向能项目办公室（DEPO）于2024年7月发布特别通知，2025年11月发布生产需求信息征询书（RFI），计划在FY26 Q2或之后启动竞争性源选择，生产最多20套E-HEL系统。2025年3月HII获得高能激光武器系统原型开发合同。",
  "mosa_standards_used": "基于DEWS MOSA参考架构（Directed Energy Weapon System MOSA Reference Architecture）版本1.0使用指南（2022年6月）。该参考架构由MITRE公司开发，由国防部副部长（研究与工程）办公室（OUSD(R&E)）委托编制，适用于所有新的定向能系统。",
  "mosa_implementation_status": "实施中（Implementing）。E-HEL从设计之初即采用MOSA，基于DEWS MOSA参考架构进行开发。所有E-HEL子系统接口将附带政府目的权利（GPR）。",
  "modular_architecture_description": "E-HEL采用基于DEWS MOSA参考架构的模块化开放系统设计。系统采用'灰盒'（gray box）概念——架构定义模块和接口的功能（做什么），而非实现方式（怎么做）。E-HEL可配置为'托盘化'（palletized）构型或集成到标准陆军联合轻型战术车辆（JLTV）上，支持半固定和机动作战。系统可使用标准装卸设备（叉车）进行搬运，满足C-17空运要求。",
  "interface_specifications": "E-HEL所有子系统接口均附带政府目的权利（GPR）。工业界可使用政府提供的接口控制文件（ICD）或提供具有GPR的行业ICD。接口基于DEWS MOSA参考架构中定义的标准接口规范。",
  "compliance_certification": "[不确定] E-HEL要求符合DEWS MOSA参考架构v1.0，但是否需要通过正式的合规认证流程未明确。DEWS参考架构包含合规认证（Conformance Certification）作为关键使能要素。",
  "brownfield_vs_greenfield": "新研（Greenfield）。E-HEL为陆军首个定向能武器系统采购项目（program of record），基于经验证的激光和光束控制技术进行全新开发。",
  "acquisition_pathway": "快速原型（Middle Tier of Acquisition / MTA），由RCCTO管理",
  "contract_type": "[不确定] 2025年3月HII获得原型开发合同，具体合同类型（如OTA其他交易协议或传统合同）未公开披露。",
  "milestones": [
    "2024年7月：RCCTO发布E-HEL特别通知",
    "2025年3月：HII Mission Technologies获得高能激光原型开发合同",
    "2025年11月：RCCTO/DEPO发布E-HEL生产RFI，寻求最多20套系统的生产能力",
    "计划FY26 Q2或之后：启动竞争性源选择"
  ],
  "total_program_value": "[不确定] 项目总价值未公开披露。计划生产最多20套E-HEL系统。",
  "osa_description": "E-HEL的开放系统架构基于DEWS MOSA参考架构，该架构由MITRE公司开发，于2022年7月发布。DEWS参考架构具有以下特点：(1) 服务和领域无关，适用于所有定向能系统；(2) 基于MOSA原则，利用开放/商业标准和开放系统架构；(3) 非专有、供应商无关的模块和接口定义；(4) 保护供应商知识产权，模块内采用平衡的数据权利；(5) 大小企业均为架构开发和治理的全面合作伙伴；(6) 仅在必要时创建新标准。架构愿景是定向能武器项目利用广泛适用的参考架构，基于MOSA原则，加速创新、加快开发、增加标准要素的重用。",
  "key_modular_subsystems": [
    "激光源模块（经验证的激光技术）",
    "光束控制/定向模块",
    "目标探测与跟踪模块（支持'蓝天'和杂乱环境中的Group 1-3 UAS跟踪）",
    "电源与热管理模块",
    "指挥控制与通信模块（接受外部前沿区域防空（FAAD）系统的目标指示）",
    "平台适配模块（支持托盘化构型或JLTV集成）"
  ],
  "digital_engineering_integration": "[不确定] DEWS MOSA参考架构强调加速创新和加快交付，可能涉及数字工程方法，但E-HEL项目具体的MBSE/数字孪生集成情况未公开披露。",
  "cost_benefit_analysis": "[不确定] 根据GAO-25-106931报告，国防部项目普遍未进行正式的MOSA成本效益分析。E-HEL作为快速原型项目，可能未进行正式的成本效益分析，但MOSA的采用预计将降低全寿命周期维护成本并加速技术插入。",
  "competition_effects": "E-HEL的MOSA设计明确旨在促进供应商竞争。RFI要求基于DEWS MOSA参考架构，所有接口具有GPR，这使得多个供应商可以参与子系统级别的竞争。DEWS参考架构的'供应商无关'设计理念允许政府利用多个工业合作伙伴，支持大小企业全面参与。",
  "integration_challenges": "[不确定] 定向能武器系统的MOSA集成面临独特挑战：激光源与光束控制系统的精确对准、高功率电源与热管理系统的集成、以及在保持MOSA模块化的同时满足严格的性能和尺寸重量功率（SWaP）要求。",
  "mosa_non_implementation_reasons": "不适用。E-HEL从设计之初即采用MOSA。",
  "ip_data_rights_strategy": "E-HEL要求所有子系统接口附带政府目的权利（GPR）。工业界可选择使用政府提供的接口控制文件（ICD）或提供具有GPR的行业ICD。DEWS MOSA参考架构明确要求'保护供应商知识产权，在模块内采用平衡的数据权利'，这意味着模块内部实现可保留专有权利，但接口层面确保政府拥有足够的数据权利。",
  "peo_coordination": "[不确定] E-HEL由RCCTO定向能项目办公室（DEPO）管理。RCCTO作为陆军的快速能力采办机构，与传统PEO体系有所不同。具体的PEO级MOSA协调机制未公开。",
  "gao_reports": [],
  "crs_reports": [],
  "dod_directives": [
    "DEWS MOSA参考架构版本1.0使用指南（2022年6月）：由MITRE公司开发，OUSD(R&E)委托，适用于所有新的定向能系统",
    "DoDD 5000.01（2022年7月）：国防采办系统",
    "DoD MOSA实施指南手册（2025年2月）"
  ],
  "contractor_documents": [
    "MITRE DEWS MOSA参考架构：https://apps.dtic.mil/sti/trecms/pdf/AD1214114.pdf",
    "DAU演示：'Let's Be Modular and Open – Common Architecture for Directed Energy Weapons Systems'（2022年10月）",
    "HII合同公告：https://hii.com/news/hii-is-awarded-contract-to-develop-high-energy-laser-weapon-system-for-the-us-army"
  ],
  "ndaa_provisions": [
    "2017 NDAA Section 805（10 USC 4401）：要求MDAP实施MOSA",
    "2020 NDAA Section 840：要求军种发布MOSA实施指南",
    "2021 NDAA Section 804：扩展MOSA要求至所有采购项目"
  ],
  "congressional_oversight": "[不确定] 定向能武器是国会关注的重点领域，E-HEL作为陆军首个定向能武器采购项目可能受到持续的国会监督。",
  "industry_feedback": "[不确定] E-HEL RFI征求工业界意见，表明政府重视行业反馈。DEWS MOSA参考架构的开发过程中，大小企业均为'架构开发和治理的全面合作伙伴'。",
  "allied_interoperability": "[不确定] DEWS MOSA参考架构的'服务和领域无关'特性理论上支持盟友互操作性，但E-HEL的具体盟友互操作性安排未公开披露。",
  "mosa_evolution_timeline": "[不确定] DEWS MOSA参考架构于2022年7月发布，E-HEL于2024年开始基于该架构开发。DEWS参考架构计划持续演进以适应新的定向能技术。",
  "uncertain": [
    "compliance_certification",
    "contract_type",
    "total_program_value",
    "digital_engineering_integration",
    "cost_benefit_analysis",
    "integration_challenges",
    "peo_coordination",
    "congressional_oversight",
    "industry_feedback",
    "allied_interoperability",
    "mosa_evolution_timeline"
  ]
}