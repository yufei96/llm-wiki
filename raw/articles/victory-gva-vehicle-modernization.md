1

DEFENSE SOLUTIONS 

TECHNOLOGY 

WHITEPAPER

Read About

Ground vehicle modernization

Network integration evaluation 
and deployment

Achieving GVA and VICTORY 
goals through COTS solutions

Modern efforts like VICTORY and GVA are simplifying system upgrades and 

modifications and while reducing complexity.  

Ground Vehicle Modernization with 
VICTORY and GVA

Introduction

Historically, adding or enhancing command, control, communications, computers, 
intelligence, surveillance and reconnaissance (C4ISR) functionality in tactical ground 
vehicles has been a challenge. While advancements in technology have done much 
to improve vehicles’ capability in the field, such upgrades have typically burdened 
vehicles with cumbersome “bolt-on” electronics equipped with proprietary, stove-piped 
communication interfaces and numerous independent Global Positioning System (GPS) 
and Human Machine Interface (HMI) peripheral devices.  

As a result, modernizing ground vehicles to add new capabilities or feature the 
latest technology is unnecessarily complex. Upgrading technology with proprietary 
interfaces entails a costly and complicated migration process. As well, the lack of 
interoperability between in-vehicle systems results in redundant equipment, consuming 
excess power and taking up valuable real estate in an already constrained space that 
must accommodate people, ammunition and supplies. In this cramped environment, 
manually enabling communication between systems creates additional work for 
vehicle operators. Ultimately, these factors combine to create a poor, unsafe in-vehicle 
experience for warfighters, with reduced reliability and an increased chance of mission 
failure.

INFO: CURTISSWRIGHTDS.COM
EMAIL: DS@CURTISSWRIGHT.COM


2

Fortunately, modern efforts like the U.S. Army’s VICTORY 
(Vehicle Integration for C4ISR/EW Interoperability) initiative 
and the United Kingdom’s Ministry of Defence (MOD) Generic 
Vehicle Architecture (GVA) are paving the way for a modern 
battlefield where system upgrades and modifications are 
quicker and less expensive. This white paper will explore 
these two emerging and comparatively similar frameworks, 
highlighting key similarities and differences between these 
initiatives and discuss the benefits of using such frameworks 
in land vehicle upgrades and new builds.  

Forces Driving Modernization

Siloed governmental acquisition processes have historically 
led to ground vehicles featuring a number of duplicative and 
proprietary C4ISR systems. Today’s combat vehicles are 
typically deployed with multiple independent systems that 
have limited ability to share their functionalities or data. When 
a vehicle program office wants to put a new capability into a 
vehicle, the additional hardware usually comes with its own 
chassis, cables, keyboards, and other components. This 
results in unnecessary redundant hardware and software, 
which in turn increases cost and maintenance while taking 
up valuable space. Some vehicles, for instance, have 
multiple systems that all have independent GPS receivers, 
each with its own external GPS antenna, that draw from the 
same GPS source, but aren’t yet integrated together. 

A host of different strategic, operational and technological 
drivers are instigating change in modern vehicle electronics 
architectures. Budgetary pressures to reduce cost, 
requirements for specific networked technologies to 
improve situational awareness, governmental mandates 
for advanced GPS technologies, and the underlying size, 
weight, and power (SWaP) constraints of today’s tactical 
vehicle platforms are all key factors influencing this shift. As 
well, high-level fiscal pressures in the acquisition community 
are motivating governments to address these problems. 
Initiatives like Better Buying Power, VICTORY, GVA, and 
Modular Open Systems Approach (MOSA) are evidence of a 
global push for improved practices. Since there are currently 
many legacy systems that are difficult to upgrade because 
they can’t easily be pulled out and replaced, the goal of these 
initiatives is to ensure that new C4ISR systems or platforms 
don’t suffer from the same legacy stovepipe challenges, 
and are instead easily modified and upgradable due to 

device interoperability.  Additionally, the integration of open 
systems into vehicle designs will increase product availability 
and vendor competition, which will in turn “facilitate a more 
open market, improve procurement, enhance market 
competitiveness, and achieve smarter procurement and 
value-for money”.1 

With multiple different programs aiming to ease system 
integration and reduce complexity, it can be confusing 
to understand which framework should guide system 
architecture design. The obvious choice can be made if 
you are developing a ground vehicle for the U.S. (VICTORY) 
or the U.K. (GVA), but without the clear distinction, 
understanding the differences between VICTORY and GVA 
(as well as its global counterpart, NATO GVA) will give you a 
better understanding of which provides the right framework 
for your system architecture.  

The VICTORY specification was officially kicked off in 2010 
by the U.S. Army PEO C3T (Program Executive Office 
for Command, Control and Communications-Tactical) 
and a consortium of defense and industry participants, 
which included Curtiss-Wright. According to the VICTORY 
standards organization, the initiative “was started as a way 
to correct the problems created by the ‘bolt-on’ approach 
to fielding equipment on U.S. Army vehicles. Implementation 
of VICTORY enables tactical wheeled vehicles and ground 
combat systems to recover lost space while reducing 
weight and saving power. Additionally, implementation 
allows platform systems to share information and provide 
an integrated picture to the crews. Finally, implementation 
provides an open architecture that will enable platforms to 
accept future technologies without the need for significant 
redesign.” At its core, the VICTORY framework promotes the 
use of open standard physical and logical interfaces between 
LRU subsystems on C4ISR/EW combat vehicles. The open 
architecture standard is not intended to define how LRUs 
are built, but rather how these LRUs can intercommunicate 
and share data and resources, resulting in SWaP savings. 

In addition to decreasing the size, weight, and power 
consumption of the myriad C4ISR subsystems overcrowding 
the crew area inside a vehicle, VICTORY integration also 
increases situational awareness and reduces users’ 
operational burden. For example, the three major pieces of 
gear in a vehicle — the gun station on top of the vehicle, 
the threat detection system and the battle command system 

2

CURTISSWRIGHTDS.COM


3

CURTISSWRIGHTDS.COM

that tracks allies and adversaries - operate independently 
in a non-VICTORY design. In this scenario, when the threat 
detection system alerts troops that someone is shooting at 
the vehicle, the person at the battle command system must 
manually input the information. With VICTORY architecture, 
these systems are linked and can pass information to 
streamline operations, simplify the in-vehicle experience, 
reducing the risk of human error, and ultimately saving lives.

To ensure that companies can create VICTORY compliant 
systems, the U.S. Army built its own mature open source 
libraries, and used standard Ethernet protocols.  This 
enables the use of commercial off-the-shelf (COTS) switch 
and router products, with minimal change.  

The GVA Approach

Similar to VICTORY, GVA is an approach introduced by 
the U.K.’s Ministry of Defence to mandate open, modular, 
and scalable architectures in the design of land vehicles. 
Its standards apply to electronic and power infrastructures, 
mechanical interfaces, Human Machine Interfaces (HMI) and 
Health and Usage Monitoring Systems (HUMS). 

Outlined in Ministry of Defence Standard (Def Stan) 23-
09, the goal of the GVA approach is to realize operational, 

technical, and cost benefits by promoting open standards 
for software and hardware interfaces to enable simple and 
rapid replacements or upgrades of equipment as needed. 
Intended to be applied not only on new land vehicle designs, 
but also “whenever practicable by amendment to those 
already in existence”2, the GVA infrastructure encourages 
the use of adapters or gateways to enable interoperability 
with legacy equipment. Similar to VICTORY, GVA does 
not mandate specific solutions but specifies a generic 
architecture that is platform and vendor agnostic, which can 
be tailored to design requirements. Interoperability is enabled 
by the Data Distribution Service (DDS) middleware system, a 
generic software interface that allows the exchange of data 
between equipment of different manufacturers.

Comparing GVA and VICTORY

GVA and VICTORY have very similar goals and their approach 
is fundamentally different.  Where VICTORY specifically aims 
to provide an architecture for C4ISR/EW systems, GVA has 
a wider remit across the entire land vehicle platform (Tony 
White, 2018). Additionally, both standards are based on 
global open standards and make use of technology such as 
Ethernet but while GVA is freely available on the public U.K. 
MOD website, VICTORY is limited to U.S. citizens working 
on U.S. programs.   

VICTORY’s Vision

Figure 1: VICTORY Ethernet Architecture

Platform systems internally use native (proprietry / legacy) physical and data interfaces 

while providing VICTORY compliant interfaces for VDB

Ethernet 

(Copper or Fibre)

VDB enables the integration of...

Web Services Definition Language WSDL

VBD provides interfaces to ...

Open Standards Interface

VICTORY compliant systems from multiple vendors

Network 

Infrastructure

Shared 
Services

Management 

Services

Shared 

HW Services

Access Controls 

Services

Automotive  
(Vetronics)

Power 

Distribution

Lethality 
(Weapons)
Protection
Logistics

Data 

Protection

Situational 

Awareness & C2

Threat Detection 

& Reporting

Audio 

Communication

Video & 

Imagery SA

Mission 

Recording
Data Radios
EW Systems

VICTORY Databus

VICTORY Databus


4

CURTISSWRIGHTDS.COM

Figure 2: GVA Data Distribution Model

In the VICTORY architecture in Figure 1, all systems 
communicate over Ethernet, enabling shared use of data, 
signals and peripherals, such as a keyboard, across multiple 
pieces of equipment. To achieve this, system integrators create 
VICTORY software using open source libraries based on SOAP 
(Simple Object Access Protocol) to allow communication 
between devices over Ethernet and ensure interoperability. 
This service-based network (referred to as the VICTORY Data 
bus or VDB) is similar to GVA’s middleware approach based 
on the Data Distribution Service (DDS) messaging protocol 
and DDS wire protocol (DDS is an open standard released by 
the Object Management Group, a systems software standards 

organization), that enables inter-device communication 
across any common data bus.  Similar to VICTORY, GVA’s 
middleware approach decouples applications and enables 
“plug-in” integration, and does so through a real time 
publish/subscribe method of communication (Figure 2). 

Though VICTORY and GVA are similar in defining open 
standards software to increase technical flexibility and 
scalability of C4ISR/EW systems, GVA takes it a step further 
by including guidance on physical interfaces, HMI, and video 
distribution standardization across all the electronic systems 
on a ground vehicle. 

Data  

Connector

Data Connector
Data Connector
Data Connector

Power Management and Distribution

Data Connector

Data  

Connector

Data  

Connector

Data  

Connector

Data Distribution

Data  

Connector

Data Gateway

Legacy Role 
Equipmenet

Crew Station 
Equipment

Role Equipment

Platform

Power 
Adapter

Future Role 
Equipment

Human Machine 

Interface

HUMS

Def Stan  

23-09

Automotive 

Gateway

Automotive
Key


5

CURTISSWRIGHTDS.COM

Figure 3: VICTORY - Data-bus centric design

Scalable, Modular, Open 
System Technology 

Ease of integration of both new and legacy systems is 
streamlined through the use of scalable, modular, open 
systems technology. For this reason, both GVA and 
VICTORY emphasize the use of modular COTS systems.  

The GVA Def Stan 23-09 breaks down the definition of 
scalability to describe both horizontal and vertical capability 
expansion. It describes horizontal scalability (or “scaling out”) 
as the ability to scale system performance with the addition or 
subtraction of system elements, whereas vertical scalability 
(“scaling up”) “addresses how the existing architecture can 
be extended to provide additional performance (bandwidth, 
processing power, etc.) by exploiting existing spare capacity, 
simple replacement, or minor modification”3. As well, it 
posits that a modular architecture is “designed in such a 
way as to allow the replacement or addition of subsystems 
and upgrades as required without any undesirable emerging 
properties.”4 Both vertical and horizontal scalability is 
achievable by enabling communication between devices 
via the open source data distribution model, using software 
and connectors. Using modular, upgradable, COTS, open 

standards based systems or electronics increases system 
scalability with the ability to quickly add (or subtract) 
functionality. 

In the U.S., the Department of Defense (DoD) Modular Open 
System Architecture (MOSA) initiative is similarly driving 
the use of open system approaches for ground vehicles 
both from the technical and the procurement perspectives. 
VICTORY is a prime example of MOSA policy implementation 
and explicitly encourages the use of COTS open standards. 
VICTORY LRUs exploit cutting-edge commercial networking 
technology such as Web Services, SOAP, and XML through 
VICTORY open source libraries.  This ensures system 
interoperability and encourages VICTORY complaint COTS 
development resulting in modular, open COTS systems that 
are inherently scalable in a VICTORY Ethernet architecture.  

Leveraging a modular system architecture gives systems 
architects a great degree of freedom to scale and optimize 
vetronics to their platform mission requirements. As 
standards are leveraged for in-vehicle LRU subsystems, 
platform architects can implement multi-vendor solutions 
(which, by definition, should be interoperable) and phase-in 
support for relevant VICTORY or GVA component types, as 
needed.

Shared Network Fabric

Other 

Networked 
Subsystems

DBH-672 Digital Beachhead 

Shared Processor Unit with Integrated 

Ethernet Switch & GPS

Network Attached 

Storage

Radio/Digital Comms

Legacy Subsystems

Network Bridge

Laptop

Display
Network Router

Mission Computer


6

CURTISSWRIGHTDS.COM

Choosing Between GVA 
and VICTORY

While both are network-centric architectures that support 
equipment or service publishers and subscribers at an 
application software level, VICTORY provides the architecture 
to support C4ISR/EW systems and GVA includes direction 
on physical cables, connectors and electrical interfaces as 
well as common HMIs.  Modern frameworks, both GVA and 
VICTORY architectures are based on a common Ethernet 
data-bus and rely on the concept of network adaptors or 
connectors; VICTORY uses SOAP and XML to publish data 
or provide access to networked systems and GVA uses 
the DDS to do the same. In theory, GVA and VICTORY are 
interoperable with the addition of software that supports 
both frameworks and converts messages from one to the 
other.  While full interoperability between the frameworks will 
require years of development and convergence, today, the 
use of middleware can enable a VICTORY compliant system 
to work in GVA architecture. 

Upgrading versus New Build

One of the key reasons for moving to either standard is to 
enable quicker integration or upgrade of components.  Both 
standards are driven by the need to easily change out a 
vehicle’s role/capability by simply disconnecting network 
cables and connecting the new device to the system.  Ideally, 
adding and removing software wouldn’t be necessary, nor 
would modifications to cabling.  Though this is the long-term 
goal, it isn’t immediately achievable to update an existing 
system to either architecture. When updating existing 
systems, significant software configuration is required to 
enable communication when plugged into the system. 
If all new systems are GVA or VICTORY compliant, future 
generations of land vehicles will reap the interoperability 
benefits of GVA or VICTORY architectures implemented 
today. 

Compliance

Though it is easy to use these standards as design 
guidelines, being fully compliant to either is very costly and 
time consuming for system developers.  GVA does not have 
a third-party certification house that can determine if your 
product is compliant. Instead, it is left with system developers 

to determine their own compliance given the available 
documentation on GVA. VICTORY, on the other hand, 
supplies developers with a test suite that enables companies 
to self-test compliance.  Passing the test enables you to 
call your system compliant and ensures interoperability with 
other systems in a VICTORY architecture.  

Compliance to either standard can be a lengthy process with 
much room for error and, due to lack of industry knowledge 
of either standards, compliance might still leave customers 
confused.  For example, you can develop a mission computer 
that has Ethernet and the ability to run VICTORY software, 
but it is up to the customer to develop, install and manage 
the software to get their system to be VICTORY compliant.  
Similarly, a product may claim to be GVA compliant but that 
could just mean that, given the correct software, it could 
communicate with the GVA data model.  

Similar Frameworks around the World

Adoption outside of the U.S. and U.K. is also seen, with 
approaches like NATO GVA (NGVA) and Australian Generic 
Vehicle Architecture (AS GVA). These variants widen GVA’s 
reach and promote interoperability and standardization 
between systems from allied nations.  

Similar to GVA, NGVA is “an open standards-based 
approach to the design and integration of multiple electronic 
subsystems onto a military vehicle, which are controllable 
from a multifunction crew display and control unit. It has been 
based on the U.K. [Ministry of Defence] GVA approach but 
NGVA strives to enhance and expand it.”5 The NATO GVA 
enhancements to GVA include coverage for a wider range 
of platforms such as unmanned vehicles and additional 
requirements on, for example, the Crew Terminal Software 
Architecture.  Like GVA, NATO GVA uses the DDS and Land 
Data Model.

Also derived from GVA, AS GVA is defining a Land Data 
Model  and DDS for seamless information exchange across 
a common communication network. An example of AS 
GVA’s success can be seen in General Dynamics’ Ajax 
armored vehicle, touted as the most advanced armored 
fighting vehicle available.6 Its digital architecture featuring 
GVA allows common interfaces for all the sensor systems, 
communications and extra screens to be plugged in 
without requiring re-engineering of the vehicle every time 
it’s upgraded.


7

CURTISSWRIGHTDS.COM

Conclusion

In today’s budget climate, VICTORY and GVA ready 
solutions are well positioned for use in enhancement 
upgrade packages, as well as new designs, to help 
reduce the number of boxes that are needed to add 
capabilities into a particular ground vehicle over time. 
VICTORY and GVA also help combat obsolescence, since 
their core principles mandate interoperability and enable 
an upgrade path that speeds and eases the addition of 
new capabilities to vehicles in the future.

The promise of both VICTORY and GVA standards is that 
its wide adoption will help to increase interoperability, 
eliminate redundant functionality and hardware, and 
ultimately reduce vehicle acquisition and upgrade costs. 
By all indications, the VICTORY and GVA standards 
have passed the “tipping point,” and have now become 
a de facto requirement, and common line-item, in many 
requests for proposal (RFP) issued by the DoD, MOD 
and system integrators. Government Program Executive 
Offices (PEOs) are now commonly stipulating these 
standards as a requirement for upgrades. Commercial 
vendors, including Curtiss-Wright’s Defense Solutions, are 
already beginning to see VICTORY and GVA compliance 
as a requirement for new light tactical vehicle subsystems, 
as well as in the emerging modernization requirements for 
combat vehicle platforms.

Functionally, both VICTORY and GVA address the same 
needs for lower cost system development, reduced 
redundancy, and higher communication and cooperation 
between stove-piped systems. Both standards achieve 
this but with different languages.  Choosing which 
framework, if any, is best for you depends on a number 
of factors, including where the system or subsystem will 
be fielded (VICTORY for U.S., or GVA for U.K.), the type 
of system being developed, and if it is an upgrade or new 
build.  

At the frontline of bringing the VICTORY and GVA 
architecture 
into 
ground 
vehicles, 
rugged 
COTS 

technologies from Curtiss-Wright are helping to showcase 
the benefits of adopting a common communications 
architecture 
and 
consolidating 
modern 
computing 

and networking architectures for SWaP optimization. 
Leveraging over 80 years of experience and expertise 
developing rugged, field-proven defense technology, 
Curtiss-Wright has engineered its GVA and VICTORY 
ready solutions to not only optimize SWaP, flexibility and 
modularity in ground vehicle systems, but also ensure 
scalability and interoperability with legacy systems.  Beyond 
providing these benefits to ground vehicle designers and 
the armies they provide for, these open standards-based 
solutions improve the in-vehicle experience for today’s 
warfighters. By reducing system complexity and clutter 
while enhancing situational awareness, Curtiss-Wright 
solutions like the DBH-670 and DBH-672 switch router 
and GVDU Mission Display provide the performance and 
reliability ground vehicle operators can trust to protect 
them as they protect our nations.


8

Authors

8

Lisa Sarazin 
Marketing Portfolio Manager 
Curtiss-Wright Defense Solutions

Aaron Frank, BaSC 
Senior Product Manager 
Curtiss-Wright Defense Solutions

Elisabeth O’Brien 
Manager of Portfolio Marketing 
Curtiss-Wright Defense Solutions

Val Chrysostomou 
Product Manager 
Curtiss-Wright Defense Solutions

© 2019 Curtiss-Wright. All rights reserved.  Specifications are subject to change without notice.  
All trademarks are property of their respective owners   I   W169.0519

CURTISSWRIGHTDS.COM

References

1. National Security Through Technology: Technology, Equipment, and Support for   

 U.K. Defence and Security, U.K. Ministry of Defence

2. Ministry of Defense Standard (Def Stan) 23-09

3. Def Stan 23-09

4. Def Stan 23-09

5. NATO Generic Vehicle Architecture

6. GDLS pitches Ajax IFV for LAND 400 Phase 3

Learn More

GVDU Mission Display

DBH-672 Digital Beachhead

DBH-670 Digital Beachhead

DuraCOR 80-41 Mission Computer

DuraNET 20-11 8-port Ethernet Switch

DuraNET 20-10 20-port Ethernet Switch

VPX3-671 – 3U VPX Ethernet Switch

Vehicle Integration for C4ISR/EW Interoperability (VICTORY)


