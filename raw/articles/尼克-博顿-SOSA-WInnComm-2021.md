<!-- Page 1 -->
WInnComm 2021:
Sensor Open Systems 
Architecture V1.0 Overview
November 30th, 2021 
Nick Borton, SOSA Steering 
Committee Vice Chair (SRC Inc.)


<!-- Page 2 -->
The SOSA Approach in a Nutshell*
The SOSA Consortium is a C5ISR-focused technical and business collaborative effort…
What
• Develop a unified technical Open Systems Architecture standard for RADAR, EO/IR, SIGINT, 
EW, and Communications – and the supporting business models
Why
• Improve sub-system, system, and platform affordability, re-configurability, upgradability, and 
hardware/software/firmware re-use – and to shorten cycle times to counter emerging threats
Who
• The Air Force, Navy, Army, other government agencies, industry and academia
How
• Developing an OSA via modular decomposition (defining functions and behaviors) and associated 
interfaces (including physical, protocol, and data structure) between the modules
2
___________
* Based on abstract of “Sensor Open System Architecture (SOSA) Evolution for Collaborative Standards Development,” SPIE 
Open Architecture/Open Business Model Net-Centric Systems and Defense Transformation 2017


<!-- Page 3 -->
Building with SOSA
• SOSA provides a set of tools to build a system with
– System designers choose what tools to use
• For Example: only use the SOSA Modules necessary to achieve the 
Sensor’s Mission
– Systems are built with SOSA Components, Systems are not SOSA in 
and of themselves
• All SOSA Components (or tools) are based on standardized 
interfaces
– Some components have functions and behaviors w/ data
– Other components have physical interfaces
– Yet other components have APIs or Protocols
Signal/Data Structure
Interface
Protocol (Method)
Physical (Medium)
Example builds coming up


<!-- Page 4 -->
SOSA V1.0 Taxonomy
4
Each leaf block is a set of interfaces
which can be additive
Modules provide functions and behaviors
-
Input / Output data aspects of interfaces
-
Perform Work
-
Implementation Agnostic
Infrastructure provides:
-
Physical and Protocol aspects of interfaces
-
Housing for Module implementation
-
Down select of existing standards


<!-- Page 5 -->
SOSA Sensor System
SOSA Sensor Management
SOSA V1.0 Modules
5
2.3: 
Conditioner-
Receiver-
Exciter
4.6: 
Storage/ 
Retrieval 
Manager
5.1: 
Reporting 
Services
3.1: 
Signal/Object 
Detector and 
Extractor
3.2: 
Signal/Object 
Characterizer
3.3: 
Image Pre-
Processor
3.4: 
Tracker
4.1: 
External Data 
Ingestor
4.2: 
Encoded Data 
Extractor
Support System Operation
4.3: 
Situation 
Assessor
4.4: 
Impact Assessor 
and Responder
6.1: 
Security 
Services
6.2: 
Encryptor/ 
Decryptor
6.3: 
Guard/ 
Cross-Domain 
Service
6.4: 
Network 
Subsystem
6.5: 
Calibration 
Service
6.6: 
Nav Data 
Service
6.7: 
Time & 
Frequency 
Service
6.8: 
Compressor/ 
Decompressor
6.10: Power
6.9: 
Host Platform 
Interface
2.4: 
Emitter/
Collector
1.1: System Manager
1.2: Task Manager
Transmission/Reception
Process Signals/Targets
Analyze/Exploit
Convey


<!-- Page 6 -->
5.1: Reporting 
Services
6.9: Host Platform 
Interface (HPI)
Selected Format from Standard Formats
(i.e. JICD 4.2, etc.)
SOSA V1.0 Module High Level Data Flow
SOSA Sensor Management
State Control
Config
Health Monitoring
Sensor Tasking
Capabilities
Task Scheduling
Resource Management 
Task Monitoring 
Platform
System Monitoring and Control
Platform C2
Sensor Products
Processed Data
3.1: Signal/Object 
Detector / 
Extractor
3.2: 
Signal/Object 
Characterizer
6.2: Encryptor/ 
Decryptor
2.3: Conditioner-
Receiver-Exciter
Collection
Collected Digital 
Data
2.4: Emitter/
Collector
Processing Chain / Data Path
Data
System Support Services
6.6: Nav Data
6.7: Time and 
Frequency
Relative Pointing Info
Platform Nav
Time Data
Local Oscillator Frequency
Characterizations
Emission
3.3: Image Pre-
processor
Processed 
Imagery
1.2: Task 
Manager
1.1: System 
Manager
Transmission/Reception
Process Signals/Targets
Convey


<!-- Page 7 -->
SOSA Software Runtime Environments (RTE)
7
The Runtime Environment provides an 
executable software infrastructure with 
defined profiles and interfaces which 
promote interchangeability, portability, 
and reuse.
The profile choices are:
•
FACE
•
Containers (conforms to Open 
Container Initiative)
•
Virtual Machines (conforms to Open 
Virtualization Format)


<!-- Page 8 -->
SOSA Plug-In Cards
8
Data/Control Plane Switches
RF/Optical Payloads
- Mechanical
- Electrical Signaling
- Some Layer 2 Protocols
Key Interfaces Provided:


<!-- Page 9 -->
Electrical/Mechanical: Sample Output
9
SOSA Electrical Interface Recommendations
J2-Signal (25-7 insert, N-Keying)
For Part Numbers insert receptacle choice (20 or 24) and relevant plating finish
Sensor MIL-DTL-38999/***J7SN (receptacle with socket inserts)
Platform Umbilical MIL-DTL-38999/26*J7PN (plug with pin inserts)
EO-IR Turreted 
Sensor
Radar/SAR 
Turreted SensorEW Sensor
SIGINT 
Sensor
Comms
Conn/ 
Desc.
Pin
Wire Type
Signal Name
Signal Source
Signal Type
Used
Used
Used
Used
Used
Ethernet
28
100Ω STP - AWG 24, 
CAT 6A, SAE AS 
6070/6
DA+
Platform/ Sensor
1000BaseT





35
DA-
36
DA Shield
44
DB+
53
DB-
62
DB Shield
45
DC+
54
DC-
63
DC Shield
70
DD+
71
DD-
78
DD Shield
Serial 
Comms 1
7
100 Ohm STP 2419
TX1+
Sensor
RS422





8
100 Ohm STP 2419
TX1-
Sensor
17
SC-AWG24
422_1_RTN
16
100 Ohm STP 2419
RX1+
Platform
23
100 Ohm STP 2419
RX1-
Platform
Serial 
Comms 2
22
100 Ohm STP 2419
TX2+
Sensor
RS422





30
100 Ohm STP 2419
TX2-
Sensor
RS422
29
SC-AWG24
422_2_RTN
RS422
37
100 Ohm STP 2419
RX2+
Platform
RS422
38
100 Ohm STP 2419
RX2-
Platform
RS422
Emi-ssion
Arming
2
AWG22
MASTER_ARM Platform
open/closed ckt

95
AWG22
MASTER_ARM_
RET
Platform
open/closed ckt



<!-- Page 10 -->
Inter-Module Interaction Bindings
Current Binding List:
• MORA
• OAS REST
• OMG DDS
• ZMTP
• AMQP
• NVMe (PCIe)
• NVMe over RoCEv2
10
• Specific Communications Technology choices to 
enable the following:
– Interchangeability
– Upgradeability
– Portability
– Reuse
• Provides protocol structure and low-level data 
encodings for information exchange


<!-- Page 11 -->
SOSA Component Usage 
AKA Instantiation Examples
11
2.4: 
Emitter/
Collector
Firmware
SOSA Interaction Infrastructure
Bindings
SOSA Interaction Infrastructure
Bindings
SOSA Interaction 
Infrastructure
Bindings
Or
4.6: 
Storage/ 
Retrieval 
Manager
3.1: 
Signal/Object 
Detector and 
Extractor
Or
