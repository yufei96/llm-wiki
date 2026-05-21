---
title: "尼克·博顿 SOSA架构V1概述 WInnComm 2021"
created: 2026-05-18
updated: 2026-05-18
type: source
tags: [SOSA, WInnComm, OpenVPX, FACE, 模块化]
sources: [raw/papers/尼克-博顿-SOSA-WInnComm-2021.pdf, raw/articles/尼克-博顿-SOSA-WInnComm-2021.md]
author: "Nick Borton, SOSA Steering Committee Vice Chair (SRC Inc.)"
confidence: EXTRACTED
evidence: "直接从原始PDF提取"
---

# 尼克·博顿 SOSA架构V1概述 WInnComm 2021

## 摘要

SOSA联盟指导委员会副主席 Nick Borton 在 WInnComm 2021（2021年11月30日）上的演讲，系统介绍了SOSA V1.0参考架构的全貌。涵盖SOSA联盟的What/Why/Who/How、V1.0分类体系（Modules vs Infrastructure的职责划分）、传感器系统模块清单与数据流、软件运行时环境（FACE/容器/虚拟机）、插件卡物理接口规范、以及模块间交互绑定协议（MORA/OAS REST/DDS/ZMTP/AMQP/NVMe）。提供了SOSA V1.0的设计哲学——"提供工具箱而非单一方案，系统设计者按需选用SOSA组件"。

## 关键要点

1. **SOSA设计哲学**：SOSA是一套工具，系统设计师按需选用，系统不是"SOSA的"而是"用SOSA组件构建的"
2. **V1.0分类体系**：Module（功能行为，实现无关）+ Infrastructure（物理/协议接口，标准下选）
3. **传感器模块清单**：涵盖发射/接收、信号处理、分析利用、传输四大类共20+模块
4. **软件运行时环境**：三选一——FACE标准、OCI容器、OVF虚拟机
5. **交互绑定协议**：7种协议支持互换性/可升级性/可移植性/可复用
6. **物理接口**：MIL-DTL-38999连接器标准化，含以太网/RS422/发射保险等信号定义

## 模块清单

- **发射/接收**：2.3 Conditioner-Receiver-Exciter、2.4 Emitter/Collector
- **信号/目标处理**：3.1 Signal/Object Detector & Extractor、3.2 Signal/Object Characterizer、3.3 Image Pre-Processor、3.4 Tracker
- **分析/利用**：4.1 External Data Ingestor、4.2 Encoded Data Extractor、4.3 Situation Assessor、4.4 Impact Assessor & Responder、4.6 Storage/Retrieval Manager
- **传输**：5.1 Reporting Services
- **系统支撑服务**：6.1 Security Services、6.2 Encryptor/Decryptor、6.3 Guard/Cross-Domain、6.4 Network Subsystem、6.5 Calibration、6.6 Nav Data、6.7 Time & Frequency、6.8 Compressor/Decompressor、6.9 Host Platform Interface、6.10 Power
- **管理**：1.1 System Manager、1.2 Task Manager
