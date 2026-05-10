Systems and software engineering — 
System life cycle processes

Ingénierie des systèmes et du logiciel — Processus du cycle de vie du 
système

INTERNATIONAL 
STANDARD
ISO/ 
IEC/IEEE 
15288

Second edition 
2023-05

Reference number 
ISO/IEC/IEEE 15288:2023(E)

© ISO/IEC 2023 
© IEEE 2023

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ii

ISO/IEC/IEEE 15288:2023(E)

COPYRIGHT PROTECTED DOCUMENT

©  ISO/IEC 2023
©  IEEE 2023
All rights reserved. Unless otherwise specified, or required in the context of its implementation, no part of this publication may 
be reproduced or utilized otherwise in any form or by any means, electronic or mechanical, including photocopying, or posting 
on the internet or an intranet, without prior written permission. Permission can be requested from either ISO or IEEE at the 
respective address below or ISO’s member body in the country of the requester.
ISO copyright office 
Institute of Electrical and Electronics Engineers, Inc
CP 401 • Ch. de Blandonnet 8 
3 Park Avenue, New York
CH-1214 Vernier, Geneva 
NY 10016-5997, USA
Phone: +41 22 749 01 11 
Fax: +41 22 749 09 47 
Email: copyright@iso.org 
Email: stds.ipr@ieee.org
Website: www.iso.org
Website: www.ieee.org

Published in Switzerland

  
© ISO/IEC 2023 – All rights reserved

© IEEE 2023 – All rights reserved

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

Foreword ..........................................................................................................................................................................................................................................v

Introduction .............................................................................................................................................................................................................................vii

1 
Scope .................................................................................................................................................................................................................................1

2 
Normative references .....................................................................................................................................................................................1

3 
Terms, definitions, and abbreviated terms .............................................................................................................................1

4 
Conformance ............................................................................................................................................................................................................9
4.1 
Intended usage ....................................................................................................................................................................................... 9
4.2 
Full conformance ...............................................................................................................................................................................10
4.2.1 
Full conformance to outcomes ............................................................................................................................10
4.2.2 
Full conformance to tasks .......................................................................................................................................10
4.3 
Tailored conformance ...................................................................................................................................................................10

5 
Key concepts and their application ...............................................................................................................................................11
5.1 
General ........................................................................................................................................................................................................11
5.2 
System concepts .................................................................................................................................................................................11
5.2.1 
Systems ....................................................................................................................................................................................11
5.2.2 
System structure .............................................................................................................................................................12
5.2.3 
Interfacing, enabling, and interoperating systems ..........................................................................13
5.2.4 
Concepts related to the system solution context................................................................................13
5.2.5 
Product line engineering (PLE).......................................................................................................................... 14
5.3 
Organizational concepts .............................................................................................................................................................15
5.3.1 
Organizations .....................................................................................................................................................................15
5.3.2 
Organization and project-level adoption ...................................................................................................16
5.3.3 
Organization and collaborative activities .................................................................................................16
5.4 
System of systems concepts ....................................................................................................................................................16
5.4.1 
Differences between systems and SoS .........................................................................................................16
5.4.2 
Managerial and operational independence .............................................................................................17
5.4.3 
Taxonomy of SoS ..............................................................................................................................................................17
5.4.4 
SoS considerations in life cycle stages of a system ...........................................................................17
5.4.5 
Application of this document to SoS ..............................................................................................................18
5.5 
Life cycle concepts ............................................................................................................................................................................18
5.5.1 
System life cycle model ..............................................................................................................................................18
5.5.2 
System life cycle stages .............................................................................................................................................18
5.6 
Process concepts ................................................................................................................................................................................ 19
5.6.1 
Criteria for processes ..................................................................................................................................................19
5.6.2 
Description of processes .......................................................................................................................................... 19
5.6.3 
General characteristics of processes ............................................................................................................. 19
5.7 
Processes in this document ......................................................................................................................................................20
5.7.1 
General .....................................................................................................................................................................................20
5.7.2 
Agreement processes ..................................................................................................................................................22
5.7.3 
Organizational project-enabling processes .............................................................................................22
5.7.4 
Technical management processes....................................................................................................................23
5.7.5 
Technical processes ......................................................................................................................................................24
5.8 
Process application ..........................................................................................................................................................................25
5.8.1 
Overview ................................................................................................................................................................................25
5.8.2 
Process iteration, recursion, and concurrency ....................................................................................27
5.8.3 
Process views .....................................................................................................................................................................28
5.9 
Concept and system definition ..............................................................................................................................................28
5.10 
Assurance and quality characteristics...........................................................................................................................29
5.11 
Process reference model .............................................................................................................................................................30

6 
System life cycle processes ....................................................................................................................................................................30
6.1 
Agreement processes .....................................................................................................................................................................30
6.1.1 
Acquisition process .......................................................................................................................................................30

iii
© ISO/IEC 2023 – All rights reserved 
 

© IEEE 2023 – All rights reserved

Contents 
Page

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

6.1.2 
Supply process ...................................................................................................................................................................32
6.2 
Organizational project-enabling processes ...............................................................................................................34
6.2.1 
Life cycle model management process ........................................................................................................34
6.2.2 
Infrastructure management process ............................................................................................................36
6.2.3 
Portfolio management process ...........................................................................................................................37
6.2.4 
Human resource management process .......................................................................................................38
6.2.5 
Quality management process ...............................................................................................................................40
6.2.6 
Knowledge management process .....................................................................................................................41
6.3 
Technical management processes ......................................................................................................................................43
6.3.1 
Project planning process ..........................................................................................................................................43
6.3.2 
Project assessment and control process ....................................................................................................45
6.3.3 
Decision management process............................................................................................................................47
6.3.4 
Risk management process ......................................................................................................................................49
6.3.5 
Configuration management process ..............................................................................................................51
6.3.6 
Information management process ..................................................................................................................54
6.3.7 
Measurement process .................................................................................................................................................56
6.3.8 
Quality assurance process ......................................................................................................................................57
6.4 
Technical processes .........................................................................................................................................................................59
6.4.1 
Business or mission analysis process ...........................................................................................................59
6.4.2 
Stakeholder needs and requirements definition process ...........................................................62
6.4.3 
System requirements definition process...................................................................................................67
6.4.4 
System architecture definition process .....................................................................................................70
6.4.5 
Design definition process .........................................................................................................................................74
6.4.6 
System analysis process ........................................................................................................................................... 76
6.4.7 
Implementation process ...........................................................................................................................................78
6.4.8 
Integration process .......................................................................................................................................................81
6.4.9 
Verification process ......................................................................................................................................................83
6.4.10 Transition process .........................................................................................................................................................85
6.4.11 Validation process ..........................................................................................................................................................88
6.4.12 Operation process ..........................................................................................................................................................91
6.4.13 Maintenance process ...................................................................................................................................................94
6.4.14 Disposal process ..............................................................................................................................................................98

Annex A (normative)  Tailoring process ................................................................................................................................................... 101

Annex B (informative)  Example process artefacts and information items .......................................................103

Annex C (informative)  Process reference model for assessment purposes ......................................................107

Annex D (informative)  Model-based systems and software engineering (MBSSE) ..................................109

Bibliography .........................................................................................................................................................................................................................113

IEEE notices and abstract ........................................................................................................................................................................................117

iv
 
  
© ISO/IEC 2023 – All rights reserved

 
© IEEE 2023 – All rights reserved

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

Foreword

ISO (the International Organization for Standardization) and IEC (the International Electrotechnical 
Commission) form the specialised system for worldwide standardization. National bodies that are 
members of ISO or IEC participate in the development of International Standards through technical 
committees established by the respective organization to deal with particular fields of technical 
activity. ISO and IEC technical committees collaborate in fields of mutual interest. Other international 
organizations, governmental and non-governmental, in liaison with ISO and IEC, also take part in the 
work.

The procedures used to develop this document and those intended for its further maintenance are 
described in the ISO/IEC Directives, Part 1. In particular, the different approval criteria needed 
for the different types of ISO/IEC documents should be noted. This document was drafted in 
accordance with the editorial rules of the ISO/IEC Directives, Part 2 (see www.iso.org/directives or 
www.iec.ch/members_experts/refdocs).

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating 
Committees of the IEEE Standards Association (IEEE-SA) Standards Board. The IEEE develops its 
standards through a consensus development process, approved by the American National Standards 
Institute, which brings together volunteers representing varied viewpoints and interests to achieve the 
final product. Volunteers are not necessarily members of the Institute and serve without compensation. 
While the IEEE administers the process and establishes rules to promote fairness in the consensus 
development process, the IEEE does not independently evaluate, test, or verify the accuracy of any of 
the information contained in its standards.

Attention is drawn to the possibility that some of the elements of this document may be the subject of 
patent rights. ISO shall not be held responsible for identifying any or all such patent rights. Details of 
any patent rights identified during the development of the document will be in the Introduction and/
or on the ISO list of patent declarations received (see www.iso.org/patents) or the IEC list of patent 
declarations received (see https://patents.iec.ch).

Any trade name used in this document is information given for the convenience of users and does not 
constitute an endorsement.

For an explanation of the voluntary nature of standards, the meaning of ISO specific terms and 
expressions related to conformity assessment, as well as information about ISO's adherence to 
the World Trade Organization (WTO) principles in the Technical Barriers to Trade (TBT), see 
www.iso.org/iso/foreword.html. In the IEC, see www.iec.ch/understanding-standards.

This document was prepared by Joint Technical Committee ISO/JTC 1, Information technology, 
Subcommittee SC 7, Software and systems engineering, in cooperation with the Systems and Software 
Engineering Standards Committee of the IEEE Computer Society, under the Partner Standards 
Development Organization cooperation agreement between ISO and IEEE.

This second edition cancels and replaces the first edition (ISO/IEC/IEEE 15288:2015), which has been 
technically revised.

The main changes are as follows:

— improvements to selected technical processes including business or mission analysis, system 
architecture definition, system analysis, implementation, integration, operations, and maintenance;

— improvements to selected technical management processes including risk management and 
configuration management;

— updates to Clause 5, key concepts, including a better description of iteration, recursion, system-of-
systems, quality characteristics, etc.;

— new content in Clause 5 on concept and system definition, and expanded content on process 
application and system concepts;

v
© ISO/IEC 2023 – All rights reserved 
 

© IEEE 2023 – All rights reserved

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

— updates to the terms and definitions;

— a new annex addressing model-based systems engineering (MBSE).

Any feedback or questions on this document should be directed to the user’s national standards 
body. A complete listing of these bodies can be found at www.iso.org/members.html and 
www.iec.ch/national-committees.

vi
 
  
© ISO/IEC 2023 – All rights reserved

 
© IEEE 2023 – All rights reserved

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

Introduction

The complexity of systems continues to increase to unprecedented levels. This has led to new 
opportunities, but also to increased challenges for the organizations that create and utilise systems. 
These challenges exist throughout the life cycle of a system and at all levels of architectural detail. This 
document provides a common process framework for describing the life cycle of systems, adopting a 
systems engineering approach. This document concerns systems that can be configured with one 
or more of the following system elements: hardware elements, software elements, data, humans, 
processes, services, procedures, facilities, materials, and naturally occurring entities.

This document focuses on defining stakeholder needs, concerns, priorities, and constraints for the 
required functionality early in the development cycle, establishing requirements, then proceeding 
with design synthesis and system validation while considering the complete problem. It integrates all 
the disciplines and specialty groups into a team effort forming a structured development process that 
proceeds from conception through production to operation. It considers the needs of all stakeholders 
with the goal of providing a quality product that meets the needs of users and other applicable 
stakeholders. It provides the processes for acquiring and supplying systems. It helps to improve 
communication and cooperation among the parties that create, utilise, and manage modern systems 
in order that they can work in an integrated, coherent fashion. Finally, this document provides the 
framework for assessment and improvement of the life cycle processes.

There is a wide variety of systems in terms of their purpose, domain of application, complexity, size, 
novelty, adaptability, quantity, location, life span, and evolution. The processes in this document form a 
comprehensive set from which an organization can construct system life cycle models appropriate to its 
products and services. An organization, depending on its purpose, can select and apply an appropriate 
subset to fulfil that purpose.

This document can be used in one or more of the following modes:

— By an organization — to help establish an environment of desired processes. These processes can be 
supported by an infrastructure of methods, procedures, techniques, tools, and trained personnel. The 
organization may then employ this environment to perform and manage its projects and progress 
systems through their life cycle stages. In this mode this document is used to assess conformance 
of a declared, established environment to its provisions. It can be used by a single organization in 
a self-imposed mode or in a multi-party situation. Parties can be from the same organization or 
from different organizations and the situation can range from an informal agreement to a formal 
contract.

— By a project — to help select, structure, and employ the elements of an established environment to 
provide products and services. In this mode this document is used in the assessment of conformance 
of the project to the declared and established environment.

— By an acquirer and a supplier — to help develop an agreement concerning processes and activities. 
Via the agreement, the processes and activities in this document are selected, negotiated, agreed to, 
and performed. In this mode this document is used for guidance in developing the agreement.

— By process assessors — to serve as a process reference model for use in the performance of process 
assessments that can be used to support organizational process improvement.

In the context of this document and ISO/IEC/IEEE 12207, there is a continuum of human-made systems 
from those that use little or no software to those in which software is the primary interest. When 
software is the predominant system or element of interest, ISO/IEC/IEEE 12207 should be used. Both 
documents have the same process model, share most activities and tasks, and differ primarily in 
descriptive notes.

Although this document does not establish a management system, it is intended to be compatible with 
the quality management system provided by ISO 9001, the service management system provided by 
ISO/IEC 20000 series, the IT asset management system provided by the ISO/IEC 19770 series, and the 
information security management system provided by ISO/IEC 27000.

vii
© ISO/IEC 2023 – All rights reserved 
 

© IEEE 2023 – All rights reserved

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


INTERNATIONAL STANDARD
ISO/IEC/IEEE 15288:2023(E)

Systems and software engineering — System life cycle 
processes

1 Scope

This document establishes a common framework of process descriptions for describing the life 
cycle of systems created by humans, defining a set of processes and associated terminology from an 
engineering viewpoint. These processes can be applied to systems of interest, their system elements, 
and to systems of systems. Selected sets of these processes can be applied throughout the stages of a 
system's life cycle. This is accomplished through the involvement of stakeholders, with the ultimate 
goal of achieving customer satisfaction.

This document defines a set of processes to facilitate system development and information exchange 
among acquirers, suppliers, and other stakeholders in the life cycle of a system.

This document specifies processes that support the definition, control, and improvement of the system 
life cycle processes used within an organization or a project. Organizations and projects can use these 
processes when acquiring and supplying systems.

This document applies to organizations in their roles as both acquirers and suppliers.

This document applies to the full life cycle of systems, including conception, development, production, 
utilization, support and retirement of systems, and to the acquisition and supply of systems, whether 
performed internally or externally to an organization. The life cycle processes of this document can be 
applied iteratively and concurrently to a system and recursively to the system elements.

This document applies to one-of-a-kind systems, mass-produced systems, and customised, adaptable 
systems. It also applies to a complete stand-alone system and to systems that are embedded and 
integrated into larger more complex and complete systems.

This document does not prescribe a specific system life cycle model, development methodology, method, 
modelling approach or technique.

This document does not detail information items in terms of name, format, explicit content, and 
recording media. ISO/IEC/IEEE 15289 addresses the content for life cycle process information items 
(documentation).

2 Normative references

There are no normative references in this document.

3 Terms, definitions, and abbreviated terms

For the purposes of this document, the following terms and definitions apply.

ISO, IEC, and IEEE maintain terminology databases for use in standardization at the following addresses:

— ISO Online browsing platform: available at https:// www .iso .org/ obp

— IEC Electropedia: available at https:// www .electropedia .org/ 

— IEEE Standards Dictionary Online: available at: https:// dictionary .ieee .org/ 

NOTE 
Definitions for other system and software engineering terms can be found in ISO/IEC/IEEE 24765, 
available at www .computer .org/ sevocab.

1
© ISO/IEC 2023 – All rights reserved 
 

© IEEE 2023 – All rights reserved

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

3.1
acquirer
stakeholder (3.44) that acquires or procures a system (3.46), product (3.32) or service (3.42) from a 
supplier (3.45)

Note 1 to entry: Other terms commonly used for an acquirer are buyer, customer (3.12), owner, purchaser, or 
internal/organizational sponsor.

3.2
acquisition
process (3.27) of obtaining a system (3.46), product (3.32) or service (3.42)

3.3
activity
set of cohesive tasks (3.51) of a process (3.27)

3.4
agreement
mutual acknowledgement of terms and conditions under which a working relationship is conducted

EXAMPLE 
Contract, memorandum of agreement.

3.5
architecture
fundamental concepts or properties of a system (3.46) in its environment (3.16) and governing principles 
for the realization and evolution of this system and its related life cycle (3.21) processes (3.27)

[SOURCE: ISO/IEC/IEEE 42020:2019, 3.3, modified — ‘entity’ has been replaced with ‘system’; notes to 
entry have been removed.]

3.6
artefact
work product (3.32) that is produced and used during a project to capture and convey information

EXAMPLE 
Models, stakeholder requirements, system/software requirements, architecture descriptions, 
design descriptions, source code, implemented system elements, verified or validated system.

[SOURCE: ISO 19014-4:2020, 3.9, modified — EXAMPLE has been added.]

3.7
audit
independent examination of a work product (3.32) or set of work products to assess compliance with 
specifications, standards, contractual agreements (3.4), or other criteria

3.8
baseline
formally approved version of a configuration item (3.11), regardless of media, formally designated and 
fixed at a specific time during the configuration item's life cycle (3.21)

[SOURCE: IEEE Std 828-2012]

3.9
concept of operations
verbal and graphic statement, in broad outline, of an organization’s (3.25) assumptions or intent in 
regard to an operation or series of operations of new, modified, or existing organizational systems (3.46)

Note 1 to entry: The concept of operations frequently is embodied in long-range strategic plans and annual 
operational plans. In the latter case, the concept of operations in the plan covers a series of connected operations 
to be carried out simultaneously or in succession to achieve an organizational performance objective. See also 
operational concept (3.23).

Note 2 to entry: The concept of operations provides the basis for bounding the operating space, system 
capabilities, interfaces (3.19), and operating environment (3.16).

 
  
© ISO/IEC 2023 – All rights reserved

 
© IEEE 2023 – All rights reserved

2

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

[SOURCE: ANSI/AIAA G-043B-2018, 5.2, modified — The second definition has been used; the last two 
sentences of Note 1 to entry have been removed; Note 2 to entry has been added.]

3.10
concern
matter of interest or importance to a stakeholder (3.44)

Note 1 to entry: A concern pertains to any influence on a system (3.46) in its environment (3.16), including 
developmental, technological, business, operational, organizational, political, economic, legal, regulatory, ethical, 
ecological, and social influences.

[SOURCE: ISO/IEC/IEEE 42020:2019, 3.8, modified — EXAMPLE has been removed; Note 1 to entry has 
been added.]

3.11
configuration item
item or aggregation of hardware, software, or both, that is designated for configuration management 
and treated as a single entity in the configuration management process (3.27)

3.12
customer
organization (3.25) or person that receives a product (3.32) or service (3.42)

EXAMPLE 
Consumer, client, user (3.53), acquirer (3.1), buyer, or purchaser.

Note 1 to entry: A customer can be internal or external to the organization.

3.13
design, noun
specification of system elements (3.47) and their relationships, that is sufficiently complete to support a 
compliant implementation of the architecture (3.5)

Note 1 to entry: Design provides the detailed implementation-level physical structure, behaviour, temporal 
relationships, and other attributes of system elements.

3.14
design characteristics
design attributes or distinguishing features that pertain to a measurable description of a product (3.32) 
or service (3.42)

3.15
enabling system
system (3.46) that supports a system-of-interest (3.48) during its life cycle (3.21) stages (3.43) but does 
not necessarily contribute directly to its function during operation

EXAMPLE 
Production-enabling system, which is required when a system-of-interest enters the production 
stage.

Note 1 to entry: Each enabling system has a life cycle of its own. This document is applicable to each enabling 
system when, in its own right, it is treated as a system-of-interest.

3.16
environment
<system> context determining the setting and circumstances of all influences upon a system (3.46)

3.17
incident
anomalous or unexpected event, set of events, condition, or situation at any time during the life cycle 
(3.21) of a project (3.33), product (3.32), service (3.42), or system (3.46)

Note 1 to entry: An incident is elevated and treated as a problem (3.26) when the cause of the incident needs to 
be analysed and corrected to prevent reoccurrence to avoid or minimise loss of life, or damage of property or 
natural resources (3.37).

© ISO/IEC 2023 – All rights reserved 
 

© IEEE 2023 – All rights reserved

3

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

3.18
information item
separately identifiable body of information that is produced, stored, and delivered for human use

[SOURCE: ISO/IEC/IEEE 15289:2019, 3.1.12, modified — The preferred term "information product" has 
been removed; notes to entry have been removed.]

3.19
interface
point at which two or more logical, physical, or both, system elements (3.47) or software system 
elements meet and act on or communicate with each other

[SOURCE: ISO/IEC/IEEE 24748-6: —, 3.1.3]

3.20
interoperating system
system (3.46) that exchanges information with the system-of-interest (3.48) and uses the information 
that has been exchanged

3.21
life cycle
evolution of a system (3.46), product (3.32), service (3.42), project (3.33) or other human-made entity 
from conception through retirement (3.38)

3.22
life cycle model
framework of processes (3.27) and activities (3.3) concerned with the life cycle (3.21) which can be 
organized into stages (3.43), acting as a common reference for communication and understanding

3.23
operational concept
verbal and graphic statement of an organization’s (3.25) assumptions or intent in regard to an operation 
or series of operations of a specific system (3.46) or a related set of specific new, existing or modified 
systems

Note 1 to entry: The operational concept is designed to give an overall picture of the operations using one or 
more specific systems, or set of related systems, in the organization’s operational environment (3.16) from the 
users’ (3.53) and operators’ (3.24) perspectives. See also concept of operations (3.9).

Note 2 to entry: The operational concept is about systems, while a concept of operations (3.9) typically refers to 
organizations.

[SOURCE: ANSI/AIAA G-043B-2018, 5.2, modified — The third definition has been used; the first 
sentence in Note 1 to entry has been removed; Note 2 to entry has been added.]

3.24
operator
individual or organization (3.25) that performs the operations of a system (3.46)

Note 1 to entry: The role of operator and the role of user (3.53) can be vested, simultaneously or sequentially, in 
the same individual or organization.

Note 2 to entry: An individual operator combined with knowledge, skills, and procedures can be considered as an 
element of the system.

Note 3 to entry: An operator may perform operations on a system that is operated, or of a system that is operated, 
depending on whether or not operating instructions are placed within the system boundary.

 
  
© ISO/IEC 2023 – All rights reserved

 
© IEEE 2023 – All rights reserved

4

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

3.25
organization
person or group of people that has its own functions with responsibilities, authorities, and relationships 
to achieve its objectives

EXAMPLE 
Company, corporation, firm, enterprise, manufacturer, institution, charity, sole trader, association, 
or parts or combination thereof.

[SOURCE: ISO 9000:2015, 3.2.1, modified — Notes to entry have been removed; EXAMPLE has been 
added.]

3.26
problem
difficulty, uncertainty, or otherwise realised and undesirable event, set of events, condition, or situation 
that requires investigation and corrective action

3.27
process
set of interrelated or interacting activities (3.3) that transform inputs into outputs

3.28
iteration
<process> repeating the application of the same process (3.27) or set of processes on the same level of 
the system (3.46) structure

3.29
process purpose
high level objective of performing the process (3.27) and the likely outcomes of effective implementation 
of the process

Note 1 to entry: The purpose of implementing the process is to provide benefits to the stakeholders (3.44).

3.30
process outcome
observable result of the successful achievement of the process purpose (3.29)

3.31
recursion
<process> repeating the application of the same process (3.27) or set of processes to successive levels of 
system elements (3.47) in the system structure

3.32
product
output of an organization (3.25) that can be produced without any transaction taking place between 
the organization and the customer (3.12)

Note 1 to entry: The dominant element of a product is that it is generally tangible.

[SOURCE: ISO 9000:2015, 3.7.6, modified — Notes 1 and 3 to entry have been removed.]

3.33
project
endeavour with defined start and finish criteria undertaken to create a product (3.32) or service (3.42) 
in accordance with specified resources (3.37) and requirements (3.36)

Note 1 to entry: A project is sometimes viewed as a unique process (3.27) comprising coordinated and controlled 
activities (3.3) and composed of activities from the Technical Management and Technical Processes defined in 
this document.

Note 2 to entry: Continuous development approaches such as agile and DevOps can use different terminology for 
the creation of product and services.

© ISO/IEC 2023 – All rights reserved 
 

© IEEE 2023 – All rights reserved

5

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

3.34
quality assurance
QA
part of quality management focused on providing confidence that quality requirements (3.36) will be 
fulfilled

[SOURCE: ISO 9000:2015, 3.3.6, modified — The abbreviated term has been added.]

3.35
quality characteristic
inherent characteristic of a product (3.32), service (3.42), process (3.27), or system (3.46) related to a 
requirement (3.36)

[SOURCE: ISO 9000:2015, 3.10.2, modified — ‘object’ has been replaced with ‘product, service, process, 
or system’; notes to entry have been removed.]

3.36
requirement
statement which translates or expresses a need and its associated constraints and conditions

[SOURCE: ISO/IEC/IEEE 29148:2018, 3.1.19, modified — Notes to entry have been removed.]

3.37
resource
asset that is utilised or consumed during the execution of a process (3.27)

Note 1 to entry: Resource includes diverse entities such as funding, personnel, facilities, capital equipment, tools 
and utilities such as power, water, fuel, and communication infrastructures.

Note 2 to entry: Resources include those that are reusable, renewable or consumable.

3.38
retirement
<system> withdrawal of active support by the operation and maintenance organization (3.25), 
partial or total replacement by a new system (3.46), or installation of an upgraded system, or final 
decommissioning and disposal

3.39
risk
effect of uncertainty on objectives

Note 1 to entry: An effect is a deviation from the expected — positive or negative. A positive effect is also known 
as an opportunity.

Note 2 to entry: Objectives can have different aspects [such as financial, health and safety (3.40), and 
environmental goals] and can apply at different levels [such as strategic, organization-wide, project, product 
(3.32) and process (3.27)].

Note 3 to entry: Risk is often characterized by reference to potential events and consequences, or a combination 
of these.

Note 4 to entry: Risk is often expressed in terms of a combination of the consequences of an event (including 
changes in circumstances) and the associated likelihood of occurrence.

Note 5 to entry: Uncertainty is the state, even partial, of deficiency of information related to understanding or 
knowledge of an event, its consequence, or likelihood.

[SOURCE: ISO Guide 73:2009, 1.1, modified — The last sentence in Note 1 to entry has been added.]

 
  
© ISO/IEC 2023 – All rights reserved

 
© IEEE 2023 – All rights reserved

6

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


ISO/IEC/IEEE 15288:2023(E)

3.40
safety
expectation that a system (3.46) does not, under defined conditions, lead to a state in which human life, 
health, property, or the environment (3.16) is endangered

Note 1 to entry: The term is alternatively defined as freedom from risk (3.39) which is not tolerable.

[SOURCE: ISO/IEC/IEEE 12207:2017, 3.1.48, modified — Note 1 to entry has been added.]

3.41
security
protection against intentional subversion or forced failure

Note 1 to entry: Security includes authenticity, accountability, confidentiality, integrity, availability, non-
repudiation, and reliability, all of which have the related issue of their assurance.

[SOURCE: NATO AEP-67, modified — Note 1 to entry has been updated.]

3.42
service
output of an organization (3.25) with at least one activity (3.3) necessarily performed between the 
organization and the customer (3.12)

Note 1 to entry: The dominant elements of a service are generally intangible.

Note 2 to entry: A service is coherent, discrete, and can be composed of other services.

[SOURCE: ISO 9000:2015, 3.7.7, modified — Notes 2, 3, and 4 to entry have been replaced by a new 
Note 2 to entry.]

3.43
stage
period within the life cycle (3.21) of an entity that relates to the state of its description or realization

Note 1 to entry: As used in this document, stages relate to major progress and achievement milestones of the 
entity through its life cycle.

Note 2 to entry: Stages often overlap.

3.44
stakeholder
individual or organization (3.25) having a right, share, claim, or interest in a system (3.46) or in its 
possession of characteristics that meet their needs and expectations

EXAMPLE 
End users (3.53), end user organizations, supporters, developers, customers (3.12), producers, 
trainers, maintainers, disposers, acquirers (3.1), suppliers (3.45), regulatory bodies, and people influenced 
positively or negatively by a system.

Note 1 to entry: Some stakeholders can have interests that oppose each other or oppose the system.

3.45
supplier
organization (3.25) or an individual that enters into an agreement (3.4) with the acquirer (3.1) for the 
supply of a product (3.32) or service (3.42)

Note 1 to entry: Other terms commonly used for supplier are contractor, producer, seller or vendor.

Note 2 to entry: The acquirer and the supplier sometimes are part of the same organization.

© ISO/IEC 2023 – All rights reserved 
 

© IEEE 2023 – All rights reserved

7

iTeh STANDARD PREVIEW

(standards.iteh.ai)

ISO/IEC/IEEE 15288:2023

https://standards.iteh.ai/catalog/standards/sist/4109ef6c-8070-4ebe-89d8-

c45ae8413981/iso-iec-ieee-15288-2023


