---
title: "NDIA MOSA White Paper — Top 10 Recommendations"
date: 2026-04-05
type: source_summary
source: raw/papers/ndia-mosa-white-paper-2019.pdf
author: "NDIA SE Division - Architecture Committee (Steve Thelin, Chair)"
tags: [MOSA, NDIA, recommendations, systems-engineering, policy]
---

# NDIA MOSA White Paper Summary (2019, Rev. D, October)

## Document Meta

- **Author**: NDIA Systems Engineering Division — Architecture Committee, chaired by Steve Thelin
- **Membership**: 38 Industry, 14 Government, 5 Academia
- **Key focus on MOSA since 2017**
- **16 pages** — presentation format, summarizing white paper recommendations

## Context

Government and industry need to work together to define MOSA implementation that delivers:
- Increased competition
- Reduced costs
- New synergistic capabilities across product lines
- **MOSA is the foundation** that Mission Engineering, Digital Engineering, and System Security Engineering can build on

## Audience

| Stakeholder | Need |
|-------------|------|
| Government | Guidance for executing contracts, producing SoS architectures |
| Prime Contractors | Investment strategy, subcontractor impacts, IP ramifications |
| Systems Engineers | MOSA requirements, RFP guidance, evaluation criteria |
| NDIA Architecture Team | Planning tool for policy/guidance changes, standards development |

## Top 10 Recommendations

### 1. Develop MOSA Strategy Early in Acquisition Process
- Define MOSA objectives and partitioning **above the planned procurement system level**
- Consider: adjacent systems, mission engineering interfaces, missing standards
- Demonstrate financial and performance justification for planned partitioning
- Provide strategy early to allow contractors to plan technology investments

### 2. Define MOSA Implementation Approach (Acquirer ↔ Supplier Roles)
- Define level of MOSA, planned partitioning, functional analysis, interfaces to be controlled/open
- Define MOSA objective per level: adaptability, sustainability, upgradeability, competition
- **Consider incentives** for MOSA implementation to facilitate acceptance
- **OSD must define Technical Data Rights and IP policy** (those impacted by MOSA)
- Develop MOSA architecture with governance of planned open interfaces
- Plan for design disclosure to enable second sourcing and competition
- Identify common standards or release ICDs and other open interface documents

### 3. Define Interfaces at MIL-STD-881D Taxonomy Levels
- **MIL-STD-881D** provides consistent common language for system hierarchy
- Eliminate ambiguous terms like "major component" and "platform level"
- Consider **MIL-STD-196F/G** nomenclature: System → Subsystems → Centers → Centrals → Sets → Groups → Units
- Define integration level (manual, automated) between platforms/systems/subsystems at all SoS taxonomy levels

### 4. Apply MOSA in Software Architectures
- Apply MOSA to software abstraction/reification levels, including SoS level
- Develop **software taxonomy similar to MIL-STD-881D** to guide software MOSA
- Define framework/lexicon for design-level partitioning at various design stages
- Develop **common reference architecture for data model** at varying fidelity levels
- Define modular software data rights at appropriate abstraction levels (OS vs microservices)

### 5. Implement MOSA as Part of Digital Engineering Strategy
- Models can define and communicate MOSA architectures and partitioning
- Develop common MOSA framework/lexicon for system functions at multiple architecture levels
- Government must articulate SoS architecture responsibility; flow down to contractors
- Standards, common modules, and interfaces should be **categorized by taxonomy level and technology state** (old, latest, emerging)

### 6. Incorporate Cybersecurity Strategy at Initial Design
- **System Security Engineering up-front** as part of development process
- Understand effects of modularity and open interfaces on cybersecurity
- Identify MOSA-induced threat vectors and associated risks
- Develop security architecture early; define risk mitigation

### 7. DOD + Industry Define MOSA Evaluation & Certification
- **Define MOSA metrics for various domains and SoS levels**
- Establish evaluation process and criteria for proposals
- Define what MOSA compliant means; develop standard certification objectives
- **Emphasize measurement methodology over structure** — shipbuilding metrics may not suit aerospace

### 8. Develop Enablers with Investment for Culture Change
- **Make MOSA a requirement — not an option — for all procurements**
- **Open Systems Management Plan (OSMP) as common as a Systems Engineering Management Plan (SEMP)**
- MOSA incorporated into technical/management reviews
- MOSA strategy defined at all SoS levels
- Include MOSA as a primary consideration in **Value Engineering**
- Government coordinate across services and weapon systems
- Build MOSA incentives into contracts and award fee structures
- **Embed MOSA in System/Mission/Digital Engineering and SoS processes**

### 9. Create Library of MOSA Certified Systems and Interfaces
- Maintain reusable archive of certified MOSA systems and interface types
- Include system partitioning architecture + ICDs + standards for open interfaces
- Include modularity objectives, how achieved, why important
- **Accelerate MOSA adoption, speed development, increase competition**

### 10. Define Method to Compare Standards and Interfaces
- Develop common method to talk about and compare standards
- Critical for **gap analysis**
- Identify tool for PMs to determine appropriate standards
- Map standards/interfaces to MIL-STD-881D

## Summary: Key Benefits vs Key Enablers

| Key Benefits | Key Enablers |
|-------------|-------------|
| Weapon system interoperability & scalability | Development of key standards and interfaces |
| Technology refresh & new technology insertion | Detailed service implementation plans + consistent application |
| Reduced cost | Formal, standard way of assessing MOSA |
| Reduced development cycle for new capabilities | Transition to MOSA culture and environment |
| Increased competition | |
| Improved sustainment & life cycle costs | |

## Comparison to Shah Thesis Findings

| NDIA Recommendation | Shah Thesis Evidence |
|-------------------|---------------------|
| Make MOSA a requirement for all procurements | ✅ Army, Navy, Air Force all mandated it (H3 supported) |
| Define MOSA metrics | ❌ Shah found no standardized metrics exist (H1 not supported) |
| MOSA incentives in contracts | Shah noted lack of quantitative evidence prevents meaningful incentives |
| Create library of certified MOSA systems | Not yet done — major gap identified in thesis |
| Evaluate MOSA at proposal stage | Shah found no MOSA evaluation criteria in MDAP data |

The NDIA recommendations and Shah thesis findings **align perfectly** — same gaps, same needs, different perspectives (thesis = retrospective analysis, NDIA = prescriptive recommendations).

## Related Concepts
- [[mosa-defense-acquisition]]
- [[adaptive-acquisition-framework]]
- [[open-systems-management-plan]]
- [[mil-std-881d]]
- [[mosa-certification]]

## Related Entities
- [[national-defense-industrial-association-ndia]]
- [[steve-thelin]]

---
*16 pages, NDIA SE Division - Architecture Committee, Rev. D, October 2019*
