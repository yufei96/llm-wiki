# mosa-five-pillars

## Source
[[sources/mosa-implementation-guidebook-27feb2025-cleared.pdf#page:5-50]]

## Overview
OUSD(R&E)-led MOSA working groups developed the **five pillars of MOSA** to ensure DoD programs have an effective approach for MOSA implementation.

## The Five Pillars

### 1. Enabling Environment
By establishing and maintaining an enabling environment that supports MOSA, the DoD can ensure the development of modular, interoperable, and adaptable systems that meet evolving defense needs efficiently and effectively.

This pillar involves:
- Setting clear MOSA goals that expand capabilities and interoperability
- Transforming requirements, business, management, technical, and acquisition practices to align with MOSA principles
- Updating contracts, data, licenses, property rights; plans; and other key areas to support modularity and openness
- Embracing an Agile Development Culture with frequent small releases based on continuous feedback
- Deploying automation with CI/CD for continuous operations
- Aligning organization structure with system design (Conway's Law)
- Adopting Digital Engineering Practices to capture MOSA elements in models

### 2. Modular Design
To accomplish the acquirer's business and technical objectives, the acquiring organization should **identify the required functionality of the modular system components before issuing the RFP**.

Benefits of effective modular design:
- Acquirers/developers can upgrade or change functions rapidly, with limited/no impact to the rest of the system
- Isolates functionality during design to simplify development, maintenance, changes, and upgrades
- Modules can be independent of technology choices → easier substitution when technologies evolve
- Immutable and disposable → deploy the same code everywhere

Key design principles:
- Separates components into scalable, reusable, self-contained functional elements
- Architectural failure isolation → when one module fails, the rest of the system remains available

### 3. Designated Interfaces
By designating modular system interfaces, the DoD can ensure that systems are flexible, interoperable, and easily upgradeable.

This pillar focuses on **decoupling interface and service implementation** to allow components to follow separate life cycles.

Best practices for interface management:
1. **Identify Modular Interfaces**: Conduct thorough analysis, define boundaries/characteristics, rank by criticality
2. **Develop and Implement an Interface Management Plan (IMP)**: Include processes, responsibilities, procedures for upgrading standards
3. **Assign Interface Ownership**: Control definition/development/implementation to ensure compliance
4. **Create Unique Identifiers**: Consistent naming for each interface
5. **Trace Requirements**: Ensure traceability from MOSA/operational requirements to interface specifications
6. **Document Interfaces**: Maintain detailed records in Interface Requirement Specifications (IRS)

### 4. Consensus-Based Open Standards
By standardizing modular system interfaces through consensus-based standards, the DoD can ensure systems are flexible, interoperable, and easily repairable/upgradeable.

Key practices:
- Prioritize consensus-based international/government standards to maximize interoperability
- Select appropriate standards tailored for your program
- Ensure proper implementation to avoid interoperability issues
- Standardize interfaces to the maximum extent feasible
- Document and manage interface specifications
- Enable competition by keeping interfaces open

### 5. Certifying Conformance
Developers must verify and validate MOSA implementation/requirements, ensuring conformance to selected internal/external open interface standards.

Certification guarantees:
- Modularity and openness objectives are met
- Ultimately supports program success and system sustainability

Verification activities include:
- Checklists guiding self-assessment
- Defined criteria and verification methods
- Documentation validation
- Modularity requirements verification
- Tool development validation

## Related Concepts
- [[mosa-defense-acquisition]]
- [[modular-open-systems-approach]]
- [[open-standards-importance-defense]]

## Tags
#extracted-from-mineru #mosa #principles #dod-policy
