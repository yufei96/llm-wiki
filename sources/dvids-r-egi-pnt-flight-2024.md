---
title: "R-EGI PNT Systems Flight Demonstrations"
source_type: news_article
source_org: DVIDS (Defense Visual Information Distribution Service)
source_url: "https://www.dvidshub.net/news/497633/"
date: 2024-02
event_date: 2024-02-03
event_end_date: 2024-02-07
location: Centennial Airport, Colorado
downloaded: 2026-05-06
tags:
  - R-EGI
  - EGI-M
  - PNT
  - GPS-denied
  - MOSA
  - navigation
  - IS4S
  - AEVEX
  - Northrop-Grumman
  - flight-test
  - AFLCMC
related_pages:
  - "[[open-architecture-hierarchy]]"
  - "[[r-egi]]"
  - "[[egi-m]]"
  - "[[mosa]]"
  - "[[pnt-resilience]]"
  - "[[aevex-lynxvbn]]"
data_quality: high
---

# DVIDS — R-EGI PNT Systems Flight Demonstrations (2024)

## 核心内容

- **IS4S R-EGI** 系统在 Centennial Airport, Colorado 完成飞行演示（2024年2月3-7日）
- R-EGI 展示了 **MOSA（模块化开放系统架构）** 能力，成功集成 **AEVEX Aerospace LynxVBN 视觉导航系统**，实现"即插即用"功能
- 在模拟 **GPS拒止环境** 中，R-EGI 仅使用视觉导航数据和惯性测量单元（IMU）维持定位精度——概念验证成功
- **AEVEX LynxVBN** 作为第三方 PNT 传感器快速集成，符合 Alternative PNT 和 Assured PNT System Network 消息标准
- **Northrop Grumman EGI-M**（嵌入式 GPS/INS 现代化项目）执行了6次专用飞行，评估三种 EGI 变体：LN-300、LN-351、LN-251
- EGI-M 测试聚焦混合导航、纯惯性导航和 GPS 独立导航解算，首次集成 NAVWAR 混合导航保障（BNA）功能
- EGI-M 纯惯性解算超越项目定位误差规范
- 5/6 次飞行使用 M-code GPS，1次使用传统 C/A码

## 关键人员

| 姓名 | 职位 |
|------|------|
| Maj Bernard Mutz | R-EGI PM, AFLCMC/WNX Electronic Systems Directorate |
| Lt Col Juan Ramirez | NAVWAR Branch Materiel Leader |
| Capt Rajeem Moore | EGI-M PM, PNT Program Office |
| Lt Col Christopher Grover | PNT Program Office Materiel Leader |

## 关键合同方

| 公司 | 角色 |
|------|------|
| IS4S (Integrated Solutions for Systems) | R-EGI 系统开发 |
| AEVEX Aerospace | LynxVBN 视觉导航传感器 |
| Northrop Grumman | EGI-M (LN-300/LN-351/LN-251) |

## 数据质量评估

- **来源**: DVIDS 官方军事新闻发布，质量较高
- **限制**: 仅含新闻稿件，无技术细节数据（精度数值、飞行轨迹等）
- **注意**: 文章实际发布日期为 2025-05-12，事件发生在 2024-02

## 相关页面

- [[open-architecture-hierarchy]] — R-EGI 是 MOSA 在 PNT 领域的典型实现
- [[r-egi]] — IS4S 弹性嵌入式 GPS/INS 项目
- [[egi-m]] — Northrop Grumman 嵌入式 GPS/INS 现代化项目
- [[mosa]] — 模块化开放系统架构
- [[pnt-resilience]] — PNT 弹性技术
