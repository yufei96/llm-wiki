---
title: "NDIA — Constructing Common Fire Control Across Weapon Platforms"
source_url: "https://ndia.dtic.mil/wp-content/uploads/2015/armament/tues17345_Wright.pdf"
downloaded: 2026-05-06
type: raw_text
---

1 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

Constructing Common  

Fire Control  

Across Weapon Platforms 

 
  
 

Presented by  

Michael Wright, Ralph Tillinghast, & 

Ross Arnold  

 

Distribution Statement A: Approved for public release; distribution is unlimited.  

 


2 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

Outline 

• Common Fire Control 

• Programmatic Considerations 

• Software Considerations 

• Hardware Considerations 

• Conclusions 


3 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
Decrease Testing 

•
Decrease Cost 

•
Decrease Development Time 

•
Increase Reliability 

•
Increase Supportability 

•
Increase Interoperability 

•
Reduce Training 

 

 

 

Common Fire Control 


4 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
Current Common Fire Control consists of reuse of 
developed components and software. 

•
Once a new system is developed it is treated as a stand-
alone system. 

 

 

Current State 


5 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014

MFCS-M

LHMBC

MCV 

M777

PEFCS

MFCS-D

PLUMSS 

M119A2

ADIM

AMPS

WULF

Development
Fielding
Post Production Support
End of Life

Current State of Reuse 


6 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

MFCS Software & 

Hardware 

$2.4M/18 mo 

avoided 

Lightweight 

Handheld Mortar 
Ballistic Computer 

Software 

$6M/35 mo avoided  

Pointing 
Devices 

Gunner’s 
 Display 

PDA 
SINCGARS Radio 

Commanders 

Interface 

Driver’s 
 Display 

 Software 

MFCS for STRYKER BCT 

Software 

LW 155 Blk 1a 

Towed Artillery  

Digitization 

$5.5M/36 mo avoided 

DragonFire II/RAMM 

Software 

Pointing Devices 

PDA 
Computer 

Gunner’s 
 Display 

Pointing Devices 

Gunner’s 
 Display 

PDA 
SINCGARS 

 Radio 

Computer 

Software 

ONR/USMC Effort EFSS Demo 

$5.67M/30 mo avoided  

$2.2 M/12 mo avoided 
$2.4M/36 mo avoided 

Portable Excalibur Fire Control System 

$9.59M/36mo avoided 

$6M/31 mo avoided 
6 

Software 

MFCS (H) Heavy 

PDA 
SINCGARS 

Radio Commanders 

Interface 

Pointing Devices 

Driver’s 
 Display 

Gunner’s 
 Display 

Current State SW Reuse 


7 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
Multiple Requirements 

•
Requirement Overlap 

•
Common CPD / KPP 

•
Government Owned vs Contractor Based 

•
Initial Cost 

•
Modular Approach 

 

•
Multiple PMs (with Unique Program-of-Record Timelines) 

•
Multiple School Houses  

•
Services (Army, USMC, Navy, Air Force) 

 

 

Programmatic Considerations 


8 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
Common Backend Architecture 

•
Trunk Based 

•
Modular Components 

•
Meteorological Data (MET) 

•
Fire Support Coordination Measures (FSCM) 

•
Peripheral Interface (PI) 

•
Comm-Network 

•
Geodetic Translation (GeoTrans)  

•
Mapping 

• User Interface / Soldier Machine Interface (UI/SMI) 

 

 

Software Considerations 


9 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
Platform Considerations 

•
Adaptable Source Code 

•
Modular Operating Environment (Net Warrior) 

•
Cloud based consideration 

•
Legacy  

 

 

 

 

Software Considerations (cont) 


10 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
ICD Control - Predefined software to hardware ICD  

•
In order to support multiple hardware components in a 
modular and universal environment a common software ICD 
is required. 

•
ICD Interpreter Components – ICD translators 

•
ICD Interpreters will need to be constructed to adapt the 
common ICD to the specific hardware communication 
standard.  These interpreters would be designed into a cable 
backshell and reside between the system cabling and the 
hardware line replaceable unit. 

 

 

 

Hardware Considerations 


11 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
Flexible / Modular Hardware 

•
Modular based computer 

•
Computer system would be brought down to the lowest common 
denominator 

•
Handheld computer with docking station connectivity would allow one 
computer to work in multiple environments 

•
Cabling standards 

•
Cabling will have to be standardized to a point where the ICD 
Interpreters could adapt signal and power to meet requirements 

•
Ethernet from computer through cables could be easily modified by 
interpreters to old interfaces (RS232, RS485) 

•
Power could be run at 24V and lowered at interpreters.  

 

 

Hardware Considerations (cont) 


12 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

•
Cost viability needs to be fully understood 

•
Long-term Army-wide savings, but heavy initial cost for 
PM/PEO 

•
Current path allows for utilization through attrition 

 

 

 

 

Conclusions 


13 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

Mortar & Common Fire Control Systems Division 
Fire Control Systems & Technology Directorate 
US Army ARDEC, RDAR-WSF-M 

 
Ross Arnold 

 
 
Mission Command Tactical Systems 

 
 
Technical Director 

 
 
973.724.8618 

 
 
ross.d.arnold4.civ@mail.mil  

 
Ralph Tillinghast 

 
 
Collaboration Innovation Lab 

 
 
Lab Director 

 
 
973.724.2095 

 
 
ralph.c.tillinghast.civ@mail.mil  

 
Michael Wright 

 
 
Weaponized Universal Lightweight Fire-Control (WULF)  

 
 
ARDEC Project Officer 

 
 
973.724.8614 

 
 
michael.t.wright88.civ@mail.mil   

 
 
 
 

Questions 


14 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

Constructing Common Fire Control across Weapon Platforms 
Briefing Type: Oral Presentation/Presentation Charts 
Authors: Michael Wright, Ralph Tillinghast, & Ross Arnold 
 
Abstract: 
  

Today’s modern artillery and mortar weapon systems heavily utilize digital Fire Control Systems. These systems increase the 
lethality and survivability of artillery and mortar systems. Across weapon platforms each has emerged with a slightly different fire 
control system, but they all have many overlapping features and requirements.  This overlap provides the potential to develop a 
common fire control system that could serve as a base for future system development for a broad application.  This paper will 
address three key points and challenges in creating a common fire control system, Software Design, Hardware Considerations 
and System Architecture.  Such an approach would produce significant cost and time savings if programmatic challenges can be 
overcome. The paper will describe the current state of common fire control in each of these areas, outline the next steps that 
must be taken, and describe the associated technical and programmatic challenges.  Ultimately, the paper will present a clear 
path from the current state of the art to the future of common fire control across multiple weapon platforms. 

 

Abstract 


15 
NDIA – May 2010  
NDIA 2015 
Distribution Statement A : Unclassified 

References 

• “Launching Artillery and Mortars into the 21st Century with Digital Fire 
Control” R. Arnold (50%) & R. Tillinghast (50%), Proceedings: NDIA Joint 
Armaments Conference, May 2014 [Paper] 
 
• “History of Fire Control and the Application of Implementing 
Technologies” R. Tillinghast, R. (50%) & V. Galgano (50%), Proceedings: 
NDIA Joint Armaments Conference, 2012 [Paper] 
 
•“Technological Advancements In Fire Control for Mortar Weapons”, M. 
Makhijani (50%) & R. Tillinghast (50%), Proceedings: National Fire Control 
Symposium, April 2009. [Paper] 
 
•“Systems Thinking in Fire Control Software Development”, R. Arnold, 
Proceedings: NDIA Joint Armaments Conference, May 2014 [Paper] 
 
•“Establishing Modular Common Fire Control in a Fiscally Constrained 
Environment” R. Tillinghast (40%), M. Wright (40%) & R. Arnold (20%), 
Proceedings: National Fire Control Symposium, 2015 [Paper] 
 
 


