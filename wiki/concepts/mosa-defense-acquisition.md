---
title: "Modular Open Systems Approach (MOSA)"
created: 2026-04-05
updated: 2026-04-05
tags: [mosa, defense-acquisition, modularity]
sources: [raw/mosa-us-defense-acquisition-shah-2021.pdf]
---

# Modular Open Systems Approach (MOSA)

## Definition

A DoD acquisition and design strategy mandating **modular architecture** with **openly published interfaces**. Mandated by **Better Buying Power 3.0** directive (2015) across all Major Defense Acquisition Programs (MDAPs).

Core purpose:
- Prevent **vendor lock-in** (single-provider dependency)
- Support affordable capability evolution
- Encourage competition and innovation
- Reduce lifecycle costs

## The Problem

**MDAP performance crisis**:
- 60%+ of programs over budget or behind schedule
- Pre-2010 programs: **62.4% cost growth** ($542.1B total), **35-month average delays**
- Post-2010 programs: 2.1% cost growth ($5.3B), 9-month delays (but many still in early phases)
- Tech obsolescence costs DoD **$750M/year**
- **$600B** lost globally to cyber threats (~1% of GDP)

**Vendor lock**: Prime contractors hold IP rights, preventing the DoD from switching to alternate service providers. Systems become un-upgradable or too expensive to modify.

## MOSA Principles

1. **Modularity**: Divide systems into discrete, interchangeable components
2. **Open interfaces**: Published, non-proprietary interface specifications
3. **Competitive procurement**: Any qualified vendor can provide components
4. **Data rights**: Government retains rights to interface definitions
5. **Platform transformability**: Systems usable beyond original scope/lifespan

## Key Standards

- **FACE™** (Future Airborne Capability Environment): Avionics open architecture. 70 orgs, 900 contributors. Supported by 20+ procurements. Five segments: OS, I/O Services, Platform-Specific, Transport, Portable Components
- **OMS** (Open Mission Systems): Sensor/payload interoperability. Examples: Automatic Target Recognition integration, Common Operating Picture sharing
- **UCS** (Unmanned Systems Command and Control): Navy LCS, Army Joint MR Rotorcraft, Air Force Global Hawk GCS
- **VICTORY**: Vehicular C4ISR/EW interoperability (Army)
- **SOSA**: Sensor Open Systems Architecture (Army)
- **CMOSS**: C4ISR Open Suite of Standards
- **MORA**: Modular Open Radio Frequency Architecture
- **HOST**: Hardware Open Systems Technologies
- **ISO/IEC/IEEE 15288**: Systems engineering lifecycle standard (adopted by DoD)

## Evidence Status (Shah 2021 Findings)

### 6 Hypotheses Tested

| Hypothesis | Result |
|-----------|--------|
| H1: MOSA → measurable cost/schedule improvement | ❌ **Not Supported** — MDAP data cannot isolate MOSA effect |
| H2: Programs claim MOSA success | ✅ Supported — Global Hawk, MQ-9, Apache, F-22, B-52, etc. |
| H3: US military requires MOSA | ✅ Supported — Army, Navy, Air Force programs exist |
| H4: Non-US governments show MOSA adoption | ✅ Supported — UK MoD (GVA), Australia, Canada |
| H5: Commercial sector adopts MOSA | ✅ Supported — Airbus HForce helicopters |
| H6: Commercial sector success with MOSA | ✅ Supported — H125M/H145M/H225M military conversion |

### Why H1 Failed to Support
- Defense programs are multiyear with too many confounding variables
- No standardized MOSA-specific metrics exist
- Data granularity insufficient (platform vs. subsystem vs. COTS level)
- **Worthington (2012)**: "Just as it is impractical to separate the cost savings attributable to OSA from those attributable to COTS, it is equally impossible to separate cost savings attributable to good systems engineering and effective program management."

## Successful MOSA Programs

| Branch | Programs |
|--------|----------|
| **Army** | Ground Common Infrastructure, Future Vertical Lift architectures, Improved Turbine Engine Program, Modular Active Protection Systems |
| **Navy** | Littoral Combat Ship, Virginia Class Submarine, CANES, P-8A Maritime Aircraft, Mobile User Objective System |
| **Air Force/Aviation** | UCS, OMS, FACE Consortium (70+ orgs), Improved Data Modem OSA |
| **Global** | UK GVA (Army vehicles), Canada CF-18 Hornet, Australian DoD |
| **Commercial** | Airbus HForce (H125M/H145M/H225M helicopters) |

## Research Limitations (per Shah)
- Modularity and openness defined too broadly for consistent measurement
- DoD programmatic information restricted for private citizens
- Multiple confounding variables in multi-year acquisition programs
- No MOSA-specific ROI study completed to date
- No standard "what to measure, how, with what metrics" framework

## Recommendations (from Ch5)
- Develop modular assessment tools and standardized metrics
- Compare technical vs. business approach effectiveness
- Determine where in acquisition lifecycle MOSA has greatest impact (DoDI 5000.02)
- Quantify modularity (hardware/software/platforms) against real dollar value
- Establish security and safety guidelines for open systems
- MOSA-specific training for all stakeholders (not just documentation)
- Pass-fail criteria for vendors and military alignment

## Android Analogy
Shah draws parallel to Android's open-source success model: initial skepticism → ecosystem explosion. Defense should shift from closed hardware to open software architectures enabling real-time upgrades.

## Key Quote (Ch5.7 Conclusion)
> "MOSA is not the end result but rather an approach that can enable innovation and is one of the many procurement strategies that can help with the DoD acquisition problem."

> "What to measure, how to measure, and with what metrics to measure remain the key challenge."

## Related
- [[vendor-lock-in]]
- [[defense-acquisition-overrun-trends]]
- [[face-technical-standard]]
- [[open-mission-systems]]
- [[better-buying-power-3]]
- [[modular-architecture-patterns]]
