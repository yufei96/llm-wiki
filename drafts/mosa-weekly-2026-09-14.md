# MOSA/数字工程周报 2026-09-14

时间窗：2026-09-07 至 2026-09-13（北京时间 CST）

## 一、本期要点

- 本周政策/GAO/DOT&E 类无窗口内新发布，属劳动节后常规周；情报重心落在**开放标准互操作落地**与**模块化软硬件产品化**。
- 时间敏感网络（TSN）为本周最强技术信号：Curtiss-Wright 撰文指出 IEEE 802.1DP 航空航天 Profile（2025-11 发布）补齐互操作最后一环，TSN 正从研究实验室进入平台系统集成实验室；其 Profile 收敛路径被明确类比为 SOSA / VITA 65 之于 VITA 46。
- 软件保障侧：RunSafe Security 发布 Operational Software Assurance 平台，对已部署二进制与固件做运行时保护，无需改源码或等补丁；技术源自 DARPA 资助研究，经 DoW Iron Bank 软件仓库向国防用户提供。
- 硬件侧：Vicor 的 VITA 62 / SOSA 对齐电源入选 Military Embedded「本周产品」，面向 3U/6U OpenVPX 系统。
- 军种动态以反无人机与模块化传感集成为主：L3Harris VAMPIRE 获美海军选用；Rheinmetall Mission Master SP 两栖套件获 USMC 订单；MESA 雷达与 KONGSBERG 反无人机武器站集成。
- 中国侧：中国汽车工程学会联合智能绿色车辆与交通全国重点实验室北京亦庄研究基地，于 9 月 11 日举办「车路云一体化关键技术」专题培训，覆盖顶层架构、协同多传感器感知融合、多路口连续绿波通行与商业化落地案例。

## 二、本期条目

### 技术标准与开放架构

2026-09-10 | TSN 时间敏感网络从研究走向平台集成：IEEE 802.1DP 航空航天 Profile（2025-11 发布）补齐互操作最后一环，业界开始演示端到端确定性 TSN，供系统集成商把 TSN 从研究实验室带入平台系统集成实验室；TSN Profile 收敛路径被类比为 SOSA/VITA 65 之于 VITA 46。TSN 是 IEEE 802.1 系列能力集合（Qav/Qbv/Qbu/CB/Qci，多已并入 802.1Q-2022），802.1DP 面向军用固定翼/旋翼、无人平台与卫星网络
https://militaryembedded.com/avionics/computers/time-sensitive-networking-its-about-time

2026-09-08 | RunSafe Security 发布 Operational Software Assurance（OSA）平台：分析已部署编译软件与固件的漏洞与依赖、判定可达性，并在运行时施加保护，无需修改源码或等待补丁；面向长期部署的国防系统、关键基础设施、车辆与工业设备；技术源自 DARPA 资助研究，已通过 DoW Iron Bank 软件仓库向国防用户提供
https://militaryembedded.com/avionics/software/runtime-software-protection-targeting-fielded-defense-systems-unveiled-by-runsafe-security

2026-09-08 | Vicor VITA 62 电源入选「本周产品」：COTS 电源，面向 3U/6U OpenVPX 系统，服务机载雷达与自主平台；VITA 62 与 SOSA 对齐电源支持工厂可配置输出电压组合，并定义并联均流接口，是开放架构标准可扩展性的基础一环
https://militaryembedded.com/unmanned/power-electronics/product-of-the-week-vicors-vita-62-power-supply

2026-09-10 | 客座博客：在快速演进环境中为技术「面向未来」——讨论模块化/开放方法如何支撑长期能力演进
https://militaryembedded.com/ai/big-data/guest-blog-future-proofing-technology-in-a-rapidly-evolving-environment

### 军种动态

2026-09-09 | L3Harris 获美海军选用交付 VAMPIRE 反无人机系统（C-UxS），针对无人机与遥控平台防御；公司称正为海军近海作战与海上环境适配该系统；同时向美陆军供货。其 Wraith Shield 软件以电台为传感器探测与反制小型无人机，可与 VAMPIRE、Drone Guardian 组合成分层反无人机架构
https://militaryembedded.com/unmanned/counter-uas/counter-drone-systems-to-be-delivered-to-us-navy-by-l3harris

2026-09-10 | Rheinmetall Mission Master SP 自主地面车辆配两栖套件获美国海军陆战队订单
https://militaryembedded.com/unmanned/payloads/autonomous-ground-vehicles-with-amphibious-kits-ordered-for-us-marine-corps

2026-09-10 | MESA 雷达与 KONGSBERG 反无人机武器站完成集成
https://militaryembedded.com/unmanned/counter-uas/mesa-radar-integrated-with-kongsberg-counter-uas-weapon-stations

2026-09-10 | 深度报道：从地面到轨道——重构建防空反导雷达以应对饱和攻击
https://militaryembedded.com/radar-ew/sensors/ground-to-orbit-rebuilding-air-and-missile-defense-radar-for-a-saturation-fight

2026-09-10 | 诺格 155mm 抗干扰精确制导套件进入量产
https://militaryembedded.com/comms/gps/anti-jamming-precision-guidance-kits-from-northrop-grumman-to-enter-production-for-155-mm-artillery

2026-09-09 | 无人货运直升机完成海上补给作业演示
https://militaryembedded.com/unmanned/test/uncrewed-cargo-helicopter-demonstrates-offshore-resupply-operations

2026-09-09 | 意大利空军订购 MQ-9A Block 5 遥控驾驶飞机
https://militaryembedded.com/unmanned/isr/mq-9a-block-5-remotely-piloted-aircraft-ordered-by-italian-air-force

2026-09-08 | 英国新太空战略为卫星通信与空间监视提供资金
https://militaryembedded.com/comms/satellites/satellite-communications-space-surveillance-funded-in-new-uk-space-strategy

2026-09-08 | 英国冬季援乌一揽子计划包含「爱国者」导弹与无人机
https://militaryembedded.com/unmanned/payloads/patriot-missiles-drones-included-in-uk-winter-defense-package-for-ukraine

2026-09-08 | 英国陆军演习中集成 LVC（实况-虚拟-构造）训练系统
https://militaryembedded.com/avionics/displays/live-virtual-constructive-training-systems-integrated-in-british-army-exercise

### 中国开放架构动态

2026-09-11 | 中国汽车工程学会联合智能绿色车辆与交通全国重点实验室北京亦庄研究基地举办「车路云一体化关键技术」专题培训（北京经开区），内容含车路云一体化顶层架构解读、车路协同多传感器感知与数据融合、协同决策规划与多路口连续绿波通行、车路协同商业化落地与试点城市建设案例
https://www.sae-china.org/news/notices/202608/7416.html

## 三、监控列表更新

检查日期统一更新为 2026-09-14，7 项均无状态变更（无新触发入库条件）。

## 四、近期峰会日历

2026-09-22 至 09-24 | MOSA Industry & Government Summit & Expo，马里兰 National Harbor（含三军 MOSA 优先级简报、数字工程与模块化验证专题）
https://events.techconnect.org/MOSA_2026

2026-10-21 至 10-23 | 2026 世界智能网联汽车大会，北京亦庄北人亦创国际会展中心
