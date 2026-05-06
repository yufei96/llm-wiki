UNCLASSIFIED

UNCLASSIFIED

Christopher Edwards

29 June 2021

PEO AVN Open Systems Demo

Task Allocations and Overall Tracking

Distribution Statement A -
Approved for Public Release
- Distribution Unlimited


UNCLASSIFIED

UNCLASSIFIED
2

MOSA TO -- Technical Goals

Goal
Demonstration
Documentation

MOSA Conformance 
Capability

Reflect the business goal in technical 
results

•
TES Demonstration of HOST Testing

•
Use of FACE Conformant Software

•
Use of FACE Transports for integration

•
MOSA News Letter

•
MOSA D.Handout – MOSA TO

•
MOSA D.Handout – MOSA Conformance

•
Demo D.Handout – FACE Statements

•
MOSA Video

Exercise AMCE 
Concepts & 
Assumptions

Open Graphical Interfaces
Open transports
Configurable Processing

•
Multiple CDS implementations showing 
mixed criticality

•
Multiple TSS Implementations across 
multiple FACE Technical Standard 
Editions

•
Multiple Mission Computer 
representations

•
Use of modular hardware approaches

•
White Paper – Configurable UA

•
White Paper – Mixed Criticality in A661

•
White Paper – Multiple TSS

•
Demo D.Handout – Relate to the white papers

•
Demo D.Handout – Lessons Learned from TSS 
integrations

FACE / SOSA 
Interoperability

Containers Exploration, Enabling Rapid 
Portability for the Future
Standards Alignment and 
Interoperability (CMOSS, etc.)

•
Containers in Stellar Relay

•
Guest Operating Systems

•
Separation of DAL through multiple 
processing cards

• Demo D.Handout – FACE Statements
• Demo D.Handout – Demonstration Open 
Standards List

Integration of Apps 
across Multiple 
Platforms

• Integration of enduring aircraft system 
software into a FACE Architecture

• Includes - PM UH, PM FW, PM EUAS, PM 
AMSA, PM CARGO

• Demo D.Handout – Demonstration Participating 
PM List

• Demo Video

Model the Demo'd 
Systems

•
Capturing Key Interfaces

•
Considerations for Integration

• Models include physical/logical system 
models and use of integration models to 
generate TSS configurations

• Mappings to KILA

• Models D.Handout – Models ADDish
• Demo Video

Feedback/Q&A Related 
to Technical Goals

•
MOSA Conformance

•
Easiest through FACE, SOSA. and 
others are harder without some 
di
i

• Participant Q&A based on integration 
efforts

• Demo D.Handout – Participant Q&A


UNCLASSIFIED

UNCLASSIFIED
3

PEO Aviation Open Systems Demo

• Open Systems Demo Logo will be 
prominent in the Army Booth.


UNCLASSIFIED

UNCLASSIFIED

OPEN SYSTEMS DEMONSTRATION 
HANDOUT INFORMATION

4


UNCLASSIFIED

UNCLASSIFIED
5

FACE TIM Message

• The Army continues its over 10-year commitment to requiring the use of the FACE Approach

•
Multiple projects utilizing the FACE Technical Standard were brought together in this demonstration

•
These products come from many Program Offices within the Army and the Navy

• PEO Aviation has stepped up its commitment to Open Standards like FACE, SOSA, HOST, CMOSS with 
the forming of the MOSA Transformation Office

•
Conformance to the FACE and SOSA Technical Standards are key among these standards

• Use of the FACE Approach and the FACE Reference Architecture make this demonstration possible.

•
Use of the common reference architecture provided by the FACE Technical Standard by multiple program offices has provided readily 
available components

•
New features of the FACE Tech Standard 3.0 provide extremely effective ways to blend transports without recompiling software.

•
The FACE Approach includes guidance on how to bring the FACE Technical Standard to Legacy systems, allowing the inclusion of 
software packages that are not aligned to FACE into future systems through FACE wrappers.


UNCLASSIFIED

UNCLASSIFIED
6

Participants and Products

Participants (20)

AdaCore

Ansys

Avalex

BAE

Bell

Boeing

Collins

DDC-I

General Atomics

L3/Harris

Lockheed Martin

Lynx

Mercury Mission Systems

NAI

Northrop Grumman

OAR

Parry Labs

RTI

Skayl

TES

Wind River

DoD Organizations (9)

DEVCOM/ASIF

DEVCOM AvMc/TDD-A

DEVCOM/CAPT

PEO Aviation

PM AMSA

PM UAS

PM UH

PM CARGO

PM FW

PMA 209 (Navy)

Software Products (29)
Company

ANSYS CDS
Ansys

Bell ITEP Engine PSSS
Bell, TES

PFD
Boeing

ARR
Collins

MFMS
Collins

Alerts UA
DEVCOM/ASIF

CommonUA
DEVCOM/ASIF

MAP UA
DEVCOM/ASIF

Menu System
DEVCOM/ASIF

RIF CDS
DEVCOM/ASIF, Preasgis

RIF PSSS
DEVCOM/ASIF

Downlink
General Atomics

Flight C2
General Atomics

Handover Manager
General Atomics

MEM
General Atomics

Passive Sensor C2
General Atomics

Uplink
General Atomics

Air Traffic Manager (ADS-B)
Lockheed Martin

eTAWS
LM/Army/Navy

IFF Reduced Size Transponder ADS-B Device Manager Lockheed Martin

60v FliteScene
PM UH, NGC, L3H

TRMC BFT
PM UH, NGC

TRMC Flight Display
PM UH, NGC

Correlator
BAE

Arke Broker
PEO Aviation

Arke Collector
PEO Aviation

IDM Software
PM AMSA

ARCM
TES

Operating Systems (5)
Company

CentOS 7
Red Hat (Open Source)

DDC-I DEOS with RTEMS
DDC-I + OAR

LynxOS 178
Lynx

RedHat 8
Red Hat

VxWorks
Wind River

Hardware Product​s (7)
Company​

4178 Display
Avalex

4105 Display
Avalex

AMCS Prototype
Mercury Mission Systems

PSM 8600B​
Collins

TRMC
Northrop Grumman

Stellar Relay
Parry Labs

SIU
NAI

TSS Products (8)
Company​

FACE 3.1 COE TSS
TES

CinC
DEVCOM AvMC/TDD-A, Skayl

Collins
Collins

Connext
RTI

EUAS TSS (Kafka)
PM EUAS, Parry Labs

L3Harris TSS
L3Harris

NG TSS
PM UH, Northrup Grumman

RRADE
PEO Aviation, OAR


UNCLASSIFIED

UNCLASSIFIED
7

MOSA TO and the 5 Principles of MOSA

• Provide organization and structure for continued discussion between program offices on common elements within Arny Aviation
• Direct program offices to utilize common approaches via a Reference Architecture Description Document (RADD)

Establish an Enabling Environment

• Develop the Enterprise Architecture Framework (EAF) that defines Major System Components as modular elements
• Require the use of the EAF and clarification of rationale in an Architecture Description (derived from the RADD)

Employ Modular Design

• Review Key Interface input from Industry through the ACWG
• Develop Key Interfaces as part of the EAF

Designate Key Interfaces

• Use Open Standards in the EAF, apply standards to Key Interfaces
• Refine program guidance for how to apply standards through Implementation Guide and RADD

Use Open Standards

• Develop a MOSA Conformance Capability to evaluate solutions against the EAF and MOSA TO direction
• Provide program support through multiple milestone reviews & ITRA assessments

Certify Conformance

MOSA is defined by 10 U.S. Code 2446a as an integrated business and technical strategy that
•
Employs a modular design that uses modular system interfaces

•
Is subjected to verification to ensure relevant modular systems interfaces

•
Uses a system architecture that allows severability

•
Complies with technical data rights guidance (10 U.S. Code 2320) prescribed in the FAR


UNCLASSIFIED

UNCLASSIFIED
8

Discussion Locations

OSD: Aircraft Demonstration
Staffed by: S3I Team
Scope: 
Instruction on using integrated functions 
• Teaming Display
• ATAK
Operating the Demo
• Run the CAPTE
• Manage Flight Plan
• Manage Tactical Symbols

OSD: UAV and ATAK Demonstration
Staffed by: S3I Team
Scope:
Instruction on Using Functions
• ATAK
Operating the Demo
• ATAK Ground Device
• UAV Simulation

OSD: Modeling and Integration
Staffed by: S3I Team
Scope:
• Description of the integrations
• Functional flows, Integration groups
• FACE/SOSA Approach
• FACE Lessons Learned

MOSA Transformation Office/MOSA Conformance
Staffed by: MOSA TO
Scope:
• What is MOSA TO
• What is MOSA Conformance
• Direct people to Meeting Room 1

Flying FACE Demo, Other PEO Aviation Activities
Staffed by: PEO Aviation

Scope:
• Flying FACE Demo
• BALSA, Arke, RRADE
• FACE, SOSA Participation

60V Cockpit, Tri-Services Demo
Staffed by: GTRI Team
Scope: 
Tri-Service Demo

OSD: Pilot
Staffed by: Nick
Scope: 
• Fly the Simulation
• Instruct on aircraft functions


UNCLASSIFIED

UNCLASSIFIED
9

Booth Layout

Flying Face Demo TV

Top Down View

60V View

CAPT View
Projection Mapping Arch

MOSA Video TV

60V

UAV SIM, TAK Devices

CAPT-EVCS


UNCLASSIFIED

UNCLASSIFIED
10

Wiring Diagram


UNCLASSIFIED

UNCLASSIFIED
11

Marketing Wiring Diagram 


UNCLASSIFIED

UNCLASSIFIED

PROJECTION MAPPING STORYBOARD
and Related
TALKING POINTS

12


UNCLASSIFIED

UNCLASSIFIED
13

Flight Display Functions

• To demonstrate integration with an enduring platform, we have brought the UH-60V 
flight deck software hosted on a TRMC.  

• We have integrated the Ansys ARINC-661 CDS to demonstrate how an enduring fleet 
cockpit can support new capabilities developed to this key interface.

• We have also replaced the 60V displayed with an alternative Avalex display, using a 
PSSS to convert the Avalex bezel inputs to the 60V Transport.

• Displayed on the ARINC 661 CDS are some indicators driven from eTAWS (an 
application developed by PMA 209) as well as a systems status and logging 
application, Arke, developed by PEO Aviation.

• 661 is one of the primary focuses for Open Graphical Interfaces. It enables 3rd parties 
to write to the displays in a safety sensitive manner. Critical to 3rd party future 
ecosystem. 


UNCLASSIFIED

UNCLASSIFIED
14

Flight Integration

• Integration of the 60V software with the Ansys CDS had been underway when 
the Open Systems Demo was initiated.

• The TSS used on the TRMC is the same TSS used in the 60V, other TSS data 
is transformed in other devices and sent to interface software in the TRMC

• The interface software was written by NGC and provides inputs to the 
remaining TRMC software that is not provided by this demonstration.


UNCLASSIFIED

UNCLASSIFIED
15

Flight Display Status

• The integration of the 60V flight deck software is assisted by a CDU Simulation. 
This simulation provides CDU functions according to the 60V software 
interfaces.  Development of a common interface between the CAPT Software 
and the flight deck software could have avoided this workaround. As it is, this is 
a good representation of how multiple test utilities (CAPT and the CDU SIM) 
can be brought together to demonstrate functionality.

• The integration of the bezel inputs from the new Avalex display was performed 
in a separate computer than the TRMC. This was completed out of expediency.


UNCLASSIFIED

UNCLASSIFIED

Flight Display Functions


UNCLASSIFIED

UNCLASSIFIED

Flight Display Data Flow


UNCLASSIFIED

UNCLASSIFIED
18

Power Train Functions

• Also displayed on the ARINC 661 CDS is a display of Engine Data presented by 
a configurable User Application as proposed in one of the white papers 
presented by the DEVCOM team at this TIM.

• To exercise the abilities of a separate mission computer interfacing to a data 
bus, the CAPT-E simulation data was routed to an ARINC 429 bus. This bus 
simulates the traditional 60V fuel and power train data, as well as data from an 
ITEP engine.

• The ITEP Engine data is transformed into data for display by the 60V flight deck 
software, as well as being displayed on the configurable UA using ARINC-661.


UNCLASSIFIED

UNCLASSIFIED
19

Power Train Integration

• The integration of DCU and ITEP engine functions is demonstrated in the TES, 
RTI and NAI booths as part of another integration on a different processor (PPC 
instead of ARM). 

• In this integration, the TSS was replaced by the RTI DDS and was bridged over 
to the 60V transport through an adapter running in the MSAD platform. 

• This TSS Conversion represents one way of supporting multiple TSS 
implementations and is necessary when two platforms do not have native 
support of the other transport. 

• NOTE: in this instance we could have had either TSS run on the other device, 
but chose to use this method out of expediency and to demonstrate the 
capability.


UNCLASSIFIED

UNCLASSIFIED
20

Power Train Status

• The ITEP Engine PSSS is currently only representing one ITEP engine, so that 
data is duplicated to represent to engines to the flight deck.

• The ITEP Component is currently sending a small portion of the data that could 
be presented.

• The display of the ITEP Data was built to represent the component and has not 
been developed to a proper PVI for this type of engine.


UNCLASSIFIED

UNCLASSIFIED

Power Train Functions


UNCLASSIFIED

UNCLASSIFIED

Power Train Data Flow


UNCLASSIFIED

UNCLASSIFIED
23

Navigation Functions

• The Flight Plan is demonstrated with an integration of the Collins MFMS FACE 
Conformant UoC. 

• The Collins Avoidance Re-Router FACE Conformant UoC is also included, 
integrated with a threat filter application that listens to the Track Correlator

• The Collins ARR and MFMS software UoCs are both conformant to the FACE 
Technical Standard 2.1.  


UNCLASSIFIED

UNCLASSIFIED
24

Navigation Integration

• A plan to replace the TSS with another TSS in the demonstration was changed to 
reduce the work in completing the integration. Like the TRMC software, a large number 
of connections would make the integration difficult without a well developed system 
model that could feed a TSS code and configuration generator.

• The conversion of Flight Plan data into the TRMC software was the most complex 
conversion performed in this demonstration. Both Collins and NGC put in effort to get 
the conversion implemented. 

• A Threat Filter TSS transform was developed as an application that runs on the Stellar 
Relay hardware.  This transform listens to the Corrlated Track Data and looks for 
enemy units, identifies them as threats, and sends threat messages to the ARR.


UNCLASSIFIED

UNCLASSIFIED
25

Navigation Status

• The MFMS Interfaces are not all connected to the Flight Display software. The 
integration is rather complex and the approach was to experiment and 
document how this could be completed.  

• Entry of Flight Plans and acceptance of a change are completed on a tablet, 
rather than through the CDU interface.

• Note: Even with two applications supporting the same high level key interface 
(Flight Plan) there can be significant effort to integrate without alignment to 
further details within that interface.


UNCLASSIFIED

UNCLASSIFIED

Navigation Functions


UNCLASSIFIED

UNCLASSIFIED

Navigation Data Flow


UNCLASSIFIED

UNCLASSIFIED
28

Teaming Functions

• To represent the aircraft interfacing with a UAV at LOI 4, software developed by 
PM EUAS was combined with software developed by UH PO as part of the 
CMS program.

• This Teaming Display represents several aspects of a Common Operating 
Picture developed as a set of configurable UoCs using data modeled interfaces.


UNCLASSIFIED

UNCLASSIFIED
29

Teaming Integration

• The Teaming Management functions provided by General Atomics are 
integrated using the multiple TSS Proxy approach presented by the DEVCOM 
team in this TIM.  This proxy was developed by Skayl.

• The CMS/RIF applications are presented in a mix of FACE Technical Standard 
editions.  Both edition 2.1 and edition 3.0 are represented here with edition 
transforms occurring seamlessly in the TSS implementation.

• The Sensor Slewing operation is provided by a separate TSS Transform that 
accepts the geo-refenced event messages from the Menu System (using the 
RTI TSS) and converts that into a Sensor Command message (using the EUAS 
TSS). Additional commands can be built using the same transform and further 
modification of the Menu System configuration.


UNCLASSIFIED

UNCLASSIFIED
30

Teaming Status

• Limited LOI 4 functions are integrated. Additional functions can be rapidly 
added.

• User interface for some of the advanced functions may require integration of 
planned features to the configurable menu system.


UNCLASSIFIED

UNCLASSIFIED

Teaming Functions


UNCLASSIFIED

UNCLASSIFIED

Teaming Data Flow


UNCLASSIFIED

UNCLASSIFIED
33

Tactical Functions

• Aircraft connectivity to multiple networks and correlation of track data into a 
coherent display is an important part of providing a common operating picture in 
the current and future battlespace.

• ADS-B software from LMCO is combined with the IDM software into a correlator 
provided by BAE. Additional messages for the ATAK devices and Link-16 are 
brought into the correlator, which presents correlated symbols to the Maps.

• The IDM Software Application was ported to the Intel i7 processor and 
implemented on a reorientation of the AMCS.

• Included in this demonstration is an ATAK device using a wireless on-board 
network to represent passengers and a second ATAK coupled with a TSM radio 
representing a ground soldier.


UNCLASSIFIED

UNCLASSIFIED
34

Tactical Integration

• The BAE Correlator and LMCO ADS-B software was developed to use a FACE 
Technical Standard edition 2.1 interface. In this integration we show that a FACE 
technical Standard edition 3.x transport can link to these applications and support 
multiple TSS connections. 

• The Correlator receives messages on one TSS, and sends messages on two others.  
One of the TSS implementations typically uses a FACE 2.1 interface.

• The Correlator also receives messages from Link-16, VMF, and CoT using the native 
radio format. The code was not modified to utilize the FACE IO API, and is shown as a 
method for integration of legacy software into a FACE Computing Environment.

• The VMF data is suppled by the IDM Software Application running on the Mercury 
Mission Systems device. This software supports the same CORBA interface to the 60V 
Flight Deck software, as well as providing a TOC LAN connection to the ATAK devices 
and the correlator.


UNCLASSIFIED

UNCLASSIFIED
35

Tactical Status

• A realistic extension of this demonstration is the inclusion of actual BFT, Link-
16, and IFF radios.

• The current state of the 60V software currently results in duplicate VMF tracks 
displayed on the cockpit displays.  A modification to the data flows in the 60V 
software can eliminate these duplicate symbols if this integration were to be 
brought to the enduring aircraft.


UNCLASSIFIED

UNCLASSIFIED

Tactical Symbols Functions


UNCLASSIFIED

UNCLASSIFIED

Tactical Data Flow


UNCLASSIFIED

UNCLASSIFIED
38

TRMC Integration

• The TRMC was developed as a reusable mission computer prior to the 
development of the HOST, SOSA, and other recent hardware MOSA standards.

• TRMCs have been used by the Nave and Army on multiple aircraft.

• In this demonstration, the integration on the TRMC was performed by NGC and 
represents the current 60V software load with the addition of the Ansys CDS for 
display of ARINC-661 capabilities.

• The TRMC uses a T4080 processor and runs the VX Works Operating system.


UNCLASSIFIED

UNCLASSIFIED
39

TRMC Face Diagram

FACE Boundary

Operating 

System
Segment

OS

OS

IO

TS

OS

OS

Portable Components Segment

I/O Services Segment

Transport Services

Segment

Configuration Capability

Data Distribution Service

(DDS)

Transport Services

Capability

Platform Specific Services Segment

TS

Graphics Services

CDS
Quality of Service (QoS)

VxWorks

MAP
Flight Display
IDM Interface


UNCLASSIFIED

UNCLASSIFIED

TRMC Integration
Weekly Meeting: TRMC/NG Meeting, Thursday @10:00 Central


UNCLASSIFIED

UNCLASSIFIED
41

PSM Integration

• The PSM presented in this demonstration represents an upgrade to the switch 
module used on the CH-47F. This version of the PSM was a major compoent of 
the 2018 TIM. During that TIM several functions were demonstrated in multiple 
partitions, showcasing the capability of this hardware.

• The PSM uses a P2080 processor and runs the VX Works as a hypervisor. In 
this demonstration, one LynxOS guests OS is using two cores while anoter two 
cores are available for other guests.

• This PSM could serve as the switch in this demonstration, as well as provide 
more processing power than we are demonstrating.


UNCLASSIFIED

UNCLASSIFIED
42

PSM Face Diagram

FACE Boundary

Operating 

System
Segment

OS

OS

IO

TS

OS

OS

Portable Components Segment

I/O Services Segment

Transport Services

Segment

Configuration Capability

Data Distribution Service

(DDS)

Transport Services

Capability

Platform Specific Services Segment

TS

Graphics Services

Quality of Service (QoS)

LynxOS

MFMS
AAR

ARCM

AdaCore
Runtime

VxWorks
Hypervisor


UNCLASSIFIED

UNCLASSIFIED

PSM-1 Integration


UNCLASSIFIED

UNCLASSIFIED
44

Mission Computer Integration

• The collection of software in the Mission Computer Integration was targeted for 
a second guest in the PSM.

• The software development and port to LynxOS was delayed to a point where a 
delivery on CentOS was implemented as a mitigation effort.  

• These components are now running on the MSAD card in the Mercury Mission 
Systems device.

• As a lesson learned, development for multiple distributed vendors to one piece 
of hardware requires more advanced planning and aggressive procurement of 
developmental licenses. Remote development tools can provide a solution and 
should be pursued for future integration events.


UNCLASSIFIED

UNCLASSIFIED
45

Mission Computer Diagram Face Diagram

FACE Boundary

Operating 

System
Segment

OS

OS

IO

TS

OS

OS

Portable Components Segment

I/O Services Segment

Transport Services

Segment

Configuration Capability

Data Distribution Service

(DDS)

Transport Services

Capability

Platform Specific Services Segment

TS

Graphics Services

Quality of Service (QoS)

CentOS

MAP
eTAWS

ARKE B
ARKE C

Common UA
Alert UA


UNCLASSIFIED

UNCLASSIFIED

Mission Computer Integration


UNCLASSIFIED

UNCLASSIFIED
47

SIU Integration

• The SIU provided by NAI represents an up-to-date take on the HOST/SOSA 
approach to hardware solutions. 

• This version is using a quad core ARM processor using the FACE Conformant 
DEOS and RTEMS operating system. Other processing cards are available, 
and this processing card is also supported by VxWorks.

• After this device was selected for the TIM, a Switch card and cable was sent to 
add the Switch capabilities to this device. This demonstrates the capabilities 
available with these MOSA devices.


UNCLASSIFIED

UNCLASSIFIED
48

SIU FACE Diagram

FACE Boundary

Operating 

System
Segment

OS

OS

IO

TS

OS

OS

Portable Components Segment

I/O Services Segment

Transport Services

Segment

Configuration Capability

Data Distribution Service

(DDS)

Transport Services

Capability

Platform Specific Services Segment

TS

Graphics Services

Quality of Service (QoS)

DeOS

FADEC PSSS

RTEMS

DCUC PSSS

429


UNCLASSIFIED

UNCLASSIFIED

SIU Integration

Entities:
•
NAI (SIU, IOS)

•
DDC-I (DEOS, Integration)

•
RTI (Connext TSS)

•
BellFlight (FADEC PSSS)

•
S3I ASIF (DCU PSSS)

Weekly Meeting: NAI Meeting, Thursday @ 3:30 Central


UNCLASSIFIED

UNCLASSIFIED
50

Stellar Relay Integration

• This Stellar Relay CCM is the same mission computing capability used on the Grey 
Eagle for PM EUAS. It represents a lighter computing environment capable of 
processing low criticality functions.

• It is using a recent generation of the Intel i7 processor and runs the Red Hat Linux 
operating system using Docker Containers for software separation and portability.

• Containers are a recent addition in the open source world and provide advantages 
when developing software for deployment to other devices and operating systems.  

• Container use in avionics systems still has a ways to go. Current implementations 
utilize code that cannot achieve flight critical airworthiness. The FACE consortium 
should consider providing container guidance and potential requirements for future 
FACE Technical Standard editions. This can provide a path to Container functionality in 
flight critical software.


UNCLASSIFIED

UNCLASSIFIED
51

Stellar Relay FACE Diagram

FACE Boundary

Operating 

System
Segment

OS

OS

IO

TS

OS

OS

Portable Components Segment

I/O Services Segment

Transport Services

Segment

Configuration Capability

Data Distribution Service

(DDS)

Transport Services

Capability

Platform Specific Services Segment

TS

Graphics Services

ADS-B in DM

Quality of Service (QoS)

RHEL8

Handover
Manager

Flight C2

Passive
Sensor C2

Uplink
Downlink

MEM

Correlator

ADS-B

Generic

Radio Simulations


UNCLASSIFIED

UNCLASSIFIED

Stellar Relay Integration

Entities:
•
Parry Labs (Stellar Relay, EUAS 
TSS (Kafka) )

•
DEVCOM AvMC/TDD-A | Skayl 
(CiNC TSS)

•
RTI (Connext TSS)

•
LMCO (ADS-B)

•
General Automics (UAV Control)

Weekly Meeting: Teaming and Tactical Meetings, Friday at 1:00 and 2:00 central


UNCLASSIFIED

UNCLASSIFIED
53

Mercury Integration

• The Mercury Mission Systems developmental unit presented here represents 
an early version of the AMCS. It is shown here with two Intel i7 cards in an open 
frame. The cards are both currently running the CentOS 7.

• This two card approach can show how a single device can easily support a 
mixed DAL implementation.  Once card can run an RTOS while the other could 
continue to support low criticality applications through Red Hat Linux, possibly 
using a Container approach.

• During development of this system, the two cards we placed in separate frames 
to develop the separate component sets. The two cards were then combined to 
show the flexibility of the standards used by SOSA.


UNCLASSIFIED

UNCLASSIFIED
54

Mercury FACE Diagram


UNCLASSIFIED

UNCLASSIFIED

Mercury Integration

S3I: Load and Test ISA
Mercury: Load the final implementation
Mercury: New VPX Card delivery 
delayed End of August
Mercury: Identify USB/Video

Entities:
•
MMS (AMCS Prototype)

•
S3I (ISA Port)

Weekly Meeting: AMCS/Mercury Meeting, Thursday @11:00 Central


UNCLASSIFIED

UNCLASSIFIED

Display Integration

Entities:
•
MMS (AMCS Prototype)

•
RTI (Connext TSS)

•
L3Harris (L3H TSS)

•
DEVCOM AvMC/TDD-A | Skayl
(CiNC TSS)

•
Boeing (PFD)

•
TES (ARCM)

•
S3I ASIF (RIF Components)

Weekly Meeting: Internal RIF/SDK Meeting, Monday @9:00 Central


