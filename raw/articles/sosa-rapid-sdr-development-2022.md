---
title: "SOSA's Rubber Is Meeting the Road in Rapid System Development"
source: https://militaryembedded.com/radar-ew/rf-and-microwave/sosas-rubber-is-meeting-the-road-in-rapid-system-development
authors: [John Orlando (Epiq Solutions), Travis Doll (Sciens Innovations)]
date: 2022-10-07
publication: Military Embedded Systems
type: article
tags: [SOSA, SDR, MORA, VICTORY, TSOA-ID, OpenVPX, rapid-development, interoperability]
---

# SOSA's Rubber Is Meeting the Road in Rapid System Development

**Authors:** John Orlando (Epiq Solutions), Travis Doll (Sciens Innovations)
**Publication:** Military Embedded Systems, October 7, 2022
**Source:** https://militaryembedded.com/radar-ew/rf-and-microwave/sosas-rubber-is-meeting-the-road-in-rapid-system-development

## 核心成果

使用SOSA对齐组件，在两周多一点的时间内创建了完整的软件定义无线电（SDR）解决方案用于TSOA-ID活动，与不使用明确定义开放标准开发的解决方案相比，**成本和进度减少高达10倍**。

## SOSA标准背景

- The Open Group的SOSA技术标准1.0于2021年9月发布
- 经过近3年美国国防部与100多家嵌入式硬件和软件制造商的协作
- 促进传感器组件的可移植性和重用，定义硬件、软件和接口标准
- RF和SDR载荷卡供应商还需符合MORA规范以确保VPX卡可被SOSA系统使用

## SOSA系统集成的关键环节

系统设计者考虑如何从外部世界命令和控制设备是拼图的关键一块。这种集成需要实现各种MORA和VICTORY接口，使其他组件能够：

- 发现硬件并与其"对话"
- 命令和控制
- 数据摄入和导出
- 健康和状态监控
- 确定其能力

## 硬件与软件协作模式

- 硬件供应商专注于SOSA技术标准定义的机械和电气要求
- 软件公司专注于所创建卡的接口要求
- 开放标准倡议使更多硬件和软件公司在开发过程中协作
- 工程师确信在硬件开发周期结束时，他们将知道完全集成卡到SOSA系统中需要什么

## TSOA-ID演示案例

### 合作方
- **Epiq Solutions**：嵌入式SDR卡供应商，SOSA对齐SDR硬件产品线
- **Sciens Innovations**：软件和固件开发团队，MORA对齐软件和固件

### 合作过程
- 两家公司通过SOSA社区相互了解多年
- 决定创建演示，展示Sciens的MORA软件层在Epiq Solutions硬件上的实现
- 目标：在即将举行的TSOA-ID现场活动中进行实时演示

### 技术实现
- 演示利用了Epiq Solutions作为嵌入式SDR卡供应商的能力
- 结合Sciens在DoD内实现MORA对齐软件和固件的声誉
- 创建并演示SDR产品并实时流式传输结果

## 开放标准的互操作性验证

互操作性验证可以以不同方式体现：

- 公司协作开发行业广泛使用的机制
- 在TSOA-ID等活动中进行物理演示和测试
- 硬件和软件开发者协作确保实现开放标准接口的时间和资源可以共享和适当分配

## 关键洞察

1. **速度优势**：SOSA标准将SDR系统开发从数月缩短到两周，证明开放标准在快速原型和部署中的价值
2. **成本效益**：10倍的成本和进度减少是MOSA经济可行性的直接证据
3. **生态协同**：SOSA社区促进了供应商之间的自然配对——硬件专家与软件专家互补
4. **MORA关键性**：RF载荷的SOSA集成离不开MORA合规，两者是互补标准
5. **TSOA-ID价值**：三军开放架构互操作性演示是验证标准实际效果的关键机制
