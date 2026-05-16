 

Modular Open Systems Approach (MOSA) 

Reference Frameworks in Defense Acquisition Programs 

 
 
 

 

 
 
 

MAY 2020  

 
 
 

Deputy Director for Engineering  

 
 
 
 
 
 
 

Office of the Under Secretary of Defense for Research and Engineering, 
Director of Defense Research and Engineering for  
Advanced Capabilities  

 

Washington, D.C. 

 

Distribution Statement A.  Approved for public release.  Distribution is unlimited.   
DOPSR Case # 20-S-1275.


 

MOSA Reference Frameworks in Defense Acquisition Programs 

ii 

 
 
Modular Open Systems Approach (MOSA) Reference Frameworks in Defense Acquisition 
Programs 
 
 
Office of the Under Secretary of Defense  
Research and Engineering 
3030 Defense Pentagon 
Washington, DC 20301-3030 
  
Distribution Statement A. Approved for public release.  Distribution is unlimited.   
DOPSR Case # 20-S-1275. 
 


 

MOSA Reference Frameworks in Defense Acquisition Programs 

iii 

Contents  
 

EXECUTIVE SUMMARY .................................................................................................................. 1 

1 
INTRODUCTION ....................................................................................................................... 2 

1.1 Purpose of DoD MOSA Guidance ...................................................................................... 2 

1.2 Preceding MOSA Efforts .................................................................................................... 2 

1.3 Modular Open Systems Working Group ............................................................................ 3 

2 
MOSA FRAMEWORK DEVELOPMENT ..................................................................................... 4 

2.1 MOSA Framework ............................................................................................................. 4 

2.2 Technical Reference Architectures ..................................................................................... 7 

2.3 Business and Stakeholder Context ...................................................................................... 8 

2.4 Modular Architectures:  Form Follows Function ............................................................... 9 

2.4.1 Modularity, Interfaces, Specifications, and Standards ............................................ 10 
2.4.2 Steps for Implementing a Modular Approach ......................................................... 11 

3 
MOSA REFERENCE FRAMEWORK ........................................................................................ 12 

3.1 Application of MOSA in a Framework............................................................................. 12 

3.1.1 Technical Architecture ............................................................................................ 13 
3.1.2 Business and Stakeholder Considerations ............................................................... 13 

3.2 Standardization and Conformance Guidance .................................................................... 14 

4 
EXAMPLE MOSA REFERENCE FRAMEWORKS ...................................................................... 16 

4.1 U.S. Army Modular Active Protection System ................................................................. 16 

4.2 Defense Intelligence Information Enterprise (DI2E) Framework .................................... 18 

APPENDIX A:  SURVEY OF MOSA IMPLEMENTATIONS ACROSS DOD ......................................... 20 

ACRONYMS AND ABBREVIATIONS .............................................................................................. 25 

REFERENCES ............................................................................................................................... 27 
 
 
 


Contents 

MOSA Reference Frameworks in Defense Acquisition Programs 

iv 

Figures  

Figure 2-1.  General MOSA Framework Concept ........................................................................... 4 

Figure 2-2.  MOSA Reference Framework Methods, Processes, and Tools ................................... 7 

Figure 2-3.  Relationships among Architectures in an Enterprise Architecture ............................... 8 

Figure 2-4.  Relationships among Business Objectives and Technical Design Considerations ...... 9 

Figure 3-1.  MOSA Reference Framework Considerations ........................................................... 13 

Figure 4-1.  Modular Active Protection System (MAPS) .............................................................. 16 

Figure 4-2.  MAPS Framework Artifacts ....................................................................................... 18 

Figure 4-3.  Defense Intelligence Information Enterprise (DI2E) Framework .............................. 18 

Figure 4-4.  DI2E Capabilities ....................................................................................................... 19 

 

Figure A-1.  Air Force Open Architecture Distributed Common Ground System (OA DCGS) ... 20 

Figure A-2.  RAS-G Interoperability Profile Quad Chart .............................................................. 22 

Figure A-3.  Interoperability Profile Conformance........................................................................ 22 

Figure A-4.  Interoperability Profile Projects ................................................................................ 23 

Figure A-5.  UH-60V Quad Chart ................................................................................................. 24 
 
 
 
Tables 

Table 2-1.  Architecture Definitions ................................................................................................ 5 

Table 2-2.  Definitions of Modular Terms ..................................................................................... 10 
 
 
 
 


 

MOSA Reference Frameworks in Defense Acquisition Programs 

1 

Executive Summary  

In response to the 2018 National Defense Strategy and 2017 legislation (P.L. 114-328 2017), the 
Department of Defense (DoD) Office of the Under Secretary of Defense for Research and 
Engineering (OUSD(R&E)) is working with the defense community to develop guidance for 
implementing modular open systems approaches (MOSA) in defense acquisition programs.  This 
document, focusing on MOSA reference frameworks, is part of a planned body of work that will 
support defense programs as they implement MOSA.   

Programs have long incorporated MOSA in varying forms, but the body of work is intended to 
promote effective use of MOSA across the enterprise by providing guidance and examples of best 
practices.  Additional guidance will address integrating new technologies, mitigating component 
obsolescence, and improving sustainment of the mission capabilities Warfighters need.  The body 
of work will promote a holistic approach to address architecture and standards in MOSA 
implementation. 

The DoD Modular Open Systems Working Group (MOSWG), under the leadership of the 
OUSD(R&E) Deputy Director for Engineering, is responsible for developing the MOSA body of 
work.  In 2016 the MOSWG conducted a Technical Standards Working Group, which defined a 
“MOSA framework” as a collection of modular open systems mechanisms (tactics, patterns, 
methods) with associated guidance for proper application and consistent implementation of MOSA 
on systems or programs in a domain.   

In 2018 the MOSWG organized a MOSA Frameworks Tiger Team to further survey MOSA 
implementation practices in DoD programs.  The team developed the concept of a MOSA 
“reference framework” to apply not just to a single program but to a domain of similar programs 
or systems across an enterprise.   

Section 1 of this document discusses the precedent and motivation for DoD MOSA efforts.  
Section 2 discusses the MOSA Frameworks Tiger Team’s development of the reference 
framework concept.  Section 3 discusses the essential elements of a MOSA reference framework, 
and Section 4 offers descriptions of two exemplary MOSA reference frameworks.  Appendix A 
includes additional descriptions of reference frameworks the Tiger Team collected during its 
survey. 

This document is intended to guide engineering staff and decision makers in common ways to 
recognize and use MOSA elements to support the technical performance and sustainment of 
acquisition systems.  The authors note the need to balance the business and technical aspects of a 
MOSA reference framework. 

Acknowledgments 

Contributors to this document include representatives of OUSD(R&E), U.S. Air Force (USAF), 
U.S. Army (USA), U.S. Navy (USN), National Reconnaissance Office (NRO), Defense 
Acquisition University (DAU), and the Joint Tactical Networking Center (JTNC).  


 

MOSA Reference Frameworks in Defense Acquisition Programs 

2 

1 Introduction  

The Department of Defense (DoD) has employed modular open systems approaches (MOSA) for 
nearly 20 years, but recent legislation (P.L. 114-328 2017) has formally mandated the use of 
MOSA to enhance the Department’s ability to modify major weapon systems efficiently.  
Modularization simplifies system design by making complexity manageable, enables programs to 
conduct parallel development efforts, and accommodates future uncertainty by allowing for 
incremental changes to a system (Baldwin 2006).   

Successful MOSA implementations have proved that proper application of modular approaches 
and flexible, open-system architectures allow for system components to evolve to respond to 
changing “technology, threat, or interoperability need” (P.L. 114-328 2017).  Accordingly, the 
Department is moving from unique architectures and closed systems that are inflexible and cost-
prohibitive to architectures that include the use of open interface standards with modular systems 
to facilitate continuous adaption and upgrades (Mattis 2018).  

MOSA provides an integrated business and technical strategy for competitive and affordable 
acquisition and sustainment of a new or legacy system (or a component within a new or legacy 
system) over the system life cycle.  The modular approach uses an architecture that separates the 
system into major functions and elements, which work together across interfaces in conformance 
with widely supported, consensus-based standards (Zimmerman et al. 2018).   

1.1 Purpose of DoD MOSA Guidance 

The Department intends its MOSA guidance to facilitate the adoption, integration, and refresh of 
defense capabilities through the use of consensus-based standards, appropriate business practices, 
and articulation of necessary data rights (P.L. 114-328 2017).  MOSA should be at the foundation 
of an acquisition program’s design strategy and architecture to address modernization, threat 
response, mission integration, competition, resource savings, and security.   

When implementing MOSA, programs must balance technical methods and business drivers.  
Technical enablers such as standard interfaces allow architecture elements to evolve separately 
and to interface with minimal impact to other system elements.  MOSA couples the technical 
design with open business practices such as selection and access to appropriate data, creating 
opportunities to improve a system’s warfighting ability.  In addition, programs need to balance 
MOSA with safety and cybersecurity design characteristics, essential to maintaining a secure, 
resilient system.  The components can be incrementally added, removed, or replaced to provide 
opportunities for cost savings or cost avoidance, resource reduction, technology refresh, capability 
change, increased interoperability, increased competition, and easier sustainment of the system.   

1.2 Preceding MOSA Efforts 

The Department conducted earlier MOSA efforts through the Open Systems Joint Task Force 
(OSJTF), which was established to provide focus and initial momentum to open system design and 
use in DoD.  At the time the Department defined open systems architecture as a characteristic of 


1  Introduction  

MOSA Reference Frameworks in Defense Acquisition Programs 

3 

a system that uses a technical architecture that adopts open standards supporting a modular, 
loosely coupled, and highly cohesive system structure that includes the publishing of key interfaces 
within the system and relevant design disclosure (DAU Glossary 2020).  

The MOSA principles were integrated into DoD systems engineering guidance, and the OSJTF 
was disestablished in 2004.  Since that time, there have been varying applications of MOSA in 
DoD acquisition programs.   

In 2016, at the request of the Defense Standardization Council (DSC), a DoD MOSA Technical 
Standards Working Group (TSWG) led by the DoD Systems Engineering office examined the role 
of the Defense Standardization Program (DSP) in supporting MOSA and related standards being 
employed across the Department.   

The TSWG identified the role and criticality of standards in enabling the effective, appropriate 
adoption of MOSA in the development and sustainment of weapon systems and national security 
systems.  The TSWG identified common barriers and enablers to the effective adoption of MOSA, 
discovered common standards in use across DoD, and assessed whether new standards should be 
developed.  The TSWG engaged with industry to discover MOSA that was industry driven or co-
developed with government initiatives related to defense, and to capture issues related to the 
development or employment of MOSA from the industry perspective.   

The TSWG identified the use of technical frameworks as a helpful reference to Program Managers 
as they develop modular and open systems.  The TSWG suggested defining a MOSA framework 
specifically for standardization as “a collection of standards and architectures with 
implementation guidance and conformance verification criteria for a specific array of functions 
within the standard” (DoD MOSA TSWG 2016). 

1.3 Modular Open Systems Working Group 

The DoD Modular Open Systems Working Group (MOSWG), under the leadership of the 
OUSD(R&E) Deputy Director for Engineering, is currently responsible for leading DoD MOSA 
guidance efforts.  The MOSWG is developing implementation guidance that supports MOSA 
across the participating Services and Agencies.   

In 2018, the MOSWG initiated a MOSA Frameworks Tiger Team to survey the use of MOSA in 
DoD acquisition programs.  The team met from April 4 to October 31, 2018, including 
representatives of the Military Services and DoD Agencies, to address a DSC suggestion to 
“develop and maintain a list of recommended MOSA frameworks, supported with guidance on the 
development and maintenance of additional frameworks” (DoD MOSA TSWG 2016).  The team 
examined MOSA frameworks and best practices in use, and it developed the core elements of a 
MOSA “reference framework” to facilitate MOSA implementation on programs.  The team drew 
on known efforts such as the Navy Future Airborne Capability Environment (FACETM), Air Force 
Open Mission Systems/Universal Command and Control Interface (OMS/UCI), and the Army’s 
Vehicle Integration for C4ISR/EW Interoperability (VICTORY). 


 

MOSA Reference Frameworks in Defense Acquisition Programs 

4 

2 MOSA Framework Development 

2.1 MOSA Framework  

DoD has used the term “framework” to identify proposed MOSA solutions that satisfy similar 
technical requirements and common elements across related applications within a domain 
(DiMario, Cloutier and Verma 2008; Fuchs and Golenhofen 2019).  The MOSWG currently 
considers a framework as applicable to a single program but is developing a concept of “reference 
framework” to refer to a framework that applies across multiple applications or programs.  This 
section discusses existing concepts, sources, and working definitions relating to MOSA 
architecture, framework, and reference framework. 

A MOSA framework includes (1) architecture, (2) standards, (3) implementation, and 
(4) conformance, as well as the use of (5) data models and (6) additional tools (Figure 2-1). 

 

Figure 2-1.  General MOSA Framework Concept 

The MOSWG Tiger Team identified MOSA frameworks currently in use throughout DoD.  The 
team examined the business and technical enablers defense acquisition programs employed when 
implementing a MOSA framework; captured best practices that assist programs in reducing the 
cost and time of integrating new and existing capabilities throughout the acquisition life cycle; and 
identified relevant terminology, policy, and guidance for architecture and standards (Table 2-1). 

 

 


2  DoD MOSA Framework Development 

MOSA Reference Frameworks in Defense Acquisition Programs 

5 

Table 2-1.  Architecture Definitions 

Term
Definition / Proposed Definition
Source
Coordinated / 
Pending 

Architecture
(System) fundamental concepts or properties 
of a system in its environment embodied in its 
elements, relationships, and in the principles 
of its design and evolution  
 
 
 
 
The arrangement of elements and subsystems 
and the allocation of functions to them to meet 
system requirements

ISO/IEC/IEEE 
42010:2011 
Systems and 
Software 
Engineering 
Architecture 
Description 
 
INCOSE Systems 
Engineering (SE) 
Handbook 2006

Coordinated

Architecture 
Description 
(AD)

Work product used to express an architecture.
ISO/IEC 
42010:2011  

Coordinated

Architecture 
Framework 

Conventions, principles, and practices for the 
description of architectures established within 
a specific domain of application and/or 
community of stakeholders.

ISO/IEC/IEEE 
42010:2011  

Coordinated

Architecture 
View 

Work product expressing the architecture of a 
system from the perspective of specific system 
concerns.

ISO/IEC 
42010:2011  

Coordinated

Architecture 
Viewpoint 

Work product establishing the conventions for 
the construction, interpretation, and use of 
architecture views to frame specific system 
concerns. 

ISO/IEC 
42010:2011  

Coordinated

DoD 
Architecture 
Framework 
(DoDAF) 

The overarching, comprehensive framework 
and conceptual model enabling the 
development of architectures to facilitate the 
ability of Department of Defense (DoD) 
managers at all levels to make key decisions 
more effectively through organized 
information sharing across the DoD, Joint 
Capability Areas (JCAs), Mission, 
Component, and program boundaries. The 
DoDAF serves as one of the principal pillars 
supporting the DoD Chief Information Officer 
(CIO) in his responsibilities for development 
and maintenance of architectures required 
under the Clinger-Cohen Act [1996]. It also 
provides extensive guidance on the 
development of architectures supporting the 
adoption and execution of Net-centric services 
within the Department.

Defense 
Acquisition 
University (DAU) 
Glossary 2020 

Coordinated


2  DoD MOSA Framework Development 

MOSA Reference Frameworks in Defense Acquisition Programs 

6 

Term
Definition / Proposed Definition
Source
Coordinated / 
Pending 

Framework

 

[Overarching term encompassing technical 
and business architecture, models, and 
guidance] 

Multiple
Pending 
Coordination 

MOSA 
Reference 
Framework 

A collection of modular open systems 
mechanisms (tactics, patterns, methods) with 
associated guidance for proper application and 
consistent implementation of MOSA on 
systems or programs in a domain. 

DoD MOSA 
TSWG 2016 

Coordinated

Reference 
Architecture 
(RA) 

An authoritative source of information about a 
specific subject area that guides and constrains 
the instantiations of multiple architectures and 
solutions.

DoD Chief 
Information 
Officer (CIO) 2012 

Coordinated

Reference 
Framework 
(RF) 
 

[Overarching framework to]

• Identify those things that need to be 
common  

• Create consistency where needed  
• Indicate where individual projects can 
diverge from the RF where appropriate  

• Provide a structured approach to managing 
standards, policies, patterns in order to 
deliver on objectives  

Wilkes 2012
Pending 
Coordination 

Reference 
Model  

An abstract framework or domain-specific 
ontology consisting of an interlinked set of 
clearly defined concepts produced by an expert 
or body of experts in order to encourage clear 
communication.

SOA-RM 
Technical 
Committee 2006 

Coordinated

Technical 
Reference 
Framework 
(TRF) 
(U.S. Navy) 
 

A framework incorporating (1) architectures, 
(2) standardized specifications and protocols, 
(3) data models, and (4) tools that enable 
programs to:  
• Provide reusable architecture for a family of 
applications. 

• Deliver an integrated set of profiles for the 
development of components. 
o Technical profiles are a set of 
(implementation-agnostic) attribute 
profiles that allow components to 
operate within the context of systems 
and platforms.   

• Promote a product line of “best of breed” 

capabilities to the Warfighter.

Guertin et al.
Pending 
Coordination 

 


2  DoD MOSA Framework Development 

MOSA Reference Frameworks in Defense Acquisition Programs 

7 

The Navy’s historical concept of MOSA Technical Reference Frameworks (TRFs) used 
(1) architectures, (2) standardized specifications and protocols, (3) data models, and (4) tools that 
enabled programs to:  

• Provide reusable architecture for a family of applications 

• Deliver an integrated set of profiles for the development of components 

o Note:  The technical profiles are a set of (implementation-agnostic) attribute profiles 
that allow components to operate within the context of systems and platforms 

• Promote a product line of “best of breed” capabilities to the Warfighter 

The Navy successfully implemented MOSA using TRFs in defense acquisitions such as the 
Program Executive Office (PEO) Submarines (SUB)–Submarine Warfare Federated Tactical 
System (SWFTS) Command, Control, Communications, Computers and Intelligence (C4I) 
Consolidated Afloat Networks and Enterprise Services (CANES) program and the PEO Integrated 
Warfare Systems (IWS) Open Systems Product Line Architectures approach (Guertin 2015). 

2.2 Technical Reference Architectures 

The Tiger Team observed that the Military Services apply elements of (1) reference frameworks, 
(2) reference architectures, and (3) reference models for platforms and systems across specific 
domains and organizations.   

Wilkes (2012) described the concept of a reference framework as “an authoritative guide for 
building of something that expands the structure into something useful.  The framework often 
contains a model, process, architecture, and organizational governance.”  Practitioners may include 
aspects of a reference architecture (blueprint) and reference model (domain-specific ontology) 
when developing a reference framework.  Thus a MOSA reference framework can assist in guiding 
the development, management, and deployment of modular and open systems (Figure 2-2). 

 

Figure 2-2.  MOSA Reference Framework Methods, Processes, and Tools 


2  DoD MOSA Framework Development 

MOSA Reference Frameworks in Defense Acquisition Programs 

8 

As illustrated in Figure 2-2, a MOSA reference framework provides a structured approach to 
manage standards, policies, and patterns that achieve business and technical objectives.  A 
reference model provides concepts, principles, and common terms.  A meta model defines the rules 
for building the reference model; for example, a meta model would define deliverables or the 
subject of a policy (Wilkes 2012).  Architectural frameworks provide users with guidance and 
rules “for structuring and organizing architectures” (DoD CIO 2010).  For instance, the DoD 
Architecture Framework (DoDAF) Version 2.02 provides more than 52 models, a meta model, 
and a standard framework for developing architectural views and capturing and presenting 
architectural data to support DoD stakeholders (DoD CIO 2010).   

2.3 Business and Stakeholder Context   

Organizational roles and responsibilities across the domains may not be codified or well 
understood; therefore, organizations may neglect the impact of their product or system in relation 
to evolving changes in the wider enterprise.  The practice of examining and codifying the impacts 
of business objectives as well as technical considerations can be captured in enterprise 
architectures (Pereira and Sousa 2004) (Figure 2-3). 

 

Figure 2-3.  Relationships among Architectures in an Enterprise Architecture 

To successfully implement MOSA, acquisition professionals must be able to understand clearly 
the respective acquisition processes, cultural behaviors, and desired outcomes across multiple 
domains.  The MOSA reference framework begins to consider both business and stakeholder 
concerns as well the technical design (Cloutier et al. 2010) (Figure 2-4). 


2  DoD MOSA Framework Development 

MOSA Reference Frameworks in Defense Acquisition Programs 

9 

 

Figure 2-4.  Relationships among Business Objectives and Technical Design Considerations 

Acquisition programs using MOSA as a foundational practice have achieved a degree of 
modernization (e.g., technology refresh, inclusion of innovative technology); cost savings (e.g., 
cost avoidance, savings realized from increased competition); and interoperability.  If programs 
are organized to incorporate MOSA, then MOSA reference frameworks can enable DoD 
engineering and business communities to structure technology investments, upgrades, and 
innovation opportunities for insertion into programs during design and at regular refresh cycles.   

To ensure programs include MOSA considerations, adequate incentives must exist for both the 
government program offices managing the effort and the contractors involved.  For the government 
program offices, the requirement and programming must be in place.  The applicable standards, 
along with appropriate training and compliance documentation and test cases, should be readily 
available.  For contractors, the government program office must articulate required data rights and 
intellectual property information early.  The government must clearly document in the contract 
which standards or architecture considerations contractors should follow, and the contract should 
include appropriate incentives and disincentives (fees, withholding item acceptance, etc.).  

2.4 Modular Architectures:  Form Follows Function  

In the modular approach of “designing a modular architecture,” the architecture (form) is used to 
describe modularization (the function of modularity) (Alberto and Tollenaere 2005).  The concept 
of a modular architecture adheres to the systems engineering principle of form following function, 
as the primary function is modularization and the architecture is the form used to represent the 
modular design.  The modular architecture is the product that depicts (1) functional decomposition 
of functions into modules, (2) de-coupled interfaces between modules, and (3) interface 
specifications and standards that define the primary interactions across/between modules (Ulrich 
1995).  The architecture serves as a blueprint for developing and maintaining a product or system, 
or a product line or family of systems, across its life cycle.   


2  DoD MOSA Framework Development 

MOSA Reference Frameworks in Defense Acquisition Programs 

10 

Creating a modular architecture requires functional decomposition (Figure 2-3) as a systems 
engineering practice across the System Development Life Cycle (SDLC) to enable the planning of 
flexible modularization and control of interfaces.  The practice of functional allocation enables 
functional modules to serve as building blocks in a system.  In addition, minimizing the 
dependencies between modules by de-coupling interfaces enables loose coupling.  Finally, the 
practice of specifying well-defined interfaces that use consensus-based standards results in 
standardized interfaces.  The functional decomposition process is paramount in implementing a 
modular approach to system development.  De-coupling helps eliminate unnecessary interfaces, 
which then makes it easier to identify the interfaces that are good candidates for standardization.  

2.4.1 
Modularity, Interfaces, Specifications, and Standards 

Modularization provides the opportunity to mix and match components in a product design in 
which the standard interfaces between components can be verified as compliant with law and are 
specified to allow a range of variation in components to be substituted in a product’s architecture.  
Researchers Sako and Murray (1999) described modularity as “a bundle of characteristics that 
define, first, interfaces between elements of the whole, second, a function-to-function component 
(or task-to-organization unit) mapping that defines what those elements are, and, third, hierarchies 
of decomposition of the whole functions, components, and tasks” (Table 2-2). 

Table 2-2.  Definitions of Modular Terms 

Term
Published Definitions
Source

Modular 
architecture 

A system architecture in which the system has been partitioned into 
architectural components that exhibit good abstraction, have high 
internal cohesion, have low coupling to other components and 
external systems, and encapsulate their internal implementation 
behind visible interfaces.

Firesmith and 
Donohoe 
2015 

Modular 
system

A modular system is made of independent units which can be easily 
assembled and which behave in a certain way in a whole system.

Baldwin and 
Clark 1997

Modularity
Modularity is a very general set of principles for managing 
complexity.  By breaking up a complex system into discrete pieces, 
which can then communicate with one another only through 
standardized interfaces within a standardized architecture, what 
would otherwise be an unmanageable spaghetti tangle of systematic 
interconnections can be eliminated.

Lanlois 2002

Module
A complex group that allocates a function to the product and which 
could be changed and replaced in a loose way and be produced 
independently.

Wilhelm 1997

Product 
architecture 

The scheme by which the function of the product is allocated to 
physical components, i.e., the arrangement of functional elements, 
the mapping from functional elements to physical components, and 
the specification of the interfaces among interaction physical 
components.

Sako and 
Murray 1999 

 


2  DoD MOSA Framework Development 

MOSA Reference Frameworks in Defense Acquisition Programs 

11 

2.4.2 
Steps for Implementing a Modular Approach 

Modular building blocks can be structured and arranged in an architecture by adhering to the 
following steps: 

• Step 1: Modularize by decomposing system capabilities into functional modules.  Below 
are some characteristics of modules to consider: 

o Single Abstraction – module represents the key aspects of a single capability or 
concept. 

o High Cohesion – module contains all parts necessary to implement its abstraction 
(sufficiency) and only parts related to its abstraction (necessity). 

o Low Coupling – module minimizes (or optimizes) the number, scope, and complexity 
of interfaces required. 

o Encapsulation – module boundaries hide implementation details behind specified 
visible interfaces and these interfaces are the only way to interact with internal 
module functions. 

o Note:  Modules may also be “components.” 

• Step 2: Specify (or Configure Interfaces) by identifying connections between system 
building blocks.  

o Interfaces “connect” modular components within the architecture.  In addition, there 
are multiple ways in which functional modules can be organized.  Some configuration 
may be optimal, some not, and the modularity of the functional interfaces will impact 
the overall modularity.   

• Step 3:  Define Interface Specifications by capturing how functional modules interact. 

o Interface specifications define “how” functional modules behave. 

o Interface specifications should address both syntactic and semantic considerations for 
data flowing through the interface. 

• Step 4:  Standardize Interface Specifications to allow for opportunities of future 
modernization. 

o Standardization of interface specifications enables technology developers to access, 
manage, and build to well-defined interfaces, thus allowing interoperability across 
new solutions (i.e., designs must “conform” to interface specifications). 

o Well-defined interface specifications will significantly reduce the effort required for 
integration of modules from disparate sources. 

o For standardized interfaces, programs should have a method for verifying compliance 
with the standard. 

 


 

MOSA Reference Frameworks in Defense Acquisition Programs 

12 

3 MOSA Reference Framework  

A MOSA reference framework identifies, defines, and documents the recommended elements for 
facilitating the implementation of MOSA consistently among similar programs.  Although using 
MOSA successfully includes relying on standards, specifying a particular standard is not sufficient 
to ensure a MOSA implementation will be successful.  Standards, along with architectures, must 
be implemented properly to be effective.   

A sample MOSA reference framework providing architecture and standards guidance for Services 
and Agencies across the Department will be stored in the newly formed Modular and Open 
Systems Standards and Specifications (MOSS) Lead Standardization Area located in ASSIST, the 
web-enabled database for standardization documents available to DoD.  OUSD(R&E) initiated the 
ASSIST MOSS Standardization Area in August 2018 to cover “specifications and standards that 
support MOSA in defense systems” (DSP 2019).  The MOSS also includes “specifications used to 
define system interfaces and system architectures that allow severable components; and standard 
formats for data exchanges, physical (electrical, mechanical, etc.) and practices for implementing 
MOSA frameworks and architectures, as well as compliance testing for implementations of 
standards in support to the MOSA practice” (DSP 2019). 

3.1 Application of MOSA in a Framework 

Programs should consider MOSA during architecture development; MOSA cannot be only the 
result of design or implementation.  In addition, programs should gather lessons learned from 
design, implementation, and integration to improve the architecture.   

DoD is developing further guidance regarding how to implement MOSA in a strategic manner to 
ensure business and technical drivers are achievable, which may vary by organization; however, 
the following principles are common among organizations: 

• There must be (1) modularity of functionality, (2) modularity of hardware components 
(including computing hardware), and (3) modularity of software components.  

• Open interfaces are required at the boundaries of each module, including (1) open 
software interfaces (including syntactic and semantic data constraints), (2) open hardware 
interfaces, and (3) well-defined functions to accompany open interfaces.  These shared 
boundaries may be  

o Between a major system platform and a major system component;  

o Between major system components; or  

Between major system platforms that are: (1) defined by various physical, logical, 
and functional characteristics, such as electrical, mechanical, fluidic, optical, radio 
frequency, data, networking, or software elements; and (2) characterized clearly in 
terms of form, function, and the content that flows across the interface in order to 
enable technological innovation, incremental improvements, integration, and 
interoperability. 


3  MOSA Reference Framework  

MOSA Reference Frameworks in Defense Acquisition Programs 

13 

3.1.1 
Technical Architecture 

Every program, system, and process has a technical architecture, but it may be documented in 
varying ways.  To successfully implement MOSA, the technical architecture is a component of the 
design that should consider external interface definition, support growing scale and functionality, 
and accommodate technology insertion opportunities.  The technical approach for implementing 
MOSA should capture not only architectures but also the architectural patterns used to implement 
MOSA when addressing hardware, software, data, and functional areas of concern. 

Architecture and design documents should capture the diverse or dissimilar mix of other systems 
(hardware, software, and human) with which the system needs to exchange information.  
Implementing MOSA requires (1) the right documentation and (2) the right data.  As such, MOSA 
supports the creation of modular, layered architectures, and MOSA should be used at major system 
interfaces.  Describing and documenting the physical, logical, and functional characteristics of 
these architectures is imperative.  Finally, data management strategies should define data models, 
descriptions, and plans for data/asset management.  

3.1.2 
Business and Stakeholder Considerations 

As part of the MOSA reference framework, each program must develop not only the technical 
guidance but also MOSA business guidance, including data and asset management, compliance 
guidance, and contracting guidance (Figure 3-1). 

 

Figure 3-1.  MOSA Reference Framework Considerations 


3  MOSA Reference Framework  

MOSA Reference Frameworks in Defense Acquisition Programs 

14 

Following are examples of information programs should include in the MOSA business guidance:  

• Guidance for achieving MOSA-related benefits, to include: enhanced competition and 
innovation, significant cost savings or avoidance, schedule reduction, opportunities for 
technical upgrades, increased interoperability, including system of systems 
interoperability and mission integration, and other benefits during the sustainment phase 
of a major weapon system 

• Strategy for acquiring system components and platforms that can be separated, competed, 
and independently evolved throughout the life cycle 

• Technical data rights for (major) system interfaces: 

o Outline the strategy for acquiring system components and platforms that can be 
separated, competed, and independently evolved throughout the life cycle 

o Address technical data rights for (major) system interfaces 

o Include data rights strategies that are defined to address specific data rights, for 
example: need for components, interfaces, and data rights options  

• Contracting guidance and evaluation factors: 

o May include tying incentive fees or item acceptance to verified MOSA enabling 
standard conformance, linking a sustainment logistics support option to delivery of 
sufficient technical data rights, etc. 

Other areas to consider include: 

• Reuse strategy and commonality approaches  

o Relate to core asset management plan  

o Include acquisition strategies and approaches 

• Policies and regulations  

• Collaborative international marketplace 

• Governance of architecture  

• Organizational approach – charters and roles for various portions of the organization 

3.2 Standardization and Conformance Guidance 

Appropriate selection and application of standards at modular interfaces can contribute to healthy 
competition among suppliers throughout the acquisition life cycle.  Many standards are available 
for the government programs to choose.  Accessing and selecting appropriate standards can be 
challenging as most were originally developed to solve a specific problem set.  Therefore, Program 
Managers should be careful to use the appropriate standards within contracts, tailored as 
appropriate for each system.   


3  MOSA Reference Framework  

MOSA Reference Frameworks in Defense Acquisition Programs 

15 

System designs implementing MOSA, with sufficient standardization at interfaces, allow greater 
flexibility and agility to reconfigure components to address evolving threats and emerging 
technology.  Contract developers of DoD systems require appropriate business knowledge 
regarding intended use, stakeholder context, data rights, and intellectual property to select the best 
standards.  Standards implemented at interfaces may contain options and default settings for which 
multiple combinations are possible, but once selected may not interoperate with other 
implementations of the same standard.  In addition, standards may serve as methods or processes 
for meeting a business or technical objective, and some process standards may influence the 
architecture process and support business implementation. 

Multiple options, as well as inconsistent availability of information to verify standard 
implementation, can lead to interoperability problems.  Therefore, standards guidance should 
provide details on implementation and conformance, including which organizations provide 
verification.  Programs should provide a test plan, procedures, and verification methods across the 
life cycle to ensure compliance. 

 


  

MOSA Reference Frameworks in Defense Acquisition Programs 

16 

4 Example MOSA Reference Frameworks 

The 2018 DoD MOSA Frameworks Tiger Team conducted a study to identify efforts in DoD that 
are already implementing a full MOSA framework.  The team reviewed many MOSA 
implementations and selected two that best illustrated the DoD reference framework proposed in 
this paper: (1) U.S. Army Modular Active Protection Systems (MAPS) and (2) Defense 
Intelligence Information Enterprise (DI2E) Framework.  Both efforts incorporate implementation 
and conformance guidance as well as plans and procedures for ensuring compliance.  The 
Appendix includes additional examples of MOSA efforts the team considered.  

4.1 U.S. Army Modular Active Protection System   

The U.S. Army MAPS (Figure 4-1) enables safe, secure, layered protection for modifying vehicle 
protection needs across ground vehicle platforms with the government-owned MAPS Base Kit.  
The program leverages a stable software code base in MAPS Controller for use with many different 
sensors and effectors.   

 

 

 

Figure 4-1.  Modular Active Protection System (MAPS) 


4  Example MOSA Reference Framework Implementations  

MOSA Reference Frameworks in Defense Acquisition Programs 

17 

MAPS enables reuse and commonality of ruggedized base kit components by multiple ground 
vehicle platforms.  The MAPS MOSA framework permits ease of understanding new or updated 
requirements and interfaces for those compliant to an earlier level of architecture, due to ongoing 
architecture and baseline release process.  MAPS supports reduced time for new sensor and 
effector pairing.  It uses a modular design and open system architecture approach that: 

• Addresses Active Protection System development aspects previously overlooked 

• Gains more insight than past efforts, which were performance‐focused demonstrations 

• Defines modular, interoperable, scalable, and reconfigurable standards 

• Permits configuration and integration to any target platform 

• Parses functionality into modules that can be replaced to adapt to changing threats 

• Permits DoD to maintain system design ownership 

• Avoids proprietary, “blackbox,” unique design solutions 

• Facilitates a more orderly upgrade process 

MAPS’ implementation of MOSA (Figure 4-2) provides: 

• Comprehensive functional decomposition at core of architecture 

o SysML model; logical architecture, interconnect diagrams, interface types and 
requirements, sequence and activity diagrams 

• Ability to derive multiple system design solutions constrained by safety and 
cybersecurity needs 

• Capacity to work with varying performance levels, variable threats, or multiple ground 
vehicles 

• Framework – Reference Implementation Guide (RIG):  describes how to leverage the 
architecture to derive a modular APS design, applicable for 

o Existing active protection systems and subsystems 

o Yet to be developed subsystems 

• Ability to grow a library of design models for compliant subsystems 

• Framework – Data Modeling: 

o Includes core data model and describes signals that define the interfaces between the 
reference architecture’s functions 

o Functions are sequenced to describe APS behaviors 

• Framework – Reference Architecture Interface Control Document, Compliance Guide, 
and Technical Standard: 

o Identifies compliance requirements for signals and interfaces 

 


4  Example MOSA Reference Framework Implementations  

MOSA Reference Frameworks in Defense Acquisition Programs 

18 

 

Figure 4-2.  MAPS Framework Artifacts  

4.2 
Defense Intelligence Information Enterprise (DI2E) Framework  

The DI2E framework (Figure 4-3) lays the foundation for embracing and implementing software, 
services, and capabilities reuse across DoD and the Intelligence Community to achieve effective 
and efficient global intelligence, surveillance, and reconnaissance (ISR) pairing. 

 

Figure 4-3.  Defense Intelligence Information Enterprise (DI2E) Framework 


4  Example MOSA Reference Framework Implementations  

MOSA Reference Frameworks in Defense Acquisition Programs 

19 

The DI2E Framework provides a software development environment; however, there are some 
internal development efforts including the following: 

• DevTools (developer environment; enables MOSA) 

• Reference Implementation (RI) (Some internal development) 

• Storefront (internally built system; follows MOSA tenets) 

• Clearinghouse (significant focus on MOSA through evaluation process) 

 

Figure 4-4.  DI2E Capabilities 

Although the DI2E framework (Figure 4-4) is mostly a developer environment, MOSA tenets and 
principles are reflected in the tools and resources provided to the community.  In areas in which 
DI2E framework develops software/capabilities, MOSA tenets and principles are implemented.  
DI2E framework has been successful in enabling MOSA to occur; however, it is difficult to 
accurately validate that the community is fully embracing MOSA tenets.  The DI2E framework is 
designed to increase reuse due to its large user base and widely used developer environment across 
the Intelligence Community and DoD. 

 


 

MOSA Reference Frameworks in Defense Acquisition Programs 

20 

Appendix A:  Survey of MOSA Implementations across DoD 

Air Force Open Architecture Distributed Common Ground System (OA DCGS) 

The Air Force OA DCGS (Figure A-1) asserts it has been transformed through MOSA.  The 
program used MOSA principles to renew internal processes, embracing agile software constructs.  
MOSA and agility go together as the best agile teams use open interfaces, operate with service 
contracts, and leverage already existing modular code.  Through MOSA and agile principles, OA 
DCGS seeks to achieve a vision of delivering capability at the “speed of relevance” (Mattis 2018).  

 

Figure A-1.  Air Force Open Architecture Distributed Common Ground System (OA DCGS) 

OA DCGS seeks to deliver a robust and cyber-secure enterprise, using commercial and 
Intelligence Community standards and best practices.  The program addressed the following in 
implementing OA DCGS: 

• Accelerate the transition to an open architecture. 

• Achieve cybersecurity for the DCGS enterprise.  

• Modernize, sustain, test, and field capabilities 

• Implement SAFe, agile, and ITIL (Information Technology Infrastructure Library) 
principles, practices and framework to deliver ISR capabilities 

The AF DCGS weapon system is implementing OA DCGS to: 

• Transition from prototype to fielded capability faster 

• Seamlessly integrate development and operational testing 


Appendix A: Survey of MOSA Implementations across the DoD 

MOSA Reference Frameworks in Defense Acquisition Programs 

21 

• Leverage and quickly integrate best-of-breed Intelligence Community and industry 
practices  

• Integrate test and evaluation (T&E) practices, hold a shorter cycle   

• Implement Intelligence Community, DoD, and commercial standards  

• Manage data and data sources 

• Own the Technical Baseline (OTB) 

• Mitigate cybersecurity vulnerabilities  

• Implement rigorous cybersecurity testing  

• Integrate system designs that are open versus closed 

• Deliver software releases, patches and enhancements on cadence 

The OA DCGS team has been forward leaning; migrating to the cloud, as in C2S or SC2S, will be 
straightforward.  As code is refactored the program is requiring task orders “12 factor app” 
compliant software, which makes the deliverable cloud compliant.  OA DCGS is making the OA 
DCGS of the future a totally composable system that can be built through automation, thereby 
allowing the program to integrate changes in minutes rather than months or years. 

RAS-G IOP (Figure A-2) implementations of MOSA use IOP versions designed with industry to 
develop standardized interfaces and supporting documentation to perform specific operational 
functions.  In addition, IOP provides government Program Managers (and others) with a master 
library of standardized interfaces, tools, and supporting documentation for use in defining an 
“instantiation” for a given unmanned ground vehicle (UGV), class of UGVs, or program. 

The vendor builds subsystem design to “instantiations” (Figure A-3) to provide an Engineering 
Change Proposal if a design is more optimal to meet system requirements.  The vendor 
system/subsystem’s IOP solution is then validated to conformance to “instantiation,” ensuring 
interoperability.  

 

 
 


Appendix A: Survey of MOSA Implementations across the DoD 

MOSA Reference Frameworks in Defense Acquisition Programs 

22 

Robotic Autonomous Systems Ground Interoperability Profile (RAS-G IOP) 
 

 

Figure A-2.  RAS-G Interoperability Profile Quad Chart 

 

 

Figure A-3.  Interoperability Profile Conformance 


Appendix A: Survey of MOSA Implementations across the DoD 

MOSA Reference Frameworks in Defense Acquisition Programs 

23 

For the RAS-G IOP, MOSA provides the following benefits: 

• Allows for use of a universal robotic controller 

• Allows for faster, easier, and less expensive replacements or upgrades to a program  

• Allows for use of a common radio solution 

• Allows for the capability to exchange payloads between systems 

• Allows for the ability to place existing chemical, biological, radiological, nuclear, and 
explosive (CBRNE) sensors on RAS-G and control and monitor from the Universal 
Control Unit 

• Allows for common interfaces with the Navy Advanced Explosive Ordnance Disposal 
Robotic System (AEODRS)  

• Allows common autonomy kits to be used with vehicle-specific drive-by-wire kits 

• Reduces dependence on operators for manned-unmanned teaming 

• NATO benefits through a Standardization Agreement (STANAG) 

TAS-G IOP uses legacy standards to save time and money while improving interoperability by 
removing ambiguity in implementation.  Vendors are able to interface IOP-compliant subsystems 
(Figure A-4) rapidly to provide enhanced capabilities.  Vendors can replace obsolete subsystems 
with little to no changes to the other subsystems, and subsequently, the universal control unit 
allows for more efficient air/ground teaming. 

 

Figure A-4.  Interoperability Profile Projects 

The IOP facilitates enhanced competition, allowing for more subsystem vendors to have their 
products evaluated for replacements or upgrades to a system.  Industry and government are able 
to work together to provide more capabilities to the Warfighter.   


Appendix A: Survey of MOSA Implementations across the DoD 

MOSA Reference Frameworks in Defense Acquisition Programs 

24 

The IOP allows reduced fielding time, integration costs, and training burden.  The strategy reduces 
the number of different subsystem variants and total number that need to be fielded for spares.  A 
reduced number of subsystems and common interfaces allows for testing efficiencies as system 
software becomes more complex.  In addition, the program could reduce its dependence on 
operators for manned-unmanned teaming.  The universal control unit allows for more efficient 
air/ground teaming.  

Upgrade UH-60L BLACK HAWK – Ground Interoperability Profile (UH-60V) 

UH-60V (Figure A-5) was motivated to implement MOSA to build a platform upon which 
software capability anticipated to be available in the future could be added with minimal impact 
to the fielded system.  The program sought to ensure the use of non-proprietary interfaces, 
standards, and protocols.  It also sought to ensure agility in the design, such that modifications to 
specific performance requirements would be reasonably isolated only to the components related 
to that requirement, and thus improve responsiveness to changing requirements both during 
development and after the system was fielded.  UH-60V was motivated to ensure delivery of a 
Technical Data Package that maximizes the Program Manager’s competitive options throughout 
the life of the program, including unlimited data rights where feasible.  UH-60V MOSA 
implementation enabled future integration efficiencies and enabled future reductions in repeated 
integration costs.  In addition, the program integrated two COTS applications. 

 

Figure A-5.  UH-60V Quad Chart 


 

MOSA Reference Frameworks in Defense Acquisition Programs 

25 

Acronyms and Abbreviations 
 
AD
Architecture Description

AEODRS
Advanced Explosive Ordnance Disposal Robotic System

APS
Advanced Protection System

C4I
Command, Control, Communications, and Computers

C4ILE
Command, Control, Communications, Computers, & Intelligence 
Learning Environment

C4ISR
Command, Control, Communications, Computers, Intelligence, 
Surveillance, and Reconnaissance

CANES
Consolidated Afloat Networks and Enterprise Services

CBRNE
Chemical, Biological, Radiological, Nuclear, and Explosive

CIO
Chief Information Officer

COTS
Commercial Off-the-Shelf 

CS/CSS
Computer Software/Computer Software System

DAU
Defense Acquisition University

DCGS
Distributed Common Ground System

DI2E
Defense Intelligence Information Enterprise

DoD
Department of Defense

DoDAF
Department of Defense Architecture Framework

DSC
Defense Standardization Council

DSP
Defense Standardization Program

ECP
Engineering Change Proposal

FACETM
Future Airborne Capability EnvironmentTM

HW
Hardware

ICD
Interface Control Document 

INCOSE
International Council on Systems Engineering

IOP
Interoperability Profile

ISO/IEC
International Organization for Standardization – International 
Electrotechnical Commission

ISR
Intelligence, Surveillance, and Reconnaissance

ITIL
Information Technology Infrastructure Library

IWS
Integrated Warfare System

JTNC
Joint Tactical Networking Center

MAF
Modular Active Protection System Framework

MAPS
Modular Active Protection System

MOSA
Modular Open Systems Approach

MOSS
Modular Open Standards and Specifications


Acronyms and Abbreviations 

MOSA Reference Frameworks in Defense Acquisition Programs 

26 

M&S
Modeling and Simulation

NAMC
National Advanced Mobility Consortium

NATO
North Atlantic Treaty Organization 

NDS
National Defense Strategy

OA
Open Architecture

OASIS
Organization for the Advancement of Structured Information Standards

OMS
Open Mission Systems

OSD
Office of the Secretary of Defense

OSTJF
Open Systems Joint Task Force

OTB
Own the Technical Baseline

OUSD(R&E)
Office of the Under Secretary of Defense for Research and Engineering

PEO
Program Executive Office

PM
Program Manager

RA
Reference Architecture

RAS-G
Robotics Autonomous System–Ground

RI
Reference Implementation

RIG
Reference Implementation Guidance

SAFe
Scaled Agile Framework

SC2S
Strategic Command and Control Software

STANAG
Standardization Agreement (NATO)

SUB
Submarine

SW
Software

SWFTS
Submarine Warfare Federated Tactical System (U.S. Navy)

SySML
Systems Modeling Language (Unified Modeling Language)

TARDEC
U.S. Army Tank Automotive Research, Development, and Engineering 
Center

T&E
Test and Evaluation

TRF
Technical Reference Framework

UCI
Universal Command and Control Interface

UGV
Unmanned Ground Vehicle

USA
United States Army

USAF
United States Air Force

USN
United States Navy

VICTORY
Vehicular Integration for (C4ISR) Command, Control, Communication, 
Computers, Intelligence, Surveillance, Reconnaissance /(EW) Electronic 
Warfare (EW) Interoperability (U.S. Army)


 

MOSA Reference Frameworks in Defense Acquisition Programs 

27 

References 

Alberto, Jose, and Michel Tollenaere. 2005. “Modular and Platform Methods for Product Family 
Design: Literature Analysis.” Journal of Intelligent Manufacturing 3 (371-390): 16. 

Baldwin, C. Y. 2006. “Modularity in the Design of Complex Engineering Systems.” In Complex 
Engineered Systems (Berlin, Heidelberg): 175-205. 

Baldwin, C. Y., and Kim B. Clark. 1997. “Managing in the Age of Modularity.” Harvard 
Business Review, September-October. 

Clinger-Cohen Act. 1996. National Defense Authorization Act (NDA) for Fiscal Year 1996 (S. 
1124; Pub.L. 104–106). Washington, D.C.: 104th Congress. 

Cloutier et al. 2010. “The Concept of Reference Architectures.” Systems Engineering 13 (1): 14-
27. 

DAU. 2020. Acquipedia. Fort Belvoir, VA: Defense Acquisition University (DAU). 

DAU Glossary. 2020. DAU Acquisition Glossary. Fort Belvoir, Va.: Defense Acquisition 
University (DAU). https://www.dau.edu/glossary/Pages/Glossary.aspx. 

DiMario, Michael, Robert Cloutier, and Dinesh Verma. 2008. “Applying Frameworks to Manage 
SoS Architectures.” Engineering Management Journal 20 (4 ): 18-23. 

DoD CIO. 2010. DoD Architecture Framework (DoDAF) Version 2.02. Washington, D.C.: 
Department of Defense (DoD) Chief Information Officer (CIO). 

DoD CIO. 2012. DoD CIO Reference Architecture Description. Washington, D.C.: Department 
of Defense (DoD) Chief Information Officer (CIO). 

DoD MOSA TSWG. 2016. Modular Open Systems Approach (MOSA) in Defense Acquisition 
Programs. Washington, D.C.: Department of Defense (DoD) Modular Open Systems 
Approach (MOSA) Technical Standards Working Group (TSWG). 

DoDM 4120.24. 2018. Department of Defense (DoD) Manual 4120.24, Defense Standardization 
Program (DSP) Procedures. 2014 incorporating Change 2 effective October 15, 2018, 
Washington, D.C.: DoD. 

DSP. 2019. Defense Standardization Program Standardization Directory (SD-1). Washington, 
D.C.: Department of Defense. 

Firesmith, Donald, and Pat Donohoe. 2015. Model Open System Architecture (OSA) 
Requirements. Special Report, Pittsburgh: Software Engineering Institute, Carnegie 
Mellon University. 

Fuchs, Christopher, and Franziska J. Golenhofen. 2019. Mastering Disruption and Innovation in 
Product Management: Connecting the Dots. Munich, Germany: Springer. 

Guertin, Nickolas H., H. R. Sweeney, and Doug Schmidt. 2015. “How the Navy Is Using Open 
Systems Architecture to Revolutionize Capability Acquisition: The Navy OSAA Strategy 
Can Yield Multiple Benefits.” Proceedings of the 12th Annual Acquisition Research 
Symposium. Tampa, FL: National Defense Industrial Association . 
https://www.dre.vanderbilt.edu/~schmidt/PDF/NDIA-2014.pdf. 


 

MOSA Reference Frameworks in Defense Acquisition Programs 

28 

Haskins, Cecilia, Kevin Forsberg, and Michael Krueger. 2006. INCOSE Systems Engineering 
(SE) Handbook. Handbook, Seattle: International Council on Systems Engineering 
(INCOSE). 

ISO/IEC 42010. 2011. ISO/IEC 42010:2011 Systems and Software Engineering Architecture 
Description. New York: ISO/IEC. 

Lanlois, Richard N. 2002. “Modularity in Technology and Organization.” Journal of Economic 
Behavior & Organization 19-37. 

Mattis, Jim. 2018. Summary of the 2018 National Defense Strategy of the United States of 
America: Sharpening the American Military Competitive Edge. Washington, D.C.: 
Department of Defense. 

OASIS Open. 2012. Reference Architecture Foundation for Service-Oriented Architecture, 
Version 1.0. Standards Track Work Product, OASIS Open. http://docs.oasis-
open.org/soa-rm/soa-ra/v1.0/soa-ra.html. 

OSJTF. 2004. An Open Systems Approach to Weapon System Acquisition, Version 1.0. Published 
Draft, Washington, D.C.: Department of Defense (DoD) Open Systems Joint Task Force 
(OSJTF). 

P.L. 114-328. 2017. U.S. Code Title 10. Subtitle A, Part IV, Chapter 144B, Subchapter I: 
Modular Open Systems Approach in Development of Weapon Systems. Washington 
United States: 114th Congress. 

Pereira, Carla Marques, and Pedro Sousa. 2004. “A Method to Define an Enterprise Architecture 
Using the Zachman Framework.” In Proceedings of the 2004 ACM Symposium on 
Applied Computing, 1366-1371. ACM. 

Sako, Mari, and Fiona Murray. 1999. “Modules in Design, Production and Use: Implications for 
the Global Auto Industry.” IMVP Annual Sponsors Meeting.  

Ulrich, Carl. 1995. “The Role of Product Architecture in the Manufacturing Firm.” Research 
Policy 24 (3): 419-440. 

Wilhelm, Bernd. 1997. “Platform and Modular Concepts at Volkswagen: Their Effects on the 
Assembly Process.” In Transforming Automobile Assembly—Experience in Automation 
and Work Organization, by K. Shimokawa,, U. Juergens and T. Fujimoto, 146. Berlin: 
Springer. 

Wilkes, Lawrence. 2012. Establishing a Reference Framework: An Overview. Fairfax, Va.: 
Everware-CBDI, Inc. 

Zimmerman et al. 2018. “Considerations and Examples of a Modular Open Systems Approach in 
Defense Systems.” Journal of Defense Modeling and Simulation.  

 
 
 
 


 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


 

 

Modular Open Systems Approach (MOSA) Reference Frameworks in Defense Acquisition 
Programs 
 
 
Office of the Under Secretary of Defense  
Research and Engineering 
3030 Defense Pentagon 
Washington, DC 20301-3030 
 
Distribution Statement A. Approved for public release.  Distribution is unlimited.   
DOPSR Case # 20-S-1275. 
 


