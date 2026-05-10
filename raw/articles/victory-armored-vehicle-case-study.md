C U R T I S S W R I G H T D S . C O M

CASE STUDY

Enabling VICTORY Data Bus Network 
for an Armored Ground Vehicle

DEFENSE SOLUTIONS 

Challenge

• Connect C4ISR/EW equipment 
to VICTORY data bus

• Affordable, high TRL, low risk 
COTS hardware

• Satisfy information assurance 
and environmental requirements 

• Rugged COTS VICTORY 
infrastructure switch LRU

• SWaP-C optimized subsystem 
qualified for tracked vehicles

• Modular architecture capabilities 
for switch, processor, PNT hub

• Met budget and TRL with low-
cost, rugged COTS solution 

• VICTORY network support with 
low-risk, SWaP optimized switch

• Modular subsystem enables 
optional functional upgrade

Solution
Results

Challenge

Momentum continues to build within U.S. military ground 
vehicle programs to architect and implement the vetronics 
systems standard, referred to as VICTORY (Vehicle 
Integration for C4ISR/EW Interoperability). This C4ISR 
modernization initiative provides a common ground vehicle 
infrastructure to ease the integration of new technologies, 
while improving size, weight and power (SWaP). This 
progressive initiative uses open network interfaces, data 
formats, and protocols to enable integration and sharing 
of network, processing, Position Navigation Timing (PNT) 
and display resources. In the end, VICTORY aims to not 
only enhance situational awareness for the warfighter, but 
also provide a roomier vehicle cabin and more efficient data 
sharing, but reduce overall life-cycle cost for maintaining the 
platform.

A major systems integrator with proven successes 
developing combat vehicles for U.S. and foreign defense 
forces required a VICTORY compliant Ethernet switch for a 
new armored vehicle platform. This small form factor (SFF) 
switch Line Replaceable Unit (LRU) would provide mission 
electronics onboard the command and control (C2) variants 
of this new vehicle with a digital backbone for Ethernet 
connectivity for supporting VICTORY architectures. The 
platform would utilize the network switch to connect tactical 
radio and communications systems (i.e. JTRS, WIN-T), 
smart displays, electronic warfare, friendly force tracking, 
and battle command systems. The switch would support 
key program operational priorities and concerns, including 
SWaP, schedule, cost, and information assurance (IA). It 
would also need to meet the environmental requirements 
for heavy brigade combat team (HBCT) platforms per MIL-
STD-810 and MIL-STD-461. 


© 2016-2017 Curtiss-Wright. All rights reserved.  Specifications are subject to change without notice.  

All trademarks are property of their respective owners   I   A57.0917–

Solution 

Driven by a comprehensive joint program office / prime 
contractor trade study, the U.S. Government surveyed the 
marketplace to find the highest performance VICTORY 
switching solution with the most affordable price, highest 
Technology Readiness Level (TRL) and lowest risk. Not 
only were multiple COTS switch LRUs from Curtiss-Wright 
included in the trade study, but the Parvus DuraDBH-672 
Digital Beachhead model was ultimately selected for this 
program. In fact, for commonality and for logistics purposes, 
two of these switch LRUs were specified per mission 
command vehicle to enable users to swap out units or have 
the second unit take over as bus controller in the event of 
damage or failure to the primary. 

With 16-ports of Gigabit Ethernet (GbE) switching in a 
SFF rugged design, the DuraDBH-672 offered the vehicle 
program a COTS “VICTORY Infrastructure Switch” that was 
in production and qualified to MIL-STD wheeled and tracked 
vehicle environmental requirements. It also afforded nuclear 
survivability with optional nuclear event detection (NED) 
capabilities. Of great customer interest was the fact that this 
second-generation VICTORY system extended capabilities 
introduced by the original Digital Beachhead (commonly 
referred to as the “VICTORY starter kit” already used by the 
U.S. Army), but in a lower-cost, smaller form factor chassis 
more optimized for SWaP and more flexible in terms of 
I/O scalability. The unit could support functional upgrades 
via Mini-PCIe add-on cards (for more serial/Ethernet/DIO 

INFO: CURTISSWRIGHTDS.COM
EMAIL: DS@CURTISSWRIGHT.COM

Parvus® DuraDBH-672

ports), along with modularity to host an embedded SAASM 
or M-Code military GPS receiver, as well as other Assured-
PNT components like a Chip Scale Atomic Clock (CSAC) 
or Inertial Measurement Unit (IMU)—important capabilities 
for Army vehicles operating in GPS-denied environments. 
In addition to VICTORY switching, an optional processor 
module could support the U.S. Army TARDEC’s libVICTORY 
API and serve as a “VICTORY Shared Processing Unit” if 
needed. 

Results 

Leveraging proven, high-TRL rugged COTS subassemblies 
and multi-generational design experience with VICTORY 
switch architectures, the DuraDBH-672 was deemed the 
best solution to meet the customer’s budgetary, functional, 
and 
product 
maturity 
requirements. 
This 
SWaP-C 

optimized GbE switch LRU will enable the Government to 
roll-out VICTORY infrastructure switching capabilities for 
their new armored vehicle platform to network onboard 
C4ISR equipment and improving situational awareness 
for the warfighter. Complementary to the customer’s 
vision for incrementally adding new electronics equipment 
and technologies onboard the vehicle over time, the 
scalable DuraDBH-672 can potentially consolidate what 
have traditionally been multiple standalone LRUs into a 
single multifunction system solution. Modular VICTORY 
subsystems like this will enable vehicle system architects to 
significantly reduce integration, SWaP and complexity, while 
supporting future capability enhancements. 

GbE

          

ARM Cortex A9
System Processor, 
800 MHz, 4-Core

DRAM 
Memory

NAND 
FLASH

          

Gigabit 
Ethernet Switch

MIPS 
CPU

Network 
Application

          
Power Supply
28V, MIL-STD-1275/704

Mini-PCIe

Mini-PCIe

mSATA SSD

J4

J3

J1

J2

J6

J5

KEY-FILL
(for optional  
internal GPS)

GPS Antenna 
connector (for optional 
internal GPS)

OPTIONAL
To J4 from Processor
30 x Mini-PCIe I/O pins
6 x GPIO
2 x CANbus
2 x USB 2.0

To J3 from Processor
1 x RS-232 (for ext GPS)
1 x RS-232 (console)
1 x GbE

To J2 from Switch
8 x GbE
RS-232 (console)
Zeroize

2x RS-232/422/485
1 x HDMI 
1-PPS (for external GPS)
Audio (optional)

To J3 from Switch
8 x GbE

Nuclear Event 
Detection

GB-GRAM 
GPS

Atomic Clock

Inertial 
Measurement Unit

Removable SSD

Figure 1: DuraDBH-672 
block diagram


