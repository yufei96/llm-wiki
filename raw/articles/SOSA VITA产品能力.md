SOSA PRODUCT OVERVIEW
1
1
Sensor Open Systems
ArchitectureTM (SOSA)
Technical Overview and 
Product Guide
SYSTEMS SOLUTIONS
www.elma.com
ELMA.COM
ELMA.COM
3
3
SOSA PRODUCT OVERVIEW
SOSA STANDARD OVERVIEW
The Sensor Open Systems Architecture™, more commonly referred to as the SOSA™ Technical Reference Architecture, leverages and 
brings together multiple open standards to define and apply a common modular and interoperable approach to systems used in both 
defense and rugged commercial applications. At the core of SOSA’s hardware specifications is VITA 65 - or OpenVPX - a widely ad-
opted architecture and form factor for rugged, high-performance computing. The OpenVPX family of open standards defines system-lev-
el interoperability for modular multi-vendor integrated platforms. The OpenVPX standard defines clear interoperability points necessary 
for integration from module to module, module to backplane and backplane to chassis.
The SOSA standard is called out in a 2019 memo issued by the U.S. Department of Defense (DoD) and signed by the secretaries of 
the Army, Air Force and Navy. It calls for the adoption of open standards  in development activities for future weapon system modifica-
tions and new start development programs. MOSA is now codified into U.S. law (U.S.Code-2021, Title 10. 2446a, Part IV, Chapter 
144B, Sec 2446a); after January 1, 2019, major defense acquisition programs “shall be designed and developed with a modular 
open system approach to enable incremental development and enhance competition, innovation, and interoperability.”
1.	 Establish an Enabling Environment
2.	 Employ Modular Design
3.	 Designate Key Interfaces
4.	 Use Open Standards
5.	 Certify Conformance
Elma is a participant and key contributor to open standards such as VITA, SOSA, PICMG and others. We have a long history of build-
ing proven products based on these standards, and have proven expertise in rugged solutions for both development and deployment 
on air, ground and shipborne platforms.
The VITA trade association provides members with the ability to develop and design products based on open standards. The VITA 
Standards Organization (VSO) is an ANSI-accredited group that provides members with a means to work together to define and 
develop key computer specifications such as the family of VPX standards, which include those listed below. Elma is a key contributor 
to several of the Working Groups within VITA.
VITA FAMILY OF STANDARDS
SOSA TECHNICAL REFERENCE STANDARD
17.3
Serial Front Panel Data Port (sFPDP) Gen 3.0
42
XMC mezzanine cards
46.0 
VPX
46.30 & 
.31 
Higher Data Rate VPX
46.4 
PCI Express on VPX
46.6 
Gigabit Ethernet Control Plane on VPX
46.7 
10 Gigabit Ethernet on VPX
46.9 
XMC Mapped Rear IO on VPX
46.10 
VPX RTM
46.11 
System Management on VPX
47.0-3 
Environmental
48.2
VPX REDI: Mechanical Cooling
48.4
VPX REDI: Liquid Flow Through Cooling
48.8 
VPX REDI: Air Flow Through Cooling
49.0 
Radio Transport & RF Signals
62.0 
VPX power supplies
65.0 
OpenVPX
65.1 
New Slot and Module Profiles
66.0 
Optical Overview
66.1 
Optical Full size Dual MT variant
66.2 
Optical ARINC 801 Termi variant
66.3 
Optical Mini Expanded Beam
66.4 
Optical Half size MT variant
66.5
Optical Interconnect on VPX - Hybrid Variants
67.0 
RF and Mixed Signal overview
67.1 
3U RF
67.2 
6U RF
67.3 
Flexible multi-level RF on VPX
68 
SpaceVPX
68.0 
VDSTU VPX SI
68.1 
VDSTU VPX SI backplane
68.2 
VPX SI Mezzanine (under development)
90.0-7
VNX+
Fat Pipe: A channel that is comprised of four links (4 Tx pairs + 4 Rx pairs) is now being referred to as a Fat Pipe or 
by use of the x4 nomenclature. 100GBASE-KR4 and 40GBASE-KR4, PCIe-x4.
Thin Pipe: A channel that is comprised of two links (2 Tx pairs + 2 Rx pairs) is now being referred to as a Thin Pipe 
or by use of the x2 nomenclature.  10/100/1000BASE-T, PCIe-x2.
Ultra-thin Pipe: A channel that is comprised of one link (1 Tx pair + 1 Rx pair) is now being referred to as an Ultra 
Thin Pipe or by use of the x1 nomenclature. 10GBASE-KR, 1GBASE-KX, PCIe-x1.
PIPES: FAT, THIN, ULTRA THIN
Rx1+ Rx1-
Rx2-
Rx2+
Rx3-
Rx3+
Rx4-
Rx4+
Tx1+ Tx1-
Tx2-
Tx2+
Tx3-
Tx3+
Tx4-
Tx4+
Tx1+ Tx1-
Tx2-
Tx2+
Tx3-
Tx3+
Tx4-
Tx4+
Rx4+ Rx4-
Rx3+ Rx3-
Rx2+ Rx2-
Rx1-
Rx1+
Rx1+ Rx1-
Rx2-
Rx2+
Tx1+ Tx1-
Tx2-
Tx2+
Tx1+ Tx1-
Tx2-
Tx2+
Rx2+ Rx2-
Rx1-
Rx1+
Tx1-
Rx1+ Rx1-
Tx1+
Tx1+ Tx1-
Rx1-
Rx1+
2
ELMA.COM
ELMA.COM
4
5
5
3U  Plug-in Module Power Supplies
Pin name
2017 usage
Proposed     
Recommendations
VS1
+12 VDC
+12 VDC
VS2
+3.3 VDC
Not used
VS3
+5 VDC
Not used
+12V AUX
+12 VDC
Not used
-12V AUX
-12 VDC
Not used
3.3V AUX
+3.3 VDC
+3.3 VDC
VBAT
+3 VDC
+3 VDC
SOSA STANDARD OVERVIEW
SOSA STANDARD OVERVIEW
PROFILES
SLOT PROFILES
PROFILES
MODULE PROFILES
VITA 65 defines OpenVPX in terms of four types of Profiles: Slot Profiles, Backplane Profiles, Module Profiles and Chassis Profiles. 
Slot profiles are differentiated by their type (payload, switch, peripheral, etc.) and the arrangement of planes and other communi-
cations ports, including apertures for blind-mate optical and/or coaxial connections. SOSA further refines VITA 65 by defining a 
specific subset of 3U and 6U slot profiles.  These profiles can be described as Payloads, Switches, Radial Clocks, or External I/O. 
The standard also defines a set of approved protocols that can be implemented by Plug In Cards (PICs) for each of the define Pipes 
or general communications ports. 
IO Intensive:  
This is a 
general purpose 
single-board 
computer slot 
profile.
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
External I/O:  This 
was included in SOSA 
to address the need of 
bringing large numbers 
of legacy I/O into or out 
of the system.  SOSA has 
specific rules on the use 
of this profile.
Primary and Secondary Pay-
load or Compute Intensive:  
These are the main heavy-duty 
processing and payload 
profiles.  The differ in the size 
of the coax/optical aperture 
and the number of Expansion 
Plane lanes.
Switches:  These were 
chosen to address specific 
use cases required by SO-
SA-based systems 
3U
6U
Payload: 
Two payload 
profiles, one 
with XMC 
mapped pins 
and one with 
extra expan-
sion plane 
lanes.
Switch: 
Data 
Plane/
Expansion 
Plane 
switch slot 
profile
External I/O: 
Provides similar 
functionality 
and with the 
same rule set 
as the 3U 
version.
High-density 
coax/optical: 
Similar to the 
3U variant
To capture what particular protocols are supported 
by a particular PIC, a mechanism called the 
Alternative Module Profile Scheme (AMPS) is used.  
AMPS defines a string that includes a set of protocol 
fields enumerated in a manner so that one can 
quickly determine what protocols a particular PIC 
can support.  The AMPS string is constructed using 
the following format:
Figure 1: Alternative Module Profile Scheme (AMPS) String Con-
struct.  From SOSA Technical Standard, Version 1.0
SLT3x-TIM-2S1U22S1U2U1H-14.9.2-n
Radial Clock: 
Intended to drive 
common high-pre-
cision radial 
clocks (REF_CLK 
and AUX_CLK) 
across the back-
plane.
POWER AND SYSTEM MANAGEMENT
SOSA refined the rules from VITA 46.0 and VITA 65.0 regarding power.  Specif-
ically, it calls out that only the VS1 rail (12VDC) is to be used by SOSA aligned 
plug-in cards for primary power, while 3.3V_AUX is limited to system management 
functions and VBAT to powering real-time clocks.  This is an important feature of 
SOSA.  Prior to this rule, vendors could use whatever ratio of the three input power 
rails (VS1=12VDC, VS2=5VDC, and VS3=3.3VDC).  The result was that for any 
particular integrated system there was an unpredictable consumption ratio of these 
three rails, making it difficult for power supply vendors to offer truly COTS power 
supplies.  SOSA solved this, and there is a growing selection of VITA 62 and 
stand-alone power supplies available on the market. 
An important element in the SOSA architecture is System Management.  
Not only is there a SOSA module named System Manager (Module 1.1), 
but it defines both an in-band and out-of-band communication and control 
mechanism.  The out-of-band mechanism is based on the VITA 46.11 
standard. 
The Intelligent Platform Management Controller (IPMC) found on each 
SOSA Plug-in Card, along with the Chassis Manager Module (CMM) 
which interfaces with the System Manager and provide the overall hard-
ware control and monitoring function are two key elements of the System 
Manager subsystem.  Elma offers a range of products to address both of 
these functions, all SOSA aligned. 
Each code in this format has a set of values representing the approved protocols, with appropriate modifiers.
The approved protocols include:
• 	 Data Plane: PCI Express, Ethernet (1000BASE-KX, 10GBASE-KR, 10GBASE-KR4,
	
40GBASE-KR4, 25GBASE-KR, and 100GBASE-KR)
• 	 Control Plane: Ethernet (1000BASE-KX, 10GBASE-KR, 25GBASE-KR)
• 	 Expansion Plane: Dependent on the profile, but generally PCIe, Ethernet, S-FPDP, and LVDS
• 	 Other ports such as USB, Serial UART, DisplayPort, etc.
To learn about AMPS strings and the approved SOSA protocols see the SOSA Technical Standard.
SYSTEM MANAGEMENT                      
High-density 
coax/
optical:  This was 
introduced into 
SOSA primarily to 
provide a coaxial 
switching capa-
bility.
ELMA.COM
SOSA PRODUCT OVERVIEW
7
7
ELMA.COM
SOSA TECHNICAL OVERVIEW
6
ELMA PRODUCTS ALIGNED TO SOSA
Signal Integrity is the backbone of our Backplane designs
3U Backplanes
Available in standard or 
customized configurations of 
any or all with any slot profile 
for PICs aligned to SOSA. 
7
7
As a leading contributor to open standards like SOSA that support the DoD’s MOSA initiatives, Elma’s backplanes are de-
signed in alignment with The Open Group® Sensor Open Systems Architecture™  Technical Standard, or SOSA™, in slot 
counts from 2 to 12.
They provide the foundation for high-performance mission-critical systems requiring lower life-cycle costs and rapid technology 
insertion. They enable complex, high speed signal processing systems with the latest optical fiber and RF connectivity as well as 
slot profiles for SBCs and payload expansion.
The backplanes support high-speed signals on all data paths and VITA 67.3 connectors and VITA 66.5 optical connectors.
Developers can use the development backplanes as configured or work with Elma to identify your specific profile configuration needs.
As the leader in open standards backplane design and manufacturing, our cutting-edge signal integrity analysis informs the 
designs of our high-speed backplanes, handling critical data at high performance speeds.
Backplanes for Specific Cooling Schemes
VITA 48.x calls out specific configurations to 
accommodate specialty cooling methods.  3U 
backplanes are available in wider spacing for 
cooling standards such as VITA 48.8 for air 
flow-through (AFT) or VITA 48.2 for liquid 
flow-through.
6U Backplanes
6U backplanes are part 
of the standard and are 
available by request.
POWER AND GROUND
Power & Ground Only Backplanes
Elma’s wide selection of power and ground only backplanes provide 
a cost-effective solution those who are developing their own cards or 
haven’t decided on the slot configuration of their system. The only 
assigned pins are 3.3V, 5V, 12V, GND, and utility plane signals.  
The remaining pins are user-defined and pass through from front to 
rear. The rear connectors are all fully populated and can be acces-
sed with Elma’s slot-to-slot or slot-to-I/O bulkhead cable assemblies or 
rear transition modules for system development.
Power Interface Boards (PIBs)
Designed to facilitate the use of pluggable VITA 62.x power supply 
modules in systems requiring them. Elma’s standard backplanes use power 
studs which are typically wired to standalone (frame) power supplies. With 
PIBs, customers can choose between Elma’s standalone (frame) power 
supplies and pluggable VITA 62.x supplies.
Find What You Need with Interactive Backplane Charts 
Our backplane charts are designed to show a list of the profiles 
included in each available backplane configuration. Mouse over 
the backplane model number, and it will show you the backplane 
topology at a glance. 
SOSA BACKPLANES
At speeds up to 100GBASE-KR4, every feature of backplane design can influ-
ence signal integrity (SI) – every trace, layer separation, turn bend, via, via transi-
tion, etc. Elma’s signal integrity analysis and simulations consider every element in 
the channel to ensure optimal performance. 
We focus on each feature individually to model the complete channel 
and optimize the return loss for each. Once modeled, they are concat-
enated together along with the trace and connector models to create 
the complete channel. Today’s critical high-speed systems require noth-
ing less than reliable, repeatable solutions - every time.
ELMA.COM
ELMA.COM
SOSA PRODUCT OVERVIEW
SOSA PRODUCT OVERVIEW
8
9
9
Our lineup of easy access development platforms significantly enable fast and 
efficient system design and integration as well as testing of plug-in cards (PICs) 
aligned to SOSA.
Features include open frame formats for probing and quick board changes; 3U 
VPX backplane with 1-12 profiles aligned to SOSA (or power and ground only for 
board development); rear transition slots; chassis management; fixed or plug-in 
power; choice of air- and/or conduction-cooled card guides, VITA 48.x cooling, 
and more.
DEVELOPMENT CHASSIS
DEPLOYMENT-READY RUGGED ENCLOSURES
Developing high-speed signal processing equipment for harsh 
SWaP constrained installations requires a holistic design 
approach in which Elma excels. Optimal chassis designs must 
consider the payload power envelope in conjunction with 
extremes in temperature, shock, vibration, ingress, EMC and 
other environmental factors. Elma supplies chassis for use across 
a range of defense programs serving on land, sea or air. Our 
standard and custom chassis designs are available with a range 
of cooling choices: conduction cooling, air cooling, or hybrid 
conduction and air-cooled models, and liquid cooling. Choose 
from aluminum or composite chassis construction.
The COTS 12R1 and 12R2 19” rackmount chassis are
high-quality and cost-efficient rugged enclosures for
defense applications. It includes up to 14U high models
for 3U and 6U Plug-In Cards. Intended to withstand the
demands of a military environment, the 12R1 (lightweight
rugged) and 12R2 (fully rugged) are designed to
meet benchmark military standards.
19" CHASSIS - MIL RUGGED
TYPE 12R1 & 12R2 CHASSIS FAMILIES
SOSA ALIGNED DEPLOYABLE ATRs
RUGGED ENCLOSURES
This family of rugged enclosures has been specifically
designed to accommodate 3U 25Gb dual domain
backplanes and plug-in cards aligned to SOSA. Unit is
conduction-convection cooled to maximize airflow and
cooling (other cooling methods supported). VITA 46.11
Tier 3 out of band (OoB) chassis manager. Designed to
meet most environmentally rugged MIL standards.
Accelerate your time to deployment with our development chassis 
for 3U OpenVPX plug-in cards aligned to SOSA™
CompacFrame
Lightweight and compact, this
platform family comes in a
Slimline unit for 1-4 slots, or or a
mid-range unit for up to 8 slots
or 5 AFT (VITA 4.8) wide slots.
E-Frame Platform
This full-sized platform ships with a 
12-slot backplane that includes all 
SOSA 1.0 & CMOSS slot profiles. 
Optional 2-slot PIB for VITA 62     
plug-in power supplies.
D-Frame Platform
When space is at a premium, or 
you need take it on the road, the 
D-Frame is the smallest platform 
available. It can accommodate 
up to four 3U PICs.
Choose the Development Platform That Best Fits Your Needs:
This enclosure family is designed to meet the dimensional require-
ments of the CMOSS Mounted Form (CMFF) and Standard A-Kit 
Vehicle Envelope (SAVE) trays. This fieldproven platform ships in 
multiple PIC slot configurations of 3U backplanes aligned to SOSA.
CMFF
ELMA.COM
ELMA.COM
SOSA PRODUCT OVERVIEW
SOSA PRODUCT OVERVIEW
10
11
11
Plug-In Cards (PICs) Aligned to SOSA
Elma platforms aligned to SOSA are functionally tested and proven 
to work with top tier plug-in card suppliers, an essential step in 
building mission-critical systems for use in defense applications. 
Elma can help select or ensure that the complement of boards for 
your system are functionally interoperable in your development or 
deployed system.
PLUG-IN CARDS
Compute-Intensive Payload Cards (SBCs)
High performance processing features on lea-
ding-edge single board computers and GPGPU 
processors. Other boards that fit this profile are 
FPGA cards, RF transceivers, microwave tuners, and 
software-defined radio (SDR) cards.
Networking
High-performance Ethernet switches are the communication 
building blocks of a system. Elma offers boards supporting 
either single or dual planes, up to 100 Gbps on copper or 
optical interfaces, with field-proven software management of 
Layer 2 & 3 configurations.
IO-Intensive Payload Cards (SBCs)
These cards are general purpose single board 
computers with Intel or ARM-based CPUs for high 
performance processing.
Our COTS sub-system embedded designs are realized through a combination of best in classs partner products and Elma‘s 
field-proven chassis management, I/O and networking boards.  – integrated with renowned Elma packaging solutions. Elma 
has established, long-term relationships with highly qualified industry leaders, teaming to deliver the best solutions for mission 
critical applications the world over. As a trusted provider of integrated COTS solutions and board products to the defense in-
dustry, we support long-term defense programs with leading-edge technologies and crucial legacy solutions that keep systems 
up and running.
10
ELMA.COM
SOSA PRODUCT OVERVIEW
SOSA PRODUCT OVERVIEW
12
13
13
ELMA.COM
Power Supply cards
VITA 62 defines a the power connector for the 
backplane or interface board and the module that 
can be plugged into a SOSA aligned system. PSUs 
currently support up to 750W each.
Cabling for Development
Compliant to the latest VITA 46 specifications, ca-
bling assemblies are ideal for backplane and system 
development. They can be used to make I/O and 
slot-to-slot connections.
Radial Clock Cards (PNT)
The Radial Clock profile supports cards that provide 
accurate position, navigation, and timing (PNT) solu-
tions. It is critical to precise navigation solutions.
Our COTS sub-system embedded designs are realized through a combination of best in classs partner products and Elma‘s 
field-proven chassis management, I/O and networking boards – integrated with renowned Elma packaging solutions. Elma 
has established, long-term relationships with highly qualified industry leaders, teaming to deliver the best solutions for mission 
critical applications the world over. As a trusted provider of integrated COTS solutions and board products to the defense in-
dustry, we support long-term defense programs with leading-edge technologies and crucial legacy solutions that keep systems 
up and running.
EMBEDDED BOARDS
FIELD-PROVEN PERFORMANCE
Modular Interoperability Comes in Many Functions
Elma works with many partners in the community that 
SOSA has enabled. Whether it‘s high performance net-
working or storage, or support for legacy and discreet 
I/O interfaces, we are well connected to the community 
in order to support unique requirements. 
Chassis Management
Maximizing system uptime is critical. Elma‘s chassis 
management products provide Tier 3 and Out-
of-Band features to ensure proper operation of 
platforms aligned to SOSA.
External I/O & High-Density Coax/Optical Cards
This slot profiles address legacy I/O commonly found in aircraft discreets and well as commonly found RF switching boards.
SOSA PRODUCT OVERVIEW
12
ELMA.COM
ELMA.COM
SOSA PRODUCT OVERVIEW
14
15
15
Elma provides program oversight from initial project definition through final 
delivery. Project level activity tracking is managed by a designated individual 
who serves as a communication hub for status updates. The goal of our 
experienced program management team is to ensure on-time delivery of 
systems that meet project specifications.
“
Program Management
Quality - Assured
An Experienced Approach
SERVICES AND CAPABILITIES
Open standards architectures form the backbone of our embedded computing designs. Our team of mechanical and electrical 
design engineers are experts in enclosure configuration, complex thermal management, I/O interconnects, EMC, shock & 
vibration, system monitoring, as well as lifecycle management and reliability considerations.
We perform rigorous design and test with in-house design verification and testing, including thermal chambers and vibration 
tables. The lab enables Elma engineers to thoroughly test and verify performance each step of the way.
We use the latest in 3D modeling, thermal analysis, structural analysis and signal integrity software, and apply a modular 
building block approach to leverage proven designs for new system concepts. Combine all this with a proactive product life-cycle 
management system for the long-term support and reliability you need.
Elma is an ISO 9001: 2015 and AS9100 certified supplier. All of our quality procedures are implemented and 
maintained in accordance with those standards. At Elma, we strive for excellence by practicing completeness, 
accuracy, timeliness, and by exceeding expectations in everything we do.
SERVICES AND CAPABILITIES
 › Signal integrity and simulation​
 › EMC and ESD experience
 › Cooling and thermal simulations
 › Shock and vibration mitigation
 › Integration of displays and touch screens
 › Digital printing technologies 
 › Front panel and enclosure customization
 › Sub-system integration and assemblies
Elma hires the best teams for all phases of the customer journey 
– from initial design with the product and engineering teams, to 
manufacturing and project management, our people are experts 
in providing every process along the way. Below are some of the 
services and capabilities we offer.
SOSA PRODUCT OVERVIEW
SOSA PRODUCT OVERVIEW
14
www.elma.com
Elma Electronic AG,  
Switzerland
Hofstrasse 93
CH-8620 Wetzikon
T: +41 44 933 41 11
F: +41 44 933 42 15
sales@elma.ch
Elma Electronic GmbH,  
Germany
Stuttgarter Strasse 11
D-75179 Pforzheim
T: +49 7231 97 34 0
F: +49 7231 97 34 97
info@elma.de
Elma Electronic France SA
16 rue de Hannah Arendt 
Parc des Forges
F-67200 Strasbourg
T: +33 38 85 67 25 0
sales@elma-electronic.fr
Elma Electronic UK Ltd.
Solutions House
Priory Business Park
Fraser Road
Bedford MK44 3BF
Great Britain
T: +44 1234 838822
F: +44 1234 836650
sales@elma.co.uk
Elma Electronic Romania SRL
Chisoda, DN 59 km8 + 550m
RO-307221 Judetul Timis
T: +40 374 480 400
F: +40 256 249 820
sales@elma.ch
Elma Electronic Israel Ltd.
34, Modi'in St., I.Z.Sgula
IL-49271 Petach-Tikva
T: +972 3 930 50 25
F: +972 3 931 31 34
sales@elma.co.il
Elma Electronic Inc., USA
44350 S. Grimmer Blvd
Fremont, CA 94538, USA
T: +1 510 656 3400
F: +1 510 656 3783
sales@elma.com
Optima Stantron, USA
2305 Newpoint Parkway
Lawrenceville, GA 30043, USA
T: +1 770 496 4000
F: +1 770 496 4026 
sales@elma.com
Elma Electronic Private Ltd., 
India
Green Arch
3rd Phase 1st Main
J.P. Nagar
Bangalore 560078
sales@elma.com
Elma Asia Pacific Pte. Ltd., 
Singapore
8 Ubi Road 2
# 07-14 Zervex Building
SG-408538 Singapore
T: +65 6479 8552
F: +65 6479 8662
sales.elmaap@elma.com
Your local solution partner
Edition 10/23
