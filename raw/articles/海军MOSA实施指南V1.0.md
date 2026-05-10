Naval Modular Open 
System Approach 
Guidebook
OPEN BUSINESS AND TECHNICAL APPROACH FOR WEAPON SYSTEMS 
Interoperable
Scalable
Speed of Upgrade
Technology Refresh
Version 1.0


- ---
---
--
Forward 
It is with great pride and anticipation that I present this Naval Guidebook for implementing a Modular 
Open System Approach (MOSA). This guidebook focuses on the operational imperative of designing 
flexibility into our products and business models and represents a significant step forward in our ongoing 
commitment to enhancing the flexibility, interoperability, and cost-effectiveness of our naval systems. 
As the Assistant Secretary of the Navy for Research, Development, and Acquisition (ASN-RDA), I have 
witnessed firsthand the transformative impact that MOSA can have on our naval capabilities. The 
integration of MOSA principles into our acquisition strategies and system designs is a proven way to 
facilitate operational choice as well as a strategic and legal imperative. MOSA empowers us to efficiently 
build and sustain adaptable and resilient systems in order to stay combat relevant. Our contracting 
approaches and the associated systems must evolve in response to emerging threats and technological 
advancements, ensuring that our fleet remains at the cutting edge of naval warfare. 
This guidebook is a useful set of instructions and a blueprint for innovation and excellence. By following 
the guidelines outlined within these pages, we can foster a culture of modularity and openness that will 
enhance our ability to rapidly and efficiently integrate new technologies, while also promoting cost 
effectiveness and reducing lifecycle risks. 
Modular Open System Approaches and techniques are still being developed and explored with different 
levels of detail and varied success. Lessons and best practices are being discovered as organizations 
implement their approaches and learn to innovate even faster. This Guidebook will evolve and update 
best practices and recommendations in future revisions. 
The principles of MOSA align seamlessly with our broader goals of improving system performance and 
operational readiness. By adopting modular and open systems, we not only advance our technological 
capabilities but also ensure that our naval forces will remain agile and prepared for the challenges of the 
future. This guidebook is a testament to our commitment to innovation and to equipping our Navy and 
Marine Corps with the tools they need to achieve mission success. 
I would like to extend my deepest gratitude to the dedicated team who contributed to the development 
of this guidebook. Their expertise and effort produced a resource that will undoubtedly serve as a 
cornerstone in our journey towards a more dynamic and responsive naval force. 
As you delve into the pages of this guidebook, I encourage you to embrace the principles of MOSA and 
apply them with diligence and creativity. Together, we can harness the full potential of this approach to 
drive our naval systems into a new era of capability and efficiency. 
Nickolas H. Guertin 
Assistant Secretary of the Navy 
(Research, Development and Acquisition) 


P a g e  | 1 
 
Contents 
1. 
Introduction .......................................................................................................................................... 3 
2. 
Purpose and Applicability ..................................................................................................................... 5 
3. 
MOSA Benefits and Requirements ........................................................................................................ 5 
3.1   MOSA Motivation and Benefits ........................................................................................................ 5 
3.2   Summary of MOSA Legal and Policy Requirements .......................................................................... 6 
4. 
MOSA Process ....................................................................................................................................... 6 
4.1 
Starting Points for Modernization of Current Programs ............................................................... 6 
4.2 
Starting Points for New Programs ................................................................................................. 7 
4.3 
Business Case Analysis (BCA)  and Analysis of Alternatives .......................................................... 9 
4.4 
Intelectual Property ...................................................................................................................... 9 
4.5 
Modular Decomposition ............................................................................................................. 10 
4.6 
Functional Decomposition .......................................................................................................... 11 
4.7 
Physical Decomposition .............................................................................................................. 12 
4.8 
Open Interfaces .......................................................................................................................... 12 
4.9 
MOSA versus Non-MOSA Interfaces ........................................................................................... 14 
4.10 
MOSA Reference Architectures and Standards .......................................................................... 14 
4.11 
Program Interface Repository ..................................................................................................... 14 
5. 
Acquisition Strategies .......................................................................................................................... 14 
5.1  
Considerations across Adaptive Acquisition Framework Pathways ............................................ 14 
5.2        Basic Steps in the Development of a MOSA-aligned System ...................................................... 17 
5.3        Implementation within a Commercial Off-The-Shelf (COTS) or Non-Developmental Item (NDI) 
Acquisition Strategy ................................................................................................................................ 18 
5.4  
Considerations within the Logistics Framework ......................................................................... 19 
6. 
Technical Standards and Interfaces ..................................................................................................... 20 
6.1 
Identifying and Selecting Relevant Technical Standards and Interfaces for MOSA .................... 20 
6.2 
System of Systems Considerations: Ensuring Interoperability and Compatibility with Existing 
Systems in the Navy Enterprise ............................................................................................................... 23 
7. 
Considerations within a Systems Engineering Plan (SEP) ................................................................... 26 
8. 
Considerations across Systems Engineering Technical Reviews (SETR) .............................................. 28 
9. 
MOSA Training and Resources ............................................................................................................ 31 
10. 
References ....................................................................................................................................... 32 


P a g e  | 2 
APPENDIX A: Legal and Policy Requirements Covering MOSA ................................................................... 34 
A.1 
United States Codes (U.S.C) Title 10 ........................................................................................... 34 
A.2 
Defense Federal Acquisition Regulation Supplement MOSA Policy ........................................... 34 
A.3 
Department of Defense MOSA Policy ......................................................................................... 35 
A.4 
Navy MOSA Policy ....................................................................................................................... 35 
 
 
 
 


P a g e  | 3 
 
1. Introduction 
Weapon systems that are delivered today must be capable of accepting rapid updates and technology 
insertion in order to maintain operational relevance in a dynamic environment.  Our warfighters are put 
at risk when our adversaries are more agile than we are through their novel use of readily available 
commercial technology. We must be agile as well. And we can be agile by building our systems with 
modular and open architectures that are easily adapted and upgraded to meet the evolving threat. This 
guidebook will help our acquisition and engineering professionals establish such a basis. This is version 
1.0 of the guidebook that will be revised frequently because the advances in systems engineering and 
business process technologies demand it. Your feedback is encouraged. An internal website with 
common access card and Yubikey access will provide a mechanism for feedback. A more open, accessible 
site for feedback from anyone interested in improving Naval capability is also being considered.  
The Modular Open System Approach (MOSA) is an integrated acquisition and technical approach which 
has two “sides” (see Figure 1): A Business side that addresses the acquisition of a system (including 
procurement methodology) and a Technical side that defines the make-up of the system to be procured.  
 
 
Figure 1. MOSA has a Business Side and a Technical Side (from "SOSA 101") 
 
“The objective in implementing this approach is to ensure systems are designed, where possible, with 
highly cohesive, loosely coupled, and severable modules that can be competed separately and acquired 
from independent vendors. This can allow the DoD to acquire warfighting capabilities, including systems, 
subsystems, software components, and services with an increased level of flexibility and competition 
over previous proprietary programs. MOSA implies the use of modular open systems architectures: an 
existing concept in which system interfaces share common, widely accepted standards.” [NDIA MOSA 
White Paper, 2020-07] 
There are five overarching MOSA Principles that are essential to a successful MOSA acquisition: 


P a g e  | 4 
1. Establish Enabling Environment 
2. Employ Modular Design 
3. Designate Open Interfaces 
4. Use Widely Available Consensus Based Standards, and  
5. Certify Conformance.  
When implementing an established Open Systems Architecture, principles 3, 4, and sometimes 5 are 
inherently addressed, providing a solid foundation for your acquisition strategy. 
 
A MOSA is also a statutory requirement and policy-directed systems acquisition and engineering 
architecture approach for the United States Department of Defense. The benefits sought from a Modular 
Open System Approach are developing, delivering, fielding and maintaining our warfighting and mission 
effectiveness advantage across our diverse portfolio of weapons systems, which may also result in other 
benefits, including savings in time and increases in operational value for new systems development, 
faster technical upgrades, easier interoperability, and continuing savings during the sustainment phase of 
a system lifecycle (Defense Standardization Program, 2024). These reasons for using a MOSA are a basis 
for measuring the impact of MOSA in Navy programs, and for assessing the acquisition strategy and 
technical implementation of the 
approach. This guide will help 
programs to establish sound MOSA 
acquisition strategies. Title 10, sections 
4401, 4402, and 4403 establish the 
requirements for MOSA in the DoD. 
Section 4402 requires that a program’s 
Milestone B decision not be approved 
if the program did not implement a 
MOSA or provide an analysis showing 
why a MOSA was not chosen. Systems 
developed using modern digital 
engineering techniques are more likely to do well with these key indicators of a MOSA. This statutorily 
required analysis comparing a Modular Open System Approach to another approach should assess 
schedule and cost differences, future system technical upgrades, interoperability, and operational   costs. 
The Navy is looking for these business case analyses and will ensure that appropriate rigor is applied 
throughout the gate review process. It should also consider operational impacts of a MOSA. Modular 
systems allow component swapping. Open architecture interfaces that are software defined allow faster 
upgrades and can provide increased resilience from cyber-attack by leveraging secure software 
development standards. A MOSA enables adoption of operationally advantageous modifications when 
broadly adopted and well managed software defined interfaces are used.  
“Our current system is too slow and too focused on acquiring systems not designed to address 
the most critical challenges we now face… This orientation leaves little incentive to design open 
systems that can rapidly incorporate cutting-edge technologies, creating long-term challenges 
with obsolescence, interoperability and cost effectiveness.” 
- 2022 National Defense Strategy, pg. 27 [emphasis added] 


P a g e  | 5 
 
2. Purpose and Applicability 
This guidebook provides a process for implementing a modular open system approach. It is applicable to 
all Naval acquisition programs on any acquisition pathway in any SYSCOM — for new systems as well as 
for upgrades to existing systems. This guidebook was developed in collaboration with the Naval System 
Commands (SYSCOMS), and benefits from collaboration between the Navy, Air Force, Army, and Office of 
the Secretary of Defense. This guidebook is maintained by the office of the Chief Engineer of the Navy 
for the Assistant Secretary of the Navy for Research, Development, and Acquisition.  This guide is a 
complement to the DoD MOSA Implementation guidebook and a companion to those from the Army 
and Air Force. In this guide you will find the MOSA principles, practices, and processes for Naval 
engineering and acquisition professionals.   
3. MOSA Benefits and Requirements 
The implementation of MOSA is a statutory requirement – and a sensible acquisition practice. The old 
joke, “It’s not just a good idea, it’s the law” applies to MOSA. 
3.1   MOSA Motivation and Benefits 
The primary motivation for MOSA is operational capability. The United States Navy and Marine Corps 
need systems that can adapt and accept upgrades after delivery.  It is advantageous to industry and 
government for modern systems to be modular and open because it allows the most capable 
technology to be fielded efficiently. This allows the best performers to compete in areas that they 
are strongest. Benefits of MOSA include: 
· 
Facilitating technology refresh by using modular design (for both hardware and software), easily 
replaced modules can be independently replaced with more modern or technologically capable 
equivalents, often from a completely different supplier, without impacting the rest of the system 
· 
Enabling reuse (portability) because severable software and hardware modules that are aligned 
to standards can easily be used in other systems that are based on the same standards 
· 
Enhancing competition through the use of open architecture and standard interfaces, thereby 
allowing system elements (software and hardware modules) to be openly competed 
· 
Encouraging innovation by providing small business with the opportunity to innovate on 
modular elements of a system regardless of who the original manufacturer is, and when smartly 
implemented intellectual property policy is included, it provides a financial incentive for R&D 
investment 
· 
Enabling operational flexibility because of the availability of standardized modules thereby 
creating the opportunity for warfighters to configure and reconfigure available assets to respond 
to rapidly changing operational conditions 
· 
Enabling cost savings and cost avoidance which can be realized through the reuse of technology, 
modules, and/or system elements from any supplier across the acquisition and sustainment life 
cycle (e.g., common modules reduce burden on training and depot supplies) 
It is important to realize that the benefits of MOSA extend beyond the initial procurement; the real 
power of MOSA is realized over the lifecycle, where systems initially procured with the then-state-of-


P a g e  | 6 
the-art capabilities can much more easily be upgraded with the current state-of-the-art. By 
employing open interfaces and modular design, a decade-old system can efficiently incorporate a 
more capable module in place of the older one. This will at least ensure that systems stay in 
operation, and at best will markedly increase that systems capability. 
3.2   Summary of MOSA Legal and Policy Requirements 
The Fiscal Year 2017 National Defense Authorization Act’s (NDAA's) Section 805 requires major 
defense acquisition programs to adopt a Modular Open System Approach (MOSA) for incremental 
development, competition, innovation, and interoperability. It mandates updates to legacy systems 
and the creation of data repositories. The Fiscal Year 2021 NDAA's Section 804 extended the MOSA 
requirement to all defense acquisition programs and emphasized the importance of open systems 
and modularity. NDAA ’21 imposed regulations to promote modular interfaces and improve 
interoperability and cybersecurity. These are now codified in Title 10 of the US Code sections 4401, 
4402, and 4403. The Defense Federal Acquisition Regulation Supplement (DFAR) and DoD policies 
further support MOSA implementation, requiring its inclusion in acquisition strategies and risk 
assessments. 
Because of the operational need, Secretary of The Navy Instruction 5000.2G Enclosure (9) mandates 
MOSA design principles in acquisition programs, requiring digital representation of system 
components for integration and upgradeability. The Defense Standardization Program provides 
guidance on naval MOSA initiatives, including various open system architectures and standards. 
These efforts aim to enable strategic advantage, system interoperability and technology integration 
to maintain operational relevance throughout the system’s life. 
4. MOSA Process 
4.1 Starting Points for Modernization of Current Programs 
This section applies to improving Naval readiness through modernization of current programs and 
align them with MOSA objectives. Older in-service programs tend to have architectures with low 
cohesion and high coupling (many functions are highly intertwined) which may present technical 
challenges. Consider the following analyses for when upgrading/modernizing systems: 
 
What is the Expected Service Life of the system? 
o Programs nearing end of life within 5 years with little-to-no future modifications planned 
may not benefit from altering their architecture to include MOSA interfaces. Use 
historical information when predicting if the expected end of life is likely to be delayed. 
 
Is the modification replacing obsolete components? 
o Obsolescence is a large cost driver on programs and open architecture standards employ 
hardware and/or software abstraction techniques that allow for cost effective 
replacement. 
 
Can the modification be executed in such a way as to open a portion of the overall architecture? 
o Modification programs may not allow for the application of MOSA enabling standards at 
all interfaces, but an assessment should be conducted to see which interfaces can be 
open. Contractors should be involved with this process to achieve the best possible 
outcomes. 


P a g e  | 7 
 
What future modifications are projected for the system? 
o An example of an incremental MOSA is during an upgrade of a sensor subsystem in 
which the Mission System portion of the architecture is converted from a deterministic 
architecture to a Service Oriented Architecture. An element of mission processing can be 
converted to handle integration with subsystems using the publish-and-subscribe 
methodology reducing the integration work and regression test cases needed during 
further integration efforts. Then subsequent subsystem modifications on the platform 
will benefit from the reduced coupling and allows for better modularity. 
 
What is the threat environment for the system? 
o Rapidly evolving threat environments can be overcome with systems properly 
modularized for rapid upgrade. 
If required, the Systems Engineering Plan (SEP) or Acquisition Strategy should be updated to include 
the program’s MOSA strategy, and the acquisition program office should develop an Open Systems 
Management Plan (OSMP) for the system. If either a SEP or OSMP do not exist, they should be 
written to describe how the program can address incremental changes to the architecture to build in 
open interfaces during modifications. For example, without these plans, shared components or 
modules of a system may get tailored over time thereby losing commonality. An enterprise business 
case may drive these differences back into a common MOSA component or module.  
If a MOSA cannot be applied to a system, ensure the rationale is documented in the SEP and justified 
with a Business Case Analysis. After the MOSA strategy is written for inclusion in the SEP and OSMP, 
the components being modified or added should be decomposed. Logical and functional 
decompositions should be created to provide a starting point for discussing MOSA requirements 
with contractors. Failing to provide a functional and/or logical decomposition of the system may limit 
the government’s ability to clearly articulate which interfaces they wish to be targeted to be open.  
4.2 Starting Points for New Programs 
Navy programs at the beginning of the acquisition lifecycle have the maximum ability to implement 
MOSA concepts into their design. Figure 2 below shows an outline for implementing MOSA and 
where those steps can apply in the acquisition lifecycle. Careful planning at the outset (including 
defining overall and MOSA objectives) is crucial for achieving the desired outcome. Matching to the 
right Open Systems Architecture enables efficient reuse. Most systems will find that existing system 
architectures will meet requirements. There are numerous reference architectures that offer a good 
starting point for identification of existing open solutions. The modular decomposition and 
identification of modular interfaces, as well as required deliverables and data rights, should precede 
drafting an Open Systems Master Plan (OSMP) to ensure lifecycle needs and IP rights are correctly 
incorporated. 
 


P a g e  | 8 
 
Figure 2: MOSA implementation process flowchart 
The engineering team on a new program should either include Model Based Systems 
Engineering (MBSE) tools and data storage in the funding requests or ensure that Navy 
enterprise tools are available. MOSA should be included in any digital strategy. As previously 
mentioned, the first pillar of MOSA is the establishment of an enabling environment to support 
sharing of architecture and system design information. The 2018 DoD Digital Engineering 
Strategy encourages planning for models to support engineering activities and decision-making 
across the lifecycle. In February 2022, the DoD published the Systems Engineering Guidebook 
(DoD, 2022), which provides guidance and recommended best practices for defense acquisition 
programs. Once the digital environment and MBSE tools are instantiated, they should be used to 


P a g e  | 9 
create a modular decomposition of the system architecture based on a set of criteria aligned 
with the MOSA goals for the system or the incarnation of an established OSA. 
We can ensure low-risk implementations of MOSA by extending the MOSA concept to 
cybersecurity requirements and implementing cutting-edge, modular security solutions for 
operational technology. Programs should also consider using their MBSE processes to allocate 
DoD Zero Trust Architecture requirements across technical baselines to achieve a robust security 
configuration and enable rapid assessment of their cybersecurity posture.  
4.3  Business Case Analysis (BCA) and Analysis of Alternatives (AoA) 
Title 10 United States Code Section 4402 requires that Analysis of Alternatives (AoA) and the 
Acquisition Strategy of a program include MOSA considerations.  
A BCA and AoA is required if a Modular Open System Approach is not chosen. The technical and 
business advantages of MOSA as described in this guidebook are good considerations for this 
analysis. The use of MOSA in acquisition is assumed, but if a program has justification for a 
different approach, it will be included in an AoA and BCA. The MOSA avoidance BCA must 
consider the full lifecycle of the system, future upgrades, and components that are likely to 
become obsolete or be subject to frequent upgrade. For example, commodity computer 
hardware and software will experience frequent update due to cybersecurity and market 
conditions that are out of the control of the program office. Modern operating systems and 
software components are continuously developed and released resulting in rapid obsolescence. 
Up front consideration of this will mitigate the risk of unforeseen costs and barriers to future 
system upgrades and technology refreshes. Refer to the DoD MOSA website at cto.mil/sea/mosa 
for guidance as it evolves. There is information about business case analysis available at, 
https://www.dau.edu/glossary/business-case-analysis. Finally, DoD Instruction 5000.73 “Cost 
Analysis Guidance and Procedures” instructs programs on cost analysis activities.  
 
4.4 Intellectual Property 
Intellectual Property (IP) plays a crucial role in a MOSA acquisition. A MOSA can incentivize 
industry to invest in innovative technologies with confidence that their IP rights are protected. 
The Navy benefits when industry is incentivized to innovate and develop the next generation of 
technology advances.  The IP protections that MOSA offers is part of the acquirer-supplier win-
win that MOSA provides.  
Central to the MOSA IP approach is the so-called “Gray Box Concept” whereby: 
 
Functions within Modules are defined and known 
 
Behaviors exhibited by the Modules defined and known 
 
Interfaces between Modules are defined and known 
 
What is not defined and known is how the Functions (Modules) are instantiated  
Modules are not Black Boxes 
An acquirer that wishes to replace (upgrade) a Module later only needs to know the 
functionality contained within the module (the “what”) as well as the Module’s open interfaces. 


P a g e  | 10 
But does not need to know the methodology used to achieve the functionality (“the how”). The 
key point in this is that MOSA allows the developer to protect their intellectual property – and 
therefore this removes disincentives for investment in innovative solutions – while at the same 
time, the government ensures that incremental upgrades are possible even without the 
cooperation of the original equipment provider. 
By analogy, the familiar “light bulb standard” only requires that the bulb produce light when 
120VAC is applied, and that the interface be defined as the standard Edison 26 (E26) base we 
are all familiar with. The consumer does not need to know the details of the manufacturing 
process used to extrude a Tungsten filament – nor does it care. All that matters is that the 
functionality is there (light is produced) and the bulb can be screwed into the socket. The 
manufacturer’s method of producing the light is their IP and their “secret sauce” that will enable 
them to remain competitive (and producing light bulbs). In fact, by not specifying how the light 
is produced incentivizes the manufacturer to invent alternate methods of producing light, such 
as substituting light emitting diodes (LEDs)for a hot Tungsten filament – thereby creating a more 
efficient and rugged light bulb. One can think of that as the very first MOSA.  
 
4.5 Modular Decomposition 
Decomposition is the process of dividing of an entity into the budling blocks that can be 
combined to create the intended system. More technically Modularity is where “… functionally is 
partitioned into discrete, cohesive, and self-contained units with well-defined interfaces that 
permit substitution of such units with similar components or products from alternate sources 
with minimum impact on existing units.” 
Modularity is one of the most powerful tools for dealing with complexity. Before including MOSA 
requirements in the request for proposals it is important to understand and document the 
intended decomposition of the system architecture. Modular Decomposition should be 
accomplished with open interfaces in mind, and the criteria used when defining the modular 
decomposition should be derived from the overall MOSA objectives of the program, such as ease 
of integration of new/upgraded technology, third-party replacement of major subsystems, depot 
maintenance leveraging an existing component supplier ecosystem, etc. 
With the advancement of MOSA enabling standards and open systems architectures (OSAs), the 
preferred approach is to align the modular decomposition in alignment in one of the many OSAs 
available.  
Functional decomposition should be performed prior to physical decomposition (see the 
following sections), so that functional partitioning can be accounted for during physical 
decomposition. Modular decomposition will identify relevant subsystems or major system 
component interfaces where open architecture techniques should be applied. 
 


P a g e  | 11 
4.6 Functional Decomposition 
Functional decomposition refers broadly to the process of assigning the many functions that a 
system performs to the modules that make up the system. The MOSA community uses the term 
“encapsulation” to describe the process whereby a set of functions are bundled together and 
treated as a unified model. MOSA modularity is about these functional building blocks, as 
depicted in Error! Reference source not found.. 
 
 
Figure 3. Modularity is Encapsulating Functions 
  
Generally speaking, the functions encapsulated within the modules consume signals and/or data 
and produce signals and/or data. Some functions consume the products of other functions, 
leading to input/output (I/O) relationships. Individual I/O relationships are called “interactions.” 
The cases where an Interaction involves two functions that are contained within a module (an 
intra-modular interaction) are not addressed by MOSA. But cases where a function in one 
module has an interaction with a function in another module (inter-modular interactions) are 
key to MOSA. These inter-module interactions form the basis of an interface; an interface 
between modules consists of the aggregate of the inter-module interactions between them. In 
MOSA, we define the interfaces between the specific and various modules that make up a 
system. 
A central tenet of MOSA is that there is high cohesion with modules, and there is loose coupling 
between modules. Using the light bulb analogy (above), the electrical contact at the E26 base of 
the bulb is loosely coupled with the lamp socket (one can easily unscrew the bulb), whereas 
inside the bulb, the Tungsten filament is soldered to the base, and enclosed in an evacuated 
glass envelope (you would not want to try to replace the filament of a burned-out bulb by 
unsoldering it because of the tight coupling). 
There are many considerations to consider when determining the right functional encapsulation 
(see Error! Reference source not found.). For example, if safety critical and nuclear surety 
functionality might benefit from loose coupling (isolation) from the rest of the architecture, it 


P a g e  | 12 
would be best to encapsulate them together inside a module. Another consideration is testing 
methodology; it is desirable to minimize the need for regression testing of safety/nuclear critical 
functionality when non-critical functionality is upgraded, modified, or replaced. Ultimately, the 
process of defining and applying the encapsulation criteria is an iterative one and should be 
undertaken with full Stakeholder cognizance. 
4.7 Physical Decomposition 
Program offices may perform some physical decomposition of the system or (possibly less 
desirable) may task the responsibility of the physical decomposition to a contractor. The physical 
decomposition is driven largely by factors such as volume, weight distribution, power availability, 
and environment (temperature, pressure, shock/vibration). Physical partitioning is also driven by 
the functional decomposition and presence of modular interfaces. It is counterproductive to split 
a module (which has high internal cohesion) into separate physical units. It is more practical to 
co-locate modules in one physical unit; multiple functional capabilities may be achieved through 
one physical component. Some examples: 
 
A multi-function sensor that combines electro optical, passive optical, and synthetic 
aperture radar.  
 
Multiple software modules hosted on a one single board computer and occupying a 
chassis with other similar multi- or single-module single board computers 
 
Front-end processing co-located with a radar aperture.  
 
The Functional and Physical decompositions should be created to work together – but it is 
important to ensure that the functional (e.g., electronic and digital) interfaces are exposed, and 
standard connectors are used internal to the physical partitioning so that independent, third-
party modular upgrades are practical. In the same vein, in complex systems where several 
software modules exist within a physical component, it is required that all interfaces between 
software modules, as well as their interfaces with the physical components be exposed. In other 
words, simply co-hosting functional modules on physical infrastructure does not remove the 
MOSA requirement for interface exposure, separability, and upgradability.  
Proper federation of critical and non-critical functions position a program for constant lifecycle 
savings by significantly cutting unnecessary test cost and schedule. Due to the varying 
capabilities and mission requirements for Naval systems, there is no single checklist applicable to 
every program to ensure the modular decomposition is done correctly; program offices are 
strongly advised to leverage the expertise of SMEs during architecture reviews to prevent 
physical partitioning from undermining MOSA objectives. 
4.8 Open Interfaces 
The term “open” is often used – and more often abused. It is very context dependent, so it is 
important to clarify how the term is used in MOSA. Please be clear about one thing: “Open” 
does not mean “you can find it on the Internet” 


P a g e  | 13 
In their very well-written essay, “Fifty Shades of Open,” authors Jeffery Pomeranz and Robin 
Peek address how the term “open” is used in a wide variety of contexts. Among the many uses 
of the term “open” that they cover, the following have nothing to do with MOSA: Open Source, 
Open Access, Open Content, Open Technology, Open Approach, Open Principle, or Open License. 
Among the uses of the term “open” that do apply to MOSA are: 
Open Standards: Widely accepted and supported standards set by recognized standards 
organizations or the marketplace. These standards support interoperability, portability, and 
scalability and are equally available to the general public at no cost or with a moderate license 
fee. [Glossary of Defense Acquisition Acronyms & Terms, 14th Edition, June 2011]  
Open Systems: Employs modular design tenets, uses widely supported and consensus-based 
standards for its key interfaces, and has been subjected to successful validation and verification 
tests to ensure the openness of its key interfaces. [Cenotes] 
Two key phrases come out of these: “recognized standards organizations” and “consensus-based 
standards” 
The “Open” in MOSA really boils down to three things (and all three are necessary): 
1. Widely available (to the relevant community), will document definitions 
2. Consensus-based, typically set by a recognized standards-body, so that interested parties 
can shape it through a governance process that enables stakeholders to influence and 
effect the development and evolution 
3. Has conformance/compliance validation process to ensure it is fully testable 
These are the criteria to be used for all MOSA-based acquisition. A supplier simply 
publishing something does not make it “open” (because in all likelihood, only the 
supplier will be in a completive position to use that published proprietary artifact. 
Interfaces generally have three dimensions that must be defined:  
 
Physical: Medium (e.g., wire, fiber, connector) and/or mechanical (e.g., thermal, 
fastener, bolt circle, etc.) 
 
Protocol: The method used to exchange signals or data (e.g., carrier, framing, 
acknowledgments methods, etc.) 
 
Signal/Data Structure: The “payload” being delivered (e.g., waveform, messages, files, 
discrete signals, etc.), including all relevant functional interactions 
For interfaces that involve the exchange of data, it is a best practice to use a Data Model to 
capture the nature of the data: Conceptual Data Model (DIV-1) documents at a high-level the 
type and nature of the data to be exchanged (including their relationships), Logical Data Model 
(DIV-2) captures (in detail) the data content (including the units or coordinate frame), and 
Physical Data Model (DIV-3) that documents the physical manifestation of the data (exact 
format; bits per field, formats, schemas, structures). When these are fully defined, it enables 
independent third-party replacement. 


P a g e  | 14 
4.9 MOSA versus Non-MOSA Interfaces 
There is a difference between MOSA interfaces and non-MOSA interfaces. For a modular 
interface to be considered a MOSA interface, the interface must be widely used, consensus 
based, and subject to compliance or conformance validation – in other words, open. By 
leveraging an open systems architecture (OSA) the MOSA interface is automatically open. 
In the case where a MOSA interface is derived from an offering from a single vendor – in other 
words not open – the Government must attain required technical data and computer software 
deliverables related to MOSA interfaces with sufficient rights to enable incremental upgrades to 
be fairly competed. 
Non-MOSA interfaces are acceptable in situations where the government is deliberately allowing 
one vendor (e.g., a prime) to maintain control. There are very few specific circumstances where 
that’s acceptable. 
4.10 
MOSA Reference Architectures and Standards 
The Navy Modular System Interface (MSI) Repository lists reference architectures and standards. 
The MSI repository will be maintained by Navy Chief Engineer and will take input from program 
offices and engineers. This resource will help engineers and program managers to leverage work 
and share across the community of system architects. The MSI repository can be found on the 
Naval Digital Engineering Body of Knowledge (NDEBOK) site at, 
https://wiki.lift.mhpcc.hpc.mil/confluence/x/twgSDQ. 
4.11 
Program Interface Repository 
Title 10 U.S.C. Section 4401 mandates that the department establish and maintain repositories 
for interfaces, syntax and properties, documentation, and communication implementations. 
Interface repositories should consist of the following: 
1. Software-defined interface syntax and properties, specifically governing how values are 
validly passed and received between major subsystems and components, in machine 
readable format. 
2. A machine-readable definition of the relationship between the delivered interface and 
existing common standards or interfaces available in Department interface repositories; and  
3. Documentation with functional descriptions of software-defined interfaces, conveying 
semantic meaning of interface elements, such as the function of a given interface field. 
Programs should use the Naval Integrated Modeling Environment and the MSI repository to 
fulfill the requirements in Title 10 U.S.C. Section 4401 – 4403. 
5. Acquisition Strategies 
5.1  Considerations across Adaptive Acquisition Framework Pathways  
Implementing the Modular Open System Approach (MOSA) across the various pathways of the 
Adaptive Acquisition Framework (AAF) enhances flexibility, interoperability, and cost-
effectiveness. Here's a tailored approach for integrating MOSA into each specific AAF pathway:  


P a g e  | 15 
1. Urgent Capability Acquisition (UCA)  
 
Objective: Rapidly address urgent operational needs with a focus on speed and 
effectiveness.  
 
MOSA Integration:  
- 
Modular Prototyping: Develop modular prototypes that can quickly incorporate or 
replace components based on evolving needs or new threats.   
- 
Open Standards: Use open standards to ensure that solutions can be easily 
integrated with existing systems and modified as needed.  
- 
Vendor Flexibility: Engage with vendors who can provide modular solutions that 
meet open standards, enabling rapid deployment and adaptation.  
 
2. Middle Tier of Acquisition (MTA)  
 
Objective: Accelerate the development and deployment of new capabilities, focusing on 
rapid prototyping and fielding.  
 
MOSA Integration:  
- 
Incremental Prototyping: Apply MOSA principles in prototype design to allow for 
iterative development and testing of modular components.   
- 
Scalable Design: Ensure that prototypes are designed with scalability in mind, 
allowing for gradual enhancements and integration of new technologies.  
- 
Standards Compliance: Implement modular interfaces based on open standards to 
facilitate rapid integration and upgrades.  
 
3. Major Capability Acquisition (MCA)  
 
Objective: Develop and deploy major defense systems with a focus on long-term 
capability and sustainability.  
 
MOSA Integration:  
- 
Architecture Planning: Design the system architecture to be modular from the 
outset, using open standards to ensure that components can be easily replaced or 
upgraded throughout the system’s lifecycle.  
- 
Lifecycle Management: Incorporate MOSA principles in lifecycle management to 
reduce maintenance costs and extend system longevity through modular upgrades.  
- 
Contracting: Include MOSA requirements in contracts to ensure all system 
components are interoperable and adhere to open standards, promoting 
competitive procurement and reducing dependency on specific vendors.   
 
4. Software Acquisition  
 
Objective: Acquire or develop software solutions that meet operational needs while 
ensuring flexibility and interoperability.  
 
MOSA Integration:  
- 
Modular Software Design: Develop software using modular architectures that 
support interchangeable components and plugins based on open standards.  
- 
Utilize secure software development pipelines that enable continuous authorization 
of modular applications for rapid deployment. 


P a g e  | 16 
- 
Interface Standards: Use open APIs and standardized interfaces to facilitate 
integration with other systems and ease the process of updating or replacing 
software modules.  
- 
Agile Development: Apply agile methodologies in conjunction with MOSA to allow 
for iterative development and rapid incorporation of new features, security updates 
or changes.  
 
5. Defense Business Systems  
 
Objective: Implement and manage systems that support the business operations of the 
DoD, such as logistics, financial management, and personnel systems.  
 
MOSA Integration:  
- 
Modular Business Solutions: Design business systems using modular components 
that can be easily integrated or replaced to address evolving business needs or 
regulatory changes.  
- 
Interoperability Standards: Employ open standards for data exchange and system 
interfaces to ensure compatibility with existing systems and facilitate future 
upgrades.  
- 
Data Management: Ensure that modular components adhere to open standards for 
data management, supporting interoperability and effective integration with other 
business systems.  
 
6. Acquisition of Services  
 
Objective: Procure services that support operational needs, including maintenance, 
logistics, and consulting.  
 
MOSA Integration:  
- 
Service Modularity: Define service contracts with modular deliverables that can be 
adapted or replaced as requirements change.  
- 
Standardized Interfaces: Use standardized interfaces and performance metrics to 
ensure that service components can be easily integrated and assessed.  
- 
Performance-Based Contracts: Structure service contracts to focus on modular 
outcomes and performance metrics, allowing for flexibility in service delivery and 
easier adjustments as needs evolve.  
 
7.  Key Considerations Across All Pathways  
 
Open Standards: Implement and adhere to open standards to ensure interoperability, 
reduce integration challenges, enhance security and support future upgrades.  
 
Flexibility and Scalability: Design systems and contracts to accommodate modularity, 
allowing for easy replacement or enhancement of components without extensive 
rework.  
 
Cost Efficiency: Use MOSA to drive cost efficiencies through competitive procurement, 
reduced lifecycle costs, and minimized dependency on specific vendors.  


P a g e  | 17 
5.2 Basic Steps in the Development of a MOSA-aligned System 
1. Understand MOSA Principles: MOSA aims to enhance system flexibility, reduce lifecycle 
costs, and improve interoperability by using modular, open standards. Key principles include 
modularity, interoperability, and open standards.  
 
2. Define Architectural Objectives: Determine how MOSA principles align with your project's 
goals. This includes identifying the need for modularity, interoperability, and the use of open 
standards in your system.   
 
3. Use DoDAF Viewpoints to Document MOSA Implementation:  
 
All Viewpoint (AV): Document the overarching vision, principles, and guidelines for 
applying MOSA. This includes describing the modularity and open standards 
requirements.  
 
Capability Viewpoint (CV): Identify and document the capabilities required for 
implementing MOSA, such as modular interactions.  
 
Operational Viewpoint (OV): Define how modules will support operational processes. 
Illustrate modular interactions within the operational context.  
 
Systems Viewpoint (SV): Detail the system architecture using MOSA principles. Include 
descriptions of modular components, interfaces, and how they adhere to open 
standards. Show how individual modules are integrated and how they interact.  
 
Services Viewpoint (SvcV): Document the services provided by each modular component 
and their interactions.  
 
4. Apply Open Standards: Ensure that all modules and interfaces adhere to industry standards 
and open specifications to the maximum extent practicable. Document these standards in 
the relevant DoDAF Viewpoints.   
 
5. Assess Interoperability: Evaluate how different modules and components will interact and 
integrate. This involves documenting interface requirements and integration strategies. 
Consider Fit-for-Purpose Viewpoints as needed to ensure integration intent is understood. 
 
6. Assess cyber survivability: Utilize Mission-Based Cyber Risk Assessment methodology to 
apply relevant threat models against services and systems viewpoints referencing the Joint 
Chiefs of Staff Cyber Survivability Endorsement to the System Survivability Key Performance 
Parameter Cyber Survivability Attributes. 
 
7. Evaluate Modularity: In SVs, illustrate the modular design, showing how components are 
designed to be independently replaceable, upgradable, or testable – and by an independent 
third party (not just the OEM). 
 
8. Review and Iterate: Continuously review the evolving system design to ensure it remains 
true to the intended architecture and compliant with MOSA principles. In cases where the 


P a g e  | 18 
design deviates from the architecture, an independent architecture SME review should be 
conducted to determine if the design needs to be adjusted to compensate.  
5.3   Implementation within a Commercial Off-The-Shelf (COTS) or Non-Developmental Item 
(NDI) Acquisition Strategy 
1. Define MOSA Requirements  
 
Identify Objectives: Clearly define the objectives you want to achieve with MOSA, such 
as increased flexibility, reduced lifecycle costs, or easier integration with existing 
systems.  
 
Establish Standards: Specify open standards and interfaces for modular components. 
These should align with industry standards or be defined in a way that supports future 
upgrades and integration.  
 
2. Assess COTS/NDI Solutions  
 
Evaluate Compatibility: Assess COTS/NDI solutions against the MOSA requirements. 
Ensure that the products can be easily integrated into a modular architecture and that 
they adhere to the open standards defined.  
 
Conduct Market Research: Research available products and suppliers to identify those 
that offer the best alignment with MOSA principles and can meet the specific needs of 
your system.  
 
3. Develop an Acquisition Strategy  
 
Create a Modular Architecture: Design a system architecture that is modular, with well-
defined interfaces. This allows for the easy integration of COTS/NDI products and 
ensures they can be replaced or upgraded independently.  
 
Specify Interface Requirements: In your acquisition documentation, specify the interface 
requirements and standards that COTS/NDI products must adhere to. This helps ensure 
compatibility and interoperability.  
 
4. Incorporate MOSA into Contracting  
 
Include MOSA Clauses: In the acquisition contracts, include clauses that enforce 
adherence to open standards and modular design principles. This might include 
requirements for providing documentation, compliance with standards, and support for 
integration.  
 
Define Integration Points: Clearly define integration points and interfaces in the contract 
to ensure that COTS/NDI components will fit seamlessly into the modular architecture. 
 
5. Manage and Monitor Implementation  
 
Establish Integration Procedures: Develop procedures for integrating COTS/NDI 
components into the modular system. This includes testing for compatibility and 
performance against MOSA requirements.  
 
Monitor Compliance: Continuously monitor the compliance of COTS/NDI solutions with 
the defined standards and requirements throughout the lifecycle of the system.  
 


P a g e  | 19 
6. Plan for Upgrades and Evolution  
 
Support Future Upgrades: Ensure that the modular architecture and the COTS/NDI 
solutions support future upgrades and technological advancements. This might involve 
designing for backward compatibility or defining upgrade paths.  
 
Review and Adapt: Regularly review the system and acquisition strategy to adapt to new 
standards or changes in technology, ensuring that the modular architecture remains 
effective and relevant. 
5.4  Considerations within the Logistics Framework 
Modularity and Design 
 
How does the modular design of the system enhance logistics supportability? 
 
What specific modular components are critical for logistics, and how are they 
documented? 
Interoperability 
 
How do modular components ensure interoperability with existing logistics systems and 
processes? 
 
What standards are being used to facilitate compatibility across different platforms? 
Support and Maintenance 
 
What logistics strategies are in place to support the maintenance of modular 
components? 
 
How will the modularity of the system impact spare parts inventory and management? 
Cost Implications 
 
What are the projected life cycle costs associated with maintaining modular components 
compared to traditional systems? 
 
How does the use of multiple vendors for modular components affect overall logistics 
costs? 
Sustainability and Upgradability 
 
How does the modular approach accommodate future upgrades without significant 
logistics disruption? 
 
What plans are in place to evaluate the logistics impacts of evolving technology on the 
system? 
Risk Management 
 
What risks associated with modular components have been identified in the logistics 
assessment? 
 
How are risks being mitigated to ensure continuous logistics support? 
Documentation and Training 


P a g e  | 20 
 
What documentation practices are in place to ensure all logistics personnel understand 
the modular components and their support requirements? 
 
How is training being conducted to prepare logistics teams for the unique challenges of 
managing modular systems? 
Stakeholder Involvement 
 
How are logistics stakeholders engaged in the design and assessment process of modular 
components? 
 
What feedback mechanisms are established to gather insights from logistics personnel 
about the effectiveness of the modular design? 
 
6. Technical Standards and Interfaces 
6.1 Identifying and Selecting Relevant Technical Standards and Interfaces for MOSA 
One of the key aspects of MOSA is the careful identification and selection of open systems 
architectures (reference architectures) and technical standards and interfaces that ensure 
interoperability and modularity. 
 
The following steps are guidelines on how to identify and select the most relevant technical 
standards and interfaces when implementing a MOSA. By following the steps outlined below, 
programs can ensure that their systems are modular, interoperable, and adaptable, thereby 
enhancing their capability to respond to evolving requirements and technological 
advancements. 
 
Step 1:   Understand Mission and System Requirements 
Before selecting technical standards and interfaces, clearly define the mission and 
operational requirements for the system. This information is part of the “Define 
System and MOSA Objectives” phase. These requirements form the foundation of 
the system’s architecture and dictate the necessary functionality and performance 
levels. Ask these questions: 
•   What are the system’s primary functions? 
•   What environmental or operational constraints will the system face? 
•   How important is system interoperability with other platforms? 
•   Will the system need to be upgraded or modified in the future? 
By understanding the mission and system requirements, the systems engineer will 
be better equipped to choose standards that meet both current and future needs. 
 
Step 2: Identify Applicable Domains and Categories 
Once system requirements are clear, identify the domains in which standards and 
interfaces must be applied. These may include: 
•   Software (e.g., operating systems, middleware, data formats) 
•   Hardware (e.g., processors, communication buses, power interfaces) 


P a g e  | 21 
•   Communications (e.g., data link protocols, wireless standards) 
•   Security (e.g., encryption protocols, authentication methods) 
•   Data Management (e.g., data formats, storage standards) 
Each domain may require different types of standards to ensure modularity and 
interoperability. 
 
Step 3: Research Existing Open Standards 
In MOSA, the use of Open Systems Architectures (OSAs) and open standards are 
preferred because they reduce dependency on proprietary solutions thereby 
enabling module reuse, incremental third-party upgrades, and system 
interoperability.  
 
Table 1 identifies the applicability of some of the more common OSAs to the internal 
MOSA for various system types. 
Table 1. OSA Applicability 
 
Type 
OMS/ 
UCI 
VICTORY 
FACE 
SOSA 
OCS 
HOST 
COARPs 
Big 
Iron 
CoPaIS 
WOSA 
DEWS 
RA 
Sensors: Radar 
 
 
 
 
 
 
 
 
 
 
 
Sensors: Active EO/IR 
 
 
 
 
 
 
 
 
 
 
 
Sensors: Passive 
EO/IR 
 
 
 
 
 
 
 
 
 
 
 
Communications: LOS 
(Tactical) 
 
 
 
 
 
 
 
 
 
 
 
Communications: 
BLOS (Satellite) 
 
 
 
 
 
 
 
 
 
 
 
BMC3 
 
 
 
 
 
 
 
 
 
 
 
Weapons: Kinetic 
 
 
 
 
 
 
 
 
 
 
 
Weapons: 
Electromagnetic/EW 
 
 
 
 
 
 
 
 
 
 
 
Weapons: Directed 
Energy 
 
 
 
 
 
 
 
 
 
 
 
Avionics 
 
 
 
 
 
 
 
 
 
 
 
Systems Integration 
 
 
 
 
 
 
 
 
 
 
 
 
Begin by researching the following types of open standards: 
•   International Standards Organizations (ISOs): 
- 
ISO has a vast repository of standards covering various technical 
domains. 
- 
Explore ISO's online catalog to search for relevant standards based on 
keywords or subject matter. 
•   National Standards Bodies: 
National standards bodies, such as ANSI (American National Standards Institute) or 
BSI (British Standards Institution), often adopt and adapt international standards for 
their domestic markets. 


P a g e  | 22 
•   Industry Consortia and Associations: 
- 
Industry-specific consortia and associations often develop and promote 
standards to facilitate interoperability within their respective domains. 
- 
Examples include OASIS (Organization for the Advancement of Structured 
Information Standards) and IEEE (Institute of Electrical and Electronics 
Engineers). The Open Group manages FACE, SOSA, and VICTORY. 
•   Government Agencies: 
- 
Government agencies may publish standards or guidelines related to 
specific technical areas. 
- 
For example, the National Institute of Standards and Technology (NIST) in 
the United States provides a wide range of standards and 
recommendations. 
- 
Use open standards where feasible to ensure vendor neutrality and ease 
of future upgrades. 
 
Step 4: Evaluate Compatibility and Interoperability 
The chosen standards and interfaces must support seamless interoperability with 
existing systems and components. Assess compatibility by considering: 
•   Backward compatibility with legacy systems. 
•   Cross-domain interoperability (e.g., how well software can integrate with 
hardware components). 
•   Scalability to future versions or emerging technologies. 
Additionally, ensure that interfaces are well-documented, clearly defined, and 
adhere to widely accepted protocols. 
 
Step 5: Analyze Modularity and Flexibility 
MOSA emphasizes modularity, allowing system components to be independently 
developed, maintained, and upgraded. To support this: 
•   Choose modular interfaces that allow easy addition, removal, or replacement 
of components. 
•   Ensure that the selected standards support the decoupling of system 
components. 
For instance, selecting a common communication protocol like TCP/IP for network 
interfaces ensures that the system can evolve without needing to redesign the 
entire architecture. 
 
Step 6: Consider Lifecycle and Sustainment 
When selecting standards, consider the lifecycle of both the system and the 
standards themselves. Questions to ask include: 
•   Are the standards mature and widely supported? 
•   What is the likelihood that the standard will become obsolete or unsupported 
during the system’s life? 
•   Are there established support and documentation resources? 


P a g e  | 23 
Standards with strong industry backing and long-term viability ensure that the 
system remains supportable and upgradable throughout its lifecycle. 
 
Step 7: Verify Compliance with Regulations and Policies 
Ensure that the selected standards comply with relevant regulations, security 
requirements, and organizational policies. Consider: 
•   Security Requirements: Choose standards that support encryption, 
authentication, and other security protocols necessary to protect sensitive 
information. 
•   Regulatory Compliance: Systems may need to meet specific national or 
international regulatory standards (e.g., ITAR, FIPS). 
•   Environmental or Operational Compliance: Standards should account for 
environmental conditions such as temperature, humidity, and shock tolerance in 
the case of military systems. 
 
Step 8: Leverage Standards Consortia and Communities 
Many industries and sectors, including government, have consortia or 
standardization bodies that can help guide the selection of standards. Participation 
in these organizations can provide insights into the latest developments and trends 
and help to ensure that the selected standards remain relevant and aligned with 
industry trends. Examples include: 
•   The Open Group (for enterprise architecture standards like TOGAF) 
•   VMEbus International Trade Association (VITA) (for open hardware standards 
in embedded systems) 
•   The SOSA Consortium (government consortium for C5ISR standards) 
6.2 System of Systems Considerations: Ensuring Interoperability and Compatibility with 
Existing Systems in the Navy Enterprise  
A key objective of a Modular Open System Approach (MOSA) is to design systems that are 
modular and can easily integrate with other systems, both existing and future, across different 
platforms, domains, and vendors. Interoperability ensures that different system components can 
work together seamlessly, while compatibility ensures that new components can integrate into 
existing systems without costly redesigns or rework.  
The steps below provide guidelines to ensure interoperability and compatibility in MOSA, 
emphasizing techniques to minimize risk and ensure future adaptability. By following these 
guidelines, programs can create modular systems that seamlessly integrate with existing 
platforms, support mission-critical operations, and remain adaptable to future technologies.  
Step 1: Define Interoperability and Compatibility Requirements  
The first step to ensuring interoperability and compatibility is to establish clear requirements 
based on system use cases and operational environments. Consider these factors:  
 
Functional Requirements: Identify which systems or components need to 
communicate or work together.  


P a g e  | 24 
 
Data Interchange Requirements: Define the types, formats, and protocols for data 
exchanges between systems.  
 
Operational Requirements: Identify how systems must work together in different 
operational contexts (e.g., in the field, across networks, with different 
environments).  
Ensure that these requirements are aligned with mission goals and documented in system 
specifications.  
Step 2: Analyze Legacy Systems  
To ensure compatibility with existing systems, a detailed analysis of legacy systems is critical. 
This involves:  
 
Mapping existing external interfaces and protocols: Document the interfaces, 
communication standards, and protocols used by legacy systems.  
 
Identifying legacy constraints: Understand the limitations, such as outdated 
hardware, proprietary protocols, or unsupported interfaces, that may pose 
challenges to integration.  
 
Determining upgrade paths: Where possible, identify how legacy systems can be 
incrementally upgraded to improve compatibility with MOSA-based solutions (e.g., 
via adapters, middleware).  
This analysis will guide the selection of technical standards and highlight any areas where 
modifications or retrofitting may be needed.  
Step 3: Use Open Standards for Data Interoperability  
Interoperability in MOSA is best achieved by using open, widely accepted standards that 
ensure systems can communicate and interact seamlessly. Open standards:  
 
Reduce reliance on proprietary solutions (hardware, communications protocols, and 
data structures/formats).  
 
Allow integration with a wide range of third-party systems.  
 
Encourage vendor competition and innovation.  
Some key areas where open standards are critical include:  
 
Communication Protocols: Use open network protocols (e.g., TCP/IP, HTTP, MQTT) to 
ensure systems can communicate across different networks.  
 
Data Formats: Standardize data formats using XML, JSON, or other open formats for 
ease of data sharing.  
 
Hardware Interfaces: Adopt industry-standard hardware interfaces such as USB, 
Ethernet, and PCIe to ensure modularity and compatibility.  


P a g e  | 25 
By adopting open standards, programs can create systems that are adaptable and can evolve 
as technology advances.  
Step 5: Adopt Modular Interfaces and APIs  
To achieve modularity, MOSA requires the use of well-defined interfaces that allow 
components to be replaced or upgraded without significant redesign. Key strategies include:  
 
Application Programming Interfaces (APIs): Use standardized APIs that allow 
different software components to interact without needing to know the internal 
details of each system.  
 
Plug-and-Play Interfaces: Adopt standardized hardware interfaces that support plug-
and-play functionality, making it easier to integrate new hardware without system 
redesign.  
 
Service-Oriented Architectures (SOA): Design systems around a service-oriented 
architecture where software components can expose their capabilities through well-
defined service interfaces.  
Modular interfaces provide the flexibility to add new capabilities or replace outdated 
components while maintaining interoperability and compatibility.  
Step 6: Test for Interoperability and Compatibility  
Regular interoperability and compatibility testing is essential to verify that new systems or 
components can integrate with legacy systems and other modular components. Key testing 
approaches include:  
 
Integration Testing: Conduct tests that simulate real-world operations, ensuring that 
components can communicate and work together under operational conditions.  
 
Regression Testing: When adding new components, ensure they do not break 
existing functionality by running regression tests.  
 
Simulation-Based Testing: Use modeling and simulation environments to validate 
interoperability before actual deployment, especially for complex systems.  
Early and frequent testing will help detect issues before deployment and reduce the risk of 
costly integration failures.  
Step 7: Plan for Future Interoperability  
MOSA not only emphasizes current compatibility but also anticipates future interoperability 
as technology evolves. Futureproofing involves:  
 
Standards Roadmaps: Monitor and align with evolving standards in the industry to 
ensure long-term compatibility (e.g., upcoming versions of communication protocols 
or data formats).  


P a g e  | 26 
 
Modular Upgrades: Design systems in a way that modules or components can be 
upgraded or replaced with minimal impact on the rest of the system.  
 
Forward Compatibility: Consider the possibility of forward compatibility, ensuring 
that newly developed systems can integrate with future platforms or technologies.  
By planning for future interoperability, MOSA-based systems can evolve and adapt to new 
technologies and mission needs without requiring significant redesign.  
7. Considerations within a Systems Engineering Plan (SEP) 
Systems Engineering Plans are developed in accordance with DoD Instruction 5000.88. Utilizing 
DoD SEP Outline Version 4.1, MOSA can be integrated into sections where modularity, open 
standards, interoperability, and system architecture are discussed. 
Below are considerations where MOSA can be incorporated within a SEP: 
Program Technical Definition 
Requirements Development 
Include requirements that enforce modularity and the use of open standards. Specific 
 
requirements could be established to mandate the use of MOSA principles for the 
 
system to ensure that components can be replaced or upgraded without significant 
 
redesign. 
 
MOSA-related Requirements: Establish functional and non-functional 
requirements that reflect the need for modularity, such as the use of 
standardized interfaces, interoperability with other systems, and component 
reusability. 
Architectures and Interface Control 
Incorporate MOSA principles by detailing how system architecture will be designed with 
 
modularity in mind, using open interfaces and standards to enable easy upgrades, 
 
integration, and scalability over the system’s lifecycle. 
 
MOSA in System Architecture: Describe how the system will be designed to 
be modular, with clearly defined interfaces and open standards to ensure 
compatibility and ease of integration with future technologies and systems. 
 
Interface Control and MOSA: Explain how interface control will be managed 
to ensure that the system’s modules can communicate effectively, even 
when new components are integrated over time. 
Design Considerations 
MOSA directly impacts design decisions related to modularity, standardization, and 
future-proofing the system. 


P a g e  | 27 
 
Design for Modularity: Discuss how the design will incorporate MOSA 
principles, ensuring that each component of the system is modular, easy to 
upgrade, and replaceable. 
 
Standardized Interfaces: Highlight the importance of designing standardized 
interfaces that facilitate future technology insertion and interoperability. 
Program Technical Management  
Technical Planning 
Incorporate MOSA principles by ensuring technical planning includes strategies for 
modularity and the use of open standards. This could also be part of the risk 
management strategy, where the risks of vendor lock-in or obsolescence are mitigated 
by MOSA. 
 
MOSA in Technical Planning: Incorporate MOSA principles into the planning 
phase by setting up objectives for achieving modularity and the use of open 
standards throughout the program lifecycle. 
Maturity Assessment Planning 
MOSA could be assessed in terms of the maturity of modular components and open 
standards. This helps ensure that the approach to modularity is well integrated into the 
program’s maturity model. 
 
Maturity of Modular Designs: Include specific criteria for assessing the 
maturity of modular components, interfaces, and open standards as part of 
the overall maturity assessment. 
Technical Insertion and Refresh 
MOSA facilitates easier and more cost-effective insertion of new technologies. This could 
be emphasized as a core benefit of MOSA. 
 
MOSA for Technology Refresh: Highlight how the modular design and open 
standards allow for easier integration of new technologies, thus facilitating 
smooth technology refresh cycles without major system redesign. 
Configuration and Change Management 
Define how modular components and interfaces will be managed as part of the system’s 
configuration. The flexibility of MOSA will allow for more manageable and less disruptive 
changes. 
 
MOSA and Configuration Management: Explain how the configuration 
management process will account for modular components and interfaces, 
ensuring that changes to one module do not disrupt other parts of the 
system. 
 


P a g e  | 28 
System Security Engineering 
MOSA can be referenced in terms of how modular systems can better accommodate 
evolving security measures. Using standardized modules makes it easier to update 
security components without redesigning the entire system. 
 
Security and MOSA: Discuss how modular components and open standards 
facilitate the continuous upgrading of security features, such as encryption 
or authentication protocols, without disrupting other parts of the system. 
Digital Engineering Implementation Plan 
Incorporate digital models of modular systems. This ensures that each module is 
represented digitally, and that updates to one module can be easily simulated and tested 
within the larger system. 
 
MOSA in Digital Engineering: Describe how MOSA will be implemented in 
digital engineering practices to create flexible, modular digital models that 
can be easily updated, tested, and simulated. 
8.   
Considerations across Systems Engineering Technical Reviews (SETR) 
Systems Engineering Technical Reviews are conducted in accordance with DoD Instruction 
5000.88. Depending on the acquisition framework there are variations in content. These 
considerations are provided to assist programs in covering MOSA through these reviews. The key 
concern is that the team assess the implementation or planning for Modular Design, Key 
Interfaces, Open Standards, Conformance, and Enabling Environment. The SETR process will be 
updated in the near future, but at present, tailoring to take into account MOSA considerations is 
crucial. The MOSA Program Assessment and Rating Tool1 (PART) is a tool that can assist the SETR 
process, but it is dated and incomplete – so adapt the relevant portions into your SETR (but it is 
not fully Navy-ready).  
System Requirements Review 
 
Questions: 
o What modular design principles are being applied to meet system 
requirements? 
o How are interfaces defined in the requirements to ensure compatibility with 
modular components (particularly for joint interoperability if applicable)? 
 
Entry Criteria: 
o Approved Information Support Plan or Systems Engineering Plan that addresses 
MOSA. 
o Identified modularity and open interfaces to support MOSA. 
o Non-MOSA interfaces are captured with rationale for why they are not based on 
open standards. 
                                                          
1 MOSA PART is available from the Defense Acquisition 
University,:https://www.dau.edu/cop/mosa/documents/mosa-program-assessment-and-rating-tool-part 


P a g e  | 29 
o Identified test methodologies to verify compliance with standards. 
 
Exit Criteria: 
o Validated list of MOSA and Non-MOSA interfaces. 
o Waivers necessary for any specifically identified non-MOSA interfaces. 
Preliminary Design Review 
 
Questions: 
o Which open standards are being incorporated into the design, and how do they 
align with MOSA principles and support the objectives of the system? 
o What criteria were used for the selected modularization and how does that 
support the operational and lifecycle needs? 
 
Entry Criteria: 
o Identified modularization and loosely coupled interfaces along with supporting 
OSAs and interface standards. 
o Defined instance architecture aligned with the MOSA-based reference 
architecture supplied by the government. 
o Updated Systems Engineering Plan incorporating the instance architecture. 
o Identified test procedures to verify compliance with OSAs and open standards. 
o Updated Open Systems Management Plan (OSMP) based on the government-
supplied OSMP. 
 
Exit Criteria: 
o Approved instance architecture 
o Approved updated Open Systems Management Plan. 
Critical Design Review 
 
Questions: 
o How will components be integrated, and what integration challenges have been 
identified? 
o How well does the proposed design match the MOSA expectations and the 
government-supplied reference architecture? 
o What mechanisms are in place to accommodate independent, third-party future 
upgrades or modifications in the design, particularly regarding evolving 
missions? 
 
Entry Criteria: 
o Updated System Specification to include updated/refined instance architecture, 
complete design specifications that include final functional allocations to the 
system modules and fully defined interface specifications. 
o Updated Systems Engineering Plan. 
o Draft test plans for testing of modular systems. 
o Updated Open Systems Management Plan. 
 
Exit Criteria: 
o Approved Open Systems Management Plan 
o Approved system specification 
o Approved Systems Engineering Plan. 


P a g e  | 30 
o Approved draft test plans for testing of modular systems. 
Test Readiness Review 
 
Questions: 
o What testing strategies will ensure modular components function effectively 
together in operating environments? 
o What testing strategies will ensure full adherence with the MOSA-enabling 
standards? 
o How will validation processes adapt as new modules are integrated into the test 
plan, ensuring compliance with standards? 
 
Exit Criteria: 
o Approved Testing and Verification Documentation 
 
System Verification Review 
 
Questions: 
o What are the identified risks associated with modularity that could impact 
system verification? 
o How are the risks related to modular components being mitigated during the 
verification process? 
 
 
 


P a g e  | 31 
9. MOSA Training and Resources 
 
Defense Acquisition University’s CLE019 (“Modular Open System Approach”) (Defense 
Acquisition University, 2023) 
 
Let’s Be Modular and Open Webinars (DAU) (Defense Acquisition University, 2024) 
 
OUSD/CTO Web Site (Office of The Secretary of Defense (OSD), 2024) 
 
NDIA MOSA White Papers 
o 
MOSA: Considerations Impacting Both Acquirer and Supplier Adoption (National 
Defense Industrial Association Systems Engineering Architecture Committee, 2020) 
o 
MOSA Implementation Considerations, Information Needs and Metrics (National 
Defense Industrial Association Systems Engineering Architecture Committee, 2023) 
 
Presentation Slides: Get the Most out of MOSA: Begin with the End in Mind  (Davidson, 
2023) 
 
Defense Logistics Agency ASSIST Database (Department of Defense, n.d.) 
 
Webinar: A Best Practice for Developing a MOSA-based Reference Architecture -- Open 
Group Toolkit Tuesday (Feb. 22, 2022)  (Davidson D. S., 2022) 
 
MOSA Program Assessment and Rating Tool (PART) (Defense Acquisition University) 
Open Systems Architecture Training and Resources 
 
OMS/UCI (Open Mission Systems / Universal C2 Interface) Training (registration required) 
(United States Air Force) 
 
FACE (Future Airborne Capability Environment) Technical Overview (FACE Consortiem, 2020) 
 
SOSA (Sensor Open Systems Architecture) Primer (“SOSA 101”) (Sensor Open Systems 
Architecture Consortium, 2019) 
 
VICTORY (Vehicular Integration for C4ISR/EW Interoperability) (United States Army, 2015) 
 
MORA (Modular Open RF Architecture) (htt1) 
 
DEWS (Directed Energy Weapon System) MOSA Reference Architecture (Merkert, 2023) 
Historical References 
 
MOSA and Engineering Enablers,  (Gold, 2016) 
 
MOSA in DoD Acquisition,  (Welby, 2014) 
 
Modular Open Systems Contract Guidebook for Program Managers, May 2013 (United States 
Department of Defense, 2013) 
 
Article: DoD Open Systems Architecture Contract Guidebook for PMs,  (Guertin & Hurt, 2013) 
 
DoDI 5000.73, "Cost Analysis Guidance and Procedures," October 24, 2024 (United States 
Department of Defense, 2020) 
 
 


P a g e  | 32 
10.  References 
(n.d.). Retrieved from https://restricted.vdl.afrl.af.mil/webdav/programs/sosa/MORA/MORA V2.5 
Released 
Documents/MORA_V2.5_Training_Session_One_March_2023_CCDC_C5ISR_Center_DLB_Rev27
_DIST_A_APPROVED-23-319.pdf 
Davidson, D. S. (2022, February 22). A Best Practice for Developing a MOSA-based Reference 
Architecture. Retrieved from youtube: https://youtu.be/5E8b5jfJSec?t=287 
Davidson, D. S. (2023, September 18). events.techconnect.org/MOSA_2023. Retrieved from 
https://events.techconnect.org/MOSA_2023/slides/Get-the-Most-Out-of-MOSA-Begin-with-the-
End-in-Mind.pdf 
Defense Acquisition University. (2023, May 22). CLE 019 Modular Open System Approach. Retrieved from 
DAU: https://icatalog.dau.edu/onlinecatalog/courses.aspx?crs_id=12258 
Defense Acquisition University. (2024). Let's Be Modular and Open Webinar. Retrieved from DAU: 
https://media.dau.edu/playlist/1_8zmclxde 
Defense Acquisition University. (n.d.). DAU. Retrieved from 
https://www.dau.edu/cop/mosa/documents/mosa-program-assessment-and-rating-tool-part 
Department of Defense. (n.d.). ASSIST. Retrieved from https://assist.dla.mil/online/start/index.cfm 
DoD. (2022, February 1). Systems Engineering Guidebook. Retrieved from Mission Capabilities: 
https://ac.cto.mil/wp-content/uploads/2022/02/Systems-Eng-Guidebook_Feb2022-Cleared-
slp.pdf 
FACE Consortiem. (2020). Retrieved from Youtube: Youtube 
Gold, R. (2016, October). NDIA. Retrieved from 
https://ndiastorage.blob.core.usgovcloudapi.net/ndia/2017/groundrobot/Gold.pdf 
Guertin, N., & Hurt, T. (2013). DTIC. Retrieved from https://apps.dtic.mil/sti/tr/pdf/ADA608725.pdf 
Merkert, K. (2023, September). Tech Connect. Retrieved from 
https://events.techconnect.org/MOSA_2023/slides/Directed-Energy-Weapon-System-Modular-
Open-Systems-Approach-Reference-Architecture-(DEWS-MOSA-RA)_Publically-Released.pdf 
National Defense Industrial Association Systems Engineering Architecture Committee. (2020, July 1). 
NDIA. Retrieved from https://www.ndia.org/-/media/sites/ndia/divisions/systems-
engineering/se-monthly-meetings/division-papers/ndia-mosa-white-paper-final-release--ndia-
architecture-committee--2020.pdf 
National Defense Industrial Association Systems Engineering Architecture Committee. (2023, October 
16). NDIA. Retrieved from https://www.ndia.org/-/media/sites/ndia/divisions/systems-
engineering/_White Papers/MOSA Implementation Considerations Information Needs and 
Metrics v10 21 Sep 23 


P a g e  | 33 
Office of The Secretary of Defense (OSD). (2024). Systems Engineering and Architecture. Retrieved from 
cto.mil: https://www.cto.mil/sea/mosa/ 
OUSD(R&E). (2022, May 1). MOSA Assessment Criteria. Retrieved from Systems Engineering and 
Architecture: https://www.cto.mil/wp-content/uploads/2023/06/MOSA-Assess-2022.pdf 
Secretaries of the Navy, Army, and Air Force. (2019, January 7). Policy and Guidance. Retrieved from 
Systems Engineering and Architecture: 
https://www.dsp.dla.mil/Portals/26/Documents/PolicyAndGuidance/Memo-
Modular_Open_Systems_Approach.pdf 
Secretary of the Navy. (2022). SECNAVINST 5000.2G DEPARTMENT OF THE NAVY IMPLEMENTATION OF 
THE DEFENSE ACQUISITION SYSTEM AND THE ADAPTIVE ACQUISITION FRAMEWORK. 
Washington DC: Department of the Navy. 
Sensor Open Systems Architecture Consortium. (2019). youtube. Retrieved from 
https://www.youtube.com/watch?v=lUylabZs6H8 
United States Air Force. (n.d.). vdl.afrl.af.mil. Retrieved from OAM Brochure - OMS UCI: 
https://www.vdl.afrl.af.mil/programs/oam/brochure.php 
United States Army. (2015, July 6). Stand-To! Retrieved from 
https://www.army.mil/standto/archive/2015/07/06/ 
United States Department of Defense. (2013, May). DAU. Retrieved from 
https://www.dau.edu/sites/default/files/Migrated/CopDocuments/Open System Architecture 
%28OSA%29 Contract Guidebook for Program Managers-version 1.1- June 2013.pdf 
United States Department of Defense. (2020, March 13). Directives Division Website. Retrieved from 
https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500073p.PDF?ver=2020-
03-13-143931-413 
Welby, S. (2014, October). NDIA. Retrieved from 
https://ndiastorage.blob.core.usgovcloudapi.net/ndia/2014/system/16943WedTrack2Welby.pdf 
 
 
 


P a g e  | 34 
APPENDIX A: Legal and Policy Requirements Covering MOSA 
A.1 United States Codes (U.S.C) Title 10 
The implementation of MOSA is guided by several key laws, regulations, and policies that are integral 
to its success. Understanding these legal frameworks is crucial for compliance and effective system 
development.  
Title 10 U.S.C. § 4401 (formerly § 2446a):  
Mandates the use of MOSA in major defense acquisition programs. This requirement applies to 
programs receiving Milestone A or B approval after January 1, 2019. MOSA is designed to 
enhance competition, innovation, and interoperability by ensuring systems are developed with 
modular interfaces. These interfaces must comply with widely supported standards, allowing for 
incremental development and easier integration of new technologies. The approach aims to 
achieve significant cost savings, schedule reductions, and improved technical upgrades 
throughout the system’s lifecycle. The requirements in § 4401 also apply to other defense 
acquisition programs. 
Title 10 U.S.C. § 4402 (formerly § 2446b):  
Mandates the integration of MOSA in the development and acquisition of major defense 
systems. This section requires that program capability documents, for major defense acquisition 
programs, identify how system performance requirements may evolve due to technological 
advancements, threats, or interoperability needs. It also mandates that analyses of alternatives 
consider evolutionary acquisition, prototyping, and a modular open system approach. 
Additionally, the acquisition strategy must clearly describe the modular approach, differentiate 
between system platforms and components (modules), and address intellectual property and 
systems integration issues. This ensures that defense systems remain adaptable, interoperable, 
and capable of integrating new technologies throughout their lifecycle. 
Title 10 U.S.C. § 4403 (formerly § 2446c):  
Outlines the requirements for the availability of major system interfaces and the support for 
MOSA in defense acquisition programs. The most significant upshot of this law is that the 
modular interfaces must incorporate commercial and/or widely supported standards to the 
maximum extent practicable. Additionally, it requires sufficient systems engineering and 
development resources to support MOSA, along with necessary planning, programming, and 
budgeting resources. The section also emphasizes the importance of providing adequate training 
in MOSA to the acquisition workforce and issuing guidance to implement these requirements.  
A.2 Defense Federal Acquisition Regulation Supplement MOSA Policy 
Taken from Department of Defense Instruction (DoDI) 5000.88, Engineering of Defense Systems:  
The Defense Federal Acquisition Regulation Supplement (DFARS) Part 207.106 dictates 
additional requirements for major systems including “Use of modular, open 
architectures to enable competition for upgrades.” In addition, Part 227.7203-2 for 
Acquisition of other than commercial computer software and computer software 


P a g e  | 35 
documentation and association rights states “The assessment of life-cycle needs should 
consider alternatives to the delivery of source code and related software design details 
for privately developed computer software as necessary to meet the Government’s 
needs, such as technical data and computer software sufficient to implement a modular 
open system approach or a similar approach. This is a key part of establishing a win-win 
between government (acquirer) and industry (provider) as will be discussed below. 
A.3 Department of Defense MOSA Policy 
The DoDI 5000.88 establishes policy requiring a MOSA in Major Defense Acquisition Programs 
(MDAPs) and adds that all other acquisition pathways should consider implementing MOSA. This 
instruction was written before Congress updated the legal requirement extending MOSA to all 
acquisitions. This policy places responsibility on Lead Systems Engineers and Program Managers. 
It discusses the inclusion of MOSA in the Systems Engineering Plan and Acquisition Strategy, and 
it establishes the need to assess MOSA during Independent Technical Risk Assessments (ITRA) 
and at milestone decisions, in accordance with the legal requirement. The Army and Air Force 
have MOSA guidance, and the DoD is in process of releasing Department-wide guidance as this 
guidebook is being written.  
DoD and the services also issued policy in the form of memos and guidance to implement MOSA 
and drive horizontal integration of our program teams. The following documents and others can 
be found on the cto.mil/sea/mosa website:  
· 
OUSD(R&E) MOSA Assessment Criteria (OUSD(R&E), 2022): Establishes relationship 
between the MOSA pillars and provides guidance and methodology for MOSA 
assessment.  
· 
MOSA for our Warfighting Systems in a Warfighting Imperative — Tri Service Memo 
(Secretaries of the Navy, Army, and Air Force, 2019): Directs program teams to include 
MOSA implementation in “all requirements, programming and development activities 
for future weapon system modifications and new start development”. A new tri-service 
memorandum is under review as of this writing.  
· 
Guidance for architecture, contracting, and a reference to Defense Acquisition University 
training are also available on this website. 
A.4 Navy MOSA Policy 
Secretary of the Navy Instruction 5000.2G, Department of the Navy Implementation of the 
Defense Acquisition System and Adaptive Acquisition Framework (SECNAVINST 5000.2G) directs 
all acquisition programs to follow MOSA design principles and incorporate MOSA in contract 
requirements and source selection criteria. It directs that programs shall digitally represent the 
major system components and interfaces to support integration, interoperability, and future 
upgradeability (Secretary of the Navy, 2022).   
The Navy follows Department of Defense policy and requires that systems also develop an Open 
Systems Management Plan (OSMP), which is critical to ensuring a MOSA design is achieved. The 
OSMP describes the program plan for a MOSA. You can find the OSMP data item description on 
the ASSIST database at the website, quicksearch.dla.mil, number DI-MGMT-82-099A as of this 
writing.  Note that it is important that the government/acquirer draft the OSMP as part of the 


P a g e  | 36 
project definition process (see Figure 2). The expectation is that the contractor uses the 
government-supplied OSMP as the basis for theirs, making only minor refinements that match 
the specifics of their proposal. 
Independent Technical Risk Assessments (ITRA) include assessment of risks to implementing 
MOSA in a program. The team should consider the risk that a MOSA will not be implemented in 
a program as a potential cost and technical liability throughout the system lifecycle. Modular 
systems with open architectures are less expensive to maintain and are more easily upgraded at 
the pace of the commercial market. Newer technology, especially in operating systems and 
software, is more easily introduced into systems that employ a modular open architecture. 
Defense Standardization Program (DSP) Administration Notice, JOINT-UXS-002, in the ASSIST 
repository, provides various naval MOSA initiatives and pointers to access the related MOSA 
standards and guidance documentation. The current Administration Notice, JOINT-UXS-002, 
references the following:  
· 
Hardware Open Systems Technologies (HOST): A standard framework using multiple Open 
Architectures that standardizes on commercial-Off-the-Shelf (COTS) components for 
embedded computing.  
· 
Future Airborne Capability Environment (FACE®), The Open Group FACE Consortium: A 
Government, Industry, and Academia partnership consortium defining an open software 
environment for military platforms.  
· 
Sensor Open Systems Architecture (SOSA™): A Government and Industry partnership 
consortium to enable, enhance, and accelerate the deployment of affordable, capable, and 
interoperable sensor, communications, EW, SIGINT, and directed energy systems.   
· 
Unmanned Systems (UxS) Control Segment (UCS), Society of Automotive Engineers (SAE): An 
architecture mandated across the Tri-Services for all Unmanned Aircraft Systems (UAS) and 
naval UxS.  
· 
Open Mission Systems (OMS) / Universal C2 Interface (UCI): A Government and Industry 
partnership that defines a DoD non-proprietary mission systems integration architecture.  
Other MOSA implementation efforts are listed below:  
· 
Submarine Warfare Federated Tactical Systems (SWFTS): A systems engineering and 
integration program with a common combat system (sonar, combat control, imaging, 
electronic warfare, weapon control, etc.) used across the US Navy submarine fleet.  
· 
Unmanned Maritime Autonomy Architecture (UMAA): A defined framework for developing 
autonomy on Unmanned Undersea Vehicles (UUV) and Unmanned Surface Vehicles (USV) 
using a common architecture for unmanned Command and Control Systems (CCS).  
· 
Weapon Open System architecture (WOSA): A Government and Industry partnership that 
defines the DoD non-proprietary architectural standards for “inside the skin” of guided 
munitions.  
· 
Directed Energy Weapon System Reference Architecture (DEWS RA): Originally` a 
government reference architecture that defines the DoD non-proprietary architectural 
standards for various Directed Energy systems. The DEWS RA is being integrated into the 
SOSA Technical Standard. 
 
 


P a g e  | 37 
 
 


