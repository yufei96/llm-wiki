PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 1 of 14 

 
 
 
 
 
 

DATA ITEM DESCRIPTION 

1. TITLE 

SYSTEMS REQUIREMENTS SPECIFICATION (SyRS) 

2. IDENTIFICATION NUMBER 

PPA-002235-18 
13 January 2023 

3. DESCRIPTION/PURPOSE OF THE SyRS 

3.1 The System Requirements Specification (SyRS), specifies the requirements to be satisfied by a system, subsystem, 
Hardware Configuration Item (HWCI), component or other physical item, and optionally the requirements for 
evidence that each requirement has been so satisfied. Requirements pertaining to the system, subsystem or 
item’s external interfaces may be presented in the SyRS, or alternatively in one or more Interface Requirements 
Specifications (IRSs), invoked by reference from the SyRS. 

3.2 The SyRS, possibly supplemented by IRSs, is commonly used as the basis for acquisition, supply, design and 
development, verification and acceptance of the system, subsystem or other item. Throughout this DID, the term 
“system” may be interpreted to mean "segment", "subsystem", "element", "HWCI", component or other item, 
as applicable. The resulting document may be titled System Requirements Specification, Segment Requirements 
Specification, Component Requirements Specification or similar, as applicable, or a corresponding subject matter 
– specific name, e.g., “Air Traffic Control System Requirements Specification”, “Requirements Specification for a 
Power Supply Module”, etc. 

4. APPLICATION/INTERRELATIONSHIP 

This Data Item Description (DID) may be cited in a Statement of Requirement (SOR), Task Specification (TS), a 
Contract Data Requirements List (CDRL), within a standard invoked by a SOR or TS, or within a plan, policy 
document or procedure. 

5. PREPARATION GUIDELINES 

5.1 General Instructions 

The term “document” in this DID means data and its medium, regardless of the manner in which the data are 
recorded. 

5.2 Content Requirements 

Content requirements begin on page 4.  The numbers shown designate the paragraph numbers to be used in the 
document.  Each such number is understood to have the prefix "5.2" within this DID.  For example, the paragraph 
numbered 1.1 is understood to be paragraph 5.2.1.1 within this DID. 

  
 
 
 
 
 
 
 
  
 continued next page 

6. SOURCE 

© Copyright Project Performance International. This document may be reproduced and distributed without 
restriction except as below provided that all reproductions contain the original copyright statement in the original 
form and location. Derivative works may be produced provided each derivative work contains a copyright 
statement referring to the content in which PPI holds copyright, in a form and in a location no less prominent 
than the copyright statement on the original. Copies and derivative works may not be used for the delivery of 
training for profit.  Creative Commons license CC BY-ND as modified above. 

helping projects succeed… 
www.ppi-int.com 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 2 of 14 

 

 
 

5. PREPARATION GUIDELINES continued 

5.2 Acronyms  

Acronyms used in this document shall be interpreted as follows: 

CC 
Creative Commons  

CDRL 
Contract Data Requirements List 

DID 
Data Item Description 

HWCI 
Hardware Configuration Item 
ICD 
Interface Control Document 

IRS 
Interface Requirements Specification 

OCD 
Operational Concept Description 

SOR 
Statement of Requirement 

SyRS 
System Requirements Specification. 

TS 
Task Specification 
VRS 
Verification Requirements Specification 

5.3 Abbreviations 

Abbreviations used in this document shall be interpreted as follows: 

CapSysRS Capability System Requirements Specifications 

CONUSE Concept of Use 
SI 
 
International System of Units 

5.4 Foreword 

This Data Item Description (DID) for a System Requirements Specification (SyRS) is intended to provide guidance 
and instruction on the preparation of a requirements specification for any required physical item. A SyRS can be 
used in relation to any product or system whatsoever, from an implantable medical device to an IT or production 
system for internal use, to a whole military capability system. The system that is the subject of a SyRS may be a 
new system or a change to an existing system. The subject of a SyRS may be a logistics element, or any other 
element, except a material, software or a database. 

Hereinafter, the word “system” is used to refer to the item that is the subject of the System Requirements 
Specification. 

A SyRS specifies the essentially solution-free requirements to be satisfied by any acceptable system solution. The 
SyRS may also specify goals to be pursued during system procurement and/or system item development (if 
applicable).  

The SyRS is usually the single most important artefact in the development or acquisition of a system. Creation, 
capture and specification of the information content of the SyRS should be done with the utmost care, and with 
appropriate skills applied, to avoid problems such as: 

a. systems that do not satisfy the needs of the enterprise at all, or fall significantly short of satisfying the needs; 
b. avoidable inaccuracies in cost estimation; and 
c. delays due to rework, contractual dispute, or the need to undertake supplementary developments or 
procurements. 

5.5 SyRS Requirements 

Content requirements begin on page 3. The numbers shown designate the paragraph numbers to be used in the 
document.  


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 3 of 14 

TABLE OF CONTENTS 

 

1. 
INTRODUCTION AND SCOPE 
4 
1.1 
Identification 
4 
1.2 
Intended Use 
4 
1.3 
Background 
4 
1.4 
System Overview 
4 
1.5 
Document Overview and Use 
4 

2. 
APPLICABLE AND OTHER REFERENCED DOCUMENTS 
4 
2.1 
Applicable Documents 
4 
2.2 
Other Referenced Documents 
4 

3. 
MEANINGS, ACRONYMS AND ABBREVIATIONS 
5 
3.1 
Meanings 
5 
3.2 
Acronyms 
5 
3.3 
Abbreviations 
5 

4. 
REQUIREMENTS 
5 
4.1 
Identification of External Interfaces 
6 
4.2 
Identification of States and Modes (or “Configurations, States and Modes”) 
6 
4.3 
System Function and Performance Requirements 
6 
4.3.1 (System) Function 
6 
4.4 
Relationships Between States and Modes 
7 
4.5 
System External Interface Requirements 
7 
4.5.1 (Project-Unique Identifier of Interface) 
7 
4.6 
System Environmental Requirements 
10 
4.6.1 Classes of Environment 
10 
4.6.2 XYZ Environment 
10 
4.7 
External Resource Utilization Requirements 
10 
4.8 
System Physical Requirements 
10 
4.9 
Other System Qualities 
11 
4.10 Design and Construction Requirements 
11 
4.10.1 General Design and Construction Requirements 
11 
4.10.2 Characteristics of Subordinate Elements 
11 
4.11 Precedence of Requirements 
12 

5. 
VERIFICATION REQUIREMENTS (OPTIONAL) 
12 

6. 
NOTES 
13 
6.1 
Concept of Use (CONUSE) 
13 
6.2 
Notes to Tenderers or Bidders 
13 
6.3 
Requirements Traceability 
13 
6.4 
List of Safety Requirements 
13 
6.5 
List of Information Security Requirements 
14 
6.6 
Summary of Adaptation Requirements 
14 
6.7 
Ordering Details 
14 
6.8 
Criticality of Requirements 
14 
6.9 
Value Model 
14 

A. 
ANNEXES 
14 

 

 

 
 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 4 of 14 

1. 
INTRODUCTION AND SCOPE 

This section may be divided into the following paragraphs where the volume and content of relevant 
information justify sub-paragraphing. 

1.1 
Identification 

This paragraph should contain a full identification of the system to which the document applies, including, as 
applicable, identification number(s), title(s), abbreviation(s), version number(s) and release number(s).  

Where the system to which the document applies includes variants of the system, the above information 
should be provided for each variant. Where variants apply, this paragraph should establish nomenclature for 
the variants, and any rules for applicability in section 4. of requirements to variants.  

Where the system to which the document applies includes incremental builds of the system that are subject 
to individual specification within the specification, the above information should be provided for each build.  

1.2 
Intended Use 

This paragraph should briefly state the intended users and uses of the system to which the SyRS applies, 
referring to a Concept of Use (CONUSE)/Operational Concept Description (OCD) or comparable description for 
more detail, where such a document exists.  

1.3 
Background 

This paragraph, if used, may summarize the history of system development, operation, and redevelopment (if 
any), and identify, as relevant, the project sponsor, acquirer, user, supplier and support organizations. 

1.4 
System Overview 

This paragraph, if used, should identify, if applicable, any current and planned operating sites of parts of the 
system, and list any major subsystems which are required by 4., and which have end-use significance. 

Where a system is required to be configurable (able to be assembled/reassembled into two or more 
configurations by the user), this paragraph should state so, and should also state the nature of the 
configurability. Where configurations apply, this paragraph should establish nomenclature for the 
configurations, and any rules for applicability in section 4. of requirements to configurations. 

1.5 
Document Overview and Use 

This paragraph, if used, should summarize the purpose and contents of the SyRS and should describe any 
security or privacy considerations associated with its use. 

 

2. 
APPLICABLE AND OTHER REFERENCED DOCUMENTS 

This section should be divided into the following paragraphs, if applicable, and should list the number, title, 
revision, and date of each document referenced in the SyRS. This section should also identify the source of 
each document not available through normal channels, and any security or sensitivity classification. 

2.1 
Applicable Documents 

This paragraph should list each document that is invoked in whole or in part within 4. as containing 
requirements information. The paragraph should contain any applicable rules for establishing precedence in 
the event of conflict of requirements between 4. and the applicable documents, and between applicable 
documents. The paragraph should also contain, where applicable, rules for establishing the applicable issue 
number of documents invoked in 4. 

2.2 
Other Referenced Documents 

This paragraph should list each document that is referenced in the requirements specification, but which is not 
invoked in whole or in part by 4. as containing requirements information. 

 

 
 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 5 of 14 

3. 
MEANINGS, ACRONYMS AND ABBREVIATIONS 

This section should be divided into the following paragraphs. 

3.1 
Meanings 

This paragraph should list alphabetically and define each word or term used in 4. for which reliance on 
dictionary meanings is not appropriate. As a guide, terms which are not likely to be in the vocabulary of the 
intended users of the requirements specification, terms which have multiple dictionary meanings but only a 
single requirements specification meaning, technical terms and terms which are used with special meanings 
should be defined in this paragraph. 

The following meaning, or similar, should be incorporated into this section: 

a. Shall expresses a characteristic which is to be present in the item which is the subject of the specification, 
i.e. "shall" expresses a binding requirement. 
b. Should expresses a target or goal to be pursued, but not necessarily achieved. 
c. May expresses permissive guidance. 
d. Will expresses a declaration of intent on the part of a party, usually the sponsoring or acquiring 
organization. "Will" does not express a binding requirement. "Will" may also be used in cases where the 
simple future tense is required, for example, "The operating system will be supplied by the Company". Any 
statement that employs the term "will", if used in 4., should be present as a note so as to be clearly 
distinguishable from requirements. 

This paragraph should also identify by name and issue the dictionary to be used in the interpretation of terms 
used in 4. 

3.2 
Acronyms 

This section should list alphabetically each acronym used in the document, together with the acronym’s 
expanded meaning. 

3.3 
Abbreviations 

This section should list alphabetically each abbreviation used in the document, together with the 
abbreviation’s expanded meaning, except that abbreviations within the International System of Units (SI) 
should not be listed. 

 

4. 
REQUIREMENTS 

This section should be divided into the following paragraphs to specify the system requirements, that is, those 
characteristics of the system that are required to be present in the final product. In some cases, such 
requirements will also be conditions for acceptance of the system. Each requirement should be assigned a 
project-unique identifier to support verification and traceability, and should be stated in such a way that an 
objective, finite and cost-effective verification activity and pass criterion can be defined for it. 

If there are no requirements corresponding to a given paragraph of the DID, the DID paragraph may be deleted 
in the specification and other paragraph numbers adjusted accordingly. Alternatively, “Not used.” may be 
inserted under the paragraph heading.  

If a given requirement fits into more than one paragraph (this should not normally occur), the requirement 
should be stated once and referenced from the other paragraph(s). Duplication of requirements should be 
avoided. 

The degree of detail to be incorporated in specifying requirements should be guided by the following principle: 
include those characteristics of the system that are necessary for the system to satisfy its intended use; defer 
to design or supply those characteristics that the requirer is willing to leave up to the developer or supplier.  

In determining characteristics necessary to satisfy intended use, the criterion which should be used is the level 
of risk associated with satisfaction of the following ideal: "that any system which is supplied which satisfies the 
requirements in 4. will satisfy the need". The level of acceptable risk with respect to attainment of this ideal 
should be determined as a prerequisite to preparation of the system requirements specification. Such a level 
of acceptable risk will usually be "low". 

 
 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 6 of 14 

Typically, for a given acceptable level of risk, lesser rigor of specification will suffice for items which are non-
developmental, whilst for developmental items a more rigorous specification is called for. Similarly, where the 
requirements specification is for internal communication of requirements only then lesser rigor is needed, 
whilst to satisfy the legal demands and address the financial implications of contracting, greater rigor is called 
for. 

4.1 
Identification of External Interfaces 

This paragraph should identify required external interfaces of the system. The identification of each interface 
should include a project-unique identifier for the interface - the name of the interface may serve this purpose. 
The paragraph may designate the interfacing entities (systems, configuration items, users, etc.), by name, 
number, version and documentation reference, as applicable.  

A diagram that depicts the interfaces may be included for information, with interfaces shown which 
correspond to the specified interfaces. The context diagram is a suitable form of representation for this 
purpose. If used, a context diagram should be conceptual in nature.  

Note that paragraph 4.5 rather than this paragraph should be used to specify the external interface 
requirements applicable to each external interface identified in this paragraph. 

4.2 
Identification of States and Modes (or “Configurations, States and Modes”) 

If the system is required to be configurable, this paragraph should commence by identifying the required 
configurations. An example of potential configurations for an aircraft would be a Crop Dusting Configuration 
and a Fire Bombing Configuration. 

If the system is required to exist or operate in more than one state or mode having requirements distinct from 
those in other states or modes, this paragraph should identify each such state and mode which is permitted or 
required. Examples of states include: off, on, ready, active, unserviceable. Example of modes include flight, 
taxi, auto-pilot, post-use analysis, training, backup. A system may be described in terms of states only, modes 
only, modes within states, or any other schema that is useful. Sub-modes may be defined for a given mode. 

A system may be specified without use of states and modes, or at the other extreme, a system may be specified 
fully as a state machine (not addressed in this DID).  

A states and modes schema which has states at the highest level of requirements organization, and normally 
mutually exclusive of other states, together with modes within states, modes not necessarily being mutually 
exclusive of other modes and being able to exist in multiple states, has been found to be useful for the 
specification of systems of many types. 

If no states or modes are required, this paragraph should be omitted or should so state, without creating 
artificial distinctions. If states or modes or both are required, each requirement in the requirements 
specification that relates to a state or mode should be correlated to that state or mode, but not in this 
paragraph.  

The correlation of a requirement to one or more states and modes (or sub-modes) should be specified by 
inclusion of such correlation in the specification of the requirement where it appears in the requirements 
specification (somewhere in 4.3 to 4.10). This may be achieved in the requirement sentence (preferable) or 
paragraph (if necessary for clarity) in which the requirement is stated. 

Any statements about the applicability of requirements in general to the states and modes identified in this 
paragraph should be included in this paragraph. 

4.3 
System Function and Performance Requirements 

This paragraph should be divided into subparagraphs to specify each function required to be performed by the 
system, together with associated required performance. Each requirement may reference as necessary any 
external interfaces, configurations, states or modes (or sub-modes) identified in 4.1 or 4.2. 

4.3.1 
(System) Function 

This paragraph (numbered 4.3.1 to 4.3.x with one function per paragraph) should identify a required system 
function and should specify the corresponding requirement or requirements. The word “Function” should 
appear in each leaf subparagraph heading. The requirements should specify required behavior of the system 
and should include, for each function, applicable initiating and terminating conditions, applicable performance 
parameters and values, such as response times, throughput times, other timing constraints, sequencing, 
accuracy, capacities (how much/how many), priorities, continuous operation requirements, and allowable 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 7 of 14 

deviations based on operating conditions. The requirements should include, as applicable, required behavior 
under unexpected, un-allowed or “out of bounds” conditions, and any requirements for error handling. Each 
functional requirement should also state the conditions during which the specified function is to be performed, 
such as configuration, state, mode in state, or requirement-specific environmental conditions. 

Functional and performance requirements may be organized in a structure of section, paragraphs, 
subparagraphs, etc. Requirements should be placed only in the leaf subparagraphs. 

The word “Mode” may also be used in a paragraph heading. 

If the requirement is a requirement of a subordinate element of the system rather than of the system overall, 
the requirement should be placed in 4.10.2 and not in this paragraph. 

4.4 
Relationships Between States and Modes 

This paragraph, if states and modes are used, should specify the required relationships between the various 
states and modes, including default states and modes, temporal relationships, the conditions that are required 
to cause state and mode transitions and the external response(s) that the system is required to produce as a 
reflection of each required transition having taken place.  

The paragraph should state in the order matching 4.2, as applicable, and for example: 

a. Default State (the state in which the system commences) 
b. State A<>State B, followed by transition and response requirements, including any prohibitions of 
transitions and permissive guidance (may) statements 
c. State A<>State C, etc. 
d. Default Mode(s) in State A (the mode(s) in which the system is to commence upon entering State A, or if 
there is to be no default mode(s), the corresponding requirement to that effect) 
e. Mode A in State A<>Mode A in State B, followed by transition and response requirements, including any 
prohibitions of transitions and permissive guidance (may) statements 
f. 
Mode A in State A<>Mode A in State C, etc. 
g. Mode A in State A<>Mode B in State A, etc. 
h. Mode B in State A<>Mode C in State A, etc. 
i. 
Default Sub-mode of Mode A 
j. 
Sub-mode A of Mode A in State A<> Sub-mode B of Mode A in State A 
k. Default Mode(s) in State B, etc. 

4.5 
System External Interface Requirements 

This paragraph should be divided into subparagraphs to specify the requirements, if any, for each of the 
system’s required external interfaces, including user interfaces, listed in 4.1. This paragraph may reference one 
or more Interface Requirements Specifications (IRSs), Interface Control Documents (ICDs) or other documents 
containing these requirements, which may be either annexes to the system requirements specification or 
(more commonly) separate documents. 

Subparagraphs should be arranged in alphabetical order in accordance with the names of the interfaces. 

Where an interface is inherently simple, its specification may be contained rather than referenced in this 
paragraph. 

4.5.1 
(Project-Unique Identifier of Interface) 

This paragraph (numbered 4.5.1 to 4.5.x with one interface per paragraph) should identify a required system 
external interface by name and any additional project-unique identifier and should briefly identify the 
interfacing entities. Where an interface comprises a lower-level physical structure of sub-interfaces, these 
should be reflected in a sub-paragraphing structure. Requirements may be defined for interfaces and sub-
interfaces at any level or levels in the structure. 

Each paragraph should be divided into subparagraphs as needed to state the requirements that the interface 
must satisfy. The interface should be specified from the viewpoint of the interface as a surface through which 
inputs and outputs pass. The paragraph should specify all required characteristics of the surface, of the inputs, 
and of the outputs, including relationships between members of each of these classes of item. The paragraph 
may reference other documents (such as mechanical drawings, item dictionaries, data dictionaries, standards 
for communication protocols, and standards for user interfaces) in place of stating the information here. 
Requirements should note any differences in these characteristics from the point of view of the interfacing 
entities (such as different expectations about the size, frequency, or other characteristics of data elements).  


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 8 of 14 

Requirements for data-orientated interfaces may be structured in a manner that adopts an open systems 
approach. An open system approach is an approach in which interfaces are defined in a series of abstract 
layers, accessible from the interfacing entity(ies), which progressively and in a structured manner provide the 
required interface mechanism. The internet's TCP/IP protocol suite is one such schema.  

The requirements should include the following, as applicable, presented for each interface in any order suited 
to the requirements (subject to the open systems guidance contained above): 

a. requirements on the types of interface (such as real-time data transfer, storage-and-retrieval of data, 
human/machine interface, mechanical interface, physical interface, facilities interface, etc.), to be 
implemented; 

b. interfacing entity(ies) to exchange items such as: 
i. 
sources (setting/sending entities) and recipients (using/receiving entities). 
ii. 
names/identifiers: 
1. project-unique identifier; 
2. non-technical (natural-language) name; 
3. standard data element name; 
4. technical name (e.g., variable or field name in code or database); 
5. abbreviation or synonymous names; 
iii. 
data type (alphanumeric, integer, etc.); 
iv. 
size and format (such as length and punctuation of a character string); 
v. 
units of measurement (such as meters, dollars, nanoseconds); 
vi. 
range or enumeration of possible values (such as 0-99); 
vii. 
accuracy (how correct) and precision (number of significant digits); 
viii. 
priority, timing, frequency, volume, sequencing, and other constraints; and 
ix. 
security and privacy constraints;  

c. required characteristics of data element assemblies (records, messages, files, arrays, displays, reports, etc.) 
used to present information that the interfacing entity(ies) must receive, store, send, access, output, etc., 
such as: 
i. 
names/identifiers: 
1. project-unique identifier; 
2. non-technical (natural language) name; 
3. technical name (e.g., record or data structure name in code or database); and 
4. abbreviations or synonymous names; 
ii. 
data elements in the assembly and their structure (number, order, grouping); 
iii. 
medium (such as disk) and structure of data elements/assemblies on the medium; 
iv. 
visual and auditory characteristics of displays and other outputs (such as colors, layouts, fonts, 
icons and other display elements, beeps, lights; 
v. 
relationships among assemblies, such as sorting/access characteristics; 
vi. 
priority, timing, frequency, volume, sequencing, and other constraints; 
vii. 
security and privacy constraints; 
viii. 
message formatting; and 
ix. 
sources (setting/sending entities) and recipients (using/receiving entities). 

d. required characteristics which the interface must satisfy to enable organization and synchronization of 
connections between interfacing entity(ies), such as: 
i. 
project-unique identifier(s); 
ii. 
session-connection establishment—creation of an exchange between interfacing entity(ies); 
iii. 
session-connection release; 
iv. 
session-connection synchronization; 
v. 
exception reporting—permitting the interfacing entity(ies) to be notified of exceptional situations; 
vi. 
data transfer rate, whether periodic/aperiodic, and interval between transfers; 
vii. 
message formatting; and 
viii. 
safety/security/privacy considerations, such as user authentication and auditing inputs/outputs. 

e. required characteristics of data flow methods that the interfacing entity(ies) must use for the interface, 
enabling the interfacing entity(ies) to assume cost-effective and reliable data exchange such as: 
i. 
project-unique identifier(s); 
ii. 
transmission services, including priority and grade; 
iii. 
message formatting; and 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 9 of 14 

iv. 
safety/security/privacy considerations, such as auditing inputs/outputs. 
f. 
required characteristics of communication methods that the interfacing entity(ies) must use to establish, 
maintain and terminate connections between systems, such as: 
i. 
project-unique identifier(s); 
ii. 
communication links/bands/frequencies/media, communication end points and their 
characteristics; 
iii. 
message formatting; 
iv. 
flow control (such as sequence numbering and buffer allocation); 
v. 
routing, addressing, and naming conventions; 
vi. 
synchronization, including connection establishment, maintenance, termination; and 
vii. 
safety/security/privacy considerations, such as auditing inputs/outputs. 

g. required characteristics of protocols the interfacing entity(ies) must use for the interface, such as: 
i. 
project unique identifier(s); 
ii. 
priority/layer of the protocol; 
iii. 
packeting, including fragmentation and reassembly, routing, and addressing; 
iv. 
legality checks, error control, and recovery procedures; and 
v. 
status, identification, and any other reporting features. 

h. required physical compatibility such as interface pin assignments; 

i. 
static mechanical characteristics, such as physical compatibility of the interfacing entities (dimensions, 
tolerances, loads, plug compatibility, alignment, etc.). Reference may be made to Interface Control 
Drawings where applicable; 

j. 
dynamic mechanical characteristics such as shock, vibration, acceleration, deceleration; 

k. electrical power interface: type, voltage, frequency, phases, power factor; 

l. 
hydraulic/pneumatic interface: type, flow rate, temperature of fluid, pressure; 

m. use of nameplates, part marking, serial and lot number marking and other identifying markings; 

n. the system human/machine external interface requirements, included to accommodate the number, skill 
levels, duty cycles, training needs, and other system requirements related to the personnel who will use 
or support the system. An example is the requirement for the number of operator positions to be provided. 
Also included should be the human factors engineering requirements, if any, imposed on the system. These 
requirements should include, as applicable, considerations for the capabilities and limitations of humans, 
foreseeable human errors under both normal and extreme conditions, and specific areas where the effects 
of human error would be particularly serious. Examples include requirements for adjustable-height 
operator positions, color, duration of error messages, physical placement of critical indications or controls 
and use of auditory signals; and 

o. facility interface requirements, including floor loads, heat loads, in-out temperatures, axle or wheel 
loads, load surface inclination, load surface flatness, facility access constraints, special water 
requirements, special air requirements, fire protection environmental constraints, earthing connections, 
minimum clearances. 

Any requirements related to the interface that are of the nature of system functionality should be incorporated 
in 4.3 and not in this paragraph, except where ease of use of the SyRS would be enhanced by incorporation of 
such requirements in this paragraph. This can occur when, for example, a particular communications protocol 
is required to be used across an interface. If such requirements regarding functionality of the interfacing 
systems are included in the IRS, a pointer to the required functionality should be included in the Section 4.3 
"Functional and Performance Requirements" of the system (or software) requirements specification for each 
of the interfacing systems. 

Any requirements that specify the consumption or usage of externally supplied resources should be 
incorporated in 4.7 and not in this paragraph. 

External interface requirements should be specified only to the degree necessary to bound the design or supply 
of the external interface. For a developmental project, this degree will often increase throughout the course 
of the project, i.e. external interfaces will be initially specified at a high level of abstraction but will eventually 
be specified at the level of detail suitable for physical fabrication of the interface.  

An external interface may also be specified in terms of achieving physical and functional interoperability with 
the interfacing external system. Considerable care should be taken if using this form of specification, as it relies 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 10 of 14 

on the specifier defining required system characteristics in terms which include the characteristics of external 
systems, characteristics which may not be under the control of the specifier, and which may not be stable with 
time. 

The identification should state as applicable and in note form: which interfacing items impose interface 
requirements on the system, which interfacing items are to have interface requirements imposed on them by 
the system and which interfacing items are subject to both influences. 

4.6 
System Environmental Requirements 

This paragraph should specify in the subparagraphs below the requirements, if any, regarding the environment 
in which the system must meet other requirements as specified in the remainder of the Requirements section.  

Examples include the environmental conditions that the system must withstand during transportation, storage, 
and operation, such as conditions in the natural environment (wind, rain, fog, temperature, humidity, pressure, 
driven dust, geographic location, magnetic field, ambient light level, ionospheric conditions), the induced 
environment (motion, shock, noise, electromagnetic radiation, ambient light level) and for military systems 
environments due to enemy action or threat (explosions, radiation). Constraints on rates of change of 
environmental parameters should be included where applicable. 

This paragraph should also specify the requirements, if any, which limit the effect that the system is to have 
on the external environment. Examples include limits on the electromagnetic radiation (various wavelengths, 
tempest), gaseous emissions, heat or acoustic noise that the system is permitted to generate. 

If the requirement is a requirement of a subordinate element of the system rather than of the system overall, 
the requirement should be placed in 4.10.2 and not in this paragraph. 

If the requirement is a requirement on an input, e.g. the type of fuel oil, the requirement should be 
incorporated in 4.5 and not in this paragraph. 

4.6.1 
Classes of Environment 

This paragraph, if used, should make an informative statement identifying the classes of environment, with 
reference to which environmental requirements are specified, e.g., Storage Environment, Transportation 
Environment, Operational Environment. Classes of environment should be listed in order of the time sequence 
in which they are encountered, where this applies, otherwise listed alphabetically. 

4.6.2 
XYZ Environment 

This paragraph should specify, in a format appropriate to the information, the external environmental 
parameters, if any, within which the system is to meet all other requirements, with any stated exceptions. The 
paragraph must make clear the degree to which the possible parameter environmental combinations apply 
simultaneously for the class of environment, i.e. environmental envelope(s). 

This paragraph should also specify, in a format appropriate to the information, limits on unwanted outputs 
from the system into the enveloping environment.  

Subsequent paragraphs should apply to other classes of environment (if any). 

Subject to any formatting needs related to requirements traceability, the requirements information may be 
presented in text, tables, or other suitable format. 

4.7 
External Resource Utilization Requirements 

This paragraph should specify the requirements, if any, regarding the consumption or utilization by the system 
of externally provided resources. Examples are constraints on consumption of externally-provided power or 
fuel. 

Paragraphs should be arranged in alphabetical order in accordance with the name of the resource. 

If the resource requirement is a requirement on a subordinate element of the system rather than of the system 
overall, the requirement should be placed in 4.10.2 and not in this paragraph. 

4.8 
System Physical Requirements 

This paragraph should specify the requirements, if any, which represent constraints on the physical (properties 
of matter) characteristics of the system as a whole. Example physical characteristics are mass, dimensions, 
shape, volume, density and center of gravity. 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 11 of 14 

Paragraphs should be arranged in alphabetical order in accordance with the names of the physical properties. 

If a physical requirement is a physical requirement of a subordinate element of the system rather than of the 
system overall, the requirement should be placed in 4.10.2 and not in this paragraph. 

Interface requirements which are physical in nature e.g. geometry of a connection, should be incorporated in 
4.5 and not in this paragraph. 

4.9 
Other System Qualities 

This paragraph should specify the requirements, if any, pertaining to other qualities required of the system as 
a whole. Example other system qualities include: 

a. reliability (the ability to perform with correct, consistent results - such as mean-time-between-failure for 
equipment); 
b. maintainability (the ability to be easily serviced and repaired - such as mean-time-to-repair for equipment); 
c. availability (the ability to be accessed and operated when needed); 
d. reuseability (the ability to be adapted for use in multiple applications); 
e. testability (the ability to be easily and thoroughly tested); 
f. 
useability (the ability to be easily learned to use, and easily used); 
g. interchangeability of parts (the ability to have parts of the same part number interchanged without 
necessitating readjustment); 
h. transportability (the ability to be transported from one location to another); 
i. 
ease of set-up (the ability to be set up by one, or a given number of, persons); 
j. 
expandability (the ability to be easily modified in response to potential areas of growth in requirements); 
k. flexibility (the ability to be easily adapted to changes in mission, threat or technology); 
l. 
interoperability (the ease of interfacing and/or interoperation with external systems in general. Interfacing 
with specific external systems should be specified in 4.1 and 4.5); and 
m. durability (the life of the item when used as intended). 

Paragraphs should be arranged in alphabetical order in accordance with the names of the qualities. 

Any requirement, related to other system qualities, and which is functional in character, should be 
incorporated in 4.3 and not in this paragraph. 

Any requirement for other system qualities which is a requirement of a subordinate element of the system 
rather than of the system overall should be placed in 4.10.2 and not in this paragraph. 

Note that the information content of the requirement governs whether it is of “Other Qualities” type, not its 
purpose. For example, a mass limit for reason of safety is a physical requirement and is placed in 4.8. 

4.10 
Design and Construction Requirements 

This paragraph should specify any requirements that direct aspects of the design and construction of the 
system (build it internally in this way, or don’t build it internally this way). This paragraph, if used, should be 
divided into the following subparagraphs. 

4.10.1 General Design and Construction Requirements 

This paragraph should specify any general aspects of design and construction that apply as requirements 
system-wide. Examples include requirements concerning: 

a. use of a particular system architecture, or requirements on the architecture, such as required subsystems; 
b. use of customer-furnished property (equipment, information, software or services); 
c. use of standard, military or existing components; 
d. materials that may and may not be used; 
e. use of particular design or construction standards, use of particular internal data standards, use of a 
particular programming language(s), workmanship requirements and production techniques; and 
f. 
use of specific surface coatings. 

Paragraphs should be arranged in alphabetical order in accordance with the names of the aspects or properties. 

4.10.2 Characteristics of Subordinate Elements 

This paragraph should be divided into subparagraphs that correspond to a simple, flat, alphabetical list of items 
– organizations, hardware, software, databases, materials, etc., to which requirements apply as requirements 
on the system, using paragraphing 4.10.2.x where x corresponds to the subordinate element.  


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 12 of 14 

Paragraphs should be arranged in alphabetical order in accordance with the names of the subordinate 
elements.  

For physical system elements, each element should be specified, to the extent justified by the reasons for 
directing design, using the paragraph and subparagraph names and content corresponding to 4.1 to 4.10.1 
inclusive, as applicable. For elements of other types, e.g., software, materials, manuals, the corresponding 
structure of the Requirements section from a sound corresponding DID for that type of element should be 
used. 

This paragraph should also specify any requirements regarding computer software that must be incorporated 
into the system. Examples include types of operating systems, database management systems, 
communications/network software, utility software, input and equipment simulators, test software and 
manufacturing software that are to be an integral part of the system. The correct nomenclature, version and 
documentation references of each such software item should be provided, where applicable. 

If training devices or training materials are required to be included as part of the system, any requirements on 
such devices or materials should be specified in this paragraph. 

If user documentation or maintainer documentation are required to be included as part of the system, any 
requirements on such documentation should be specified in this paragraph. 

If logistics support devices and logistic support materials are required to be included as part of the system, any 
requirements on such devices or materials should be specified in this paragraph. 

If packaging materials are required to be included in the system, any requirements on such materials should 
be specified in this paragraph. 

Only those characteristics that the specifying enterprise requires be implemented by the above subordinate 
elements should be specified in this paragraph. Note that by specifying the existence or characteristics of 
subordinate elements, the requirer assumes responsibility for aspects of system design. Care should be 
exercised in taking on this responsibility. 

4.11 
Precedence of Requirements 

This paragraph, if used, should state whether all paragraphs have equal precedence in the event of conflict 
between requirements. If all requirements are not to be of equal precedence in the event of conflict, this 
paragraph should state the rules of precedence. 

Note that the possibility of conflict between requirements is increased where design requirements are 
specified. In this case, the paragraph should state rules of precedence between 4.10 and other requirements 
paragraphs. 

 

5. 
VERIFICATION REQUIREMENTS (OPTIONAL) 

This section, if used, should define for each requirement in 4. the requirement (or otherwise) for qualities of 
evidence that the system requirement has been met. The section may also state the method(s) to be used to 
evidence that the requirement has been met, although a list of verification methods rarely constitutes an 
adequate set of verification requirements. Verification methods, if specified, may include: 

a. Test - the operation of the system, or a part of the system, using instrumentation or other special test 
equipment to collect data for later evaluation; 
b. Demonstration - the operation of the system, or a part of the system, that relies on observable functional 
operation not requiring the use of instrumentation, special test equipment, or subsequent analysis; 
c. Analysis - the processing of accumulated data, sometimes obtained from other verification methods. 
Examples are reduction, interpolation, or extrapolation of test results; 
d. Inspection - the visual examination of system components, documentation, etc.; 
e. Analogy - the use of evidence from verification of an analogous product, for example a prior version; 
f. 
Certification - a declaration by a designated stakeholder, usually the supplier or developer; and 
g. Special verification methods - any special verification methods for the system, such as special tools, 
techniques, procedures, facilities, acceptance limits, use of standard samples, preproduction or periodic 
production samples, pilot models, or pilot lots. 

Where sampling is to be used, this section should define the rules for selection of samples. 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 13 of 14 

Alternatively, the VERIFICATION REQUIREMENTS may be placed in a separate document or database and 
(optionally) referred to in 6. NOTES. 

A Table format for specification of verification requirements is often suitable, with columns: 

a. identifier for system requirement; 
b. subject area; and 
c. verification requirement; 

not necessarily in that order. 

The guidance and instruction in Verification Requirements Specification (VRS) DID applies. 

 

6. 
NOTES 

This section, if used, should contain any general information that aids in understanding or using the 
specification (e.g., background information, rationale). 

This section may include the following paragraphs, as applicable. 

6.1 
Concept of Use (CONUSE) 

This paragraph, if used, should contain or reference a description of who the users of the system are intended 
to be, what it is intended or expected that each user will use the system for, how it is intended or expected 
that each user will use the system for each intended use, and under what conditions it is intended or expected 
that the system will be used.  

This paragraph will not be applicable if a Concept of Use (CONUSE) as a separate document is referenced out 
from the SCOPE section of the SyRS. 

6.2 
Notes to Tenderers or Bidders 

This paragraph, if used in a solicitation or tendering application of the requirements specification, should 
contain any explanatory notes to, or requests for information from, tenderers/bidders. Alternatively, such 
notes may be contained partially or completely in a separate document that references the requirements 
specification, or in individual notes to tenderers/bidders incorporated in the body of the requirements 
specification. 

Where a note to tenderers/bidders is included within the body of the requirements specification, the note 
should be clearly distinguishable from a system requirement. A suitable format is: “Note to Tenderer: The 
tenderer is to ...”. 

6.3 
Requirements Traceability 

This paragraph, if used, should contain: 

a. data which details traceability from each system requirement in the requirements specification, including 
each requirement in IRSs invoked by reference, to the higher physical level requirement(s) it addresses. 
Alternatively, this traceability may be provided by annotating each requirement in 4; or alternatively 
b. reference to the document which contains corresponding requirements traceability information. 

Note:  Higher physical level requirements are requirements on a larger system for which the system which is 
the subject of the requirements specification is a part of the solution. 

6.4 
List of Safety Requirements 

This paragraph, if used, should list the system requirements, specified in 4. and concerned with preventing or 
minimizing unintended hazards to personnel and property. Examples include restricting the use of dangerous 
materials; abort/escape provisions from enclosures; gas detection and warnings; grounding of electrical 
systems; decontamination and explosion proofing. 

Alternatively, safety requirements may be annotated as such in 4. 

Safety requirements are typically listed only if they are subject to special actions, for example, increased 
verification as to their satisfaction, or regulatory procedure. 


PPA-002235-18 
© Copyright Project Performance International (PPI) 2012-2023 
Page 14 of 14 

6.5 
List of Information Security Requirements 

This paragraph, if used, should list the system requirements, specified in 4. and concerned with maintaining 
information security, viz. confidentiality and integrity of information.  

Alternatively, information security requirements may be annotated as such in 4. 

Information security requirements are typically listed only if they are subject to special actions, for example, 
increased verification as to their satisfaction. 

6.6 
Summary of Adaptation Requirements 

This paragraph, if used, should identify the requirements, specified in 4. and concerning installation-dependent 
data that the system is required to use (such as site-dependent latitude and longitude or site-dependent post 
codes) and operational parameters that the system is required to use that may vary according to operational 
needs (such as parameters indicating operation-dependent targeting constants or data recording). 

Alternatively, adaptation requirements may be annotated as such in 4. 

6.7 
Ordering Details 

This paragraph, if needed, should provide any information necessary for identification of the system and any 
variants of the system for ordering purposes. 

6.8 
Criticality of Requirements 

This paragraph, if applicable, should specify the criticality, or assigned weights, indicating the relative 
importance of the requirements in this specification. An example is identification of those requirements 
deemed critical to mission, or to safety, or to security, for purposes of singling them out for special treatment, 
e.g., a higher level of independent verification and validation. 

6.9 
Value Model 

Where goals (design goals) are expressed as goals above a specified minimum standard, this paragraph should 
state the relative importance of the difference between the minimum standard and the goal, for each design 
goal, as related to the value perceptions of the relevant stakeholders in the system, together with how the 
value changes between the minimum standard and the goal. Alternatively, this paragraph may reference an 
external value model, typically a data file accessed via value modeling computer software. 

 

A. 
ANNEXES 

Annexes may be used to provide information published separately for convenience in document maintenance 
or use (e.g., charts, databases, interface specifications). As applicable, each annex should be referenced in the 
main body of the document where the data would normally have been provided. Annexes may be bound or 
prepared digitally as separate documents for ease in use. Annexes should be lettered alphabetically (A, B, etc.).  

Appendices may be used to annexes. Appendices should be numbered numerically (1, 2, etc.). 


