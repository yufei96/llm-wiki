---
created: 2026-04-06
updated: 2026-04-06
tags: [MOSA, defense-acquisition, modularity, systems-engineering, DoD]
sources: 12 raw files
---

# Modular Open Systems Approach (MOSA) in Defense Acquisition

## Summary [coverage: high]

**MOSA (Modular Open Systems Approach)** is a United States Department of Defense acquisition and system design strategy mandated since 2015 under the Better Buying Power 3.0 initiative. It requires weapon systems to be designed with **modular architecture** and **openly published standardized interfaces**, with the goal of preventing vendor lock-in, enabling affordable technology insertion, increasing competition, and reducing lifecycle costs.

The core motivation is the chronic crisis in Major Defense Acquisition Programs (MDAPs): before MOSA, 62.4% of pre-2010 programs experienced cost growth totaling $542.1B, with an average delay of 35 months. Technology obsolescence alone costs the DoD $750M per year.

Despite widespread mandate and qualitative success stories across all services, **quantitative evidence of MOSA's cost/schedule benefits remains elusive**. Research (Shah 2021) found that existing MDAP data cannot isolate MOSA's causal effect due to confounding variables. The field broadly agrees that the key unmet need is **standardized evaluation methodology and metrics** to assess whether a program is actually MOSA-compliant and to measure its benefits.

## Timeline [coverage: high]

- **2010** — DoD issues Better Buying Power 2.0, lays conceptual groundwork for open systems
- **2015** — Under Secretary of Defense Frank Kendall issues **Better Buying Power 3.0**, formally mandates MOSA for all MDAPs (codified in USC 10 §2446a)
- **2018** — **MIL-STD-881D** published, provides standardized WBS taxonomy critical for MOSA interface definition
- **2019** — NDIA Systems Engineering Division publishes white paper with **Top 10 Recommendations** for MOSA implementation
- **2020** — DoDI 5000.02 restructured into Adaptive Acquisition Framework; MOSA policy moved to separate instructions (DoDI 5000.85)
- **2021** — Parth Devang Shah publishes GWU doctoral praxis providing the first holistic quantitative assessment, confirming the measurement gap

## Current State [coverage: high]

- **Mandate**: All US Major Defense Acquisition Programs are required to adopt MOSA principles
- **Adoption**: All three services (Army/Navy/Air Force) have active MOSA programs and standards
- **Qualitative evidence**: Multiple successful programs (Global Hawk, MQ-9 Reaper, AH-64E Apache, F-22, B-52) demonstrate MOSA benefits in practice
- **International adoption**: UK MoD (GVA), Australian DoD, Canadian Armed Forces all use MOSA-derived approaches
- **Commercial adoption**: Airbus uses MOSA on its HForce military helicopter conversion program (H125M/H145M/H225M)
- **Key gap**: No standardized evaluation/certification criteria, no agreed-upon metrics for measuring modularity or quantifying benefits

## Key Decisions [coverage: high]

1. **Mandate MOSA for all procurements** — OSD has made MOSA a requirement, not an option
   - Rationale: Addresses the root causes of cost growth and vendor lock-in
   - Status: Complete, codified in law (USC 10 §2446a)

2. **Leverage existing standards** — MOSA builds upon MIL-STD-881D for component hierarchy
   - Rationale: Eliminates ambiguity in "what level is an interface"
   - Status: NDIA recommendation #3, broadly accepted

3. **Early strategy development** — Define MOSA partitioning before procurement
   - Rationale: Allows industry to plan investments and compete effectively
   - Status: NDIA recommendation #1, best practice but not uniformly enforced

4. **Certification-based library approach** — Maintain a library of certified MOSA components/interfaces
   - Rationale: Accelerates adoption by reuse of proven designs
   - Status: Recommended but not yet implemented DoD-wide

## Experiments & Results [coverage: medium]

| Study/Experiment | Result | Sources |
|------------------|--------|---------|
| Shah (2021) — 6 Hypotheses on 86 MDAPs | H1 (measurable cost improvement) **Not Supported**; H2-H6 all **Supported** | [Shah 2021](sources/2026-04-05-mosa-shah-thesis.md) |
| NDIA (2019) — Industry/Government Working Group | Consensus reached on 10 key recommendations; aligns with Shah's identified gaps | [NDIA 2019](sources/2026-04-05-ndia-mosa-white-paper-2019.md) |
| FACE Consortium (aviation) | 70+ organizations, 900 contributors, 20+ productions procurements demonstrates ecosystem success | [concepts/face-technical-standard](concepts/face-technical-standard.md) |

## Key Standards & Frameworks [coverage: high]

MOSA relies on several key standards for implementation:

| Standard | Domain | Purpose |
|----------|--------|---------|
| **MIL-STD-881D** | Work Breakdown Structures | Provides common hierarchical taxonomy for system components (required by NDIA Rec #3) | [sources/2026-04-05-mil-std-881d-wbs-defense-materiel.md](sources/2026-04-05-mil-std-881d-wbs-defense-materiel.md) |
| **FACE™** | Avionics | Open architecture standard for airborne capability integration | [concepts/face-technical-standard](concepts/face-technical-standard.md) |
| **OMS** | Mission Systems | Open Mission Systems for sensor/payload interoperability | [concepts/open-mission-systems](concepts/open-mission-systems.md) |
| **UCS** | Unmanned Systems | Command and control interoperability |  |
| **VICTORY** | Ground Vehicles | Vehicular C4ISR/EW interoperability |  |
| **SOSA/CMOSS** | C4ISR | Sensor Open Systems Architecture |  |

## Gotchas & Known Issues [coverage: medium]

1. **Measurement problem** — No agreed methodology to quantify MOSA compliance or its benefits. This prevents meaningful incentive structures and ROI tracking. [coverage: high]

2. **Data rights & IP** — Open interfaces require clear technical data rights, but IP policy is still catching up to MOSA principles. [coverage: medium]

3. **Confounding variables** — Even with good data, isolating MOSA's effect on cost/schedule in multi-year programs is practically difficult. Other factors (requirements creep, underestimation) dominate. [coverage: high]

4. **Cultural change** — MOSA requires changing how government and industry do business. Incentives are not yet properly aligned in contracts. [coverage: medium]

5. **Software taxonomy gap** — MIL-STD-881D works well for hardware, but software lacks an equivalent standardized taxonomy for MOSA partitioning. [coverage: medium]

## Open Questions [coverage: low]

1. What quantitative metrics best capture modularity and openness in practice?
2. How can program offices be incentivized to prioritize MOSA investment despite short-term budget pressures?
3. Will the expected lifecycle cost savings actually materialize at scale over the next decade?
4. How can MOSA best integrate with modern cybersecurity practices given the increased attack surface of open interfaces?
5. What level of modularity is "enough"? Is there a point of diminishing returns?

## Sources [coverage: n/a]

All source materials are summarized in the wiki:

- [sources/2026-04-05-mosa-shah-thesis.md](sources/2026-04-05-mosa-shah-thesis.md) — Parth Devang Shah, GWU D.Eng. Praxis (2021)
- [sources/2026-04-05-ndia-mosa-white-paper-2019.md](sources/2026-04-05-ndia-mosa-white-paper-2019.md) — NDIA SE Division (2019)
- [sources/2026-04-05-dodi-5000-02-2020.md](sources/2026-04-05-dodi-5000-02-2020.md) — DoDI 5000.02 Adaptive Acquisition Framework (2020)
- [sources/2026-04-05-mil-std-881d-wbs-defense-materiel.md](sources/2026-04-05-mil-std-881d-wbs-defense-materiel.md) — MIL-STD-881D (2018)
- [sources/2026-04-05-face-technical-standard-3.2-2023.md](sources/2026-04-05-face-technical-standard-3.2-2023.md) — FACE 3.2 Technical Standard (2023)
- [concepts/mosa-defense-acquisition.md](concepts/mosa-defense-acquisition.md) — Original concept page
- [concepts/adaptive-acquisition-framework.md](concepts/adaptive-acquisition-framework.md) — AAF concept page
- [concepts/vendor-lock-in.md](concepts/vendor-lock-in.md) — Vendor lock-in concept
- [concepts/open-mission-systems.md](concepts/open-mission-systems.md) — OMS concept
- [entities/parth-devang-shah.md](entities/parth-devang-shah.md) — Author entity
- [entities/better-buying-power-3-0.md](entities/better-buying-power-3-0.md) — BBP 3.0 entity

## Related Topics

- [[adaptive-acquisition-framework]]
- [[vendor-lock-in]]
- [[face-technical-standard]]
- [[open-mission-systems]]
- 国防采办改革
