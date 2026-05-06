---
title: "R-EGI Program Achieves Key Milestone"
source_url: https://insidegnss.com/r-egi-program-achieves-key-milestone/
downloaded: 2026-05-06
type: raw_text
---

# R-EGI Program Achieves Key Milestone

## **Key Milestone Achieved**
The Resilient-Embedded GPS/INS (R-EGI) program successfully completed **four comprehensive test flights** (three in August, one in October 2024) at Holloman Air Force Base, New Mexico. The system, integrated into a modified F-16 Line Replaceable Unit (LRU), was flown on a C-12J aircraft, demonstrating its **Modular Open Systems Architecture (MOSA)** and exceptional functional performance in maintaining precise positioning and orientation.

> **"These successful test flights mark a significant advancement in PNT technology and validate the capabilities of the R-EGI system."**
> — Major Bernard Mutz, AFLCMC/WNX R-EGI Program Manager

## **Program Overview & Architecture**
R-EGI is a **government-owned, open-architecture** system designed to deliver robust, reliable Positioning, Navigation, and Timing (PNT) for U.S. Department of Defense platforms. Its core principles include:
- **Modular Open Systems Architecture (MOSA):** Enables adaptability across platforms and rapid integration of new sensors/algorithms.
- **Government Reference Architecture (GRA):** Fosters industry collaboration and rapid capability insertion.
- **Model-Based Systems Engineering (MBSE):** Ensures interface consistency and reuse.
- **Layered Design:** Separates safety-critical from mission-critical functions.

### **Key Architectural Features:**
- Open VPX system management (VITA 46.11 compliant).
- Separation of safety and non-safety data.
- LRU design supporting multiple form factors.
- Safety-critical software developed to **RTCA/DO-178B/C** and **MIL-STD-882E** standards.
- Open software environments enabling third-party applications and complementary PNT sources (e.g., cameras, LiDAR, radar).

## **Demonstration Components & Team**
The rapid prototype was developed in **<8 months** by a team including **IS4S** (design agent), Kearfott, General Dynamics-Mission Systems, Collins Aerospace, and the 746th/586th Test Squadrons.

### **Core Hardware in Demonstrated LRU:**
- **Large Form Factor (LFF) Modified F-16 LRU** (produced by GD-MS).
- **Safety Critical Navigation (SCNAV) Subsystem** (Kearfott): Handles safety-critical PNT, attitude, and host interfaces.
- **Inertial Measurement Unit (IMU)** (Kearfott): High-performance ring-laser gyroscope unit.
- **GNSS Receiver (GNSSR)** (Collins Aerospace): M-Code GPS receiver with Galileo Open Service mezzanine.
- **Mission Capability Navigation (MCNAV) Subsystem** (GD-MS/IS4S): Provides resilience via open software (**pntOS**, **ASPN23 messages**), integrating complementary PNT sources.
- **Trimble Force 28M GPS M-Code Receiver:** Successfully integrated in **<4 weeks** for the fourth flight, demonstrating architectural flexibility.

## **Pre-Flight Preparation & Testing**
Rigorous testing ensured system readiness:
- **Lab, Van, and Large Test Vehicle (LTV) Testing:** Over 4 hours of continuous PVT data collected daily.
- **746 TS Vibration & Rapid Decompression Testing:** Validated resilience under operational stress.
- **Commercial Aircraft Ride-Share Flights:** Provided early flight data.

## **Flight Test Outcomes**
The flights validated multiple operational modes:
- **Blended M-Code GPS/IMU solutions** (enhanced accuracy).
- **M-Code GPS-only solutions**.
- **IMU-only solutions**.
- **MCNAV solutions** using government-owned plug-in architecture.
- **Successful integration** with aircraft systems and accurate attitude output.

> **"The data collected during these flights will be crucial for refining and optimizing the system to meet future operational demands."**
> — Dr. Mikel Miller, R-EGI Program Director at IS4S

## **Upcoming 2025 Milestones**
- **Q1:** Complementary PNT flight demo (vision navigation in GNSS-denied environment).
- **Q2:** Production of Functional Engineering Units (FEUs) for aircraft System Integration Labs (SILs); Advanced receiver/antenna demo at **NAVFEST25**.
- **Q4:** Functional Qualification Testing (FQT) and availability of Production Representative Units (PRUs).

## **Significance**
The R-EGI program represents a **paradigm shift** in DOD PNT, emphasizing open architecture, rapid upgradeability, and resilience against emerging threats. The successful flight demonstration confirms the system's readiness to enhance navigation accuracy and reliability for future military operations.

**Authors:** Dr. Mikel Miller, Matthew Jonas, Dennis M. Miller, Dr. Robert Leishman (IS4S), and Major Bernard Mutz (AFLCMC).
