---
title: "[PDF] Modular Open Systems Approach"
source_url: "https://www.ndia.org/-/media/sites/ndia/divisions/systems-engineering/se-monthly-meetings/division-papers/ndia-mosa-white-paper-final-release--ndia-architecture-committee--2020.pdf"
downloaded: 2026-04-26
---

# Modular Open Systems Approach (MOSA) - NDIA White Paper Summary

## Overview
**Document:** NDIA Systems Engineering Architecture Committee White Paper (July 1, 2020)  
**Purpose:** Provide practical guidance for implementing MOSA in defense acquisitions, balancing technical and business considerations for both acquirers (DoD) and suppliers (industry).  
**Core Definition:**  
> "MOSA is an integrated business and technical strategy to achieve competitive and affordable acquisition and sustainment over the system life cycle."

**Primary Driver:** Congressional mandate (2017 NDAA) requiring MOSA in major defense acquisition programs (MDAPs) receiving Milestone A/B approval after January 1, 2019.

## Key Concepts
- **Modular Design:** Systems partitioned into discrete, self-contained units with high internal cohesion and loose coupling between modules.
- **Open Interfaces:** Use of widely supported, consensus-based standards where available and suitable.
- **Business Strategy:** Enables competition, innovation, and interoperability through defined interfaces and data rights.
- **Not "One Size Fits All":** MOSA implementation varies by system tier (Joint Force, platform, subsystem, software) and objectives (e.g., production efficiency, technology refresh, competition).

## Stakeholder Perspectives

### Acquirer (DoD) Objectives & Concerns
**Benefits:**
- Increased interoperability and innovation
- Enhanced competition and reduced costs
- Faster technology refresh and capability delivery
- Simplified acquisition process

**Key Concerns:**
- Need for early definition of MOSA strategy and objectives in acquisition
- Importance of clear IP/data rights strategy
- Risk of "bolt-on" MOSA implementations if not designed in from start
- Need for investment in reference architectures and standards

### Supplier (Industry) Objectives & Concerns
**Benefits:**
- More competitive products and faster time-to-market
- Increased market opportunities through interoperability
- Structured upgrade paths and longer product lifespans
- Foundation for commonality across product lines

**Key Concerns:**
- Need for early MOSA strategy definition to plan investments
- Protection of intellectual property (IP) within modular "gray boxes"
- Clear evaluation criteria for MOSA compliance
- Cybersecurity integration from initial design

## Implementation Considerations

### Architecting for Modularity
- **MIL-STD-881D Taxonomy:** Provides common language for system hierarchy (platforms, systems, subsystems, components)
- **Three Grouping Concept:**
  1. **Group 1 (Joint Force/Mission Tier):** Platform-to-platform interfaces, Mission Engineering focus
  2. **Group 2 (System Acquisition Tier):** Platform/system/component interfaces, primary acquisition focus
  3. **Group 3 (Software):** Unique requirements for software decomposition and interfaces

### Software Considerations
- Software benefits significantly from MOSA ("Plug & Play" model)
- Need for software architectural lexicon and reference architectures
- Software modularity enables IP protection within "gray boxes"

### Cybersecurity Integration
- Must be incorporated at initial design, not bolted on later
- Open interfaces can increase cyber risk if not addressed early
- Requires up-front system security analysis and risk mitigation

## MOSA Evaluation

### Measurement Framework
**Technical Openness Values (Table 5-1):**
| Value | Criteria |
|-------|----------|
| 3 | Commercial or DoD Standard |
| 2 | Fully disclosed with well-defined documentation |
| 1 | Proprietary interface with good documentation |
| 0 | Undisclosed Proprietary Interface |

**Key Principle:** Measurement methodology should map to MOSA objectives; metrics may vary by domain (aerospace vs. shipbuilding).

## 10 NDIA Recommendations

1. **Develop MOSA strategy early** in acquisition process (before RFP)
2. **Define MOSA implementation approach** with clear acquirer/supplier roles
3. **Define interfaces using MIL-STD-881D taxonomy** and leverage existing Open System Architectures
4. **Apply MOSA in software architectures** at appropriate abstraction levels
5. **Implement MOSA as part of Digital Engineering strategy**
6. **Incorporate cybersecurity strategy** at initial design
7. **DoD and industry collaborate** to define MOSA evaluation methods
8. **Develop enablers for culture change** with appropriate investment
9. **Create Library of MOSA Systems and Interfaces**
10. **Define means for comparing/specifying standards** in MOSA-enabled environment

## Legislative Context

### Key Mandates (10 U.S.C. §§ 2446a-c):
- **§ 2446a:** MDAPs must use MOSA to maximum extent practicable after Jan 1, 2019
- **§ 2446b:** Program capability documents must address MOSA; acquisition strategy must describe MOSA approach
- **§ 2446c:** Military departments must coordinate on interface standards and ensure MOSA support resources

### DoD 5000 Mandates:
- Program managers responsible for evaluating and implementing MOSA where feasible

[... summary truncated for context management ...]