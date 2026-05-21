---
title: "R-EGI在军用C-12J测试飞机上的飞行演示（2025年2月）"
created: 2026-05-21
updated: 2026-05-21
tags: [R-EGI, EGI-M, C-12J, PNT, GPS拒止, 导航战, MOSA, IS4S, Northrop-Grumman, AFLCMC, 视觉导航, M-code]
confidence: EXTRACTED
evidence: "基于DVIDS 2025年5月12日飞行测试新闻稿深度提取"
type: source
---

# R-EGI在军用C-12J测试飞机上的飞行演示（2025年2月）

## 概述

2025年2月3日至7日，美国空军生命周期管理中心（AFLCMC）电子系统局在科罗拉多州Centennial机场完成了R-EGI（韧性嵌入式GPS/惯导）系统的飞行演示。此次测试由空军联合IS4S、AEVEX Aerospace和Northrop Grumman共同执行，重点验证了在模拟GPS拒止环境下的定位导航授时（PNT）能力和开放架构系统的可行性。

## 核心内容

### R-EGI系统演示

IS4S的R-EGI系统展示了其模块化开放系统架构（MOSA）的核心能力——通过"即插即用"方式成功集成了AEVEX Aerospace的LynxVBN视觉导航系统，并遵循替代PNT和确保PNT系统网络消息标准。

在模拟GPS拒止场景中，R-EGI仅依靠视觉导航数据和惯性测量单元（IMU）维持定位精度，验证了PNT韧性的概念验证能力。

> "在GPS拒止条件下实现精度，经过快速集成，真正彰显了R-EGI开放架构在PNT韧性革命中的潜力。" — Maj. Bernard Mutz, R-EGI项目经理

### EGI-M并行测试

Northrop Grumman的EGI-M（嵌入式GPS/惯导现代化）项目执行了6次专项飞行，评估三种EGI变体（LN-300, LN-351, LN-251参考单元）的性能。测试聚焦于EGI-M的混合导航、自由惯性和GPS-Only导航方案，并首次集成了导航战（NAVWAR）混合导航保证（BNA）功能。

- 6次飞行中5次使用M码GPS，1次使用传统C/A码
- EGI-M自由惯性方案超越了项目定位误差规格

> "自由惯性方案超越定位误差规格是一项重大成就，展示了EGI-M在挑战性环境中的强劲性能。" — Capt. Rajeem Moore, EGI-M项目经理

### 开放架构的意义

Lt. Col. Juan Ramirez（NAVWAR分部装备负责人）强调了快速而成本有效的第三方PNT集成的重要性，并鼓励进一步参与开源PNT社区。Lt. Col. Christopher Grover（PNT项目办公室装备负责人）总结称：

> "这些飞行演示体现了为作战人员交付尖端PNT能力所必需的协作精神。R-EGI和EGI-M的成功展示了行业合作在满足关键任务需求方面的切实效益。"

## 笔记

此次联合飞行测试展示了美军PNT现代化的两条并行路径：R-EGI代表"开放架构+第三方集成"路线，EGI-M代表"传统厂商升级"路线。R-EGI通过MOSA实现视觉导航系统的即插即用集成，验证了在GPS拒止条件下维持导航精度的可行性——这对未来对抗性环境中的作战至关重要。M码GPS在5/6次飞行中的使用也标志着军用GPS信号从开发测试向作战应用的过渡。IS4S作为非传统国防承包商在R-EGI项目中的核心角色体现了MOSA降低准入壁垒的目标。

## 来源

- DVIDS Story ID 497633, "R-EGI PNT Systems Flight Demonstrations," May 12, 2025
- 原始文件：raw/articles/DVIDS-R-EGI导航飞行测试2024.md, raw/articles/IS4S-R-EGI C12J飞行测试.md
