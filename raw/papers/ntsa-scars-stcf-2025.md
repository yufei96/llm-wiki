---
title: "SCARS (Simulators Common Architecture and Requirements) Summary - 2025"
source: NTSA
url: https://www.ntsa.org/-/media/sites/ntsa/events/2025/51a0/scars-stcf-brief.pdf
date: 2025
type: briefing
tags: [SCARS, simulation, MOSA, USAF, cybersecurity, open-architecture, training]
note: >
  Original PDF blocked by Incapsula bot protection. Content extracted via web_extract.
---

# SCARS (Simulators Common Architecture and Requirements) Summary — 2025

## Program Overview

- **Purpose:** A sustainment initiative to establish a Modular Open Systems Approach (MOSA) for Air Force simulators, enabling application reuse, efficient updates, evolving cybersecurity, and minimized life cycle costs.
- **Program Sponsor:** HAF/A3T
- **Supported MAJCOMs:** ACC, AFGSC, AFRC, AFSOC, AMC, PACAF, USAFE
- **Acquisition Pathway:** Sustainment Initiative
- **Prime Vendor:** CAE USA
- **Contract:** IDIQ with a 5-year base ordering period (2020-2025) + five 1-year options (2025-2030)

## Background & Problem Statement

The USAF faces significant challenges with its Operational Training Infrastructure (OTI):

- **Scale & Disparity:** Over 2400 training devices across 50+ platforms supporting 9 MAJCOMs, with very limited reuse due to disparate configurations.
- **Cost & Complexity:** Uniqueness requires costly unique development, production, and support.
- **Cybersecurity:** Continuous, evolving threats require compliance with the DoD Risk Management Framework (RMF), which is costly to sustain (scans) and implement (patches).
- **Demand:** Increasing demand for higher fidelity and greater interoperability is limited by a lack of standards and common architectures.

## Key Components

- **Security Operations Center (SOC):** Provides remote management, a central dashboard, and a help desk.
- **On-Premise Equipment (OPE):** A scalable local cloud for hosting simulation applications with common security controls.
- **Wide Area Network (WAN):** Utilizes existing partner networks; the SCARS WAN is in a proof-of-concept phase.
- **Prerequisite:** Training systems must have an approved Authority to Operate (ATO) to connect to SCARS.

## Three-Phased Approach

### Phase 1: Efficient Cybersecurity

- **Goal:** Centralized cyber-maintenance for vulnerability scans, patches, anti-virus, and enterprise-wide RMF controls.
- **Warfighter Benefit:** Significantly reduced training system downtime for maintenance and faster ATOs.

### Phase 2: Common Architecture

- **Goal:** Move majority of training system functionality to a common infrastructure, supporting cloud/virtual computing, common modeling, and interfaces.
- **Warfighter Benefit:** Improved reliability, minimized maintenance, and reduced cost of functional improvements.

### Phase 3: Standard Applications

- **Goal:** Training systems embrace common applications hosted on a common infrastructure. Only non-virtualizable software remains trainer-specific.
- **Warfighter Benefit:** Application re-use across platforms and consistent performance enhances the "fair fight."

## SCARS Standards

Standards are critical for establishing a common architecture and are published annually. The USAF funds training system programs for implementation.

### Key Mandated Industry Standards:

- **OGC Common Database (CDB):** Mandated as the interchange format.
- **SISO CIGI (SISO-STD-013):** Mandated interface between simulations and image generators.
- **Internet of Things (IoT):** Mandated for interfaces between simulations and aircrew control systems.
- **ARINC-610C:** Mandates common simulator functions when using aircraft parts.
- **OMG SysML:** Mandated for Model Based Systems Engineering.

### Specific SCARS Standards Include:

- Basic On-premise Equipment Integration Standard
- Common Security Controls Standard
- Certification Process Standard
- Application Certification Standard
- Data Standard (includes MBSE Modeling Guide and Geospatial Data Specification)
- DevSecOps Standard
- Architecture Standard

> **Note:** Some standards are public, others are limited distribution. Standards are required for integration with SCARS infrastructure. The USAF does **not** certify products as compliant.

**Contact for Standards:** `aflcmc.wns.scarsstandards@us.af.mil`
**Contact for Innovation Cell:** `aflcmc.wns.sims_innovate@us.af.mil`

## Architecture Transformation: Before vs. After SCARS

### Before SCARS (Proprietary & Custom):

- Internal & custom signatures, physics interactions, munitions, sensor, and aero models.
- Custom interfaces for host simulation, panels, controls, avionics, image generators, and visual systems.
- Proprietary runtime and obsolete source data.

### After SCARS (MOSA via Standards):

- **Core Simulation:** Reusable code and components with standard interfaces and data formats.
- **Common Elements:** Common Signatures & Weather Data, JSE GRID Services for physics, Common Munitions Models (JSE WSCE), Standard Aero Model Interface.
- **Standard Interfaces:** SISO CIGI, OGC CDB, Open XR, IoT for controls.
- **Host Simulation:** Still includes OFP but with standard interfaces (e.g., TBD for OMS Aircraft Interface).
