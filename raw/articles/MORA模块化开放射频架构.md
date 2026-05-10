2019 NDIA GROUND VEHICLE SYSTEMS ENGINEERING AND TECHNOLOGY 
SYMPOSIUM 
VEHICLE ELECTRONICS & ARCHITECTURE (VEA) & GROUND SYSTEMS CYBER ENGINEERING 
(GSCE) TECHNICAL SESSION 
AUGUST 13-15, 2019 - NOVI, MICHIGAN 
 
 
MODULAR OPEN RF ARCHITECTURE (MORA): 
STANDARDIZING THE RF CHAIN 
 
Jason Broczkowski1, Derek Bailey2, Troy Ryder3, Jason Dirner3 
 
1ASRC Federal, Aberdeen Proving Ground, MD 
2Aspen Consulting Group, Aberdeen Proving Ground, MD 
3C5ISR Center, Aberdeen Proving Ground, MD 
 
ABSTRACT 
The Modular Open RF Architecture’s (MORA) core objective is to logically 
decompose radio frequency (RF) systems for efficiency, flexibility, reusability, and 
scalability while enabling management, health monitoring, and sharing of raw 
and/or processed data. MORA extends the Army’s Vehicular Integration for 
C4ISR/EW Interoperability (VICTORY) architecture. MORA was introduced to the 
GVSETS community in 2015 at version 1.0 of the specification, and has matured 
with the help of community, industry, and academia partners to its current version 
2.3. This paper discusses the current state of the MORA specification and how it 
has evolved beyond its initial topology to encompass the entirety of the RF chain in 
an open and modular fashion. In addition, this paper will describe the purpose of 
MORA, the objectives of its development, its foundation, and the basic concepts 
and core features. 
 
 
Citation: J. Broczkowski, D. Bailey, T. Ryder, J. Dirner, “Modular Open RF Architecture (MORA): Standardizing 
the RF Chain”, In Proceedings of the Ground Vehicle Systems Engineering and Technology Symposium (GVSETS), 
NDIA, Novi, MI, Aug. 13-15, 2019. 
 
1. INTRODUCTION 
 Radio Frequency (RF) systems are typically 
implemented with a narrow scope, tailored to a 
particular function with either an individual or suite 
of specific hardware and software components to 
achieve that mission. While specialized equipment 
is invaluable for bringing capabilities to the 
warfighter, this practice of bolt-on, stove-piped 
products introduces a host of issues to the 
government and the warfighter over time. The 
following caveats apply to all platform systems, not 
only those in the area of RF: cost of redundant 
hardware components already on the platform, 
increased Size, Weight, and Power (SWaP) 
infringing 
on 
crew 
stations 
in 
vehicles, 
maintenance and procurement of replacements, 
longer timelines and reduced flexibility for 
capability insertions, etc. While there are many 
concurrent efforts to address these issues as well as 
 
Distribution Statement A: Approved for Public Release 
OPSEC# 8272 
Proceedings of the 2019 Ground Vehicle Systems Engineering and Technology Symposium (GVSETS) 
Modular Open RF Architecture (MORA): Standardizing the RF Chain 
 
Page 2 of 8 
a thrust to adopt open standards [1] within the 
Department of Defense, the MORA Specification 
[2] has been created and iterated upon to address 
the RF landscape specifically. 
Previous efforts at open architectures within the 
RF realm focused primarily on the development 
and maturation of Software Defined Radios (SDR) 
meant to advance the portability of digital 
processing 
and 
waveform 
applications, 
independent of RF chain stages.  However, RF 
chain control messaging (e.g. frequency tuning, 
gain setting, filter selection, transmit/receive 
functions) has remained vendor-specific and in 
some cases, model and/or system specific within 
the same vendors, making the need for “drivers” a 
way of life within signal data processors.  To truly 
allow for dynamic and multi-mission RF chain 
construction, 
capability 
profiles, 
resource 
management/control, 
and 
data 
and 
context 
messaging needs to be standardized. 
 
2. OBJECTIVES 
RF products spanning multiple functions have 
become increasingly critical to the warfighter. 
Military use of the electromagnetic spectrum now 
includes communications, electronic warfare, 
intelligence, and mission command systems. Due to 
the manner in which military capabilities are most 
often designed, current RF system implementations 
are typically single-mission focused with closed or 
proprietary 
interfaces 
between 
stove-piped 
resources. 
The objective of MORA is to provide 
standardized access and control of the RF chain.  
This standardization provides several benefits, 
including the enabling of resource sharing, which 
provides efficiencies in SWaP.  Additionally, it 
enables multi-mission operations and moves the 
DoD towards its objective of multi-nodal 
operations.  The standardization helps to eliminate 
the burden of driver development and the use of 
discrete signal lines through the use of standardized 
digital messaging transported on one of two 
networks.  Through breaking the traditional 
stovepipes, MORA supports development of 
interoperable and portable RF systems within the 
government and industry while still providing 
space for proprietary and best-in-class solutions for 
the DoD.  
 
3. FOUNDATION 
The Army’s Vehicular Integration for C4ISR/EW 
Interoperability (VICTORY) [3] defined an 
Ethernet-based network architecture for integrating 
electronic systems within military ground vehicles, 
as well as interface specifications for sharing sensor 
and data products, managing configuration, modes, 
and health of the infrastructure and applications, 
transporting data with quality of service, and 
implementing necessary information assurance 
controls to protect the system and its data. 
VICTORY 
supports 
the 
non-time 
critical 
messaging and management of RF systems, which 
includes setup, tasking, and monitoring of RF 
processing chains, and transport of lower-volume 
processed data messages. However, extensions to 
VICTORY are required to support the transport of 
large-volume signal data streams and to standardize 
the access and low latency control of the RF chain. 
MORA extends the scope of VICTORY by 
adding a low latency transport mechanism, data 
streaming 
interfaces, 
new 
message 
types, 
management operations, and functional concepts 
that are specific to RF applications.  
MORA decomposes RF components into logical 
groupings of interfaces enabling management, 
health monitoring, and dissemination of raw and/or 
processed data across two physical buses. It uses 
the VICTORY Data Bus (VDB) for access control, 
transport for publish/subscribe data streams, and 
device-level 
web-services 
for 
management.  
Additionally, 
it 
recommends 
leveraging 
VICTORY’s Position, Navigation, and Time 
(PNT) services. 
To achieve its goal, MORA also utilizes a specific 
implementation of standards from the VMEbus 
International Trade Association (VITA) for control 
and dissemination of data and context on the 
Proceedings of the 2019 Ground Vehicle Systems Engineering and Technology Symposium (GVSETS) 
Modular Open RF Architecture (MORA): Standardizing the RF Chain 
 
Page 3 of 8 
MORA Low Latency Bus (ML2B). VITA 49.0 
established standards for receive-only data and 
context 
while 
VITA 
49.2 
added 
transmit 
functionality and control messaging.  MORA 
leverages a subset of VITA 49.2 in a locked-down 
manner to support true interoperability. The 
MORA development group within the C5ISR 
Center worked closely with the VITA 49 Working 
Group to provide input and implement necessary 
changes in the 49.2 revision of the specification [4]. 
MORA’s dual bus architecture supports the varied 
latency and throughput constraints as well as 
providing a natural boundary for potentially 
sensitive data.  
 
4. BASIC CONCEPTS 
A MORA Device is an entity within a MORA 
system that contains signal resources and/or 
processing resources in support of receive and/or 
transmit operations. There are three MORA Device 
Types - Software Defined Radio (SDR), RF 
Conditioning 
and 
Distribution 
(RCD), 
and 
Radiohead (RHD).  The MORA specification is 
bounded to encompass two resource layers, known 
as 
MORA 
Signal 
Resources 
and 
MORA 
Processing Resources, as shown in Figure 1 below.  
These signal resources encompass the RF chain for 
both receive and transmit functions, including the 
antenna and extending to the analog-to-digital 
converter (ADC) / digital-to-analog converter 
(DAC).  This signal resource RF chain is further 
decomposed into five Signal Resource Types, 
including Antenna (ANT), RF Conditioning (RFC), 
RF Distribution (RFD), RF Frequency Translation 
(RFT), and Signal Domain Conversion (SDC).   
Figure 1: MORA Top-Down Perspective
Proceedings of the 2019 Ground Vehicle Systems Engineering and Technology Symposium (GVSETS) 
Modular Open RF Architecture (MORA): Standardizing the RF Chain 
 
Page 4 of 8 
The MORA Specification boundary also extends 
to those interfaces required to speak to standardized 
MORA Processing Resources. These Processing 
Resources are meant to be RF processes which will 
likely be reusable and/or of use to a third-party 
client.  Processing resources are component types 
that exist to convert raw data into useful 
information, convert information into raw data, or 
further process information and share it on the VDB 
in digestible formats for client consumption.  This 
alleviates the barrier of entry, simplifying the 
adoption by new and existing technologies to ingest 
EM/RF information. 
One such example, developed as part of a 
reference design, is a Direction Finding Engine 
(DFE). A DFE produces lines-of-bearing (LOB) 
information for signals of interest, derived from 
multi-channel digital receive signal data streams.  
Management interfaces includes task-specific 
settings such as the desired mode (set-on or scan), 
LOB type (2D or 3D), timing, duration, number of 
repetitions, 
repetition 
interval, 
frequency, 
bandwidth, and threshold. LOB information is sent 
to the client through its data interface on the VDB. 
This data interface includes task specific responses 
that include azimuth bearing and confidence, 
elevation bearing and confidence (for 3D types), 
received signal strength, and position (starting 
point of the LOB vector).  A DFE leverages MORA 
Signal Resources to obtain data streams for 
processing and subsequently provides situational 
awareness to any interested client through a set of 
standardized messages, consequently either adding 
capability to networked systems or reducing 
redundant processing. 
As shown in Figure 2, Signal Resource Types 
provide interfaces for basic components of the RF 
chain, while Processing Resources will either 
ingest or provide digital data and provide defined 
interfaces for tasking and response messages from 
applications. 
 
Figure 2: MORA Functional Perspective
Proceedings of the 2019 Ground Vehicle Systems Engineering and Technology Symposium (GVSETS) 
Modular Open RF Architecture (MORA): Standardizing the RF Chain 
 
Page 5 of 8 
5. CORE FEATURES 
One of the primary benefits of MORA is in the 
flexibility in system design implementation.  
MORA is unique from many other RF architectures 
in that it does not dictate where RF resources are 
implemented.  Instead, it simply defines how these 
resources announce their existence, their adjustable 
parameters, and their place in the larger system.  
This allows for a bottom-up discovery of resources 
and, through the defined interfaces which users and 
other MORA resources utilize, enables dynamic 
construction of an RF chain with mission-agnostic 
standard messages. 
MORA also supports partial implementations for 
capability and technology insertions into existing 
systems by offering standardized access to newly 
introduced 
MORA 
Signal 
and 
Processing 
Resources from other pre-existing, un-exposed 
resources already in place. MORA Signal 
Resources can also feed into newly introduced 
MORA Processing Resources, which in turn 
provide new capabilities to pre-existing application 
resources. 
Another core feature of MORA is its use of VITA 
Radio Transport (VRT) within its MORA Data 
Message (MDM) Type 1 for control and context of 
analog and digital signal streams. MDM Type 1 
messages provide command, data, and context of 
temporal and spectral data streams to/from radios 
and users to promote interoperability between RF 
systems. MDM VRT messages are defined within 
the MORA Specification and the ANSI/VITA-49.2-
2017 VITA Radio Transport (VRT) Standard [4]. 
The MORA Specification takes precedence over 
the VITA 49.2 Standard by limiting and providing 
further definition to ensure interoperability in 
MORA systems. 
 
6. MORA SPECIFICATION MATURATION 
MORA was introduced to the GVSETS 
community in 2015 at version 1.0 of the 
specification. Many aspects of the early versions of 
MORA have been enhanced over time as reference 
designs provided insight in how to improve the 
modularity and broaden the use cases supported. 
The MORA specification development team 
continually iterates over the specifications to 
address self-identified findings or those brought 
forth by its community. MORA has continued to 
evolve beyond its initial topology to encompass the 
entirety of the RF chain in an open and modular 
fashion. It has matured with the help of community, 
industry, and academia partners. Findings and 
feedback from reference builds, demonstrations, 
requests for information (RFI), and continued 
experimental developments have been incorporated 
into subsequent specification releases of MORA.  
Currently, the MORA Specification is at version 
2.3. 
 
7. MORA ARCHITECTURE DETAILS 
 
7.1. MORA Terms 
 
The “Basic Concepts” section above covers the 
overarching architecture and is not repeated here.  
MORA defines a number of terms, many of which 
will be briefly described here for context. 
 MORA Device: An entity within a MORA 
system that contains signal resources and/or 
processing resources in support of receive and/or 
transmit operations.  MORA Device types include: 
Radiohead, RF Conditioning and Distribution, and 
Software Defined Radio. MORA Device subtypes 
include Receive Only (RXO), Transmit Only 
(TXO, Transmit or Receive (TOR), and Transmit 
and Receive (TAR). 
MORA Signal Resource: A resource within a 
MORA Device that captures, radiates, conditions, 
distributes, translates, and/or converts RF signals in 
support of receive and/or transmit operations in a 
MORA system. Signal Resource types include: 
Antenna (ANT), RF Conditioning (RFC), RF 
Distribution (RFD), RF Frequency Translation 
(RFT), and Signal Domain Conversion (SDC). 
MORA Signal Port: A logical partition of signal 
resources with an external access point on a MORA 
Proceedings of the 2019 Ground Vehicle Systems Engineering and Technology Symposium (GVSETS) 
Modular Open RF Architecture (MORA): Standardizing the RF Chain 
 
Page 6 of 8 
Device in support of receive and/or transmit 
operations in an RF system. A MORA Signal Port 
consists of analog (radio frequency, intermediate 
frequency, or baseband) or digital (real or complex 
IQ in time or frequency domains) signals 
transported between devices in coaxial, copper 
wire, or fiber optic interconnect cables. MORA 
Signal Port classes include the Analog Signal, 
Digital Signal, and Reference Signal classes. 
MORA Processing Resource: A resource within 
a MORA Device that processes signal data into 
information, processes information into signal data, 
or further processes information in support of 
receive and/or transmit operations in a MORA 
system. A processing resource can contain either 
one signal port and one processing port or two 
processing ports. 
MORA Processing Ports: A logical partition of 
processing resources with an external access point 
on a MORA Device in support of receive and/or 
transmit operations in an RF system. Processing 
ports include management and data interfaces on 
the VICTORY Data Bus (VDB) and may also 
interface with signal resources through signal ports 
on the MORA Low Latency Bus (ML2B). The 
information consists of digital formats transported 
between devices in copper wire or fiber optic 
interconnect cables. 
 
7.2. MORA Component Types 
 
The four (4) MORA component types are (1) Low 
Latency Switch, (2) MORA Device, (3) MORA 
Signal Resource Manager, and (4) MORA Signal 
Port Manager. The Low Latency Switch defines 
requirements for switch(s) comprising the ML2B.  
The MORA Device component type is the logical 
representative of the hardware device as a whole.  
The MORA Device specific management interface 
supports file operations, configuration, device level 
commanding, and responding to queries for device 
status and description.  The waveform management 
interface (if supported, such as an SDR) also exists 
under MORA Device for reporting and managing 
available 
waveforms. 
The 
MORA 
Device 
interfaces with both the VDB and the Signal Port 
Manager for device level commanding, nominally 
via an intra-device medium. 
The MORA Signal Resource Manager component 
type is the logical representative of all RF Signal 
resources that are a part of the device.  Its specific 
management interface includes support for fetching 
signal port information and descriptions (RFC, 
RFT, or SDC and sub ports) in fine detail, 
management and reporting of reservations per 
signal 
port, 
reporting 
signal 
port 
default 
performance data, retrieving internal reference 
connections as well as static internal and external 
connections, and fetching antenna array and 
manifold band information. Additionally, the RF 
Distribution management interface (if supported, 
such as an RCD) exists for fetching switch group 
information, and management and reporting of 
reservations per switch group. The Signal Resource 
Manager interfaces with the VDB and the Signal 
Port Manager, nominally via an intra-device 
medium. 
The MORA Signal Port Manager component type 
has direct control of all of the signal ports and RF 
components, executing configuration, tuning, and 
commands received from MORA Device, MORA 
Signal Resource, or MORA Signal Port Manager 
clients. It uses implementation specific protocols to 
achieve this, allowing for MORA clients to 
communicate 
in 
standardized 
MORA 
Data 
Message (MDM) syntax, described later. Figure 3 
shows these component types in the high-level, 
dual-bus MORA Architecture with the three 
MORA Device Types. Figure 4, below, shows the 
high-level communication amongst the component 
types, and clients. 
 
7.3. MORA Data Messages 
 
Communication on the ML2B, or intra-device, is 
accomplished with MDMs. MORA adopts and/or 
adapts from VITA 49.2 specifications, which come 
from a standards body that has already defined 
Proceedings of the 2019 Ground Vehicle Systems Engineering and Technology Symposium (GVSETS) 
Modular Open RF Architecture (MORA): Standardizing the RF Chain 
 
Page 7 of 8 
protocol-agnostic messages in the extremely 
complex RF domain. There are currently seven (7) 
types of MDMs. 
MDM VITA Radio Transport (VRT) (Type 1): 
MDM VRT (Type 1) messages provide command, 
data, and context of temporal and spectral data 
streams to/from radios and users to promote 
interoperability between RF systems.  VRT Type 1 
messages have three (3) variants: VRT Command, 
VRT Context, and VRT Signal Data. 
MDM Acknowledge Message (Type 2): The 
MDM Acknowledge Message provides a positive 
acknowledgement to the sender of certain MDMs 
that a specific message was received by the 
recipient. In addition to delivery confirmation 
functionality, the MDM Type 2 also provides a 
means by which the recipient may further delineate 
success or failure in executing the delivered 
message. 
MDM Time of Day (ToD) Message (Type 3): 
The MDM Time of Day Message is used to achieve 
time synchronization between the VDB, which 
nominally has Network Time Protocol (NTP) 
and/or Precision Time Protocol (PTP) provided by 
a VICTORY Time Synchronization Service, and 
the Signal Port Manager on the ML2B. 
MDM Signal Port User ID Message (Type 4): 
The MDM Signal Port User ID Message is intended 
to provide a means to communicate that a 
reservation or release of a signal resource has 
occurred. 
MDM Health Message (Type 5): The MDM 
Health Message is used to convey health and status 
about the MORA Signal Port Manager, and its 
constituent parts, to the MORA Device and MORA 
Signal Resource component types so that the 
information can be converted to VICTORY’s 
Figure 3: MORA Component Types & Architecture
Proceedings of the 2019 Ground Vehicle Systems Engineering and Technology Symposium (GVSETS) 
Modular Open RF Architecture (MORA): Standardizing the RF Chain 
 
Page 8 of 8 
Syslog-Based Health Publishing Interface and 
format. 
MDM Command Message (Type 6): The MDM 
Command Message is utilized for course device-
level communication.  For instance, instructing the 
unit to go into a certain mode like operate, standby, 
or transmit inhibit, or actions like shutdown, restart, 
or zeroize.  
MDM Switch Port User ID Message (Type 7): 
The MDM Switch Group User ID Message is 
intended to provide a means to communicate that a 
reservation or release of switch group has occurred. 
 
8. CONCLUSION 
After various R&D implementations from 
community, industry, and academia partners, 
lessons learned helped to refine the MORA 
specification.  MORA v2.3 brings opens standards 
and thoughtful decomposition to the RF chain, 
radios, and applications for singular or multi-
mission capabilities.  Programs can reduce initial 
technical risk, cost, and schedule with MORA 
while lowering sustainment costs and reducing time 
to insert new capabilities in the long term. 
 
9. REFERENCES 
[1] Tri-Service Memorandum, “Modular Open 
Systems Approaches for our Weapon Systems is 
a Warfighting Imperative”, 07 Jan 2019. 
[2] CCDC C5ISR Center, “MORA Specification 
v2.2, 28 Sep 2018”, and “MORA Specification 
v2.3”, 20 May 2019. 
[3] Vehicular 
Integration 
for 
C4ISR/EW 
Interoperability 
(VICTORY) 
Standard 
Specifications, Version 1.7, 15 February 2018. 
[4] ANSI/VITA-49.2-2017 VITA Radio Transport 
(VRT) Standard for Electromagnetic Spectrum: 
Signals and Applications, Revision 00.55. 
 
Figure 4: MORA Component Type Interaction
