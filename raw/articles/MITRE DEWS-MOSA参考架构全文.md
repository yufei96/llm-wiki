---
title: "MITRE DEWS MOSA Reference Architecture"
source_url: "https://apps.dtic.mil/sti/trecms/pdf/AD1214114.pdf"
downloaded: 2026-04-26
type: raw_text
---

REPORT DOCUMENTATION PAGE

Standard Form 298 (Rev. 8/98) 
Prescribed by ANSI Std. Z39.18

Form Approved 
OMB No. 0704-0188

The public reporting burden for this collection of information is estimated to average 1 hour per response, including the time for reviewing instructions, searching existing data 
sources, gathering and maintaining the data needed, and completing and reviewing the collection of information. Send comments regarding this burden estimate or any other 
aspect of this collection of information, including suggestions for reducing the burden, to Department of Defense, Washington Headquarters Services, Directorate for Information 
Operations and Reports (0704-0188), 1215 Jefferson Davis Highway, Suite 1204, Arlington, VA 22202-4302. Respondents should be aware that notwithstanding any other 
provision of law, no person shall be subject to any penalty for failing to comply with a collection of information if it does not display a currently valid OMB control number.   
PLEASE DO NOT RETURN YOUR FORM TO THE ABOVE ADDRESS.

1.  REPORT DATE (DD-MM-YYYY)
2.  REPORT TYPE
3.  DATES COVERED (From - To)

4.  TITLE AND SUBTITLE
5a.  CONTRACT NUMBER

5b.  GRANT NUMBER

5c.  PROGRAM ELEMENT NUMBER  

5d.  PROJECT NUMBER

5e.  TASK NUMBER

5f.  WORK UNIT NUMBER

6.  AUTHOR(S)

7.  PERFORMING ORGANIZATION NAME(S) AND ADDRESS(ES)
8.  PERFORMING ORGANIZATION 
     REPORT NUMBER

10. SPONSOR/MONITOR'S ACRONYM(S)

11. SPONSOR/MONITOR'S REPORT 
      NUMBER(S)

9.  SPONSORING/MONITORING AGENCY NAME(S) AND ADDRESS(ES)

12.  DISTRIBUTION/AVAILABILITY STATEMENT

13.  SUPPLEMENTARY NOTES

14.  ABSTRACT

15.  SUBJECT TERMS

16.  SECURITY CLASSIFICATION OF:

a.  REPORT
b. ABSTRACT
c. THIS PAGE

17.  LIMITATION OF 
       ABSTRACT

18.  NUMBER
       OF  
       PAGES 

19a.  NAME OF RESPONSIBLE PERSON

19b.  TELEPHONE NUMBER (Include area code)

06/15/2023
Conference Briefing

Directed Energy Weapons System Modular Open Systems Approach 
Reference Architecture (DEWS MOSA RA)

Keegan Merkert

The MITRE Corporation 
7515 Colshire Drive 
McLean, VA 22102
PRS-23-1891

Program Executive Office for Integrated Warfare Systems (PEO IWS)

W56KGU-18-D-0004

PEO IWS

DISTRIBUTION STATEMENT A. Approved for public release: distribution unlimited.

Presentation for Kitty Hawk Week

Outline: 
§ DEWS Reference Architecture Development 
§ Reference Architecture Implementation through MBSE tools 
§ DEWS MOSA RA and SOSA harmonization

Ordnance; Systems Architectures, DEWS; Directed Energy Weapons System; modular system architecture

33

Susan Carpenito

781-271-7646


June 2023

Keegan Merkert  

Directed Energy Weapons System 
Modular Open Systems Approach 
Reference Architecture (DEWS 
MOSA RA)

Approved for Public Release; Distribution Unlimited. Public 
Release Case Number 23-1891

The view, opinions, and/or findings contained in this report are those of The MITRE 
Corporation and should not be construed as an official Government position, policy, 
or decision, unless designated by other documentation.


2

§ DEWS Reference Architecture Development

§ Reference Architecture Implementation through MBSE tools

§ DEWS MOSA RA and SOSA harmonization 

Outline

This technical data deliverable was developed using contract funds under 

Basic Contract No. W56KGU-18-D-0004.

© 2023 The MITRE Corporation.


3

MOSA is …

“An integrated business and technical 
strategy that employs a modular 
design and, where appropriate, defines 
key interfaces using widely supported, 
consensus-based standards that are 
published and maintained by a 
recognized industry standards 
organization.”

“A Modular Open Systems Approach (MOSA) to 
Acquisition,” Open Systems Joint Task Force (OSJTF)

Improve interoperability – severable software and hardware 
modules that can be changed independently.

Facilitate technology refresh – delivery of new capabilities or 
replacement technology without requiring change to all elements in 
the entire system.

Enhance competition – open architecture with severable modules, 
allowing elements to be openly competed.

Incorporate innovation – operational flexibility to configure and 
reconfigure available assets to meet rapidly changing operational 
requirements.

Enable cost savings/cost avoidance – reuse of technology, 
modules, and/or elements from any supplier across the acquisition life 
cycle.

© 2023 The MITRE Corporation.


4

Tri-Service Secretaries Memorandum: MOSA as a 
Warfighting Imperative (Jan 7, 2019)

SUBJECT: Modular Open Systems Approaches 
for our Weapon Systems is a Warfighting 
Imperative

We determined the continued implementation of 
these standards, and further development of 
Modular Open Systems Approach (MOSA) 
standards* in areas where we lack them is vital to 
our success. As such, MOSA supporting standards 
should be included in all requirements, programming 
and development activities for future weapon system 
modifications and new start development programs 
to the maximum extent possible.

* OMS/UCI, SOSA, FACE and VICTORY

© 2023 The MITRE Corporation.


5

Decomposing MOSA

Business

Contracting 
Language

Intellectual 

Property 

Policy

… etc.
FACE
OMS
SOSA
VICTORY

Technical

Modularity

Consensus-

based 

Standards 
and OSAs

MOSA

Subject to 

Conformance 

Certification

Derived from “SOSA 101”

© 2023 The MITRE Corporation.


6

Defining Modularity for the DEWS MOSA RA 

“… functionality is partitioned into discrete, cohesive, and self-contained units with well-defined interfaces 
that permit substitution of such units with similar components or products from alternate sources with 
minimum impact on existing units.”

Function C

Function E

Function G

Function A

Function K

Function F

Function D

Function M

Function J

Function L

Function H

Function N

Function P

Function Q

Function D
Function M

Function E
Function J

Function P
Function Q

Function C

Function A

Function H
Module 1

Module 2

Function G

Function N

Function F
Module 3

Function K

Function L

Module 4

Functions are encapsulated; treat 
them as an integrated whole – 
with one set of input/outputs à 
interfaces

Modularity is not limited to the physical; 
software functionality can be modularized too

© 2023 The MITRE Corporation.


7

How a Reference Architecture fits into the Development 
Process

________________
* The Reference Architecture will evolve over time as experience from its use is folded back into it
** Selection of the Implemented Design will be based on factors such as price/performance trades, SWaP, etc.

Derived from a SOSA Keynote

Derived from SOSA 101

© 2023 The MITRE Corporation.


8

Directed Energy Weapon System (DEWS) MOSA 
Reference Architecture

§ Directed energy systems are becoming technically mature, on the verge of being more widely deployed

§ Services and programs all going in their own direction – and there was no OSA for DEWS

Needs

§
MOSA-based approach to “guide and constrain” development 
and procurement

§
Well-defined, government “owned” open interfaces between 
modules

§
Developer-independent modules

§
Service- and Host Platform-independent OSA

To Enable

•
Rapid, cost-effective, and supportable DEWS fielding (reduced time 
from R&D, to prototyping, to integration, to DT and OT)

•
Extend service life of systems through incremental upgrades 
(including from third-party sources)

•
Industrial base expansion and engagement à ecosystem (economies 
of scale)

•
Aligned R&D investment

•
Reuse across programs and Services

© 2023 The MITRE Corporation.


9

Learn from Systems under Development

Program Name
Service
Type
Domain
Government Lead
Industry Partners

Bane
Navy
HPM
Land
Dahlgren DEW Office 
(DEWO)

Tactical High-Power Microwave 
Operational Responder (THOR)
USAF
HPM
Land
AFRL
BAE Systems (BAE), 
Leidos, Verus Research

DE-Maneuver Short Range Air Defense 
(MSHORAD)
Army
HEL
Land
Army RCCTO
Kord Technologies (Kord)

Indirect Fire Protection High Energy 
Laser (IFPC-HEL)
Army
HEL
Land
RCCTO, OSD, SMDC

Dynetics (a Leidos Co.),
Lockheed Martin 
Corporation (LMC),
MZA Associates 
Corporation (MZA)

High Power Joint Electromagnetic Non-
Kinetic Strike (HiJENKS)

Navy: ONR

USAF: AFRL

HPM
Air
Dahlgren /Kirtland
LMC

Self-protect High Energy 
Laser Demonstrator (SHiELD)
USAF
HEL
Air
AFRL
LMC

Airborne High Energy Laser (AHEL)
USAF
HEL
Air
AF Special Operations 
Command (AFSOC)

High Energy Laser with Integrated 
Optical-dazzler and Surveillance 
(HELIOS)

Navy
HEL
Sea
PEO IWS 2
LMC

Layered Laser Defense (LLD)
Navy
HEL
Sea
ONR
LMC

Solid State Laser Technology 
Maturation (SSL-TM)
Navy
HEL
Sea
Dahlgren
Northrop Grumman

© 2023 The MITRE Corporation.


10

DEWS RA Vision, Goals, Enablers

Key

Vision

Goals

Enablers

Broadly Applicable

a) Stakeholder 

definition of CV-1, 
QAs, Use Cases, 
Architecture 
Principles

b) Agnostic with respect 

to operating 
environment

c) Agnostic with respect 

to host platform

Based on MOSA 

Principles

a) Leverage 

open/commercial 
standards and OSAs

b) Non-proprietary, 

supplier-agnostic 
module & interface 
definitions

c) Protect supplier IP and 

employs balanced 
Data Rights within 
modules

d) Large and small 

business are full 
partners in 
architecture 
development and 
governance

e) Create new only when 

necessary

f) Conformance 

Certification

Accelerate Delivery 

of Innovation

a) Follow “gray box” 

concept (architecture 
defines what the 
modules and 
interfaces do, not 
how they do it)

b) Provide alternative 

methods to 
instantiate near-term 
and future-focused 
technologies

c) Ensure small 

businesses- are fully 
enfranchised

d) Evolvability is 

incorporated

Increase Reuse

a) Facilitate backward 

compatibility

b) Open business model
c) Portable modules 

enables cross-
weapon portfolio 
application to reduce 
design time for new 
systems

Expedite Acquisition

a) Reduce traditional 

weapon system 
integration & test 
time

b) Vendor-agnostic 

open reference 
architecture allows 
government to 
leverage multiple 
industry partners

c) Allow faster insertion 

of new tech from 
best of breed

d) Enable small 

businesses- 
developed 
enhancements at 
reduced costs

Directed Energy Weapon programs leverage a broadly applicable Reference Architecture, 

founded on MOSA principles, that accelerates innovation, expedites development, and 

increases the reuse of standard elements

© 2023 The MITRE Corporation.


11

DEWS MOSA RA Development Approach

Derived from “SOSA 101”

“Interfaces exist in 

service of the Modules”

Vision, Goals, and 

Enablers

Stakeholder 

Input

Quality Attributes

Use Cases

Architecture 

Principles

Detailed List of 

Functions

Criteria for 

Aggregation of 
Functions into 

Modules

Module 

Definition

Module I/O 

Requirements

Interface 
Definition

Exemplars
Digital Models of 

Exemplars

Digital Model of the Reference 

Architecture

Interfaces

The Foundation

Modules

© 2023 The MITRE Corporation.


12

DEWS Open Reference Architecture Modules

System Monitor
Fire Control

DEWS Management

External 

Data 

Ingestor

DEWS 
Scope

Local 

Operator 
Human 
Machine 
Interface
Deconfliction 

Safety
DE Source
Beam Director
Beam 

Transport

Data Storage
Supporting 

Services

Thermal 

Management
Power
Host Platform 

Interface

Support System Operation

Security 
Services

Track Manager

Tracker(s)

Integrated 
Sensor(s)

Camera(s)

Local Sensor(s)

_____________
* Showing only a small subset of interfaces to ensure clarity of the graphic

© 2023 The MITRE Corporation.


13

Example of Functions Encapsulated in one Module

ID
Name
Description

21.11
Display Situational Awareness 
Data 

Displays map of system tracks relative to host platform. May include symbology 
(e.g., MIL-STD-2525), overlays, etc. Display sources include result of the current 
track store, Local Sensors, primary aperture, or direct feed from External Sensor or 
Host Platform. This display is also a user interface for functions such as 
designating tracks. If a track is to be designated for attack, the designated object is 
tagged as the target 

21.13
Display Video

Displays Integrated Sensor video feeds to DEWS operator for use in carrying out 
engagements. The feeds may be real-time or pre-recorded. The operator display 
allows the replay, pause, rewind, fast forward, etc. (so-called TiVo functionality) 
permitting reconstruction and analysis. 

21.14
H&S Status Update
Requests and receives system H&S from the System Monitor 

21.15
Display and Control Status

Provides visual display of system status (received from Fire Control), view and 
control states/modes (conveyed to Fire Control),system power on/off, fault 
conditions and alarms (including the ability to drill-down to gather more detail, and 
clearing alarms) 

21.16
Initiate BIT
Requests that the System Monitor Module that a Built-in Test (BIT) to be performed 

© 2023 The MITRE Corporation.


14

Mapping Functions à I/O Needs à Inter-Module 
Interactions

ID
Name
Input Needs
Input Source
Product Produced
Product Destination

21.11
Display Situational 
Awareness Data 

Track Data (tracks 
and kinematic data)
Track Manager Module
Data in display format
Fire Control Module

21.13
Display Video
Video data

Local Sensor Module 
(real-time) and Data 
Storage Module 
(playback)

Video in display format
(local operator display)

21.14
H&S Status Update H&S status report
System Monitor Module
Status request
System Monitor Module

21.15
Display and Control 
Status
System status data, 
Fire Control Module
Data in display format, 
Control messages

(local operator display), Fire 
Control Module

21.16
Initiate BIT
Operator input
(controls internal to this 
module)
Request to initiate BIT
System Monitor Module

Only showing five of the 26 functions for Module 21 (Local Operator HMI)

© 2023 The MITRE Corporation.


15

DEWS MOSA Reference Architecture Model

Module Architecture

Module Behavior

Module Interfaces

•
The DEWS MOSA RA will be provided as a Digital Engineering product, directly usable as a base for implementing programs

•
Accompanying documentation will provide guidance on use, including with other standards

© 2023 The MITRE Corporation.


16

DEWS RA Module System Architecture 

Module Blocks connected via ports with interface definitions

Module Definitions

© 2023 The MITRE Corporation.


17

DEWS RA Data Model – Track Message Data Object

© 2023 The MITRE Corporation.


18

DEWS RA Data Model – Track Message Definitions

API Object
Data Object Description
Name
Documentation
Type

Multipli

city

Minimu

m

Maxim

um
Enumeration

Acceleration
Three dimensional acceleration
xAcceleration
Acceleration of the x-component of an XYZ_ENU 
axis; if no reference point is specified, reference 
point should be the center of ownship/host; 
(units: Kilometers/Second^2)

Real
1

Acceleration
Three dimensional acceleration
yAcceleration
Acceleration of the y-component of an XYZ_ENU 
axis; if no reference point is specified, reference 
point should be the center of ownship/host; 
(units: Kilometers/Second^2)

Real
1

Acceleration
Three dimensional acceleration
zAccerleration
Acceleration of the z-component of an XYZ_ENU 
axis; if no reference point is specified, reference 
point should be the center of ownship/host; 
(units: Kilometers/Second^2)

Real
1

Aimpoint
Aimpoint used by tracker
aimpointPostitionX Three dimensional position of aimpoint
Position
0..1

Aimpoint
Aimpoint used by tracker
adjustmentMode
Adjustment mode of the aimpoint
ModeOfOperation
1

Aimpoint
Aimpoint used by tracker
aimpointPositionAz Three dimensional position of aimpoint
PositionAzEl
0..1

Aimpoint
Aimpoint used by tracker
aimpointPositionLa
tLong

Three dimensional position of aimpoint
PositionLatLong
0..1

ModeOfOper
ation

Indicates the mode of an operation
mode
Indicates the mode of an operation
String
1
AUTOMATIC
SEMI_AUTOMATIC
MANUAL

Orientation
Three dimensional angular offset
yaw
Angular offset for pitch  (units: Degrees).
Real
1

Orientation
Three dimensional angular offset
pitch
Angular offset for pitch  (units: Degrees).
Real
1

Orientation
Three dimensional angular offset
roll
Angular offset for roll (units: Degrees).
Real
1

Pose
Object position and orientation
orientation
How the object is placed or pointed
Orientation
0..1

Pose
Object position and orientation
positionAzEl
Horizontal coordinate system position
PositionAzEl
0..1

Pose
Object position and orientation
positionLatLong
Latitude and Longitude position
PositionLatLong
0..1

Pose
Object position and orientation
positionXYZ
Three dimensional position
Position
0..1

Showing only a sample of the Track Message Definitions

© 2023 The MITRE Corporation.


19

DEWS RA Activity Diagram (Power On Sequence)

Power Module: Power on DEWS

Power Module: Power 

Distribution

System Monitor 
Module: Orderly 

Power On

Fire Control Module: 
System Initialization

System Monitor 
Module: Receive 

H&S Reports

Fire Control Module: 

Report H&S

Power Module: Receive 

Host Provided Power

System Monitor 
Module: System 

Initialization

Fire Control Module: 

Perform BIT

Fire Control Module: 

Monitor H&S

© 2023 The MITRE Corporation.


20

DEWS RA Landing Page

© 2023 The MITRE Corporation.


21

DEWS RA Model Components

Requirements
Behavioral
Structural

Interfaces

Data

Functions

Requirements
States

Functions

Modules

Landing Page to Navigate 
the Reference Architecture

Exchanges

© 2023 The MITRE Corporation.


22

Published version DEWS MOSA RA 1.1

Version 1.1 of the Reference Architecture

§  
Reference Architecture Document 1.1

§  
Magic Draw Digital Model

Supplemental Material

§  
Implementation Guidance

§               DEWS RA Assessment

§  
Acquisition Framework

RA Document
The RA complete with imported tables, charts, graphics, and descriptions will be made available in an MS 
Word Report

HTML Extract
Export of MBSE model diagrams and data will be provided in HTML extract for users without access or 
familiarity with the Cameo software

Cameo zip file
Users will unzip all files to a folder and use Cameo to open the “DEWS_MOSA_Reference_Arch.mdzip” file. 
Cameo is a generic name for Dassault Systems CATIA Cameo Enterprise Architecture 19.0 SP4 also known 
as Magic System of Systems Architect (MSOSA) 19.0 SP4

Options to Access DEWS MOSA RA

© 2023 The MITRE Corporation.


23

DEWS MOSA RA integration with SOSA

© 2023 The MITRE Corporation.


24

SOSA-DEWS Comparison/Relationship

SOSA
DEWS

Modules 
that are 
unique 
to DEWS

Modules 
that are 
unique 
to SOSA

Data Model

Interaction 

Patterns

Common 
Modules

System Manager / System Monitor

Task Manager / Fire Control

External Data Ingestor
Tracker / Track Manager

Security Services

Storage-Retrieval Manager / Data Storage

Nav Data and Time & Frequency Services / Supporting Services

Power

Host Platform Interface

Local Operator HMI 
Local Sensor(s)
Deconfliction Safety 
DE Source 
Beam Transport 
Beam Director 
Thermal Management 

Emitter / Collector
Conditioner-Receiver-Exciter
Signal/Object Detector and Extractor
Signal/Object Characterizer
Encoded Data Extractor
Situation Assessor
Impact Assessor and Responder
Reporting Services
Guard / Cross-Domain Service
Network Subsystem
Calibration Service
Compressor/Decompressor  

© 2023 The MITRE Corporation.


25

SOSA-DEWS Comparison/Relationship

DEWS_ID 
DEWS Func 
DEWS Description 
SOSA Function

68.13 
Generate Power 
In cases where the DEWS operates independently 
of Host-provided power, generate its own power 
internally. This Function is optional 

68.15 
Receive Host-
Provided Power 

In cases where the DEWS doesn't generate its 
own power, receive input electrical power (e.g., 
440VAC, 120 VAC, etc.) from Host Platform 
Interface Module. This is an optional function.

Convert between different power 
characteristics - From Host Platform 
Interface

68.16 
Power on DEWS 
A discrete (an external button or key) to turn on the 
entire DEWS. After powering up, this function will 
request power distribution (68.41) to SMM to begin 
DEWS initialization 

68.21 
Power conversion 
Transform prime power to match requirements for 
each DEWS Module (including DC/AC conversion, 
high voltage, spike protection, etc.) 

Convert between different power 
characteristics

68.23 
Provide Storage of 
Electrical Power 

Stores energy (for example, in a battery) for use 
when needed by system modules 

Store power for intermittent input 
power loss

Store power to provide long-term 
power to loads without input power

This element should be eliminated from DEWS 
as a functional requirement

Power-on process for DEWS is different from that of 
SOSA (which is very chassis-oriented)

Use of storage is different between 
DEWS (which is focused on energy 
surge) and SOSA (which is to coast 
through intermittent source outages)

Showing only a sample of the Power Module Functions

© 2023 The MITRE Corporation.


26

SOSA-DEWS Comparison/Relationship

DEWS_ID 
DEWS Func 
DEWS Description 
SOSA Function

68.41 
Power Distribution 
Discharges energy as needed to support DEWS 
modules, based on system condition and individual 
module needs 

Distribute power from power 
supplies to power loads

68.55 
Power Conditioning 
Delivers power at the proper voltage and current 
characteristics by protecting against high/low voltage or 
current conditions, filter noise, transient impulse 
suppression, etc. 

Condition/filter power

68.61 
Accept Remote 
Control 

Provides a digital interface to Local Operator and/or Host 
Platform to enable remote management and control of all 
functions 

Provide a digital control 
interface

Protect against voltage and 
over-current conditions

Consider adding this to Power Conditioning and remove as a 
separate function.  Need clarification if this is internal to SOSA 
(protecting the sensor) or external (e.g., breaker on host to 
keep wiring from catching on fire)

Showing only a sample of the Power Module Functions

© 2023 The MITRE Corporation.


27

Summary

Modular Open Systems Approach will accelerate development of Directed 
Energy Weapon Systems (DEWS) 

§
DEWS are becoming technically mature, but no OSA currently exists for these systems

§    The DEWS MOSA RA will enable rapid, cost-effective, and supportable DEWS fielding

Digital Engineering and model-based systems engineering (MBSE) provides 
an efficient means of standardizing a modular approach

§ 
Digital products can be directly used by supporting programs 

§ 
Views can be adapted depending on a specific user’s needs

§    Technical updates are made in a single location in the digital model

The DEWS MOSA RA is actively aligning modules with analogous SOSA 
module definitions

§ 
Standardizes technical requirements under a common OSA 

SOSA
DEWS

Modules 
that are 
unique to 

DEWS

Modules 
that are 
unique to 

SOSA

Data Model

Interaction 

Patterns

Common 
Modules

© 2023 The MITRE Corporation.


Closing Slide

Keegan Merkert

Kmerkert@mitre.org

Linkedin.com/in/keegan-Merkert-653bb118

© 2023 The MITRE Corporation.


29

Backup

© 2023 The MITRE Corporation.


30

Systems in Development

• Directed Energy Weapons (DEW) utilize beams of energy 

to destroy, damage, or disrupt a target. Examples include 
lasers, high power microwaves (HPM), and particle beams. 
They offer:

– Potential to “Bend” the Cost Curve

– Deep Magazines with Rapid Reload and Reduced Logistics

– Highly reduced collateral damage

– Precision Effects / Adjustable Effects

– Engagement at the Speed of Light

– Air / Land / Sea Platforms

Lockheed Martin

HiJENKS
Air Force/Navy
HPM

THOR
Air Force/Army
HPM

DE-MSHORAD
                Army
                Laser

AHEL
SOCOM
Laser

SSL-TM
Navy
Laser

© 2023 The MITRE Corporation.


31

DEWS MOSA RA needs to grow along side of technology 
development

Key Aspects
• Achieve military 

dominance in every 
mission area where DEW 
makes technical sense

• Develop operational 

experience, knowledge,  
and confidence through 
operational 
demonstrations

• Advance and mature the 

technology to increase 
lethality, expand the 
mission set, and counter 
future adversaries

• Deliver new military 

capabilities with proven 
technology

Tactical Missions  
with current proven technology:
Directed Energy Strike, cUAS, cRAM, Counter 
Intelligence, Surveillance, and Reconnaissance cISR

Tactical Missions with  advanced 
technology:
Counter Anti-Ship Cruise Missile (C-ASCM), 
Counter Land Attack Cruise Missile (C-
LACM), Base Defense,  Aircraft Defense,  
Close-Combat

Strategic Missions  with 
advanced  technology:
Ballistic and Hypersonic Missile 
Defense

2019-24

2025-30

2030+

Increasing Military Capability

Time

We are advancing 
Hypersonics to the 
left

© 2023 The MITRE Corporation.


32

DEWS Are Arriving and Being Used

•ODIN – Optical Dazzling Interdictor, Navy

– Low-power laser system for dazzling of Unmanned Aerial System (UAS)-mounted Electro-

Optical (EO)/Infrared (IR) sensors

– First three systems installed on DDG51 Flt IIA ships,  five more to be installed through 2023

•HELIOS, Navy

– cUAS, cFIAC, 60 kW, Lockheed
– To be installed on DDG51 Flt IIA ship in FY22

•SSL-TM – Solid State Laser- Technology Maturation, Navy

– cUAS, cFIAC, 150 kW, Northrup
– Installed on USS Portland (LPD 27) in 2019, deploys in 2021

•CLAWS – Compact Laser Weapons System, Marines

– cUAS, 5 kW, Boeing, 5 systems, in CENTCOM
– Integrated with Army C-RAM C2 system and radar

•HELWS – High Energy Laser Weapons System, Air Force

– cUAS, 10 kW, Raytheon
– 1 unit in CENTCOM

•THOR – Tactical High Power Microwave Operational Responder, Air Force

– cUAS, Raytheon, OCONUS evaluation later this year

•DE M-SHORAD – Maneuvering Short Range Air Defense, Army

– Experimental prototype with combat capability : 50 kW-Class laser for cUAS, cRAM, cRW
– Prototype demo FY21, 1st Platoon (4 platforms) fielded FY22

•IFPC-HEL – Fixed/Semi-Fixed Site Protection, Army

– Lab demo FY22: 300 kW-Class laser for cUAS, cRAM, cCM will inform prototyping effort
– Joint range demonstration with Navy HELCAP in FY23, 1st Platoon (4 platforms) fielded FY24

© 2023 The MITRE Corporation.


33

Functional and Interface Requirements

Module functions are defined as requirements

Module SysML Block Activities (Functions) traced to requirements

© 2023 The MITRE Corporation.


