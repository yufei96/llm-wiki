---
title: "FACE Technical Standard, Edition 3.2 (August 2023)"
date: 2026-04-05
type: source_summary
source: raw/papers/face-technical-standard-edition-3.2.pdf
author: "The Open Group — FACE Consortium"
tags: [FACE, MOSA, avionics, open-architecture, technical-standard, airborne, UoC, conformance]
---

# FACE Technical Standard — Edition 3.2 (August 2023)

## Document Meta

- **Full name**: FACE™ Technical Standard, Edition 3.2
- **Published**: The Open Group, August 2023
- **Document number**: C232 | ISBN: 1-957866-29-1
- **Consortium**: 70+ organizations, 900+ contributors (per Shah thesis)
- **592 pages**
- **Mentions**: 4x "MOSA" (p29: architecture description, p588: glossary)

## Relationship to MOSA

FACE is the **most mature real-world MOSA implementation** in defense. While the FACE standard only mentions MOSA twice (in architecture description and glossary), it embodies MOSA principles in the most detailed, technically prescriptive form of any open systems standard in DoD.

## 5 FACE Architectural Segments

The standard divides airborne software into **5 segments** connected by **3 FACE Standardized Interfaces** (aka "KEY" interfaces per MOSA). These interfaces are the **open interfaces** required by MOSA.

### 1. Operating System Segment (OSS)
- POSIX-compliant OS abstraction
- Hardware-independent interface layer

### 2. I/O Services Segment (IOSS)
- I/O device drivers and data access
- Hardware-specific data acquisition services

### 3. Platform-Specific Services Segment (PSSS)
- Platform-specific services (graphics, platform services)
- System-specific services

### 4. Portable Components Segment (PCS)
- Mission application software
- The "portable" layer — components can move between FACE-conformant systems

### 5. Transport Services Segment (TSS)
- Inter-process communication
- Data distribution and messaging

## 3 KEY Interfaces (MOSA Open Interfaces)

The 3 FACE Standardized Interfaces connect the 5 segments. These are the **open, published interfaces** that enable component portability — the core mechanism by which FACE achieves MOSA.

## Unit of Conformance (UoC)

The atomic unit of FACE component portability:
- Each UoC defines a software component with standardized interfaces
- UoCs must conform to FACE specifications to be compatible
- Enables "build once, deploy anywhere" for avionics software

## Conformance Testing

FACE operates a formal conformance testing program:
- Components tested against FACE specifications
- Third-party conformance verification
- Conformance status recorded in FACE registry

## Significance for MOSA Research

1. **FACE = MOSA in practice**: While policy documents mandate MOSA abstractly, FACE implements it concretely. The 592-page standard provides exactly the **technical detail** that MOSA policy lacks.

2. **Interface standardization**: FACE shows how MOSA's "open interface" requirement can be operationalized through detailed interface specifications, UoC definitions, and conformance testing.

3. **Software-only focus**: FACE targets avionics software portability, not hardware modularity or business practice. This is a narrower scope than MOSA's full mandate (DoDI 5000.85 says architecture + interfaces + business practices).

4. **Conformance testing addresses Shah's H1 gap**: FACE has a conformance process; most MOSA domains don't. This is a model MOSA evaluation could emulate.

5. **NDIA Rec #4 (software MOSA) fulfilled**: FACE is the embodiment of NDIA's recommendation to apply MOSA to software architectures with defined taxonomy.

## Related Concepts
- [[mosa-defense-acquisition]]
- [[open-mission-systems]]
- [[adaptive-acquisition-framework]]
- [[vendor-lock-in]]

## Related Entities
- [[the-open-group]]
- [[parth-devang-shah]]

---
*592 pages, August 2023, Edition 3.2. Only 4 MOSA mentions — FACE operates on its own terms as a technical specification.*
