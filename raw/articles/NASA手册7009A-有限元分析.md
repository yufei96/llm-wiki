APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED 

 
METRIC/SI (ENGLISH)

 

 

  
 NASA TECHNICAL HANDBOOK 

 

 

NASA-HDBK-7009A 

Office of the NASA Chief Engineer

Approved: 2019-05-08

Superseding NASA-HDBK-7009

(Baseline)

 
 
 
 
 
 

NASA HANDBOOK FOR MODELS AND SIMULATIONS: 
AN IMPLEMENTATION GUIDE FOR NASA-STD-7009A 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


NASA-HDBK-7009A 

 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED 
 

2 of 157 

DOCUMENT HISTORY LOG 

 

Status
Document 
Revision

Change 
Number

Approval Date
Description

Baseline
2013-10-18
Initial Release

Revision 
A
2019-05-08
Significant changes were made to this 
NASA Technical Handbook. It is 
recommended that it be reviewed in its 
entirety before implementation.  
 
Key changes were: 
   
• Alignment with NASA-STD-7009A. 
• M&S Life Cycle Focused. 
• M&S Life-Cycle Worksheet Revised. 
•
Addresses M&S Risk.

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

3 of 157 

FOREWORD 

 
This NASA Technical Handbook is published by the National Aeronautics and Space 
Administration (NASA) as a guidance document to provide engineering information; lessons 
learned; possible options to address technical issues; classification of similar items, materials, or 
processes; interpretative direction and techniques; and any other type of guidance information 
that may help the Government or its contractors in the design, construction, selection, 
management, support, or operation of systems, products, processes, or services. 
 
This NASA Technical Handbook is approved for use by NASA Headquarters and NASA 
Centers and Facilities. It may also apply to the Jet Propulsion Laboratory (a Federally Funded 
Research and Development Center (FFRDC), other contractors, recipients of grants and 
cooperative agreements, and parties to other agreements only to the extent specified or 
referenced in applicable contracts, grants, or agreements. 
 
This NASA Technical Handbook establishes general guidance to assist in complying with the 
requirements and recommendations of NASA-STD-7009A, Standard for Models and 
Simulations, including technical information, application instructions, data, recommended 
practices, procedures, and methods used in support of NASA-STD-7009A. NASA technical 
standards, by definition and intent, are constrained in their content to include requirements as to 
what is to be accomplished within the scope of their use. This NASA Technical Handbook 
includes suggestions as to methods by which to satisfy those requirements. As modeling and 
simulation span a wide range of technical disciplines, not all methods are similarly applied 
across all types of models and simulations (M&S). 
 
Requests for information should be submitted via “Feedback” at https://standards.nasa.gov. 
Requests for changes to this NASA Technical Handbook should be submitted via MSFC Form 
4657, Change Request for a NASA Engineering Standard. 

 

 

 

 

____Original signed by_______
__________05/08/2019____________

Ralph R. Roe, Jr.
Approval Date

NASA Chief Engineer
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

4 of 157 

 
SECTION 

TABLE OF CONTENTS

 

 

 
PAGE 

DOCUMENT HISTORY LOG.........................................................................................
2

FOREWORD......................................................................................................................
3

TABLE OF CONTENTS...................................................................................................
4

LIST OF APPENDICES ...................................................................................................
6

LIST OF FIGURES ...........................................................................................................
7

LIST OF TABLES .............................................................................................................
8

1.
SCOPE.................................................................................................................
9

1.1
Purpose .................................................................................................................
9

1.2
Applicability .........................................................................................................
9

2.
APPLICABLE DOCUMENTS .........................................................................
11

2.1
General..................................................................................................................
11

2.2
Government Documents.......................................................................................
11

2.3
Non-Government Documents...............................................................................
13

2.4
Order of Precedence .............................................................................................
14

3.
ACRONYMS, ABBREVIATIONS, SYMBOLS, AND DEFINITIONS .......
14

3.1
Acronyms, Abbreviations, and Symbols ..............................................................
14

3.2
Definitions ............................................................................................................
16

4.
INTRODUCTION ..............................................................................................
23

4.1
Background ..........................................................................................................
24

4.2
Applicability .........................................................................................................
26

4.3
Interpreting and Tailoring.....................................................................................
26

4.4
Compliance with NASA-STD-7009A..................................................................
27

4.5
Models – Key Concept .........................................................................................
28

4.5.1
Pedigree and Provenance in Models and Simulations..........................................
29

4.5.2
Model of Models...................................................................................................
29

4.5.3
NASA’s Motivation to Model ..............................................................................
30

4.6
The Modeling (and Simulation) Process/Life Cycle ............................................
31

4.7
Relation to NPR 7150.2........................................................................................
35

4.8
Program/Project Management and Delegated Technical Authority
Responsibilities .....................................................................................................  
 38 

5.
M&S LIFE-CYCLE PROCESSES...................................................................
40

5.1
Model Initiation (Pre-Phase A).............................................................................
40

5.1.1
Accomplishing the Model Initiation Phase ..........................................................
40

5.1.1.1
Gathering RWS Information.................................................................................
41


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

5 of 157 

SECTION 

TABLE OF CONTENTS, continued

 

 

 
      PAGE 

5.1.1.2
M&S Statement of Intended Use..........................................................................
41

5.1.1.3
Performing the CriticalityAssessment ..................................................................
42

5.1.1.4
Justifying the M&S Approach..............................................................................
43

5.1.1.5
Empirical Data Availability/Assessment..............................................................
45

5.1.2
Products and Expected Outcomes of the Model Initiation Phase.........................
45

5.2
Model Concept Development (Phase A)..............................................................
45

5.2.1
Accomplishing the Model Concept Development Phase .....................................
46

5.2.1.1
Real World System/Environment Specification and Data Acquisition................
46

5.2.1.2
Model Concept Trade Studies and Selection........................................................
49

5.2.1.3
Preliminary Model Requirements and Specifications ..........................................
50

5.2.2
Products and Expected Outcomes of the Concept Development Phase...............
53

5.3 
Model Design (Phase B).......................................................................................
54

5.3.1
Accomplishing Model Design ..............................................................................
55

5.3.2
Considerations in Model Design ..........................................................................
57

5.3.3
Model Concept (Design) Validation.....................................................................
58

5.3.4
Products and Expected Outcomes of the Model Design Phase............................
58

5.4
Model Construction (Phase C)..............................................................................
59

5.4.1
Accomplishing Model Construction.....................................................................
59

5.4.2
Considerations in Model Construction.................................................................
61

5.4.3
Products and Expected Outcomes of the Model Construction Phase...................
61

5.5
Model Testing and Release (Phase D)..................................................................
61

5.5.1
Activity Precedence for Model Testing and Release............................................
62

5.5.2
Model Verification (What is Verification?) .........................................................
64

5.5.2.1
Accomplishing Model Verification (What is Done in Verification?) ..................
64

5.5.2.2
Considerations in Model Verification (What is Considered During 
Verification?)........................................................................................................
65

5.5.2.3
Products and Expected Outcomes of Model Verification ....................................
66

5.5.3
Model Empirical Validation .................................................................................
66

5.5.3.1
Accomplishing Model Empirical Validation........................................................
67

5.5.3.2
Considerations in Model Empirical Validation....................................................
69

5.5.3.3
Products and Expected Outcomes of Model (Empirical) Validation ...................
75

5.5.4
Model Release ......................................................................................................
76

5.5.4.1
Accomplishing Model Release.............................................................................
76

5.5.4.2
Considerations in Model Release .........................................................................
76

5.5.4.3
Products and Expected Outcomes of Model Release ...........................................
76

5.6
Model Use (Phase E) ............................................................................................
77

5.6.1
Model Pre-Use......................................................................................................
77

5.6.1.1
Readiness for Use .................................................................................................
77

5.6.1.2
Use Assessment ....................................................................................................
78


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

6 of 157 

SECTION 

TABLE OF CONTENTS, continued

 

 

 
      PAGE 

5.6.1.3
Input Scenario Definition and Pedigree................................................................
79

5.6.2
Model Use (Setup and Execution)........................................................................
82

5.6.2.1
Model Setup..........................................................................................................
82

5.6.2.2
Model Execution (Application)............................................................................
83

5.6.2.3
Sensitivity Studies ................................................................................................
84

5.6.3
Model Post-Use ....................................................................................................
84

5.6.3.1
Analyze Data ........................................................................................................
85

5.6.3.2
Assessing and Reporting Results..........................................................................
93

5.6.4
Products and Expected Outcomes of the Model Use Phase .................................
97

5.7
Model and Analysis Archiving (Phase F).............................................................
98

6.
WORKSHEET....................................................................................................
99

6.1
Header
...............................................................................................................
100

6.2
M&S Planning Section .........................................................................................
102

6.3
M&S Development Section..................................................................................
103

6.4
M&S Use Section .................................................................................................
105

 

LIST OF APPENDICES

APPENDIX
PAGE

A
Requirements and Recommendations Per Life-Cycle Phase................................
107

B
Quality of Referent Data Used in Empirical Validation.......................................
124

C
M&S User’s Guide Outline ..................................................................................
128

D
Assessing and Influencing M&S Results Credibility..........................................
132

E
M&S Risk Assessment .........................................................................................
146

F
References.............................................................................................................
154

G
Technical Working Group....................................................................................
157

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

7 of 157 

FIGURE 

LIST OF FIGURES

 

 

 
PAGE 

1 
M&S Life Cycle in an RWS Life Cycle ...........................................................
33

2
Overall Representative System Expanded Diagram (SLS example)................
47

3
Distinguishing the RWS and its Environment..................................................
47

4
Conceptual Model Example (Free Body Diagram) ..........................................
48

5
General Model Diagram with Nondeterministic Elements...............................
53

6
General Flowchart for M&S Development.......................................................
63

7
Domain of Validation........................................................................................
68

8
Empirical Validation Process, Including Correlation and Calibration .............
69

9
RWS to Referent Similarity..............................................................................
71

10
Simple Comparison of Uncertainty Bounds Between M&S and Referent.......
72

11
Comparison of Uncertainty Bounds Between M&S and Referent over Range
of Input Values..................................................................................................
73

12
ISS Power Prediction ........................................................................................
75

13
Example Placard ...............................................................................................
85

14
Sources of Model Uncertainty ..........................................................................
88

15
Worksheet Header.............................................................................................
101

16
Worksheet Example of All Columns ................................................................
102

17
Credibility Assessment Synopsis......................................................................
134

18
NASA RIDM Process .......................................................................................
149

19
NASA CRM Process.........................................................................................
149

 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

8 of 157 

 
 
TABLE 

LIST OF TABLES 
 

 

 
 
PAGE 

1
Program/Project and M&S Life Cycles................................................................
32

2
M&S Life-Cycle Phase Descriptions ...................................................................
34

3
Classes of NASA Software...................................................................................
36

4
Program/Project Management and Delegated Technical Authority 
Responsibilities.....................................................................................................
39

5
Alternative Method Assessment Factors ..............................................................
43

6
M&S Use Assessment ..........................................................................................
79

7
Model Setup Definition Options...........................................................................
83

8
Potential Caveats to M&S Results........................................................................
85

9
Uncertainty Characterization Synopsis ...............................................................
86

10
Uncertainty in M&S Results.................................................................................
89

11
Technical Review Synopsis..................................................................................
93

12
People Qualifications Synopsis ............................................................................
93

13
Documentation Synopsis ......................................................................................
94

14
M&S Risk Elements .............................................................................................
96

15
M&S Reporting Synopsis.....................................................................................
97

16
Example Archival Products in the M&S Life Cycle ............................................
99

17
Worksheet Organization.......................................................................................
100

18
Worksheet – M&S Planning.................................................................................
102

19
Worksheet – M&S Development .........................................................................
104

20
Worksheet – M&S Use.........................................................................................
105

21
R/r M&S Life-Cycle Phase Designations.............................................................
108

22
R/r per M&S Life-Cycle Phase ............................................................................
109

23
M&S versus Referent Data/Results Relationship.................................................
127

24
M&S Life-Cycle Phase Affects M&S Results Credibility Factors ......................
133

25
Data Pedigree Credibility Achievement...............................................................
136

26
Life-Cycle Phase Influence on Data Pedigree......................................................
137

27
Life-Cycle Phase Influence on Verification .........................................................
138

28
Life-Cycle Phase Influence on Validation............................................................
139

29
Life-Cycle Phase Influence on Input Pedigree.....................................................
140

30
Sample Table for the Uncertainties of a Process..................................................
142

31
Life-Cycle Phase Influence on Uncertainty Characterization ..............................
142

32
Life-Cycle Phase Influence on Results Robustness .............................................
143

33
Life-Cycle Phase Influence on M&S History.......................................................
144

34
Life-Cycle Phase Influence on M&S Product/Process Management...................
145

35
Risk-Related Topics in NASA-STD-7009A ........................................................
147

36
Examples of Possible Risks throughout the M&S Life Cycle..............................
148

37
Detailed M&S Risk Elements...............................................................................
151

 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

9 of 157 

NASA HANDBOOK FOR MODELS AND SIMULATIONS: 

AN IMPLEMENTATION GUIDE FOR NASA-STD-7009A 

 
1. 
SCOPE 

 
1.1 
Purpose 

 
The purpose of this NASA Technical Handbook is to provide technical information, clarification, 
examples, processes, and techniques to help institute good modeling and simulation practices in 
the National Aeronautics and Space Administration (NASA).  As a companion guide to NASA-
STD-7009A, Standard for Models and Simulations, this NASA Technical Handbook provides a 
broader scope of information than is included in a NASA technical standard and promotes good 
practices in the production, use, and consumption of NASA modeling and simulation products. 
NASA-STD-7009A specifies what a modeling and simulation activity shall or should do (in the 
requirements and recommendations), but does not prescribe how they are accomplished, which 
varies with the specific engineering discipline, or who is responsible for accomplishing them, 
which depends on the size and type of project.  A guidance document, which is not constrained 
by the requirements of a NASA technical standard, is better suited to address these additional 
aspects and provide necessary clarification.  
 
This NASA Technical Handbook stems from the Space Shuttle Columbia Accident Investigation 
(2003), which called for Agency-wide improvements in the “development, documentation, and 
operation of models and simulations”1 that subsequently elicited additional guidance from the 
NASA Office of the Chief Engineer to include “a standard method to assess the credibility of the 
models and simulations.”2  General methods applicable across the broad spectrum of model and 
simulation (M&S) disciplines were sought to help guide the modeling and simulation processes 
within NASA and to provide for consistent reporting of M&S activities and analysis results.  
From this, the life cycle for M&S development and use was developed.  
 
The major contents of this NASA Technical Handbook are the implementation details of the 
general M&S requirements of NASA-STD-7009A, including explanations, examples, and 
suggestions for improving M&S credibility throughout the M&S life cycle.   
 
1.2 
Applicability 

 
This NASA Technical Handbook is applicable to a broad audience, ranging from the variety of 
M&S practitioners (developers, users, and analysts, for example) and consumers of M&S-based 
products and analyses to technical reviewers of M&S activities and analyses.   
 

                                                 
1A Renewed Commitment to Excellence: An Assessment of the NASA Agency-Wide Applicability of the Columbia 
Accident Investigation Board Report.  B2005-100968, January 30, 2004. Retrieved April 22, 2013. 
http://www.nasa.gov/pdf/55691main_Diaz_020204.pdf. 

2 NASA Office of the Chief Engineer (September 1, 2006).  Guidance in the Development of NASA-STD-7009. 
(Memo) 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

10 of 157 

NASA-STD-7009A and this NASA Technical Handbook are intended for use by M&S 
practitioners, technical reviewers, decision makers, and others in the organization implementing, 
reviewing, using, or receiving the results from an M&S-based analysis.  Further, as NASA-STD-
7009A is primarily focused toward the results of an M&S-based analysis, which may be used by 
a variety of people, both internal and external to a given implementing organization, this NASA 
Technical Handbook may be used by anyone, as in the following examples:  
 

a. In receiving a presentation of an M&S-based analysis, a decision maker may use the 
Worksheet (section 6) as a guide to a more complete understanding of the analysis. 

 
b. In substantiating an M&S product or analysis, a peer review team may use the 
Worksheet and NASA Technical Handbook to structure the results of a technical review. 

 
c. In conducting an analysis with an existing M&S, a user/analyst may use the 
Worksheet and NASA Technical Handbook as a guide to covering basic M&S topics, which may 
be addressed during a future technical review or presentation for decision making. 

 
d. During the course of an M&S activity, an M&S development team may use the 
NASA Technical Handbook to ensure meeting the minimal expectations of a product used for 
critical analysis. 

 

Anyone may use NASA-STD-7009A or this NASA Technical Handbook in the course of their 
modeling and simulation activities; however, the use is highly recommended for M&S that meet 
established risk criteria determined by program/project management in collaboration with the 
NASA delegated Technical Authority as outlined in Appendix D of NASA-STD-7009A. The 
application of many different types of M&S is possible in the creation of an analytical tool. 
While the elucidation of those types may be instructive, it is also most likely to be incomplete; 
therefore, the types of possible M&S are not included here, but are discussed briefly in section 
4.1 of this NASA Technical Handbook. 
 
NASA-STD-7009A applies to any point in the program/project life cycle to which an M&S-
based analysis may be applied. However, the expectations on the quality of the M&S products 
and analysis credibility will vary (most likely, improve) as the program/project matures. For 
example, the results from an M&S-based analysis in predicting the behavior of a Real World 
System (RWS) will likely be less precise and less accurate in the conceptual phase of a project 
than after several years of operations.  A listing of the NASA program/project management 
phases is given in section 4.6 of this NASA Technical Handbook. 
 
NASA-STD-7009A also applies to any size M&S activity if the criticality of the analysis, based 
on the influence of the M&S to the decision and the decision consequence, warrants its 
application. 
 
This NASA Technical Handbook is approved for use by NASA Headquarters and NASA Centers 
and Facilities. It may also apply to the Jet Propulsion Laboratory (a Federally Funded Research and 
Development Center (FFRDC)), other contractors, recipients of grants and cooperative agreements, 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

11 of 157 

and parties to other agreements, only to the extent specified or referenced in their applicable 
contracts, grants, or agreements. 
 
This NASA Technical Handbook, or portions thereof, may be referenced in contract, program, 
and other Agency documents for guidance. 
 
2. 
APPLICABLE DOCUMENTS 

 
2.1 
General 

 
The documents listed in this section are applicable to the guidance in this NASA Technical 
Handbook. 
 
2.1.1 The latest issuances of cited documents may apply unless specific versions are 
designated. 
 
2.1.2 Non-use of a specifically designated version is approved by the delegated Technical 
Authority. 
 
Applicable documents may be accessed at https://standards.nasa.gov or obtained directly from 
the Standards Developing Body or other document distributors. When not available from these 
sources, information for obtaining the document is provided.  
 
2.2 
Government Documents 

 
 
Office of Management and Budget (OMB) 

 

OMB Circular A-119
Federal Participation in the Development and Use of Voluntary 
Consensus Standards and in Conformity Assessment Activities

 
 

 
NASA 

 

NPD 1000.0
NASA Governance and Strategic Management Handbook

NPR 7120.5
NASA Space Flight Program and Project Management 
Requirements 

NPR 7150.2
NASA Software Engineering Requirements

NPR 8000.4
Agency Risk Management Procedural Requirements

NPR 8715.3 
NASA General Safety Program Requirements

NASA-STD-7009A
Standard for Models and Simulations


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

12 of 157 

NASA/SP-2016-6105 
Rev 2 

NASA Systems Engineering Handbook
 

NASA/SP-2010-576
NASA Risk-Informed Decision Making Handbook

NASA/SP-2011-3422
NASA Risk Management Handbook

NASA/SP-2009-569
Bayesian Inference for NASA Probabilistic Risk and Reliability 
Analysis 

Aerospace Safety Advisory Panel Annual Report for 2008

Aerospace Safety Advisory Panel Annual Report for 2009

Expanded Guidance for NASA Systems Engineering Volume 
1:  Systems Engineering Practices - March, 2016. 

Expanded Guidance for NASA Systems Engineering Volume 
2:  Crosscutting Topics, Special Topics, and Appendices – March 
2016. 

A Renewed Commitment to Excellence: An Assessment of the 
NASA Agency-Wide Applicability of the Columbia Accident 
Investigation Board Report.  B2005-100968, January 30, 2004. 
Retrieved April 22, 2013. 
http://www.nasa.gov/pdf/55691main_Diaz_020204.pdf

NASA TM-2002-
211715, IECEC-2002-
20113

"Comparison of ISS Power System Telemetry with Analytically 
Derived Data for Shadowed Cases", Fincannon, H. James 

 
 
Department of Defense (DoD) 

 

DoD Modeling and Simulation (M&S) Glossary. Retrieved May 8, 
2018.  
https://www.msco.mil/MSReferences/Glossary/MSGlossary.aspx

Conceptual Model Development and Validation, VV&A 
Recommended Practice Guide special topic, May 18, 2011.  
Retrieved Feb 21, 2018. 
https://vva.msco.mil/default.htm?Special_Topics/Conceptual/defaul
t.htm

MIL-STD-3022
Standard Practice Documentation of Verification, Validation, and 
Accreditation (VV&A) for Models and Simulations

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

13 of 157 

 
Environmental Protection Agency (EPA) 

 

EPA/100/K-09/003
Guidance on the Development, Evaluation, and Application of 
Environmental Models 

 
 
Sandia National Laboratories 

 

SAND2003-3769
Oberkampf, W.; Trucano, T.; and Hirsch, C. (February 2003). 
“Verification, Validation, and Predictive Capability in 
Computational Engineering and Physics.” 

SAND2002–0341
Trucano, T. G., M. Pilch, and W. L. Oberkampf (2002). General 
Concepts for Experimental Validation of ASCI Code Applications.

 
 
United States Nuclear Regulatory Commission  

 

NUREG/CR-5074
Shaw, R. A., Larson, T. K., and Dimenna, R. K. (August 1988). 
Development of a Phenomena Identification and Ranking Table 
(PIRT) for Thermal-Hydraulic Phenomena during a PWR 
LBLOCA, EG&G, Idaho Falls, ID, Inc.

 
2.3 
Non-Government Documents   

 
 
American Society of Mechanical Engineers (ASME) 

 

ASME V&V 10
Guide for Verification and Validation in Computational Solid 
Mechanics 

ASME V&V 20
Standard for Verification and Validation in Computational Fluid 
Dynamics and Heat Transfer 

ASME V&V 40
V&V for Computational. Modeling for Medical Devices

 
 
Institute of Electrical and Electronics Engineers (IEEE) 

 

IEEE 1597.1
IEEE Standard for Validation of Computational Electromagnetics 
Computer Modeling and Simulations

 
 
The Aerospace Corporation 

 

TOR-2010(8591)-17
Baxter, Michael J. (2010). Guidance for Space Program Modeling 
and Simulation.

 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

14 of 157 

Other 

 

Banks, J., ed. (1998).  Handbook of Simulation.  New York: John 
Wiley & Sons. 

Kelton, W.D.; Sadowski, R.P.; and Sturrock, D.T.  (2004). 
Simulation with Arena, Third Edition. New York:  McGraw-Hill.

Oberkampf, W.L.; Roy, C.J. (2010). Verification and Validation in 
Scientific Computing. Cambridge, England: Cambridge University 
Press, Cambridge.  

Oberkampf, W.L.; Deland, S.M.; Rutherford, B.M.; Diegert, K.V.; 
and Alvin, K.F.  (March 2002). “Error and Uncertainty in Modeling 
and Simulation.” Reliability Engineering and System Safety, Vol. 
75, Issue 3, pp. 333-357. 

Telford, Jacqueline K. (2013).  A Brief Introduction to Design of 
Experiments.  Johns Hopkins APL Technical Digest. 
http://www.jhuapl.edu/techdigest/TD/td2703/telford.pdf 

The American Heritage Dictionary of the English Language, 4th ed. 
(2006).  Boston: Houghton Mifflin Co. 

Yang, W.Y.; Cao, W.; Chung, T.-S.; and Morris, J. (2005). Applied 
Numerical Methods Using MATLAB®. Hoboken: John Wiley & 
Sons, Inc.

 
2.4 
Order of Precedence 

 
2.4.1 This NASA Technical Handbook provides guidance for promoting good practices in the 
production, use, and consumption of modeling and simulation products but does not supersede or 
waive existing guidance found in other Agency documentation. 
 
2.4.2 Conflicts between this NASA Technical Handbook and other documents are resolved by 
the delegated Technical Authority. 
 
3. 
ACRONYMS, ABBREVIATIONS, SYMBOLS, AND DEFINITIONS 

 
3.1 
Acronyms, Abbreviations, and Symbols 

 

%
percent

®
registered trademark

AHS
The American Helicopter Society International

AIAA
American Institute of Aeronautics and Astronautics

ANSI
American National Standards Institute


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

15 of 157 

ASAP
Aerospace Safety Advisory Panel 

ASC
American Standards Committee

ASCE
American Society of Civil Engineers

ASME
American Society of Mechanical Engineers

CA
California

CAD
Computer-Aided Design

CAE
ComputerAided Engineering

CAM
Computer-Aided Manufacturing

CM
configuration management

COTS
commercial off the shelf

CRM
continuous risk management

DoD
Department of Defense

DOF
degree of freedom

EPA
Environmental Protection Agency

FEM
finite element model

FEMCI
Finite Element Modeling Continuous Improvement

FFRDC
Federally Funded Research and Development Center

GNC
Guidance, Navigation, & Control

GOTS
government off the shelf

GSFC
Goddard Space Flight Center

GUI
Graphical User Interface

HI
Hawaii

I&T
Integration and Test

I/O
Input/Output

IEC
International Electrotechnical Commission

IEEE
Institute of Electrical and Electronics Engineers

ISO
International Organization for Standardization

ISS
International Space Station

JPL
Jet Propulsion Laboratory

JWST 
James Webb Space Telescope

KSC
Kennedy Space Center

M&S
Models and Simulations (See usage note in section 4 of 
this NASA Technical Handbook.)

M&SCO
Modeling and Simulation Coordination Office

MIL
Military

MOS
Margin of Safety

MOTS
modified off the shelf

MSFC
Marshall Space Flight Center

MSL
Mars Science Laboratory

MUF
Model Uncertainty Factor

NASA
National Aeronautics and Space Administration

NASTRAN
NASA structural analysis system

NCSL
National Conference of Standards Laboratories

NESC
NASA Engineering and Safety Center

NIST
National Institute of Standards and Technology

NM
New Mexico


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

16 of 157 

NPD
NASA Policy Directive

NPR
NASA Procedural Requirements

ODE
ordinary differential equatio

OMB
Office of Management and Budget

PDE
partial differential equation

pdf
probability density function

PIRT
Phenomena Identification and Ranking Table 

PLD
Programmable Logic Devices

R/r
Requirements or recommendations

Req’t
Requirement

RIDM
risk informed decision making

RWS
Real World System

S/W
Software

SI
System Internationale

SME
Subject Matter Expert

SP
Special Publication

SPIE
The International Society for Optical Engineering

SRQ
System Response Quantities

STD
Standard

SWE
Software Engineering

V&V
Verification and Validation

VCS
Voluntary Consensus Standards

VV&A
Verification, Validation, and Accreditation

w.r.t.
with respect to

 
3.2 
Definitions 

 
The definitions listed below are those used in this document and are in the context of models and 
simulations (M&S) unless otherwise stated.  Wherever possible, these definitions were taken or 
adapted from official NASA documents.  In some cases, after reviewing definitions of interest in 
the International Organization for Standardization (ISO), the Department of Defense (DoD) 
Modeling and Simulation Coordination Office (M&SCO), professional society publications (e.g., 
AIAA, ASME, IEEE), and English language dictionaries, some definitions were taken or adapted 
from relevant sources to achieve the goal or objectives.  Some definitions may have alternate 
meanings in other documents and disciplines. 
 

Abstraction:  The process of simplifying, focusing, or transforming aspects of an RWS (or 

referent system) represented in an M&S.  (Note:  Simplifying includes selecting aspects of the 
RWS to reduce in complexity in, or exclude from, the model.  Focusing includes either 
emphasizing or deemphasizing certain aspects of the RWS when including them in the model.  
Transforming includes any change in the appearance, character, composition, configuration, 
expression, or structure of aspects of the RWS (when including them) in the model (e.g., 
Rotation, Translation, Mapping, Scaling, Mathematics).  Any modeling abstraction carries with it 
the assumption that it does not significantly affect the intended uses of the M&S.)


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

17 of 157 

Accepted Use:  The successful outcome of a use assessment designating the M&S is 

sufficient for a proposed use.

Accuracy:  The closeness of a parameter or variable (or a set of parameters or variables) 

within a model, simulation, or experiment to the true value or the assumed true value.

Actual Use:  The specific purpose and domain of application for which an M&S is being, 

or was, used.

Aleatory Uncertainty: The inherent variation in the physical system; it is stochastic and 

irreducible without changes to the system or how it operates.

Analysis: The examination of a situation or problem in order to understand the item in 

question and make appropriate recommendations.  (Note:  Analysis spans the whole extent of the 
M&S process from the study of the RWS or its referents, the gathering and reduction of data from 
the RWS or accepted referents for incorporation into a model, the development of simulation 
scenarios, and the study and reduction of data from use of the M&S into recommendations for the 
RWS.) 

Architecture:  The essential elements of any system and their interrelationships, functions, 

and behaviors, including the influences of the environment and other (interfacing) systems.

Architectural Diagram: Any one of the possible visual (graphical) representations 

(viewpoints) depicting select aspects (features) of a system.  (See definition of Architecture.)

Assumption:  Asserting information as a basis for reasoning about a system. (Note: In 

modeling and simulation, assumptions are taken to simplify or focus certain aspects of a model 
with respect to the RWS or presume values for certain parameters in a model.)

Calibration: The process of adjusting numerical or modeling parameters in the model to 

improve agreement with a referent. (Note: Calibration can also be known as “tuning.”)

Caveat: “An explanation to prevent misinterpretation, or a modifying or cautionary detail 

to be considered when evaluating, interpreting, or doing something.” (http://www.merriam-
webster.com/dictionary/caveat) 

Computational Model: The operational or usable implementation of the conceptual 

model, including all mathematical, numerical, logical, and qualitative representations.  This may 
also be known as “simulation model.”

Conceptual Model: The collection of abstractions, assumptions, and descriptions of 

physical components and processes representing the reality of interest, which includes the RWS, 
its environment, and their relevant behaviors.  (Note:  The conceptual model provides the source 
information for conceptual validation with respect to the RWS, model construction, and model 
verification.  It may consist of flow charts, schematic drawings, written descriptions, math 
models, etc., that explain the RWS and its interaction with the surrounding/interfacing 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

18 of 157 

environment.  The conceptual model should be independent of any specific model 
implementation.)

Conceptual Validation:  The process of determining the degree to which a conceptual 

model (as defined in this NASA Technical Handbook) or model design adequately represents the 
real world from the perspective of the intended uses of the model or the simulation.

Configuration Management (CM): A management discipline applied over the product's 

life cycle to provide visibility into and to control changes to performance and to functional and 
physical characteristics.  (Note:  NPR 7120.5, NASA Space Flight Program and Project 
Management Requirements.)

Correlated (as in an M&S correlated with an RWS):  The extent to which an M&S and 

RWS, or some aspect of an M&S and RWS, behave similarly due to a particular change in some 
set of input variables, parameters, perturbations, etc.

Credibility: “The quality to elicit belief or trust in M&S results.” (NASA-STD-7009A.)

Critical Decision:  The selection of a course-of-action related to design, development, 

manufacturing, ground, or flight operations that may significantly impact human safety, mission 
success, or program success, as measured by program/project-defined criteria.

Data Pedigree:  A record of traceability from the data's source through all aspects of its 

transmission, storage, and processing to its final form used in the development of an M&S.  
(Note:  Any changes from the real-world source data may be of significance to its pedigree.  
Ideally, this record includes important quality characteristics of the data at every stage of the 
process.)

Design of Experiments (or Experimental Design): A series of tests in which purposeful 

changes are made to the input variables of a system or process and the effects on response 
variables are measured. (Note:  It is applicable to both physical processes and computer 
simulation models.3)

Deterministic: A term describing a system whose time evolution can be predicted exactly.

(Note: For comparison, see definition of “Probabilistic.”)

Domain of Validation:  The region enclosing all sets of model inputs for which the 

M&S’s responses compare favorably with the referent.

Domain of Verification:  The region enclosing all sets of model inputs for which the 

solution is determined to be correct and satisfy requirements for computational accuracy.

                                                 
3 This definition is largely a direct quote from A Brief Introduction to Design of Experiments, by Jacqueline K. 
Telford.  Retrieved April 22, 2013. http://www.jhuapl.edu/techdigest/TD/td2703/telford.pdf. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

19 of 157 

Empirical Validation:  The process of determining the degree to which an operating 

model or simulation is or provides an accurate representation of the real world from the 
perspective of the intended uses of the model or the simulation.

Environment of the System (or RWS): The set of elements external to a system. The 

RWS and its environment may interact through the exchange of properties.  (Note:  Only the 
interactions relevant to an analysis should be included in the M&S.)

Epistemic Uncertainty: A lack of knowledge of the quantities or processes identified with 

the system; it is subjective, is reducible, and comprises both model and parameter uncertainty.

Expanded Diagram: An illustration or diagram of a construction showing its parts 

separately but in positions that indicate their proper relationships to the whole.

Framework: A set of assumptions, concepts, values, and practices constituting a way of 

viewing reality.  (Note:  For M&S, this may be a computing environment that integrates multiple 
interacting components on a single computer or across a distributed network.4)

Human Safety:  The condition of being protected from death, permanently disabling 

injury, severe injury, and several occupational illnesses.  In the NASA context, this refers to 
safety of the public, astronauts, pilots, and the NASA workforce.  (Note:  Adapted from NPR 
8000.4 and the NASA Safety Hierarchy.)

Input Pedigree: A record of the traceability from the input data’s source through all 

aspects of its transmission, storage, and processing to its final form when using an M&S.  (Note:  
Any changes from the real-world source data may be of significance to its pedigree.  Ideally, this 
record includes important quality characteristics of the data at every stage of the process.)

Intended Use:  The expected purpose and application of an M&S.

Kriging:  An interpolation technique in which the surrounding measured values are 

weighted to derive a predicted value for an unmeasured location.  Weights are based on the 
distance between the measured points, the prediction locations, and the overall spatial 
arrangement among the measured points.5

Limits of Operation: The boundary of the set of parameters for an M&S, based on the 

outcomes of verification, validation, and uncertainty quantification, beyond which the accuracy, 
precision, and uncertainty of the results are indeterminate. (Note: NASA-STD-7009A.)

M&S Risk:  The potential for shortfalls with respect to sufficiently representing an RWS.

                                                 
4 A modification from http://www.answers.com/topic/framework#ixzz1CL7UTZYb. Retrieved April 22, 2013. 
5 http://support.esri.com/en/knowledgebase/GISDictionary/term/kriging. Retrieved April 22, 2013. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

20 of 157 

Margin:  The allowances carried in budget, projected schedules, and technical 

performance parameters (e.g., weight, power, or memory) to account for uncertainties and risks.  
(Note: NASA-SP-2016-6105, NASA Systems Engineering Handbook.)

Mathematical Model: The mathematical equations, boundary values, initial conditions, 

and modeling data needed to describe the conceptual model.  (Note:  Adapted from ASME V&V 
10, Guide for Verification and Validation in Computational Solid Mechanics.)

Mission Success Criteria:  Specifications against which the program or project will be 

deemed to have achieved operational objectives.

Model:  A description or representation of a system, entity, phenomena, or process.6

(Note:  A model may be constructed from multiple sub-models; the sub-models and the 
integrated sub-models are all considered models.  Likewise, any data that go into a model are 
considered part of the model.)

Model Capability:  The potential or ability (of a model) to represent an RWS, entity, 

phenomenon, or process.

Model Uncertainty:  Variation in M&S results due to assumptions, formulas, and 

representations, and not due to factors inherent in the RWS.

Model Uncertainty Factor (MUF):  A semi-quantitative (i.e., a quantitative magnitude 

based on past experience rather than data) adjustment, either additive or multiplicative or both, 
made to the results of an M&S-based analysis to account for uncertainty.  (Note:  The MUF is 
also likely to have some associated confidence or coverage range.)

Modeling:  (a) The act of creating a system representation (i.e., the act of creating a 

model); (b) The act of utilizing a system representation (i.e., utilizing a model) as an approach for 
analyses.

Numerical Errors: Errors traceable to various sources, including but not limited to 

floating point precision, inherent in all computer systems and leading to round off, underflow, 
and overflow; truncation of infinite series expansions; and approximations of exact solutions 
inherent in all numerical methods, e.g., approximation of derivatives and integrals by algebraic 
operations on sampled continuous functions.7

Peer Review: A technical assessment conducted by one or more persons of equal 

technical standing to person(s) responsible for the work being reviewed.

Permissible Use:  The purposes for which an M&S is formally allowed.

                                                 
6 Adapted from Banks, J., ed. (1998). Handbook of Simulation. New York: John Wiley & Sons. 
7 Yang, W.Y.; Cao, W.; Chung, T.-S.; and Morris, J. (2005). Applied Numerical Methods Using MATLAB®. 
Hoboken:  John Wiley & Sons, Inc. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

21 of 157 

Probabilistic: Pertaining to non-deterministic events, the outcome of which is described 

by a measure of likelihood.8

Proposed Use:  A desired specific application of an M&S.

Real World System: The reality of interest the model is representing, which may include 

relevant operating conditions or aspects of its environment.  (Note:  The RWS may interact with 
its environment, i.e. a set of relevant elements external to the RWS, through the exchange of 
properties.  The term RWS is used to differentiate between the “system represented” and the 
“modeling system” used for the analysis.)

Recommended Practices: Guidelines developed by professional societies, best practices 

documented for specific simulation codes, and NASA Handbooks and Guidebooks.

Referent: Data, information, knowledge, or theory against which simulation results can 

be compared.  (NASA-STD-7009A; adapted from ASME V&V 10, Guide for Verification and 
Validation in Computational Solid Mechanics.)  (Note:  A referent may be the RWS to which the 
analysis is directed, or it could be a similar or analogous system, whereby the closeness of the 
referent to the RWS becomes pertinent, or a higher fidelity model.)

Regression Testing: Selective checking of the quality, performance, or reliability of an 

M&S system or component to verify that modifications have not caused unintended effects and 
that the M&S still complies with its requirements.  (Note:  Adapted from ISO/IEC/IEEE 
24765:2010 Systems and software engineering—Vocabulary.  This term is in no way related to 
statistical regression analysis.)

Responsible Party:  The group or individual identified as accountable for complying with 

requirements in NASA-STD-7009A.  (Note:  Different parties may be identified for the various 
requirements.)

Results Robustness:  The characteristic whereby the behavior of (result from) an M&S 

does not change in a meaningful way in response to as-designed control variations in parameters.  
(Note:  The results from an M&S are robust if they are relatively stable (do not change in a 
meaningful way) with respect to as-designed changes in the control parameters or input variables 
of the M&S.  Key sensitivities are parameters and variables shown to produce large changes in 
results with relatively small perturbations to input.)

Risk: The potential for shortfalls with respect to achieving explicitly established and 

stated objectives.  (Note:  This definition has been updated from the definition found in NASA-
STD-7009A, to the recently revised definition found in NPR 8000.4B, 12/06/2017.)

Scenario: The description or definition of the relevant system and environmental 

assumptions, conditions, or parameters used to drive the course of events during the run of a 
simulation model. (Note: The scenario may include, but is not limited to the set of initial 

                                                 
8 NASA/SP-2009-569, Bayesian Inference for NASA Probabilistic Risk and Reliability Analysis 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

22 of 157 

conditions, a set of assumptions, the values of relevant parameters [including system and 
environmental conditions, locations and quantities of objects, entities, or resources], or a 
sequence of actions, which may be specified in the model itself.  Running the model with the 
given scenario is the simulation.)

Sensitivity Analysis: The study of how variation in the output of an M&S can be 

apportioned to different sources of variation in the model input and parameters.  (Note:  The 
Results Robustness of an M&S-based analysis is obtained via sensitivity analysis (NASA-STD-
7009A, adapted from Saltelli, 2005).)

Simulation: The imitation of the behavioral characteristics of a system, entity, 

phenomena, or process.

Stochastic: Involving or containing a random variable or variables. Pertaining to chance 

or probability. (Note: http://mathworld.wolfram.com/Stochastic.html.)

Subject Matter Expert (SME):  An individual having education, training, or experience in 

a particular technical or operational discipline, system, or process and who participates in an 
aspect of M&S requiring their expertise.

Tailoring:  The process used to adjust or modify a prescribed requirement to better meet 

the needs of a specific program/project task or activity.

Uncertainty: (a) The estimated amount or percentage by which an observed or calculated 

value may differ from the true value9; (b) A broad and general term used to describe an imperfect 
state of knowledge or a variability resulting from a variety of factors, including but not limited to 
lack of knowledge, applicability of information, physical variation, randomness or stochastic 
behavior, indeterminacy, judgment, and approximation (adapted from NPR 8715.3, NASA 
General Safety Program Requirements);  (c) Non-negative parameter characterizing the 
dispersion of values attributed to a measured quantity.

Uncertainty Characterization:  The process of identifying all relevant sources of 

uncertainties and describing their relevant qualities (qualitatively or quantitatively) in all models, 
simulations, and experiments (inputs and outputs).

Uncertainty Quantification: The process of identifying all relevant sources of 

uncertainties; characterizing them in all models, experiments, and comparisons of M&S results 
and experiments; and quantifying uncertainties in all relevant inputs and outputs of the simulation 
or experiment. (Note: NASA-STD-7009A.)

Unit Testing: Any type of software testing conducted on the smallest meaningful, testable 

fragments of code to ensure the code behaves exactly as intended under various conditions. For 

                                                 
9 The American Heritage Dictionary of the English Language, 4th ed. (2006). Boston:  Houghton Mifflin Co. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

23 of 157 

procedural programming languages, such code fragments are generally functions or 
subroutines.10

Use Assessment:  The process of determining if an M&S is accepted for a Proposed Use.

Validation: The process of determining the degree to which a model or a simulation is an 

accurate representation of the real world from the perspective of the intended uses of the M&S.

Verification: The process of determining the extent to which an M&S is compliant with 

its requirements and specifications as detailed in its conceptual models, mathematical models, or 
other constructs.

Voluntary Consensus Standards (VCS):  Standards developed or adopted by VCS bodies, 

both domestic and international, that include provisions requiring that owners of relevant 
intellectual property have agreed to make that intellectual property available on a non-
discriminatory, royalty-free, or reasonable royalty basis to all interested parties.  (Note:  OMB 
Circular No. A-119.)

Waiver:  A documented authorization intentionally releasing a program or project from 

meeting a requirement.  (Note:  NPR 7120.5D. Deviations and exceptions are considered special 
cases of waivers.)
 
4. 
INTRODUCTION 

 
Note:  The acronym M&S is used in a variety of ways in the literature: 
 

a. Model and simulation. 
b. Models and simulations. 
c. Modeling and simulation. 
d. Modeling and simulating. 

 
The acronym is additionally confusing in that the term “model” can be used as both a noun and a 
verb.  In the development of NASA-STD-7009A, the decision was to focus on the product of 
models and simulations, rather than on the process of modeling and simulating.  The use of M&S 
in this NASA Technical Handbook, as in NASA-STD-7009A, refers to models and simulations. 
There are times when the singular or plural form is intended, which can be inferred from the 
context. 
 
 
 

                                                 
10http://www.saravanansubramanian.com/Saravanan/Articles_On_Software/Entries/2010/1/19_Unit_Testing_101_F
or_Non-Programmers.html. Retrieved April 22, 2013. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

24 of 157 

4.1 
Background  

 
NASA-STD-7009A holds a unique place in the world of modeling and simulation in that it is 
generally applicable to all types of M&S and all phases of M&S development and use, though its 
primary focus is on the results of an M&S-based analysis, and the reporting thereof.  Most M&S 
standards and recommended practices are either focused on a single type of M&S, e.g., 
structures, fluids, or electrical controls, or on a particular phase of M&S development, e.g., 
verification or validation.  Considering that program/project management is confronted with 
numerous types of analyses with which to make critical decisions, a common framework for 
understanding the results and assessing the analysis credibility is appropriate.  However, this is 
complicated by the vast differences across engineering systems. 
 
With the formal approval of the Baseline version in July 2008, NASA-STD-7009 was available 
for the individual program, project, organization, office, or M&S practitioner to adopt.  While 
adoption of NASA-STD-7009 is not required for either development or use of an M&S, unless 
specified by formal directive, it is highly recommended for those deemed as critical.   
Many organizations, both internal and external to NASA, maintain a continuing interest in the 
NASA-STD-7009A, including the NASA Aerospace Safety Advisory Panel (ASAP Reports for 
2008 and 2009).  The interest and questions regarding the practical implementation of NASA-
STD-7009 provided the impetus to develop this NASA Technical Handbook, which was initially 
sponsored by the NASA Engineering and Safety Center (NESC) in December 2009. 
 
Development of this NASA Technical Handbook included the review of related NASA 
documentation (software requirements, product data and life-cycle management requirements, 
and NESC procedures); other related U.S. Government documentation, including OMB Circular 
A-119, VCS, DoD and Department of Energy M&S verification and validation (V&V) and 
uncertainty quantification guidance; EPA/100/K-09/003, Guidance on the Development, 
Evaluation, and Application of Environmental Models; and the following external M&S 
standards and guides:   
 

ASME V&V 10 
Verification and Validation in Computational Solid Mechanics 

ASME V&V 20 
Standard for Verification and Validation in Computational Fluid 
Dynamics and Heat Transfer 

ASME V&V 40 
V&V for Computational. Modeling for Medical Devices 

IEEE 1597.1 
IEEE Standard for Validation of Computational Electromagnetics 
Computer Modeling and Simulations 

TOR-2010(8591)-17 Mission Assurance Improvement Workshop, Guidance for Space Program 
Modeling and Simulation (Baxter, 2010, Aerospace Report) 

 
ASME V&V 40 also adapts several concepts from NASA-STD-7009A for its use. 
 
The development of this NASA Technical Handbook was initiated with several pathfinder 
evaluations of on-going NASA M&S projects:  The Orion Service Module Tank Slosh Model, 
the Orion Crew Module Water Landing Model, the Ares Thrust Oscillation Model, and the Mars 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

25 of 157 

Science Laboratory (MSL) Powered Descent Model.  The general findings from these pathfinder 
studies encourage doing the following: 
 

a. Have a structured process to follow. 

 

b. Use consistent terminology. 

 

c. Evaluate an M&S-based analysis more broadly, i.e., beyond V&V, to include all 
credibility assessment factors. 

 
d. Understand the RWS project requirements relevant to the M&S. 
 
e. Define accuracy requirements to validate critical analysis models appropriately. 
 
f. Understand how the validation of an M&S can be improved. 
 
g. Cross-link credibility assessment factors to NASA-STD-7009A requirements. 

 

h. Address M&S limits of operation. 
 
i. Provide guidance on coupled models. 

 

The questions related to implementation of the requirements of NASA-STD-7009A by M&S 
practitioners, the additional emphasis on risk by the ASAP, the details of various aspects of 
M&S provided by other government and professional organizations, and the findings from 
NASA pathfinder projects provide the basis for the development of this NASA Technical 
Handbook.  While implementation of NASA-STD-7009A is initially perceived as complex, this 
is usually a reflection of the complexity of the M&S discipline.  Besides the sheer depth of 
calculation accomplished in many M&S, the variety of M&S types and methods add to the 
difficulty of uniform application.  The following are examples of the varieties of M&S:  
 

• M&S primarily based on differential equations or difference equations. 
• A relative geometry model of various objects over time.  
• Regression models from empirical data. 
• Various system data relationship models. 
• Stochastic process simulation modeling and analysis. 

 
The uniqueness in implementing the various types of M&S is left to the discipline accomplishing 
the M&S-based analysis, e.g., finite element analysis, system process analysis, or computational 
fluid dynamics, and to the relevant professional organizations, e.g., American Institute of 
Aeronautics and Astronautics (AIAA), ASME, or IEEE.  This is not a full elucidation of the 
M&S disciplines that exist, which becomes even more complex by M&S systems that are 
combined into larger or distributed analytical platforms.  Therefore, one essential consideration 
in the development of the NASA Technical Handbook was to provide guidance and explanations 
about the requirements and recommendations included in NASA-STD-7009A and thus ease and 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

26 of 157 

broaden its use.  Understanding the development and use phasing of the NASA-STD-7009A 
requirements and recommendations, along with a worksheet for M&S planning, development, 
and use, provides context and guidance for a more complete practice of modeling and simulation.  
 
Worksheets and checklists are used in a variety of venues to ensure operations and processes are 
accomplished in an organized, consistent, and complete manner, which can improve both the 
safety and quality of the process.  “NASA research has led to standardized checklist 
characteristics in the field of general aviation.”11  Studies were also accomplished in the area of 
medical/surgical procedures showing that the implementation of checklists had associated 
“reductions in the rates of death and complications among patients” (Haynes, et al., 2009).  As 
NASA’s use of M&S can have safety or critical implications to human life or mission success, 
the use of a checklist or worksheet to guide the development, use, and discussion of M&S-based 
results is appropriate.  The worksheet resulting from the development of this NASA Technical 
Handbook combines aspects of both worksheets and checklists. 
 
Note:  This NASA Technical Handbook and associated worksheet are not intended to be 
comprehensive or overly prescriptive.  It is not possible to include everything needed for every 
type and application of M&S.  The intent is to provide guidance to a more complete discussion 
of the details surrounding M&S-based analyses and results. 
 
4.2  
Applicability 

 
The question of the applicability NASA-STD-7009A often arises in new programs, projects, or 
M&S efforts.  The wording in NASA-STD-7009A is clarified from the Baseline version (see 
NASA-STD-7009, Change 1, section 1.2).  The following are noteworthy points: 
 

a. The word “applicable” means relevant and appropriate, i.e., it does not mean 
required. 

 
b. As a general M&S Standard, it is relevant and appropriate to all M&S regardless of 
M&S type, discipline, or application (e.g., design, development, manufacturing, ground 
operations, and flight operations). 

 
c. If an M&S is used in critical decisions or functions, compliance with NASA-STD-
7009 is highly recommended. 

 
d. NASA-STD-7009 becomes required when so specified in program, project, 
organization, or office directives. 
 
4.3 
Interpreting and Tailoring 

 
Any general standard necessarily requires either interpretation or tailoring to a particular 
application.  Both are acceptable, as long as they are justified, approved (as necessary), and 

                                                 
11 http://hwebbjr.typepad.com/openloops/2005/09/how_to_create_a.html. Retrieved April 23, 2013. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

27 of 157 

documented (see Table 4 in section 4.8 for more on Program/Project Management and delegated 
Technical Authority Responsibilities).  Interpretation of the requirements and recommendations 
are often necessary and depending on the specific type, form, or application of M&S may not be 
applicable.  Tailoring provides the flexibility for these situations.  For example, static (e.g., 
unchanging, deterministic) models provide no handling for uncertainties that always exist in an 
RWS, which means the uncertainty characterization requirements might justifiably be 
eliminated.  
 
4.4 
Compliance with NASA-STD-7009A 

 
Key aspects of M&S development and use are clarified when the requirements and 
recommendations of NASA-STD-7009A are followed, such as: 
 

a. Established processes for both M&S development and use. 
 
b. The intended use (the expected purpose and application of an M&S) is documented, 
which provides the basis for M&S development. 

 
c. Abstractions, Assumptions, and M&S Design are documented. 
 
d. Uncertainties are characterized. 
 
e. The Permissible Uses are documented, as determined during development with an 
understanding of the abstractions taken in development, the assumptions made during 
development that impact model use, the constraints of implementation methods used, and the 
limits of operation based on the completeness and success of both verification and validation. 
 

f. Processes and methods for appropriately using the M&S are documented (e.g., via a 
user’s guide) 

 
g. The results from M&S use are reported with other qualifying information, to include: 
 

(1) Criticality of M&S application (as defined in NASA-STD-7009A, Appendix D). 
(2) Uncertainty of the Results. 
(3) Caveats to the Results. 

 
A. Unachieved Acceptance Criteria. 
B. Violation of Assumptions. 
C. Violation of Limits of Operation. 
D. Execution Warnings & Errors. 
E. Unfavorable Use Assessment. 
F. Requirement Waivers. 

 

(4) Credibility (as defined in NASA-STD-7009A, Appendix E). 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

28 of 157 

(5) Results from any Technical Reviews. 
(6) People Qualifications (Developers, Users, Analysts). 
(7) M&S Documentation (adequacy thereof). 
(8) M&S Risk. 

 
Note:  The documentation requirements and recommendations of NASA-STD-7009A are 
intended to convey the need for evidence that the activity was accomplished.  It does not expect 
that a new document is required, but that evidence of the activity, and the results therefrom, are 
at least cited/referenced.  DoD documentation and directives (MIL-STD-3022, Standard Practice 
Documentation of Verification, Validation, and Accreditation (VV&A) for Models and 
Simulations, and DoD Modeling and Simulation (M&S) Glossary) provide excellent process 
guidelines in documenting M&S activities, and Appendix C of MIL-STD-3022 could be utilized 
as a tailorable template to incorporate into M&S activities.   
 
For more information, the “rationale” for each requirement is included in NASA-STD-7009A and 
additional explanations are available in this NASA Technical Handbook (relevant sub-sections of 
section 5). 
 
4.5 
Models – Key Concept   

 
NASA-STD-7009A defines a model as a description or representation of a system, entity, 
phenomena, or process, including any data going into a model.  Models are necessarily imperfect, 
incomplete, or abstract for a variety of reasons, as follows: 
 

a. An exact representation is not possible because: 

 
(1) Exact knowledge about the RWS is rarely complete and usually uncertain. 
(2) Details are not sufficiently characterized so as to be included in the model. 
(3) All possible variations of the subject RWS cannot be reasonably included. 
(4) The model would exceed the limits of the computational platform. 
 

b. An exact representation is not desirable because: 

 
 

(1) Added fidelity (detail) adds cost and complexity. 
(2) Adding unnecessary details detracts from focus of the analysis. 
 

c. An exact representation is unwieldy because: 

 
(1) The RWS is extremely small and scaling the model up makes it more readily 
understood. 

(2) The RWS is extremely large and scaling the model down makes it more readily 
understood. 

  

As such, models are abstract representations of existing, proposed, or imagined systems; 
however, the intent is to include the pertinent representations necessary for the model’s intended 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

29 of 157 

purpose.  The key concept is that models and simulations are not exact representations, and 
therefore, do not produce exact or perfectly representative results.  Both the limitations and 
imperfections built into the model, i.e., epistemic uncertainty, and the inherent system variability 
included in the analysis, i.e., aleatory uncertainty, are manifested as uncertainty in the M&S 
results and need to be clearly understood (additional explanations are found in SAND2003-
3769).  Considering what is not included in the model can be as important as what is in the 
model. 
 
4.5.1 Pedigree and Provenance in Models and Simulations 
 
A prevalent and important concept in data, information, and computational science, which is also 
applicable to M&S, is pedigree or provenance.  While a variety of definitions exists for both 
terms, which are somewhat inconsistent, the concepts are overlapping.  Both terms embody the 
concepts of lineage and traceability, and either infer or directly address the quality of the data or 
information used.  For the purposes of this NASA Technical Handbook, pedigree and 
provenance are synonymous.  
 
NASA-STD-7009 and this NASA Technical Handbook encompass the general concept of data 
provenance in the form of the Data Pedigree and Input Pedigree factors of Credibility 
Assessment.  The Input Pedigree factor assesses data used as input to a model, which is 
accomplished when using a model for a specific application.  On the other hand, data used during 
model development, and the subject of Data Pedigree assessments, may be obtained, altered, or 
included any time from initial model conceptualizations through model construction.  In short, 
whenever data is incorporated in an M&S, that data becomes subject to evaluation in the Data 
Pedigree factor of the Credibility Assessment (see Appendix D.3). 
 
The concept of provenance may also be applied to a model, as it is influenced by a multitude of 
data, information, processes, and personalities during its development.  Addressing and 
improving model provenance is essentially one of the cornerstones of NASA-STD-7009.  The 
ability to reference a specific M&S life cycle and address the processes and products of each 
phase of that life cycle (section 5) is emphasized in both the Standard and the Handbook.  A 
disciplined and documented approach to model development and use directly enhances model 
provenance. 
 
4.5.2 Models of Models 
 
The definition of a model in NASA-STD-7009A also notes that “a model may be constructed 
from multiple sub-models; the individual sub-models and the integrated sub-models are all 
considered models.”  Other related terms, such as coupled model, linked model, integrated model, 
surrogate model, and metamodel, are also included as part of the model concept.  There are a 
number of reasons to construct larger models this way, including taking advantage of already 
existing models and the benefits of modularity.  The interaction between the “component 
models” may be in a simple one-way (feed-forward) direction, or a complex multipath network 
of interactions.  In either case, the interfaces and interactions between such models should be 
clearly documented and tested. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

30 of 157 

An example of a one-way, unidirectional coupling or linking of component models is found in 
the case of multidisciplinary design-analysis for telescopes and optical instruments, specifically 
where the analysis considers the impact of temperature changes upon optical image quality.  The 
linked analysis required in this case involves the following:  (1) Executing a simulation using a 
thermal model of the system; (2) Transferring (mapping) the predicted temperatures to a 
structural model of the system; (3) Executing a simulation of the temperature-induced elastic 
deformations of the structure using this structural model; (4) Transferring the structural 
deformations into an optical model; (5) Transferring the predicted temperatures to the optical 
model to account for temperature-dependent index-of-refraction of lens elements, if any; and (6) 
Executing a simulation of the geometric and physical diffraction phenomena using the optical 
model. 
 
On the other hand, aggregated models with two-way interaction between the elements may 
mirror the interactions between corresponding parts of the RWS.  A typical example is a space 
vehicle Guidance, Navigation, & Control (GNC) model, where sub-models representing the 
control system, sensors, actuators, vehicle dynamics, and internal/external environments may 
interact through complex, multipath feedback loops. 
 
There are also cases in which individual models are developed and possibly used on their own 
and then integrated into a larger analytical model to address more system-wide issues.  In either 
case, the recommendation is to apply NASA-STD-7009A to the individual M&S and, 
subsequently, to the linked or integrated M&S as a whole. The level definitions for the input 
pedigree factor in the credibility assessment anticipate exactly this scenario. 
 
Surrogate models are sometimes synonymous with metamodels in some instances, although there 
are other uses of the latter term that include the integration of sub-models and the linkage of 
stand-alone models.  Within the domain of computational M&S, the term often refers to models 
constructed in a manner similar to that used to construct empirical models, where data from 
observations (measurements) are used as the basis for approximating the relationships between 
independent and dependent variables.  For surrogate models, simulation data replaces 
observations as the source of data.  Two typical methods for creating empirical and surrogate 
models are statistical regression and neural networks.  Surrogate models are usually developed 
because of their significant performance advantage over more detailed, application- or discipline- 
specific (e.g., physics-based) model implementations.  However, surrogate models not only take 
on all the assumptions and limitations of the models on which they are based, but also 
incorporate additional limitations from their specific implementation. 
 
4.5.3 NASA’s Motivation to Model 
 
In the development of aerospace systems outside NASA, e.g., in commercial aviation, the risk 
associated with models can be mitigated by hours of flight test in the operational environment.  
The nature of NASA’s missions often involves one-of-a-kind systems that have a high impact if 
unsuccessful, such as: 
 

a. Loss of human life. 
b. Loss of high-value equipment. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

31 of 157 

c. Loss of mission products, e.g., unique science. 
d. Limited reflight opportunities. 
e. Re-design of the system. 
f. Not meeting stakeholder requirements (e.g., for reliability or affordability). 
 

Because of these impacts and a relatively high-risk profile, testing of operational systems in 
operational environments, e.g., flight tests, is typically limited.  NASA’s engineering processes, 
therefore, depend on models of the system to a higher degree than is typically found in other 
industries to help mitigate operational risk.  Thus, a methodical approach to accepting the results 
of these models is beneficial. 
 
4.6 
The Modeling (and Simulation) Process/Life Cycle   

 
An M&S life cycle was introduced in Revision A of NASA-STD-7009 to convey an 
understanding of when, in the development and use of an M&S, the requirements or 
recommendations apply.  As this life cycle developed, it became even more apparent that some 
requirements or recommendations be accomplished more specifically than just “in model 
development” or “in model use.”  Some things are better accomplished earlier in the 
development of an M&S than later.  For example, the intended use of an M&S is best determined 
as early as possible in the life cycle as a standard-bearer for development (even if it is modified 
at a later time). 
 
The M&S life cycle is adapted from NASA Project Life Cycle (NPR 7120.5E, Fig. 2-5) with its 
familiar phases and their designations.  Therefore, people who understand, for example, what 
occurs in Phase B for a program/project, will also understand what occurs in Phase B in an M&S 
life cycle, simply by thinking of the M&S as the “system” under development.  For this reason, 
the number of life-cycle phases are the same, and the names for the phases are correlated to 
promote a more immediate understanding (Table 1, Program/Project and M&S Life Cycles). 
 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

32 of 157 

Table 1—Program/Project and M&S Life Cycles 

Phase Pre-A
A
B
C
D
E
F

Prog/Proj 
Phase Name 

Conceptual 
Studies 

Concept & 
Technology 
Development 

Preliminary 
Design & 
Technology 
Completion

Final Design 
& Fabrication 

System 
Assembly, 
Integration, 
& Test

Operations & 
Sustainment 

Closeout 

 
 

↑ 

Similar 
Name, 
Function, 
Purpose 

↓ 

 
↑ 
 

Similar 
Name, 
Function, 
Purpose 

↓ 

 

↑ 

Similar 
Name, 
Function, 
Purpose 

↓ 

 

↑ 

Similar 
Name, 
Function, 
Purpose 

↓ 

 

↑ 

Similar 
Name, 
Function, 
Purpose 

↓ 

 

↑ 

Similar 
Name, 
Function, 
Purpose 

↓ 

 

M&S Phase 
Name 

Model 
Initiation 

Model 
Concept 
Development

Model 
Design 

Model 
Construction 

Model 
Testing 

Model Use 
Model & 
Analysis 
Archival

 
Note:  The function/purpose of each phase in both the program/project and M&S life cycles is 
essentially the same.  This does not imply that each M&S life-cycle phase occurs in parallel with, 
or at the same time as, the program/project life-cycle phase.  Because models can inform 
decisions in any phase of a program/project, an entire M&S life cycle can exist within one phase 
or more phases, of the program/project.  As one example, Figure 1, M&S Life Cycle in an RWS 
Life Cycle, depicts an entire M&S life cycle within the Conceptual Studies phase of a 
program/project life cycle.  For M&S developments supporting a specific RWS, care is 
warranted in specifying M&S versus RWS development phases. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

33 of 157 

 

Figure 1—M&S Life Cycle in an RWS Life Cycle 

 
Thoughts about any M&S begin and end with the RWS it is to represent (real, proposed, or 
imagined).  A brief explanation of each M&S life-cycle phase is given in Table 2, M&S Life-Cycle 
Phase Descriptions, with a more complete treatment given in the relevant portions in section 5 of 
this NASA Technical Handbook. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

34 of 157 

Table 2—M&S Life-Cycle Phase Descriptions 

Phase
Name
Brief Description

Pre-A 
Model Initiation 
The process of determining the scope of the RWS on which to apply an 
M&S and defining the intended use of the M&S. 

A 
Model Concept 
Development 

The process of compiling all relevant information about the scoped 
RWS and beginning to develop general modeling concepts and 
requirements for representing the RWS. 

B 
Model Design 
The typically iterative process of creating the detailed, verifiable and 
validated specification of an M&S for an intended use, using the 
relevant information regarding the RWS, the conceptual model, and 
other defined objectives/criteria. The model design should be 
conceptually validated prior to commencing with Model Construction 
(Phase C).

C 
Model Construction 
The process/activity of implementing (generating or building) a usable 
model, as defined by its requirements, specifications (some of which 
may be embodied in a conceptual model/diagram), and intended use.

D 
Model Testing 
Verification is the process of determining the extent to which an M&S 
is compliant with its requirements and specifications as detailed in its 
conceptual models, mathematical models, or other constructs. 

 
Validation is the process of determining the degree to which a model 
or a simulation is an accurate representation of the real world from the 
perspective of the intended uses of the M&S. 

 
Model Release is the process of establishing the baseline and 
controlled version of the model and associated key documentation for 
use.  After release, changes to the baseline are to be evaluated, 
justified, and authorized with traceability prior to implementing and 
releasing the revision.

E 
Model Use 
The application of an M&S to the purpose for which it is intended.  
This Phase begins with assessing a proposed use, preparing the model 
and scenarios for use or otherwise integrating the model into the 
simulation, using (e.g., running) the model, gathering and post-
processing the output, and assessing and reporting the results.

F 
Model & Analysis 
Archival 

The process of storing and cataloging all M&S and designated 
development and use artifacts for retrieval and use. 

 
Three final points to note about an M&S life cycle: 
 

a. It is understood that actual execution of these life-cycle phases, especially the early 
phases, is not as discrete in practice as depicted.  Pre-phase A and Phase A are often blended, as 
are Phases A and B.  The key point is the activities are best performed and products best 
developed in the given order as most effective and efficient.  Additionally, these activities often 
occur in reiterative cycles within and between the various phases as development of the end-
product matures.  This concept is also embodied, at least to some degree, in both spiral and agile 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

35 of 157 

development processes.  These are not precluded when adopting the life cycle as defined in 
NASA-STD-7009A.  It just means that the series of development and use phases occur multiple 
times for each round of the spiral or agile sprint for smaller pieces of the model and for the final 
integrated model. 

 
b. Many of the requirements and recommendations can be, or need to be, accomplished 
in several of the life-cycle phases.  It is advantageous to initially accomplish the requirements or 
recommendations in the earliest practical phase (see Appendix A) and then update the 
information as needed throughout subsequent phases.  On the other hand, if a requirement or 
recommendation is not accomplished in a particular recommended phase, it becomes incumbent 
on the subsequent phases to make up that shortfall. 

 
c. The Model and Analysis Archiving Phase (Phase F) is placed as if the entire M&S 
life cycle occurs, from development to use, before archiving any of the artifacts.  An M&S may 
not necessarily get closed out once development or a particular use is completed, but may simply 
be “put on the shelf” until needed.  The M&S and associated key products are expected to be 
archived at key points throughout development and use (e.g., at the end of each life cycle phase), 
as well as at the end of an M&S’s life cycle.  This phase is retained here for a few reasons: 

 
(1) To retain commonality with the program/project life-cycle phases. 

 

(2) To emphasize that each development or use cycle of an M&S is to conclude with 
archival of the M&S revision and its requisite by-products from development and use. 

 
The structure of section 5 of this NASA Technical Handbook follows these life-cycle phases. 
 
4.7  
Relation to NPR 7150.2 

 
Models, particularly analytical models, are usually implemented in software.  Section 4 of 
NASA-STD-7009A notes that “Specific requirements applicable to M&S implemented in 
software are found in the NASA Software Engineering Requirements (NPR 7150.2).”  The 
requirements contained within NPR 7150.2 “cover all software created, acquired, or maintained 
by or for NASA and apply to all of the Agency's investment areas containing software systems 
and subsystems.”  NPR 7150.2 classifies NASA’s software systems as follows (Table 3, Classes 
of NASA Software): 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

36 of 157 

Table 3—Classes of NASA Software 

Class 
Software Description 

A 
Human-Rated Space Software Systems 

B 
Non-Human Space-Rated Software Systems or Large-Scale Aeronautics Vehicles 

C 
Mission Support Software or Aeronautic Vehicles, or Major 
Engineering/Research Facility Software 

D 
Basic Science/Engineering Design and Research and Technology Software 

E 
Design Concept and Research and Technology Software 

F 
General Purpose Computing, Business and IT Software (Multi-Center or Multi-
Program/Project) 

G 
General Purpose Computing, Business and IT Software (Single Center or Project) 

H 
General Purpose Desktop Software 

 
NPR 7150.2, Appendix D, defines each class in detail; and NPR 7150.2, Appendix C, provides a 
detailed compliance matrix that defines which requirements are applicable to each software 
class. Classes A-E are of primary interest here, noting that models may be embedded in flight 
and ground software (Class A/B/C) systems, and are routinely used within engineering design 
software (Class D/E) systems.  The M&S practitioner is to note that Agency software 
engineering requirements (and Center implementations thereof) cover, among other things, 
modeling tools and parametric models.  Specifically, the NPR states that: 
 

a. Examples of Class D software include, but are not limited to, engineering design and 
modeling tools (e.g., computer-aided design and computer-aided manufacturing  (CAD/CAM), 
thermal/structural analysis tools); project assurance databases (e.g., problem reporting, 
analysis, and corrective action system, requirements management databases); propulsion 
integrated design tools; integrated build management systems; inventory management tools; 
probabilistic engineering analysis tools; test stand data analysis tools; test stand engineering 
support tools; experimental flight displays evaluated in a flight simulator; and tools used to 
develop design reference missions to support early mission planning. 

 
b. Examples of Class E software include, but are not limited to, parametric models to 
estimate performance or other attributes of design concepts; software to explore correlations 
between data sets; line of code counters; file format converters; and document template builders. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

37 of 157 

A significant percentage of the requirements in the NPR are (or at least may be, under certain 
conditions) applicable to Class D software, while far fewer requirements are applicable to Class 
E software (refer to Appendix C of NPR 7150.2).  Compliance with all requirements in  
NASA-STD-7009A does not ensure compliance with all requirements in NPR 7150.2 spanning 
Classes A-E.  Conversely, compliance with all requirements in NPR 7150.2 does not ensure 
compliance with all requirements in NASA-STD-7009A.  In particular, and of significant 
importance, NPR 7150.2 does not address M&S-based analysis, the M&S credibility assessment, 
or reporting of M&S results and M&S risk. 
 
Furthermore, and also likely unknown to M&S practitioners, NPR 7150.2 states: 
 

In this directive, "software" is defined as the computer programs, procedures, scripts, 
rules, and associated documentation and data pertaining to the development and 
operation of a computer system.  This definition applies to software developed by NASA, 
software developed for NASA, software maintained by or for NASA, commercial off-the-
shelf (COTS) software, government off-the-shelf (GOTS) software, modified off-the-shelf 
(MOTS) software, reused software, auto-generated code, embedded software, the 
software executed on processors embedded in programmable logic devices (see NASA-
HDBK-4008, Programmable Logic Devices (PLD) Handbook), legacy, heritage, and 
open-source software components. 

 
This means that requirements for Class D/E (e.g., engineering CAD/computer-aided engineering 
CAE) software apply to commercial tools (e.g., SOLIDWORKS®, the structural analysis system 
(NASTRAN), internally developed tools, or combinations thereof). 
 
Finally, note that NASA-STD-7009 is referenced in the NPR (in section 4.5.7 of NPR 7150.2B) 
stating that “The project shall verify, validate, and accredit software models, simulations, and 
analysis tools required to perform qualification of flight software or flight equipment. [SWE-
070].  Note:  Information regarding specific verification and validation techniques and the 
analysis of models and simulations can be found in NASA-STD-7009 and NASA-HDBK-7009.”   
In NPR 7150.2, a software engineering (SWE) number designates a requirement. 
 
Neither NASA-STD-7009 nor NASA-HDBK-7009 provide specific V&V techniques (other than 
a few simple examples contained in NASA-HDBK-7009), but leave such details to discipline-
specific recommended practices.  Also note, while the definitions of verification and validation 
in NASA-STD-7009 and NPR 7150.2 are similar, their interpretations may be different.  For an 
M&S to be valid, its results are to compare favorably with referent (or RWS) data (per [M&S 8] 
(4)). 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

38 of 157 

4.8  
Program/Project Management and Delegated Technical Authority Responsibilities 

 
Throughout NASA-STD-7009A, there are a number of explicit and implicit responsibilities on 
either program/project management or the delegated Technical Authority, which addresses the 
check-and-balance structure in the NASA organization (see NPD 1000.0, NASA Governance 
and Strategic Management Handbook, and NPR 7120.5).  These are consolidated in Table 4, 
Program/Project Management and Delegated Technical Authority Responsibilities, for easy 
reference.  On the other hand, the requirements in NASA-STD-7009A are addressed to "the 
responsible party," since it is likely different for each model.  The seventh row after the title row 
in Table 4 indicates the program/project management responsibility to identify “the responsible 
party” for each requirement. 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

39 of 157 

Table 4—Program/Project Management and Delegated Technical Authority 
Responsibilities 

Program/ 
Project 
Management 
Responsibility

Delegated 
Technical 
Authority 

Responsibility

Topic 
Sections 
Requirements 
Rec. 
Sections 

Defines 
Approves 
Acceptance 

Criteria

1 
- 
- 

Specifies 
- 
Required 
application of 

NASA-STD-7009

1.2 
- 
- 

Documents 
- 
Precedence over 

VCSs

1.2 
[M&S 1] 
- 

Documents
Approves
Tailoring
1.3
[M&S 2]
-

- 
Approves 
Non-Use of latest 
cited Applicable 

Documents

2.1.1, 2.1.2 
[M&S 3], [M&S 
4] 

- 

- 
Resolves conflicts 
Requirement 

Conflicts

2.4.2 
[M&S 5] 
- 

ID’s & 

Document

- 
Responsible 

Parties

4 
- 
- 

ID’s & 
Document 

ID’s & Document 
Criticality / 
Critical Decisions 
/ M&S In Scope

3.2 (Critical 
Decision), 

4.1

[M&S 6], [M&S 
7] 

- 

ID’s & 

Document

ID’s & Document 
Level of 
Formality

4 
- 
- 

- 
Assure appropriate 
outcomes 

Objectives & 
Req’ts for M&S 

Products

- 
[M&S 8] 
- 

Deem 
achievement 

- 
Mission Success 
Criteria 

3.2 (Mission 
Success 
Criteria)

- 
- 

Accepts 
Concurs / Approves 
Waivers 
3.2 

(Waivers)

- 
- 

- 
Assures appropriate 

outcomes

Use Assessment 
4.3.1 
[M&S 23] 
- 

- 
Establishes & 
Assures appropriate 

outcomes

Credibility 
Assessment 

4.3.6 
[M&S 31] 
4.3.7-a, c 
(thresholds) 

Is informed by
-
Risk
4.3.8
[M&S 39]
-

 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

40 of 157 

5. 
M&S LIFE CYCLE PROCESSES 

 
As introduced in section 4.6, this NASA Technical Handbook is structured according to the 
M&S life cycle, as defined in NASA-STD-7009A, Appendix F.  This section of the NASA 
Technical Handbook discusses each of the seven phases and what is best accomplished in each 
of them.  Due to the variety of M&S, the consequences and constraints of implementation and 
their application, the tasks stated for each phase may be delayed to later phases, spread across 
multiple phases, or updated in later phases.  The tasks in the phases described in section 5 and 
the requirements or recommendations (R/r’s) depicted in Appendix A are to take this potential 
flexibility into account.   
 
Note:  It is usually best to accomplish and document a given task, requirement, or 
recommendation as early as possible/practical in the M&S life cycle, and update the 
products/results as development or use continues to remain current and relevant.  This includes 
the archival of the requisite products at the end of each life cycle phase. 
 
5.1 
Model Initiation (Pre-Phase A) 

 
The beginning of any model development effort stems from consideration of the RWS and the 
possibilities of what an M&S can do for it. 
 
To start the M&S life cycle, the following are needed: 
 

a. Information about the RWS, either as: 
 

(1) Existing. 
(2) Proposed Changes to the Existing. 
(3) Imagined (but not yet existing). 

 

b. The possibility that an M&S can help (inform) the RWS (situation). 

 
With this information, additional details about the RWS (situation) and how an M&S might 
benefit the RWS are gathered and formulated. 
 
5.1.1 Accomplishing the Model Initiation Phase 
 
With the available information, this Phase accomplishes the following: 
 

a. Gathering additional RWS information. 
b. Establishing an initial statement of Intended Use for the M&S. 
c. Performing a Criticality Assessment. 
d. Justifying an M&S is needed, preferred, or appropriate. 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

41 of 157 

5.1.1.1 
Gathering RWS Information 

 
Information about the RWS is needed to give direction to, and provide a basis for, M&S 
development.  Specific parts of the RWS such as RWS elements/components (or aggregations 
thereof), subsystems, and aspects/attributes to analyze are identified, along with the possible 
boundaries between the RWS and its environment are identified. 
 
Note:  The concept of Data Pedigree, the first factor of the Credibility Assessment, is directly 
influenced in this early phase of model development.  Any data gathered, used, altered, or 
discarded during the course of model development (i.e., from Model Initiation (Pre-Phase A) 
through Model Construction (Phase C)) has the potential of positively or negatively influencing 
Data Pedigree (see Appendix D.3). 
 
5.1.1.2 
M&S Statement of Intended Use 

 
Once a basic amount of information about the RWS and the specific problem, issue, or aspect to 
apply an M&S is known, the initial statement of Intended Use [M&S 8 (2)] for the M&S may be 
documented.  The Intended Use is the expected purpose and application of an M&S and is best 
established early in the M&S development life cycle, even though it will likely be modified as 
the M&S evolves, to serve as the primary guide to M&S development and use.  As such, the 
statement of Intended Use is general, not detailed, in nature, and is intended to be short and 
concise.  The Intended Use includes: 
 

a. A general statement of what the M&S does, which may include a description of 
results expected from the M&S. 

 
b. General limits of the M&S due to: 
 

(1) What is modeled (i.e., RWS type/class, aspect(s)/attribute(s), 
context/environment(s)). 

 
(2) The presumed or chosen modeling methods or mechanisms (if any are prescribed 
at this point). 

 

c. Generalized functions or results expected from the M&S, including: 

 

(1) Providing information for use in RWS analysis (that is otherwise performed 
manually or by another M&S). 

 

(2) Depicting (visually or otherwise) the RWS (either statically or dynamically). 

 

(3) Predicting how the RWS will behave or react (generally after application of initial 
or boundary conditions). 

 

(4) Training personnel to operate, maintain, or repair an RWS. 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

42 of 157 

d. Specific portions or aspects of an RWS or set of RWSs, to include, such as: 
 

(1) The application or set/range of applications. 
 
(2) The portion(s) of a larger system or type/class of system of that portion. 
 
(3) The attributes of the system modeled. 
 
(4) The context, environment, or set/range of environments surrounding, interacting 
with, or influencing the RWS. 

 

e. Specific situations or conditions that define or influence the RWS design or as-built 
configuration, operation, maintenance, repair, storage, or testing.  These include: 
 

(1) Project/program phase(s). 
(2) Operational phase(s).  
(3) Environmental conditions. 
(4) Scenarios, including operational, maintenance, repair, testing, inspection, and 
storage. 

 
Note:  The Intended Use of an M&S communicates this information in an inclusive manner, and 
provides a reference for possible future use of the M&S.   
 
Clarity of Intended Use may be enhanced by appending specific cases or situations to be avoided 
when using the M&S. 
 
The Intended Use is established early in M&S development, during the “Model Initiation” Phase, 
to guide development, and may be substantiated or revised throughout M&S development, 
depending on specific choices made during design and implementation, or depending on results 
from the M&S during V&V testing.  The Intended Use is also used in establishing the 
permissible uses of an M&S. 
 
5.1.1.3 
Performing the Criticality Assessment 

 
The criticality assessment [M&S 6] ensures communication of the following: 
 

a. The consequences to human safety or RWS success criteria. 
b. The degree to which M&S results influence any and all related decisions. 

 
This initial assessment needs to be accomplished in pre-Phase A of the model's development. In 
part, the outcome of this assessment drives decisions that span the rest of the M&S life cycle and 
also higher-level program/project planning and resource allocations.  Appendix D of NASA-
STD-7009A suggests a risk-based approach to the criticality assessment, including a 
representative risk matrix that may be adopted or tailored to meet the needs of the 
program/project. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

43 of 157 

5.1.1.4 
Justifying the M&S Approach 

 
Another key part of the “Model Initiation” Phase is the determination whether an M&S is the 
best approach.  There are potentially many reasons why an M&S should not be developed or 
used, such as the following: 
 

a. Not enough is known about the RWS to either build or validate an M&S. 
 
b. Not enough resources (time, labor, or budget) are available for M&S development or 
use to meet the needs of the RWS. 

 
c. Other methods to achieve the same objective are better, less expensive, easier, or 
more readily available, such as: 
 

(1) Other existing or competing M&S. 
 
(2) Other analytical methods or tools, such as mathematical or statistical methods, 
which could be considered models, too. 
 

(3) Physical experiments. 
 
(4) Using the RWS. 

 

Factors to consider for each alternative method are in Table 5, Alternative Method Assessment 
Factors. 
 

Table 5—Alternative Method Assessment Factors 

Criteria 
Consideration 

Resources
Have sufficient resources (e.g., money, time, people, equipment) been 
allocated for development and use of each method?

Availability
What is the readiness of each method for use? This depends on the current 
life-cycle phase of each method and the demand on the method in that phase.

Hazards
What are the physical hazards associated with developing or using each 
method?

Risks
What are the risks associated with developing or using each method?

Uncertainties
What uncertainties are known and manifest in each method?

Practicality
Is it realistic to assume each method can be developed or used when needed?

Validation
Is each method, or can each method be, sufficiently accurate and precise?

 
The decision to produce or acquire an M&S, and subsequently use an M&S, is made when the 
M&S advantage exists for any of the needed RWS information. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

44 of 157 

The outcome of the criticality assessment described in section 5.1.1.3 partially informs these 
factors for the M&S option.  Specifically, understanding the consequences of the decision and 
the M&S influence over it may drive other potential requirements on the M&S, including but not 
limited to: 
 

a. The level of effort and rigor to be applied throughout the M&S life cycle. 
 

(1) Which requirements and recommendations from NASA-STD-7009A will be in 
play and enforced. 
 

(2) The required formality for the M&S processes. 

 

(3) The technical reviews required, as well as the scope/depth of these reviews. 

 

(4) Target M&S credibility scores.  

 

b. The requirements for M&S developers and users, in terms of knowledge, skills, and 
experience. 
 
However, some requirements on the M&S, even if only preliminary, are generally needed at this 
point to completely address the factors listed above, e.g., the requirements for M&S accuracy 
and uncertainty, or the requirements for the limits of operation.  These requirements will likely 
drive cost and schedule in all of the other M&S life-cycle phases, potentially steering the 
outcome of the trades between the M&S and other potential solutions. 
 
The purpose of the M&S is another key consideration, which is at least partially defined in the 
statement of Intended Use, but also includes the type of knowledge desired about the RWS, of 
which there are two basic types, “Scientific Knowledge” and “Technical Knowledge.” 
 
“Scientific Knowledge” is acquired to improve human understanding of the universe or a portion 
or segment thereof.  With this type of knowledge, there is no interest in influencing the RWS or 
applying the acquired knowledge to practical or earthly (real world) applications. 
 
“Technical Knowledge” is acquired to create a new or modified RWS, or to create new or 
modified processes in operating (or maintaining) the RWS.  This type of knowledge is the most 
common type acquired from M&S results in engineering and applied physical sciences. 
 
(As a matter of current interest, the scientific studies of global warming/climate change and the 
effects of human activities on this phenomenon could be classified as either “Scientific 
Knowledge,” “Technical Knowledge,” or a combination of both, depending on one’s point of 
view.  If the acquired knowledge leads to intentional changes to human activities, these studies 
could be classified in part as “Technical Knowledge.”) 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

45 of 157 

5.1.1.5 
Empirical Data Availability/Assessment 

 
After the type of needed knowledge about the RWS of interest is determined (or decided), the 
ability of physical experiments and their expected empirical results in producing all or part of the 
needed knowledge needs to be evaluated.  These experiments and results may negate the need for 
M&S completely, be embedded in the M&S, supplement M&S results, be used as M&S input 
data, or validate M&S results. 
 
Note:  Data used in the development of the model, embedded in it, or used to validate the model 
are subject to the Data Pedigree assessment.  Data used as (run-time) input to the model are 
subject to the Input Pedigree assessment. 
 
5.1.2 Products and Expected Outcomes of the Model Initiation Phase 
 
Once an M&S is determined necessary (justified), the Model Initiation Phase concludes with a 
baseline of the following products/artifacts: 
 

a. Statement of Intended Use. 
 
b. Outcome of the Criticality Assessment. 
 
c. Preliminary RWS information to begin developing the model. 
 
d. Preliminary modeling approaches, including justification of pursuing model 
development over alternative methods. 

 

e. RWS empirical data for any of the following: 
 

(1) Inclusion in the model. 
(2) Use as input to the model. 
(3) Use in validating the model. 

 
f. Initial model development plans. 

 
All of this information and data collected or developed in this phase, with knowledge of 
information and data not yet known or obtained, provide the basis for development plans of the 
M&S. 
 
5.2 
Model Concept Development (Phase A) 

 
The Concept Development Phase matures (and potentially finalizes) existing information about 
the RWS and defines/refines concepts and methods to include in the proposed model.  
Throughout the course of this phase, questions about what to model are answered, RWS data are 
gathered to support model development, and trade studies are conducted on modeling methods 
(approaches), model complexity, fidelity, accuracy, and resources.  The phase ends with a chosen 
direction of modeling method(s), a conceptual design, high-level model (and model testing) 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

46 of 157 

requirements, and preliminary model system architecture from which to commence detailed 
model design. 
 
The Model Concept Development Phase uses the products from the Model Initiation Phase: 
 

a. The Statement of Intended Use. 
b. Outcome of the criticality assessment. 
c. Initial model development plans. 
d. Preliminary RWS information. 
e. Preliminary modeling approaches. 
f. RWS empirical data. 
 

These are further developed into concepts, information, or specifications to continue model 
development and enable detailed model design. 
 
5.2.1 Accomplishing the Model Concept Development Phase 
 
The Model Concept Development Phase uses the products from the Model Initiation Phase (i.e., 
the Intended Use, preliminary RWS information, preliminary modeling approaches, and RWS 
empirical data) and develops them further into concepts, information, or specifications to 
continue model development and enable detailed model design, including: 
 

a. RWS refinement and data collection. 
b. Model concept trade studies and selection. 
c. Establishment of preliminary model requirements and specifications, including: 
 

(1) RWS elements and behaviors to represent. 
(2) Relevant RWS characteristics that are subject to M&S-based analysis [M&S 10]. 
(3) Specific RWS scenarios for empirical validation. 

 
Note:  As development progresses, it is expected that any of the products previously produced 
(at this point, the products from the previous phase, e.g., the Statement of Intended Use) may 
need to be refined or updated. 
 
5.2.1.1  
Real World System/Environment Specification and Data Acquisition 

 
The first task in refining the understanding of the RWS to model is determining the physical and 
conceptual elements to include.  An expanded diagram (Figure 2, Overall Representative  
System Expanded Diagram (SLS example)), of the overall representative system, which is the 
subject of the model, helps to clarify these elements in context.  Depending on the part or portion 
of the RWS modeled, providing a series of these diagrams at increasing levels of detail can be 
helpful in understanding the scope of the model in relation to the overall system.  This also 
includes distinguishing elements of the RWS to model from the relevant aspects of the 
environment that influence it (Figure 3, Distinguishing the RWS and its Enviroment), which 
includes all (physical, chemical, behavioral, and other types of) events and sequences of events 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

47 of 157 

considered for inclusion in the model.  A conceptual element is one that can influence the system 
in some physical way, or respond to events or activities occurring in the system in a conscious 
manner, with a goal or purpose in mind (Oberkampf, W. L. and Roy, C. J., 2010).  An example 
of a conceptual element is a human operator, who is modeled as part of a system.  A human 
interacting with or within a system is often referred to as an “actor.” 

 

Figure 2—Overall Representative System Expanded Diagram (SLS example) 

 

 

Types of information in the system and surroundings; from Oberkampf, W. L. and Roy, C. J. (2010) 

Figure 3—Distinguishing the RWS and its Environment 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

48 of 157 

 

The Phenomena Identification and Ranking Table (PIRT) is often used in the nuclear industry as 
a formal and rigorous method to perform this task (Shaw, et al. 1988).  In classifying these 
elements, the following ground-rules apply: 
 

a. The environment may or may not vary with respect to time or spatial location, but it 
also may or may not be affected by the RWS. 

 
b. The RWS is typically (but may or may not be) influenced by the environment. 

 
One common method for depicting the conceptual elements and the interrelationships to include 
in an M&S is by drawing a conceptual model (also referred to as a free body diagram in some 
disciplines), as shown in Figure 4, Conceptual Model (or Free Body Diagram).  A key part of the 
modeling process is deciding what to include or not include in the model, which is part of the 
concept of abstraction.  This task requires engineering judgment, often the most difficult aspect 
of this life-cycle phase, and is to be justified and documented.  The DoD M&SCO provides some 
background information on conceptual model development (Conceptual Model Development 
and Validation, VV&A Recommended Practice Guide special topic, 
https://vva.msco.mil/default.htm?Special_Topics/Conceptual/default.htm). 
 

 

(a) momentum wheels  
 
 
 
(b) inclined plane 

 

Figure 4—Conceptual Model Example (Free Body Diagram) 

 
Once the physical and conceptual elements designated as part of the RWS to model are 
identified, information and data for these elements relevant to the planned M&S need to be 
acquired, including the interactions between each RWS element.  Additionally, the M&S 
development team needs to work with RWS data acquisition teams (e.g., for ground facilities, 
flight tests, or mission operations) to define the referent validation data that will be obtained 
from ground tests, flight tests, or operations.  This also likely support the needs of detailed model 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

49 of 157 

design.  Data included in the model becomes subject to the Data Pedigree assessment, which will 
eventually include data design considerations (see 5.3.2 c). 
 
5.2.1.2  
Model Concept Trade Studies and Selection  

 
With a more complete understanding of the RWS to model, concepts are traded with respect to 
modeling methods (approaches), model complexity, fidelity, accuracy, and resources.  The 
following overarching concepts may be considered: 
 
“Everything should be made as simple as possible, but not simpler.”  Albert Einstein 
 
“The predictive power of a model depends on its ability to correctly identify the dominant 
controlling factors and their influences, not upon its completeness.”  This is an adaptation of 
Occam’s Razor to modeling by Oberkampf and Roy. 
 
“Model building is the art of selecting those aspects of a process that are relevant to the 
question being asked.” – Holland, JH (1995) Hidden Order. Addison-Wesley, New York, USA. 
 
In determining the required level of fidelity and complexity of a planned M&S, as well as the 
required accuracy or uncertainty bounds of or in M&S results, the following should be 
considered and evaluated: 
 

a. Programmatic considerations (constraints): 

 

(1) Model development-use schedule. 
(2) Available versus required hardware, software, and tools. 
(3) Available versus required personnel. 
(4) Available versus required budget. 

 

b. RWS considerations: 

 

(1) The variety of combinations of RWS environments and scenarios to include. 

 

(2) Risk that each environment-scenario pair or group poses to the success of the 
RWS. 
 

(3) Complexity of each phenomenon covered by the planned M&S. 

 

(4) Level of coupling between different phenomena. 

 

(5) Availability of data to support model development. 

 

c. Modeling considerations: 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

50 of 157 

(1) Abstractions (including simplifications) in the model, e.g., physical laws or 
processes ignored or adjusted. 
 

(2) Basis of empirical or phenomenological model of RWS, as opposed to that of 
physical law or explanatory model; observed behaviors mimicked vs. detailed 
processes described. 
 

(3) Complexity of the model, e.g.: 

 
A. Complexity of excitation equations. 

 

B. Mathematical sub-models used to complement sets of equations in the main 
model; e.g., analytical equations, ordinary differential equations (ODEs) and 
partial differential equations (PDEs) for constitutive properties of materials 
and fluids, PDEs for fluid turbulence modeling. 
 

C. Estimated level of temporal and/or spatial discretization needed to achieve 
defined M&S objectives and requirements. Model testing is required to 
confirm the adequacy of these initial estimates. 

 
5.2.1.3 
Preliminary Model Requirements and Specifications 

 
With the physical and conceptual elements in section 5.2.1.1 and the modeling trade decisions in 
section 5.2.1.2, the following activities are performed to develop preliminary model 
requirements and specifications:   
 

a. System and Scenario Abstraction. 
 
b. Coupled Model Specifications (e.g., coupled physics, chemistry, behaviors, etc.). 
 
c. Nondeterministic Specifications (identifying and specifying which model aspects and 
results from the above activities are to be nondeterministic). 
 
The resulting information provides the basis for model requirements and specifications. 
 
5.2.1.3.1 System and Scenario Abstraction 
 
System and Scenario Abstraction identifies the events and sequences of events that may have an 
effect on M&S goals.  These events and sequence of events include those that occur, or may 
occur, under all possible normal and abnormal operating conditions, hostile environments, and 
human or accidentally caused failure modes.  The following are to be considered and may be 
subject to the Data Pedigree assessment: 

 
a. Definition of what the M&S is to do: 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

51 of 157 

(1) 
How RWS is to be shown, depicted, or represented in the M&S. 
 

(2) 
Questions the M&S is designed to answer. 

 
(3) 
RWS information to be provided by the M&S for its analysis. 

 
(4) 
Prediction(s) or determination(s) to be made about RWS that is to be modeled, 
including how it will behave or react (generally after application of initial and 
boundary conditions and system excitations). 

 
(5) 
Required uncertainty bounds or accuracies with all model elements, inputs, or 
responses. 

 
(6) 
How the M&S will be used (e.g., training for the RWS, analysis or testing of the 
RWS). 

 
(7) 
How personnel will be trained in operating, repairing, or maintaining the model, 

 
(8) 
RWS applications, sets of applications, or range of applications to be covered 
by the planned M&S. 

 
(9) 
RWS aspect or attributes to be covered by the planned M&S. 

 
(10) Context, environment, or sets and ranges thereof surrounding, interacting with, 
or influencing RWS that are covered by the planned M&S. 

 
(11) RWS life-cycle phases applicable to the M&S. 
 
(12) RWS scenarios, including operational, maintenance, repair, testing, inspection, 
and storage, covered by the planned M&S. 

 
(13) Cases where the planned M&S should not be used, with supporting rationale. 
 
(14) Cases where the planned M&S should only be used with caution and in 
conjunction with information provided by empirical methods or another M&S. 

 

b. Definition of model application domains, use domains, and expected behavior 
characteristics: 
 

(1) 
Anticipated application domains. 

 
(2) 
Anticipated validation domains. 

 
(3) 
Customer-defined responses from the M&S (sometimes referred to as System 
Response Quantities (SRQs)). 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

52 of 157 

 
(4) 
Expected prediction accuracy requirements. 

 
(5) 
Implementation strategies and methods (e.g., Code) and quality assurance 
activities. 

 
(6) 
Adequacy of numerical error estimation techniques. 

 
(7) 
Existing capabilities for model element representation (e.g., capabilities of grid 
or mesh generation, or other methods to establish configurations and sizes of 
discrete parts or elements of the RWS), i.e. determining if they are sufficient or 
will new ones be needed. 

 
(8) 
Existing, upgraded, or new experimental facilities and test apparatuses for M&S 
validation. 

 
(9) 
Existing versus new or upgraded validation metric operators. 

 
(10) Propagation of input uncertainties through the M&S and the expected resulting 
output uncertainties. 

 
(11) Alternative M&S or contingency plans to revise or supplement M&S or its 
results if the need arises. 

 
5.2.1.3.2 Coupled Physics Specifications 
 
Coupled Physics includes any connections or interactions between physical (or chemical) 
processes that are part of the M&S.  For each identified coupling, the types and options for the 
levels of coupling are to be identified for later consideration (i.e., in the Model Design Phase).  
Even if the coupling, coupling type, or level of coupling is unlikely to be included in the model, 
it should be identified and documented during the Conceptual Development Phase.  The level of 
coupling is often a trade between M&S efficiency (practicality, affordability, minimum 
computation time) and M&S accuracy and fidelity. 
 
If and when a coupling phenomenon is identified after completion of the Conceptual 
Development phase, M&S development during later phases are to pause and the Conceptual 
Development updated to include the respective new coupling phenomenon.  More often than not, 
additional branches of connected elements, events, and event series will result. 
 
5.2.1.3.3 Nondeterministic Specifications 
 
Many models include aspects or elements that are nondeterministic in nature, i.e., where a range 
of values may occur, as opposed to a deterministic (single) value.  These are to be identified for 
further consideration as to how best to present them.  These elements may include M&S input 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

53 of 157 

data, defined processes in M&S, and output data produced by the M&S.  For stochastic 
situations, some variation of Monte Carlo analysis is accomplished using random numbers 
(variates) with the M&S.  
 
Examples of possible nondeterministic elements or situations (Figure 5, General Model Diagram 
with Nondeterministic Elements) that show the propagation of input uncertainties to obtain 
output uncertainties (Oberkampf, W. L. and Roy, C. J., 2010) include: 
 

a. Variations in material properties. 
b. Variations in manufacturing and assembly processes. 
c. Lack of information about hardware storage conditions, damage, or use history. 
d. Uncertainties about the operating environment. 

 

                  

 

Figure 5—General Model Diagram with Nondeterministic Elements 

 
Nondeterministic solutions/results are often presented as probability distributions or single 
values with each having an associated error, tolerance, or uncertainty.  Consideration should be 
given to classifying uncertainties (associated with or used to present nondeterministic solutions) 
as aleatory or epistemic, which are to be presented and later quantified separately. 
 
Mathematical representation and propagation of errors, uncertainties, and probability 
distributions are not to be performed during Conceptual Development, but deferred to later 
phases (i.e., in design, testing, or use). 
 
5.2.2 Products and Expected Outcomes of the Concept Development Phase 
 
The following items should be produced when the Concept Development Phase is complete: 
 

a. Initial Conceptual Model (including all constituent parts, their interconnections, and 
functions as needed). 

 
b. Model Assumptions. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

54 of 157 

c. Concept of Operations. 
 

(1) Determination of model users and associated use cases. 
 
(2) Extent of linkage or coupling of this M&S to other M&S (if the M&S is to be part 
of a coupled system with other M&S’s (or will be), or embedded in a larger 
(representational or analytical) system). 

 
d. High-level model requirements and specifications (as outlined in section 5.2.1.3). 
 
e. Model verification plans, including initial verification requirements. 
 
f. Model validation plans, including: 
 

(1) Initial validation scenarios, including: 

 
A. The RWS or referent used to acquire empirical data. 
B. Specific RWS behaviors and scenarios to validate. 

 

(2) Preliminary validation requirements. 
(3) Anticipated model applications. 
(4) Anticipated validation domain. 

 

5.3 
Model Design (Phase B) 

 
M&S Design is the typically-iterative process of creating the detailed, verifiable and validated 
specification of an M&S for an intended use, using the relevant information regarding the RWS, 
the conceptual model, and any other defined objectives/criteria.  Note:  Any changes to relevant 
portions of the RWS may invalidate the model design. 
 
The Model Design Phase uses the following products from earlier M&S life-cycle phases: 
 

a. Statement of Intended Use (current working version). 
 
b. Outcome of the Criticality Assessment. 
 
c. High-level requirements (needs, goals, objectives, drivers, constraints), such as: 
 

(1) Aspects of the RWS the M&S is to represent. 
(2) The problem(s) the M&S is to solve. 
(3) The decision(s) the M&S is to support. 

 

d. Concept of Operations. 
 

(1) Determination of model users and associated use cases. 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

55 of 157 

(2) Extent of linkage or coupling of this M&S to other M&S (if the M&S is to be part 
of a coupled system with other M&S’s (or will be), or embedded in a larger 
(representational or analytical) system). 
 

e. Conceptual/Mathematical Models 
 

(1) May be presented in multiple formats or combinations thereof, typically: 

 
A. Block diagrams. 
B. Flow charts. 
C. Mathematical equations. 
D. Pseudo-code. 

 

(2) May often represent the intended M&S architecture, which usually will be refined 
throughout the design process. 

 
f. Verification plans and requirements. 
 
g. Validation plans, requirements, scenarios, etc. 

 
5.3.1 Accomplishing Model Design 
 
The design process for an M&S can be the same as, or very similar to, the design process for a 
RWS, as detailed in relevant NASA requirements documentation, e.g., the Systems or Software 
Engineering procedural requirements or handbooks.  For either the RWS or M&S, the design 
process begins with the set of high-level requirements and goals, the concept of operations, and 
the (intended or initial) architecture (the realized architecture may differ), which may be 
provided in a variety of formats, e.g. formal “shall” statements, descriptive narratives, block 
diagrams, flow charts, drawings or models.  The M&S design process then addresses/includes: 
 

a. M&S composition and function: 
 

(1) What the M&S is to include or do to represent the RWS. 

 

(2) How well the M&S is to perform its function. 

 

(3) How, and under what conditions and assumptions, the M&S is to be used. 

 

(4) What the M&S architecture (general form) will be.  This may be driven by 
modularity, scalability, and integration or latency challenges, to name a few 
examples. 

 

Note:  As indicated in section 4.7, specific additional requirements applicable to M&S implemented 
in software are found in NPR 7150.2, NASA Software Engineering Requirements.  These 
requirements are to be considered part of the high-level requirements (constraints) in effect at the 
start of the design phase. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

56 of 157 

 

b. M&S Requirements and Structure, independent of the tools and methods employed: 

 

(1) The high-level requirements, concept of operations and architecture are logically 
decomposed into a well-defined collection of lower-level elements (e.g., modules, 
blocks, and components) and their associated functions, behaviors, and derived 
requirements/goals.  Each element in the resulting hierarchy will interface to one 
or more of the other elements, and potentially interface to the “M&S 
environment,” which may include, for example, the M&S operator(s), the data 
sources, other M&S and the CM system. 

 
(2) The hierarchical structure, internal/external interfaces, functional/logical 
behaviors and derived requirements are transformed into a detailed, 
implementable and verifiable design specification that enables M&S construction 
(implementation). 

 

c. M&S Design Considerations: 

 

(1) Per best engineering practices, when a requirement is written, it is essential to 
document the rationale for the requirement (backwards traceability) and the 
method by which the requirement will be verified (forward traceability).  
Capturing the traceability is critical in the event of changes to any higher-level 
requirement(s) from which the given requirement was derived.  In the extreme, 
the rationale for the requirement may disappear entirely, and the requirement may 
therefore be deleted.  More often, the requirement remains but is modified in 
some way (as well as, possibly, its verification method). 

 
(2) It is likely, if not intentionally so, that multiple design solutions will emerge at 
any given level of decomposition, requiring a trade study to decide which 
solution to pursue. Document the trade spaces (including relevant elements of 
previous phase trade studies, if any), and document the rationale for the 
outcomes, as any of the rejected design solutions may have to be revisited later 
(e.g., if the M&S is invalidated). 
 

(3) Choices in model design (component representations or constructs) are to be 
made to minimize model-based uncertainties, as much as practical at this point of 
the M&S Life Cycle, understanding that model testing is eventually required in 
order to fully accomplish this objective. 

 
(4) One key to successful design is determining when the hierarchical decomposition 
process has reached the point where further decomposition and specification 
starts to over-constrain the model construction process. Knowing when to stop 
designing, when enough decomposition and specification is sufficiently complete 
to confidently proceed to the construction phase, will always be a matter of 
discretion.  A simple and obvious analogy is that no architect or home designer 
specifies the location of every nail.  To attempt to do so would require more 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

57 of 157 

effort than could ever be justified, nor is there much chance that every 
contingency arising during the home construction could be anticipated.  Some 
decisions are simply best left to the carpenter.  Similarly, then, for the M&S 
some decisions are best left to the model construction phase.  However, it is to be 
expected that those decisions (and their rationales) will be documented as model 
construction proceeds. 

 
Note:  Once the model design is complete, and before the model is implemented, a review of the 
model design (i.e., conceptual validation) is to be accomplished with the customer.  This is 
required to meet Level 1 credibility assessment for validation (NASA-STD-7009A, Appendix 
E).  See section 5.3.3. 
 
5.3.2 Considerations in Model Design 
 
Examples of issues/questions often addressed during M&S design include: 
 

a. If not specified in advance, can any existing models, or parts of models, be re-used? 
 
b. When data is required for model development, but no source is specified, what are 
possible sources for such data? 

 
c. What are the data design considerations for use in the model? 
 

(1) Type (nominal, ordinal, interval, ratio, Boolean, categorical). 
(2) Accuracy, Precision, Uncertainty. 
(3) Units. 

 
d. What kind of user interface (e.g., command line vs. graphical user interface (GUI)) is 
needed? 

 
e. What are the relevant CM systems (e.g., for input data, for model elements)? 
 
f. What tools or systems (e.g., computer architectures, COTS software, implementation 
tools) are to be used/supported during model construction and use?  Any system or tool used in 
model development or use is best evaluated before model construction (Phase C) for their 
potential influence on the M&S and results credibility. 

 
g. For the case of coupled models, will the implementation be a single executable or 
multiple executables with appropriate mechanisms for data exchange? 

 
h. For either linked or coupled models implemented as multiple executables, what is the 
data exchange mechanism? 

 

(1) File exchange. 
(2) Inter-process communications on a single workstation. 
(3) Network communication between separate workstations. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

58 of 157 

 
i. What other user-level functionality (e.g., visualization and plotting, data input/output 
(I/O) including file formats, error/event logging , saving state of model mid-run, changing 
parameters mid-run, re-starting from saved or altered state) is either required or desirable? 

 
j. What kind of future scalability is likely?  How can the M&S be modularized to 
facilitate these future changes/upgrades? 

 
k. Are provisions for automation of multiple model runs to be included, e.g., to 
accommodate Monte-Carlo analysis or structured design of experiments? 
 
5.3.3 Model Concept (Design) Validation 
 
All of the work performed in the above steps are documented and reviewed prior to the start of 
model construction.  The objectives of this review, which, if favorable, will constitute conceptual 
validation, are to show that the model design (including the conceptual model) does the 
following: 
 

a. Acceptably reflects the RWS (including all internal functions, logic and behaviors), to 
the extent this can be shown before empirical validation. 

 
b. Satisfies the stated Intended Use of the M&S, as well as all other high-level 
requirements (needs, goals, objectives, drivers, constraints). 

 
c. Is implementable and verifiable. 
 
d. Is consistent with the available budget and schedule. 

 
5.3.4 Products and Expected Outcomes of the Model Design Phase 
 
The following items should be produced when the Model Design Phase is complete: 
 

a. The validated model design, including all conceptual models depicting, as needed: 

 

(1) The constituent parts. 
(2) The interconnection of parts. 
(3) The functions of each part. 

 

b. Model architecture. 

 

c. Model requirements and specifications. 

 

d. Model verification requirements. 
 
e. Model validation requirements. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

59 of 157 

 
5.4 
Model Construction (Phase C) 

 
Model Construction is the process/activity of implementing a model as defined by its 
requirements, specifications (some of which may be embodied in a conceptual model/diagram), 
and intended use.  The Model Construction Phase uses the following products from earlier M&S 
life-cycle phases: 
 

a. Statement of Intended Use. 
 
b. Outcome of the criticality assessment. 
 
c. The validated model design (including all conceptual models depicting constituent 
parts, their interconnection, and functions, as needed). 

 
d. M&S architecture, requirements, and specifications. 
 
e. Verification requirements. 
 
f. Validation requirements. 

 
5.4.1 Accomplishing Model Construction 
 
The M&S Construction Phase begins with a complete and detailed design specification and 
proceeds, using tools and methods specific to the type of M&S being developed, until the design 
is implemented and ready to be tested (verified and validated).  In practice, the lines between 
construction and testing often blur, in the spirit of “build a little, test a little.”  For example, both 
Agile Development (scrum/sprint sequences) and Spiral Development are modern approaches to 
software development, which take different approaches to the “build a little, test a little” 
approach.  The best approach to take is a judgment call; but factors like complexity, customer 
diversity, team composition, and precision of requirements can strongly influence the choice. 
 
Arguably, such an incremental approach is the best approach to development, as verifying 
relatively small numbers of requirements at lower levels of assembly of any product is far more 
tractable than verifying all requirements at once, at the highest level of assembly.  For the M&S, 
the lower levels of assembly are the individual elements, entities, modules, blocks, subroutines, 
etc., that compose the end-to-end M&S.  That said, testing the complete, end-to-end M&S and 
verifying all requirements is the ultimate objective of the Test Phase. 
 
Independent of the specific tools and methods employed, the M&S construction process 
necessarily encompasses the following general activities: 
 
The latest NASA Systems Engineering Handbook (SP-2016-6105, Rev 2 – section 3.7, pages 33-
34) provides an excellent summary of some key M&S Construction decisions (replacing the 
word “system” with the phrase “M&S”). 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

60 of 157 

a. Detailed planning of construction. 
 

(1) The sequence of M&S element development and integration. 
(2) The decomposition of M&S elements. 
(3) The assignment of M&S elements to development team. 
(4) Periodic/regular deliveries to interested stakeholders. 

 

b. Pulling together the model construction system (hardware, software, and tools).  
Multiple instances of the model construction system may be necessary depending on the staff on 
hand and delegation of component level construction. 

  
c. Building model components (or sections).  Specific implementation mechanism 
choices are made at this point in model development. 

 
d. Incrementally testing lower-level components, so as to find component modeling 
issues as early as possible, and preclude finding them during the (final, integrated) Test Phase. 

 
e. Assembling and integrating lower-level verified and validated M&S elements into the 
desired end product of the higher-level M&S.  This includes preparing the M&S integration 
strategy, performing detailed planning, obtaining M&S elements to integrate, confirming that the 
lower-level or component M&S elements are ready for integration, preparing the integration 
environment, and preparing M&S support documentation. 

 
f. Integration of model components (sections), as necessary, to build the overall model. 
 

(1) At least some initial (unofficial) testing of component interfaces should be 
exercised to ensure they function. 
 

(2) Consider placeholder elements to use as proxies for undeveloped M&S elements. 

 

g. Generating a specific M&S through buying, making, or reusing lower-level 
components so as to satisfy the design requirements.  This includes building or coding the M&S; 
reviewing vendor technical information; inspecting delivered, built, or reused M&S elements; 
and preparing M&S support documentation for integration. 

 
h. Documentation for guiding model use, including user requirements, such as the 
following: 

 

(1) The architecture required for using the model. 
 
(2) Setting up and using the model. 
 
(3) Limits of model use (as constructed, due to implementation choices or 
mechanisms). 

 
(4) Required training for model use. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

61 of 157 

 
5.4.2 Considerations in Model Construction 
 
To allow the greatest flexibility in model implementation, the model design (produced in Phase 
B) should contain conceptual models, or diagrams, and requirements or specifications that are 
not implementation specific.  It is during implementation (construction) that specific choices are 
made, such as what tools (e.g., COTS packages) or specific implementation methods (e.g., the 
specific method of numerically integrating differential equations) to use in the final model.  All 
tools used in the construction of the model are to be evaluated (e.g., with respect to their effect 
on the model, its use, and the results from model use) as part of the verification and validation 
credibility factors, as discussed in NASA-STD-7009A, Appendix E.3). 
 
Attention is also to be given to distribution of the model for future purposes (including testing) or 
to customers (including cost and delivery mechanisms). 
 
5.4.3 Products and Expected Outcomes of the Model Construction Phase 
 
The following items should be produced when the Model Construction Phase is complete: 
 

a. Model Implementation (Development) System (e.g., specific computers and software). 
b. Model (from Model Design). 
c. User’s Guide (1st Draft). 
d. Verification Test Procedures and Test Suites. 
e. Validation Test Procedures and Test Suites.  

 
5.5 
Model Testing and Release (Phase D) 

 
The Model Testing Phase of the M&S life cycle checks the model (and M&S system) to 
determine if it meets all requirements and operational intensions, and, if successful, releases the 
model for use.  This phase uses the latest updates to the following products: 
 

a. Statement of Intended Use. 
b. Outcome of the Criticality Assessment. 
c. M&S architecture, requirements, and specifications. 
d. Model (implemented from Model Design Phase). 
e. User’s Guide (1st Draft). 
f. Verification Test Procedures and Test Suites. 
g. Validation Test Procedures and Test Suites. 

 
Note:  During the course of verification and validation, include the evaluation of any tools for 
model construction or use for their potential influence on M&S results credibility. 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

62 of 157 

5.5.1 Activity Precedence for Model Testing and Release 
 
This phase of the M&S life cycle distinctly and separately accomplishes the activities of 
verification, (empirical) validation, and model release for use. 
 
These activities are shown in the preferred order of occurrence, as the most effective and, 
arguably, most efficient.  While model release is obviously the last activity in the development of 
an M&S, the accomplishment of verification and (empirical) validation are often reversed or 
(somewhat) combined.  Validating the model without prior verification: 
 

a. Assumes the model is working correctly. 
 
b. Will not establish a reliable basis that the model will work for any scenario other than 
those used for validation. 

 
c. May lead to an erroneous conclusion regarding the cause of an apparent model-
referent mismatch, as determined by validation, specifically that the model design (or concept) is 
at fault when the mismatch is actually due to errors in model implementation (construction). 

 
d. May result in falsely concluding that the model is valid when, in fact, all model errors 
have not been identified and accounted for as part of the model-referent comparison. 
 
Attempting empirical validation prior to full model verification is a highly risky practice, is to be 
avoided, and induces inefficiencies requiring repeated verification and validation cycles.  With 
some types of models, the process of validation includes some parameter calibrations, which are 
dependent on a fully functional and verified model. 
 
Figure 6, General Flowchart for M&S Development, which is taken from the ASME Guide for 
V&V in Computational Solid Mechanics, depicts the preferred sequence of events, with 
verification (shown separately as code verification and solution verification) down the left-hand 
side of the flowchart, preceding empirical validation (simply labeled as validation) at the bottom-
center of the flowchart.  The activities down the right-hand side of the flowchart are related to 
conducting physical experiments with the RWS (or an acceptable surrogate) in order to obtain 
the referent (data) necessary to accomplish empirical validation.  Quantification (or 
characterization) of uncertainties is a key step in each of the parallel activities (model 
verification and physical experimentation). 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

63 of 157 

                   
     

Guide for verification and validation in computational solid mechanics. American Society of 
Mechanical Engineers, ASME Standard V&V 10–2006, New York, NY. 

Figure 6—General Flowchart for M&S Development 

 
Whenever possible, incremental verification and validation of models is best accomplished in 
parallel with the development, integration, and test of the RWS.  Waiting until later in the RWS 
development life cycle, when the RWS is at higher levels of assembly and many complex 
interactions are present, poses more significant challenges to model testing.  Insight regarding 
behaviors and properties of the RWS, and regarding the corresponding representation in the 
models, is more readily obtained when model V&V occurs at lower levels of assembly.  The 
trust gained in knowledge of these behaviors and properties allows them to be “locked down” in 
the model as the model itself grows in size and complexity to match the RWS, generally 
simplifying subsequent V&V efforts tied to tests performed at larger RWS levels of assembly.  


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

64 of 157 

The generic model V&V flow illustrated in Figure 6 will then, in practice, be executed multiple 
times throughout the RWS life cycle, in parallel with its own Integration and Test (I&T) flow. 
 
5.5.2 Model Verification (What is Verification?) 
 
Model verification is the process of determining the extent to which an M&S is compliant with 
its requirements and specifications as detailed in its conceptual models, mathematical models, or 
other constructs.  Code (software) and solution (calculation) verification are key aspects of the 
overall verification process.  The M&S can be considered verified when the following three 
conditions are satisfied: 
 

a. The (computational) model meets its specifications.  These (software) specifications 
start with the conceptual/mathematical model and include additional requirements for functions, 
e.g., user interfaces and data I/O. 

 
b. All significant sources of numerical errors inherent in the (software) implementation 
are identified, quantified, and within assigned upper bounds. 

 
c. Evidence is gathered to address the following, or justify why they are not addressed: 

 

(1) The actions demonstrating, and the results showing, the model functions as 
intended, as specified by the conceptual model or other model requirements 
document. 

 
(2) The processes used in, and the results obtained from, quantifying numerical errors 
resulting from the software algorithms. 

 
(3) The processes used to quantify numerical errors resulting from factors such as 
sampling or quantization, the step size chosen for the numerical integration of 
differential equations in a time-domain simulation, and the methods and intervals 
used for interpolation of model parameters, and the results. 

 

5.5.2.1  
Accomplishing Model Verification (What is Done in Verification?) 

 
The following are needed to begin model verification: 
 

a. The defined objectives and requirements for verification [M&S 8] (4). 
b. The model design (specifications, requirements, conceptual models, etc.). 
c. The implemented model. 

 
The first task during verification is to establish the official (formal) plans and procedures for 
verification, which may be provided by the Model Design or Construction phases (Phases B or 
C).  These expound upon what is needed to accomplish verification and what exactly will be 
accomplished (inspected, demonstrated, or tested) during verification.  The actual task of 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

65 of 157 

verification then confirms the implemented model includes or addresses the objectives, 
requirements, and design. 
 
5.5.2.2  
Considerations in Model Verification (What is Considered During Verification?) 

 
The term “verification” is generally accepted to refer to two related processes:  Implementation 
(code) verification; and solution verification (or calculation verification).  These processes are 
designed to demonstrate that the implemented model (software) performs correctly. 
 

a. Code verification is the process by which the structure, flow, and fidelity of the 
(computational) model are demonstrated to be correct with respect to its intended purpose (in 
accordance with the specifications).  The first step is to ensure, structurally, by inspection that 
the model contains all the components, or elements, it is supposed to have, and nothing more.  
Verification of computational model structure or flow is performed first by code tracing and then 
unit testing, i.e., running the M&S through a series of low-level tests, and comparison of the 
implemented (coded) model with the conceptual/mathematical models.  Some, if not all, of the 
tests should be re-run any time the model (code) is changed (a process known as regression 
testing) either to fix errors or to add new functionality to ensure the changes do not introduce 
new errors.  This topic also addresses the issue of model (code) coverage, i.e., the percent of 
relevant logical branches within a model (code) tested for proper numerical and logical 
execution, as well as the handling of “hard” errors such as floating point exceptions.  The latter is 
an example where the code can produce unexpected results, including halting execution, due to 
misevaluation of conditions (branches, loops) at the boundaries of the condition parameters. 

 
b. Solution (Calculation) verification encompasses efforts to assess (computational) 
model correctness and numerical accuracy, most importantly when closed-form solutions are 
unavailable and therefore approximations are required to solve the problem at hand.  Independent 
of whether the solution is closed-form or approximate, finite precision effects such as 
underflow/overflow, rounding, and loss of precision still will contribute to accuracy/uncertainty 
in the results and needs to be evaluated.  For the case of approximate solutions, additional 
sources of error come into play.  The process of identifying and evaluating the contribution of 
these sources typically involves a systematic sensitivity analysis of parameters and behaviors 
associated with the design and implementation of the model, as opposed to the parameters and 
behaviors associated with the RWS itself.  Examination of the latter is, instead, the focus of 
Sensitivity Analysis (section 5.6.3.1.3).  Examples of model-specific parameters to be varied 
during the solution verification process include iterative solver tolerances and sampling intervals 
(e.g. temporal sampling for integration of differential/difference equations in time-domain 
models, or spatial sampling for geometric mesh and ray-trace models).  Ideally, these parameters 
are varied until the solution is stable, i.e., it appears to have converged at an asymptotic limit.  
However, it is important to understand that stability/convergence of the numerical solution is no 
guarantee that the model meets accuracy requirements – this cannot be determined until 
Empirical Validation (section 5.5.3) is complete. The final choice of the model-specific 
parameters generally involves a trade between accuracy and run-time efficiency, where it is not 
uncommon for a non-minimal numerical error to be accepted in order to achieve an acceptable 
run-time.  In such a case, the difference between the apparent stable (asymptotic) solution and 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

66 of 157 

the solution obtained using the accepted values of the model-specific parameters is factored into 
Uncertainty Characterization (section 5.6.3.1.2). 
 
Note:  An additional context for solution verification is not associated with M&S development 
testing (verification), but rather with M&S use (or execution) and is commonly called input 
verification (section 5.6.2.2). 
 
5.5.2.3  
Products and Expected Outcomes of Model Verification 

 
The positive outcome from verification is that the model is implemented according to design, 
including the following:   
 

a. Everything that is needed is in the model (per the Design) and nothing more. 
 

(1) Constituent parts (model elements/functions) are included. 
(2) Parts are “interconnected” appropriately (by Design). 
(3) Nothing extra is in the model that is not in the Design. 
(4) Logic paths work per Design. 
(5) Functions work per Design. 

 
b. Verification Scenarios (above) work as expected. 
 

(1) Results produced correctly for defined (test case) scenarios. 
(2) Numerical errors are identified/quantified/bounded. 
(3) Uncertainties are identified/qualified/quantified within defined expectation. 

 
If deficiencies are found during verification, re-work or even re-design of the model may be 
needed. 
 
Once verification is successfully completed, the domain of verification is to be documented per 
[M&S 16] and a suite of plans, procedures, and test cases can be archived for use in future 
regression testing of the model from the perspective of verification. 
 
5.5.3 Model Empirical Validation 
 
Empirical validation is the process of determining the degree to which a model or a simulation is 
an accurate representation of the real world from the perspective of the intended uses of the 
M&S, using pre-defined and accepted requirements as to what constitutes “favorable 
agreement.”  Correlation and calibration (tuning) of the model are key aspects of the empirical 
validation process.  Ultimately, and most importantly, validation determines the accuracy, 
precision, bias, sensitivity, and uncertainty of the model, and ensures these metrics satisfy any 
and all associated requirements.  This is based on comparisons between the simulation 
(computational) results and some corresponding referent.  Validation also addresses uncertainties 
arising from both experimental and modeling (computational) procedures.  The term 
“uncertainty” is used in a general sense and can comprise a number of related terms, including 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

67 of 157 

the concept of error.  The M&S is considered validated when the following conditions are 
satisfied: 
 

a. The (computational) model meets pre-defined criteria for matching RWS behavior 
(i.e., within accepted bounds of uncertainty). 

 
b. The uncertainties in the model and propagated into model results are understood. 

 
5.5.3.1  
Accomplishing Model Empirical Validation 

 
To begin model validation, the following are needed: 
 

a. The defined objectives and requirements for validation [M&S 8] (4), including the 
criteria for RWS similarity (i.e., criteria for achieving “favorable comparison” between model 
and referent, when performing empirical validation). 

 
b. The implemented model (preferably verified; see section 5.5.2). 
 
c. Test cases (scenarios) from the RWS, or an acceptable referent thereof, with requisite 
data.  The scenarios to be identified, addressed, and taken into account include: 
 

(1) Normal operating environment(s). 
 
(2) Emergency, abnormal, and off-design operating environments. 
 
(3) Testing environment(s). 
 
(4) Expected inputs and excitations to the RWS being modeled. 
 
(5) Possible unintended and unexpected inputs and excitation to the RWS (including 
human operator inputs and human-in-the-loop influences and effects). 

 
(6) Non-operational environments and processes for the RWS, including inspections, 
repairs, maintenance, storage, transport, and testing. 

 
(7) Operational processes. 
 
(8) The transitions between the different environments, processes, excitations, and 
inputs listed above. 

 
Identifying, addressing, and accounting for all scenarios for empirical validation testing are 
critical because the RWS will almost certainly be exposed to and influenced by a wide variety of 
environments as well as internal and external excitations and inputs.  These environments, 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

68 of 157 

inputs, and excitations can be, and often include those that are, unexpected, unintended, or far 
outside or far more severe than normal operating conditions. 
 
The RWS scenarios established for, and then executed during, empirical validation testing in turn 
determine and establish the “Domain of Validation,” notionally illustrated in Figure 7 and also 
known as the “Validation Domain” [M&S 18]. 

 

Figure 7—Domain of Validation 

(Trucano, T. G., M. Pilch, and W. L. Oberkampf (2002). General Concepts for Experimental 
Validation of ASCI Code Applications. SAND2002–0341, Albuquerque, NM, Sandia National 
Laboratories) 
 
As previously shown in Figure 6, there are two parallel processes that precede (empirical) 
validation.  One is the verification of the model or the M&S and the other is verification of 
empirical methods and processes to acquire resultant data from the referent, where both include 
the verification of resultant data and their associated uncertainties or errors.  Section 5.5.2 
describes the requirements for model (or M&S) verification. 
 
As previously stated, empirical validation includes the correlation and calibration sub-processes. 
These are depicted in Figure 8, Empirical Validation Process, Including Correlation and 
Calibration.  NASA-STD-7009A provides the following definitions: 
 

Calibration:  The process of adjusting numerical or modeling parameters in the model 
to improve agreement with a referent.  Note: Calibration can also be known as 
“tuning.” 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

69 of 157 

 

Correlated (as in an M&S correlated with a RWS):  The extent to which an M&S and 
RWS, or some aspect of an M&S and RWS, behave similarly due to a particular 
change in some set of input variables, parameters, perturbations, etc. 

 
 

 

Figure 8—Empirical Validation Process, Including Correlation and Calibration 

 
Assuming the model is verified, if the correlation and calibration efforts cannot achieve the 
required match between model and referent, then the model form itself is suspect, necessitating 
that the conceptual model, its assumptions, and design be revisited.  Obtaining good correlation 
between predictions from the M&S and measurements from the RWS (or independent 
predictions in some cases) over the widest range of parameter space, initial conditions, boundary 
conditions, and modes of operation is desirable to maximize confidence.  However, this is not 
always possible or affordable.  The pre-defined acceptance criteria for the M&S [M&S 8] (1) 
identifies the conditions the program/project is to satisfy to achieve a favorable comparison 
between the M&S and the referent. 
 
Once validation is successfully completed, the Domain of Validation is to be documented per 
[M&S 18] and a suite of plans, procedures, test cases, and referent data can be archived for use 
in future regression testing of the model from the perspective of validation. 
 
5.5.3.2  
Considerations in Model Empirical Validation 

 
A review of the validation process and results should address the following questions: 
 

a. What was the referent? 
 
b. What are the significant similarities and differences of: 
 

Calibration
Correlation

M&S

Referent

Favorable 

Comparison?

Return to Model 

Concept 

Development

Yes

No

Done… M&S 

ready for 
release


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

70 of 157 

(1) The referent with respect to the RWS? 
(2) The M&S with respect to the referent? 
(3) And, therefore, the M&S with respect to the RWS? 

 
c. Is the data obtained from the referent compatible with or convertible to data required 
to correctly validate the M&S? 

 
d. Which uncertainties in the simulation and referent, e.g., numerical error, input data 
variability, measurement error, were considered when comparing the simulation output to the 
referent? 

 
e. What model or input data calibration (tuning, adjustment) was performed so that 
agreement between the referent and the predictions met the requirements for the intended use of 
the model?  Was this justified? 
 
Note:  Calibration can be difficult for complex simulations, e.g., those for flight.  There could be 
hundreds of changes needed to tune the model to match the RWS.  Conversely, one change could 
make a good match for one scenario but could cause an issue for other scenarios.  For some 
modeling techniques, such as machine learning surrogates, it is possible to overfit the validation 
data such that the model only produces good results within the validation set but poor results for 
other inputs.  One can avoid overfitting by using only a portion of the validation data to tune the 
model and retain the rest of the validation data to validate the tuning.  It is also possible for 
tuning to result in a model with bias if the validation data itself exhibits bias and is not fully 
representative of the application domain. 
 
When reviewing the validation activities for a given M&S, identifying known differences 
between the referent and the RWS is important (Figure 9, RWS to Referent Similarity).  A 
referent may be the RWS to which the analysis is directed, or it could be a similar or analogous 
system, whereby the closeness of the referent to the RWS becomes pertinent.  Therefore, the 
source of referent data obtained empirically from an experiment, a series of experiments, 
simulated RWS, sections or segments of an RWS, actual RWS in simulated environments, or 
RWS in the actual environment needs to be verified with the same level of rigor used to verify 
the M&S.  Appendix B provides further details describing the importance of referent similarity 
to the RWS.  For a detailed case study to illustrate the importance of properly verifying the 
empirically acquired data used for model validation, refer to Oberkampf and Roy (2010), 11.2 
through 11.4. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

71 of 157 

 

Figure 9—RWS to Referent Similarity 

 
An essential outcome and product of empirical validation is the criteria used to determine and 
then establish whether or not an M&S is a “good,” “good enough,” or “value-added” tool for the 
project or program it is supporting.  To be effective, these criteria are to be established at or 
before the start of empirical validation, so that the actual validation testing processes and 
resulting data and information do not lead to biases in deciding what is acceptable versus 
unacceptable, especially for situations where resource constraints can influence key decision 
makers. 
 
Validation also addresses uncertainties arising from both experimental and computational 
procedures.  The term “uncertainty” is used in a general sense and can comprise a number of 
related terms, including the concept of error.  These uncertainties or errors are also used in 
establishing the criteria for RWS similarity, as they ultimately provide the quantitative 
information necessary to determine whether or not the M&S is sufficiently similar to the RWS 
being modeled.  Establishing allowed or acceptable uncertainties is also to be completed before 
validation testing is started to avoid the decision-making biases mentioned in the preceding 
paragraph. 
 
5.5.3.2.1 Uncertainty/Error Bounds for Empirical Validation 
 
The uncertainties or errors associated with data and results acquired from both the M&S and 
referent are necessary for proper and complete empirical validation of an M&S.  These provide 
the quantitative information necessary to determine whether or not the M&S is sufficiently 
similar to the RWS being modeled.  As a first step, visual inspection of the graphically plotted 
data from an M&S with uncertainty bounds should significantly overlap with the related referent 
data with uncertainty bounds, in order for the model to be presumed valid.  While this can be 
acceptable for a quick look when comparing data, statistical tests (e.g., the t-test) provide more 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

72 of 157 

reliable and objective indicators of acceptability, especially for plots with limited overlap.  This 
comparison is notionally depicted below for two scenarios. 
 
Figure 10, Simple Comparison of Uncertainty Bounds Between M&S and Referent, shows the 
simplest case where the uncertainty bounds about a single referent (data) response quantity are 
compared against the uncertainty bounds about the corresponding M&S response quantity. The 
M&S would likely be considered valid, certainly by casual inspection.  In the case of demanding 
statistical criteria, e.g., “99 percent confidence that the error is less than 1 percent,” then perhaps 
not.  
 

 

Figure 10—Simple Comparison of Uncertainty Bounds Between M&S and Referent 

 
At best, the outcome of the scenario depicted in Figure 10 is “point validation,” as it is simply 
the favorable comparison between a single model response to a single measurement, for a 
common set of inputs (conditions).  The objective of empirical validation is to establish the 
Domain of Validation, as discussed in section 5.5.3.1, which is a region in parameter space 
enclosing all points at which validation is successful.  This is accomplished by varying the inputs 
to both the test and the model, obtaining the corresponding responses for all inputs, and assessing 
validity of the model at each point.  Figure 11, Comparison of Uncertainty Bounds Between 
M&S and Referent over Range of Input Values, depicts this scenario, for the case of a single 
model/test input, and illustrates that the overlap between the uncertainty bounds can change as 
the input varies over its range.  Over most of the range in this example, the uncertainty bounds 
for the M&S lie within the empirical uncertainty bounds.  However, at the far right end of the 
data set, the uncertainty bounds for the M&S exceed the upper bound of the data.  Over this 
upper range, the acceptance or use of model results warrants more caution. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

73 of 157 

 

Figure 11—Comparison of Uncertainty Bounds Between M&S and  

Referent over Range of Input Values 

 
For the M&S, it is absolutely essential for uncertainties (or error bounds) of all input data, the 
propagation of uncertainties through M&S execution, and uncertainties of intermediate and end-
resultant data produced during M&S execution be documented and fully traceable to the 
governing equations and solution methods incorporated in the model.  It is also essential for the 
governing equations and solution methods, with their derivations, be documented; these include 
equations that are derived from governing equations to model the uncertainty propagations. 
For empirically acquired data from the referent, it is absolutely essential for uncertainties (or 
error bounds) of all data obtained from instrument measurements and the propagation of 
uncertainties through conversion and manipulation of instrument measurement data to usable 
data for M&S validation be documented or fully traceable to the governing equations and 
solution methods.  As with M&S uncertainties, it is also essential for the governing equations 
and solution methods, with their derivations, be documented.  These include equations that are 
derived from governing equations to model the uncertainty propagations. 

 

5.5.3.2.2 Limits of Validated Model 
 
The Domain of Validation is the region enclosing all sets of model inputs for which the M&S’s 
responses compare favorably with the referent.  Ideally, the limits of model use are to be 
contained within this domain, but there are many situations, mainly in exploration and research 
and development activities/projects/programs, where a model is to be used for a RWS that is, or 
is operating, outside this domain.  When an M&S is used in scenarios outside its Domain of 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

74 of 157 

Validation, the model fidelity as governed by the underlying physics, solution methods, all error 
sources, and performance of the respective model, plus the associated uncertainties of resultant 
data produced by the M&S, becomes increasingly important.  In these situations, expanding the 
Domain of Validation to the maximum possible extents through further validation testing should 
be pursued at every opportunity. 
 
The final Domain of Validation, initially described in section 5.5.3.1, shall be established and 
documented at the completion of empirical validation of the M&S.  The scenarios described in 
this section and selected for validation testing establish this Domain of Validation.  The initially 
prescribed Domain of Validation will likely be revised due to the iterative process associated 
with empirical validation.  The tracking and documentation of these revisions are essential to 
correct and complete empirical validation of an M&S, which includes a traceable documentation 
trail or records that others can use effectively for future projects, programs, activities supported 
by M&S. 

 

Note:  If the use of a model predicts beyond the range of currently existing empirical data 
and is subsequently proven correct with new ‘operational’ data, then the domain of 
validation for that model can be justifiably updated.  A model developed for long-term use 
on a RWS will likely have its domain of validation updated. 

 

As an example of empirical validation, accurate prediction of the power available from the solar 
arrays on the International Space Station (ISS) requires modeling of the location and amount of 
shadowing on the arrays.  Analysis tools are available to predict array shadowing and its impact 
on the solar array current; these tools include several key assumptions, such as lower fidelity 
geometry models of ISS, minimal Sun subtense angle effects, and minimal reflected energy from 
adjacent hardware.  With these differences between the model and the RWS, the model’s results 
were compared with on-orbit flight video stills and flight telemetry, showing the model produces 
a good representation of the RWS (Figure 12, ISS Power Prediction). 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

75 of 157 

 

Figure 12—ISS Power Prediction 

(NASA TM-2002-211715, IECEC-2002-20113, "Comparison of ISS Power System 
Telemetry with Analytically Derived Data for Shadowed Cases", Fincannon, H. James) 

 
For this example, the M&S would be assessed to satisfy all requirements to achieve a Level 4 
credibility score for the validation factor:  (1) M&S results compare favorably to measurements 
on the RWS in its operating environment; (2) validation points completely span the domain of 
operation for the RWS; (3) favorable comparisons are obtained for all response quantities. 
 
5.5.3.3  
Products and Expected Outcomes of Model (Empirical) Validation 

 
The positive outcomes from validation are:   
 

a. The model behaves similarly to the RWS. 
 

(1) The operating conditions for which the model is determined acceptable when in 
use (e.g., domain of validated use). 
 

(2) Within defined uncertainty/error bounds 

 

b. The validated uses of the M&S are determined [M&S 18]. 

 
If deficiencies are found during validation, re-work or even re-design, and probably re-
accomplishment of verification and validation, of the model may be needed. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

76 of 157 

 
5.5.4  Model Release 
 
Model Release is the process of establishing the baseline and controlled version of the model and 
associated key documentation for use, including permissible uses for the model and guidance for 
proper use (e.g., User’s Guide).  All requisite development artifacts are to be archived when the 
model is released for use.  After release, changes to the baseline are to be evaluated, justified, 
and authorized with traceability prior to implementing and releasing the revision. 
 
5.5.4.1  
Accomplishing Model Release 

 
Along with the release of the model, the M&S requirements, designs, test procedures, test 
reports, and model correlation reports are baselined as approved, built, or run.   
 
Permissible uses of the M&S are documented per [M&S 14] in NASA-STD-7009A, along with 
guidance on appropriate ways (methods) in which to use the model (NASA-STD-7009A, section 
4.2.2e) and the specifics of model calibrations (NASA-STD-7009A, section 4.2.2f).  The criteria 
for determining permissible uses of an M&S include: 
 

a. Intended use [M&S 8(2)]. 
b. Abstractions [M&S 11]. 
c. Assumptions [M&S 11]. 
d. Limits of operation [M&S 13]. 
e. Domain of verification [M&S 16]. 
f. Domain of validation [M&S 18]. 

 
5.5.4.2  
Considerations in Model Release 

 
All final artifacts from model development are to be archived, if not previously accomplished. 
 
Requirement changes are evaluated, justified, and authorized with detailed designs that are 
implemented with traceability, and versioned iterative tests that contain unique version 
identifiers.   
 
A user’s guide is released along with the model.  Refer to Appendix C. 
 

5.5.4.3  
Products and Expected Outcomes of Model Release 

 
At the conclusion of model release, all of the products and expected outcomes from verification 
and validation are to be available, and archived as necessary, along with the following: 
 

a. The formally released model. 
b. Documented permissible uses. 
c. M&S User’s Guide (Final). 
d. Procedures for M&S Use. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

77 of 157 

 
5.6  
Model Use (Phase E) 

 
The Model Use Phase of the M&S life cycle is composed of the model pre-use, model use, and 
model post-use sub-phases.  This section discusses each of these sub-phases in the context of the 
requirements and recommendations provided in NASA-STD-7009A, along with examples to aid 
the explanations. 
 
The Model Use Phase uses the latest updates to the following products: 
 

a. Formally released model. 
b. Statement of Intended Use. 
c. Outcome of the Criticality Assessment from model development. 
d. Documented Permissible Uses. 
e. M&S User's Guide (Final). 
f. Procedures for M&S Use. 
g. Proposed Use (obtained at any point prior to commencing with the Model Use Phase). 

 
5.6.1 Model Pre-Use  
 
The model pre-use sub-phase prepares for model (or M&S system) use and is composed of three 
primary activities: 
 

a. Ensuring readiness for model use. 
b. Assessing the proposed use of a model. 
c. Preparing input scenario definition and pedigree assessment. 

 
5.6.1.1  
Readiness for Use 

 
Aspects of readiness for M&S use focus on the M&S users/analysts, the processes and 
procedures for M&S use, and the criticality associated with M&S use. 
 
Before using the M&S, the user/analyst should be reasonably familiar with the M&S and the 
associated disciplines incorporated.  While there are occasions when the M&S developer also 
fulfils the role of M&S user/analyst, this is not always the case; therefore, the roles are 
considered as distinctly separate.  Except in the most trivial cases, it is advantageous, even for 
the M&S developer, to consult recommended practices and the M&S User’s Guide when using 
the M&S. 
 
Ways for the User/Analyst to prepare for using the M&S are: 
 

a. Identification and familiarization with recommended practices for the type of M&S in 
use (see the potential recommended practices in section 4.1.3 of NASA-STD-7009A). 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

78 of 157 

b. Training associated with specific M&S or, more generally, with the type of M&S (see 
the potential recommended training areas in section 4.1.4 of NASA-STD-7009A). 

 
c. Thoroughly understand the user’s guide for the specific M&S, if one is available (per 
Recommendation section 4.2.2e of NASA-STD-7009A).  Suggested content for the user’s guide 
is in Appendix C.  As a minimum, the following information about the M&S is to be well 
understood: 

 

(1) Assumptions and abstractions underlying the M&S, including their rationales 
[M&S 11] in NASA-STD-7009A. 
 

(2) Basic structure and mathematics of the model (e.g., equations solved, behaviors 
modeled, and conceptual models) [M&S 12]. 

 
(3) Limits of operation (e.g., boundary conditions) of models [M&S 13]. 
 
(4) Permissible uses of the M&S [M&S 14]. 

 
The processes and procedures for using the M&S are best established before concluding M&S 
development in Model Phase D; but if that has not occurred, they can also be established at the 
beginning of Model Phase E (recommendations are sections 4.1.2c and 4.3.2e of NASA-STD-
7009A). 
 
Reviewing or re-accomplishing the criticality assessment for the M&S during use preparations 
helps ensure the appropriate level of rigor is attained or maintained in keeping with the 
criticality. 
 
5.6.1.2 
Use Assessment 

 
Before or during the preparation for M&S use, the specific use is to be proposed, documented 
[M&S 22], and assessed [M&S 23] with respect to the permissible uses accepted and 
documented at the conclusion of M&S development [M&S 14] to determine if the M&S are 
appropriate and either within or outside the known acceptable uses of the M&S. 
 
The permissible uses were defined during the M&S Development phase and baselined during 
M&S release (section 5.5.4.1).  For M&S developed for broad or general use, even within a 
specific type of application, the permissible uses are key to correct or appropriate use.  However, 
even for M&S developed only for a specific real world system, the permissible uses provide a 
clear guideline as to what or how the M&S are appropriately applied.  In either case, the 
elements of a proposed use are to address similar criteria as the permissible uses.  Table 6, M&S 
Use Assessment, depicts these similar elements for comparison in the use assessment. 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

79 of 157 

Table 6—M&S Use Assessment 

Permissible Use(s) of Model

Proposed Use(s) of Model

Type of Use Intended.

• Implies the Type of Model. 
• The application domain 
(discipline, area of study) of the 
Model. 

• The Purpose of the Model. 

Type of Use Needed.

• Implied by the type of RWS. 
• The application area (discipline, 
area of study) of the subject 
RWS. 

• The purpose of proposed model 

use with respect to the RWS.

Model’s Abstractions and Assumptions.

• Inclusions in the M&S. 
• Exclusions from the M&S. 
• Assumptions of M&S form, fit, 
or function. 

Inclusions & Fidelity Needed.

• Specific expectations of what is 
in, or expected of, the M&S. 

• The desired level of accuracy, 
precision, & uncertainty of the 
M&S.

Limits of Model Parameters, per

• Model design (including any 
computer H/W or S/W 
limitations). 

• Verification. 
•
Validation.

Desired Domain of Use.

• With respect to the RWS. 
• Parameter values the model is 
expected to represent. 

Types of Outputs (Results) Produced, 
including: 

• Accuracy. 
• Precision. 
•
Uncertainty.

Type of Results Needed, including:

• Accuracy. 
• Precision. 
• Uncertainty of Results.  

 
An example of the assessment of assumptions, as part of the use assessment, is in computational 
fluid dynamics, where a gas is modeled as a thermodynamically perfect gas, approximating the 
behavior of molecules in a gas.  This modeling approach is applicable in many subsonic and low-
supersonic external flow regimes.  However, extending this approach to high-temperature flows, 
such as planetary entry simulations, may not be appropriate as the assumptions of a perfect gas 
model can be violated due to real gas effects.  In such a case, the use of the model is to be limited 
to subsonic and low supersonic external flow regimes.  This limitation, and associated rationale, 
should be succinctly described. 
 
5.6.1.3 
Input Scenario Definition and Pedigree 

 
Configuring a model for a particular use includes defining the scenarios to run and setting up the 
model to implement those scenarios.  The scenarios to employ during use are sequences of 
events or sets of conditions (e.g., parameter values) that define or control the function of a model 
during use, which are subject to assessment for the input pedigree credibility factor. 
The inputs to a model are dependent on the type of model of analysis employed, such as material 
property data for a structural model, atmospheric data for a trajectory model, or arrival and 
process times, event probabilities, and resource quantities and schedules for a process model.  


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

80 of 157 

The credibility of input data typically depends on traceability to a RWS, accuracy of the data, 
and known uncertainty. 
 
The input pedigree factor strives to address the adequacy or quality of the inputs to the model, 
including their completeness, breadth, and accuracy for a particular use. Models are generally 
considered as encapsulations of certain system characteristics (Figure 5, General Model Diagram 
with Nondeterministic Elements) to which a set of data is applied for a specific analysis. The 
input to a model broadly refers to the data used to obtain simulation and analysis results. The 
input does not address the model mathematics or structure, the processing of information within 
the model, or statements of uncertainty accompanying the results. The data can, however, 
include specific modifying parameters, with or without uncertainty, to the model or be used to 
set up and initialize the model. 
 
Even an imperfect input can be used in a critical analysis, but only if the associated uncertainty is 
identified.  The central idea of input pedigree is to clearly communicate the credibility of the 
input used in the analysis based on various attributes of the data used, including the source, 
quality, diversity, and quantity of the data, as well as the form of the input used.   
 
5.6.1.3.1 Source of the Input Data 
 
The goal for the input data used in any analysis is that it originates from an authoritative source, 
which could be: 
 

a. An SME. 
b. A credible document, e.g., project documents or journal articles. 
c. Test results. 
d. Operational data. 
e. Another model. 

 
5.6.1.3.2 Quality of the Input Data Source 
 
The quality characteristics of M&S input may span the range between subjective and objective, 
such as: 
 

a. Notional:  An uninformed or hypothetical estimate. 
 
b. Informed:  An educated or experienced estimate (minimum, most likely, or 
maximum). 

 
c. Specified:  From system requirements. 
 
d. Derived:  From knowledge or calculation from the general physical characteristics of 
the system (a value or expression from given or known set of data). 

 
e. Measured:  From direct knowledge (empirical readings) or calculation from the actual 
RWS. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

81 of 157 

 
Understanding the data quality is critically important to the credibility of an analysis and spans 
the full spectrum from low (notional) to high (officially accepted operational or test data).  The 
most authoritative sources are officially designated and documented, while less authoritative 
sources are not quite so formal.  Less formal sources are not necessarily inferior; the intent of 
this qualification of the data source is to clearly understand where the data originates and 
whether it is a good source. 
 
Test data can be superior to historical or quality record data, but should be used cautiously as the 
use case, RWS, assumptions and external factors may have been significantly different.  Test 
data obtained from a design of experiments generally make it possible to determine means and 
spreads accurately, while data with confusing changes in inputs and multiple outliers can make it 
difficult or impossible to perform rigorous data analysis. 
 
Even data from the best source may not have the highest quality, depending on factors such as 
the life-cycle phase of the RWS and the availability of historical or analogous data.  Early in a 
project’s life cycle, notional data are sometimes used for initial analyses. Whenever notional data 
are used, these data should be clearly noted.  The best case is for analysis accomplished on an 
RWS in operation for an extended time with plenty of officially documented data.  If data are 
obtained from an analogous RWS, then the level of data similarity should be documented.  If the 
data are obtained from another model or analysis, the data credibility is tied directly to the 
credibility of the model or analysis from which the data were obtained.  In such cases, the input 
pedigree credibility level is limited to the credibility level of the model from which the data are 
obtained. 
 
5.6.1.3.3 Diversity and Quantity of Data Source 
 
The basic idea of source data diversity is that data are increasingly and statistically more 
acceptable coming from more than one instance, item, or test.  Information obtained from an 
SME may be simply a single value for a given parameter in a model, e.g., a minimum, an 
average, a maximum, or a range of potential values.  It is better if the source is empirical 
operational or test data. So, even if M&S input data are single (deterministic) values, it is better 
if that value is derived (calculated) from a set of data than from only one value.  Additionally, if 
the data set from which the input is derived includes data from a variety of real world instances, 
then the resulting input will be more representative of the population. 
 
As an example, if the desired input to a model is the processing time for a spacecraft in a 
processing facility, then the input will be more representative of the population if data are 
obtained from multiple spacecraft and various mission flows, i.e., process iterations.  The more 
supporting data for a specific model input, the higher the quality of that particular input.  
Statistically, an average obtained from a set of 50 data points is much better than an average 
obtained from 10 data points.  The same can be said of statistically determined probability 
distributions.  This aspect of the quantity of data directly relates to the upcoming topic of 
uncertainty, with smaller data sets having statistically larger uncertainty than larger data sets. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

82 of 157 

Small sample sizes, particularly in historical data, give relatively inaccurate estimates of the true 
mean and typically underestimate true variability.  For example, the more you drive your car, the 
more likely you are to drive in all types of conditions; if you only measured drive time on a few 
sunny days, the effect of rain is missing. 
 
5.6.1.3.4 Form of Input Used 
 
As implied above, the input used in an analysis can take many forms, from textual to logical to 
numerical or mathematical.  A deterministic (single-valued) input may be obtained directly or 
derived from a set of source data.  If derived, the method of derivation should be made known.   
 
A more interesting and complete analysis may be obtained by using a span of possible parameter 
values in a Monte Carlo run of an M&S.  For example, a model may be run with the values of 
certain parameters stepped through increments from the possible minimum to maximum values 
or using parameter values randomly selected within some number of standard deviations of the 
mean.  Appropriate statistical analysis is to then be applied to the results, and the interpretation 
thereof. 
 
An even better analysis is accomplished using probabilistic parameter values.  If a set of data is 
available for a given parameter, statistical analysis of the data may produce a probability density 
function (pdf) that accurately represents the original data set but in a more general way. 
Stochastic data, or data representing how a process varies over time, are another probabilistic 
source.  Such statistical functions are then used for the parameter(s) in Monte Carlo-type runs of 
the M&S by drawing random variates from the defined probability distribution.  Probabilistic 
and stochastic analyses are more complex, requiring specific statistical methods for analyzing the 
outputs of multiple model runs.  Beneficially, however, the results also include a statistically 
calculated uncertainty.  
 
Models typically use multiple inputs with a variety of pedigrees.  Ideally, the effect of all of the 
inputs is to be considered when determining the overall input pedigree for a given M&S-based 
analysis.  As a matter of pragmatism, a rigorous assessment as to the most influential inputs to an 
M&S is helpful in reducing the effort in this task.  
 
5.6.2 Model Use (Setup and and Execution) 
 
Upon the accepted use of the model, work begins toward setting up and executing (or using) the 
model.  This portion of the Model Use Phase has three primary activities: 
 

a. Model setup. 
b. Model execution (Application). 
c. Sensitivity studies. 

 
5.6.2.1  
Model Setup 

 
Model setup encompasses two primary activities:  Setting up M&S system for use and 
developing the scenarios specific to the desired results expected by the customer.  If not already 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

83 of 157 

accomplished, the equipment (hardware and software) for the model to work is gathered and 
configured for use.  As the particulars for each type or implementation of model varies greatly, 
the user’s guide for the model or model implementation platform (e.g., COTS user’s guide) are 
to be consulted.  Possible model setup choices are shown in Table 7, Model Setup Definition 
Options.  Stochastic models also include other settings and increment the amount of data 
collected for each replication.  The data used to develop input for the model use and the rationale 
for model setup and execution are required documentation per [M&S 24] and [M&S 25], 
respectively, and documentation of any supporting software used in the preparation of input is 
recommended (NASA-STD-7009A, section 4.3.2d).  This helps to create traceability and 
evidence of the operation, which is particularly useful if changes are needed later in the analysis 
and decision making. Process components may include the platform the model was executed on 
(e.g., Window or Linux), the version/revision of any models or software used, compiling options, 
etc.  Model calibrations are considered part of model setup for specific use and also should be 
documented along with the domain of calibration (NASA-STD-7009A, section 4.3.2 c). 
 

Table 7—Model Setup Definition Options 
Run Length.
Animation Run Speed.
Initial Conditions.
Warm-up Period.
Number or Replications.
Start Time.
Stopping Conditions.
Output to collect (e.g., model run statistics).

 
5.6.2.2  
Model Execution (Application) 

 
Once the model is set up, the scenarios are executed.  This can be a very straightforward process, 
if diligent attention was given to setting up the model and developing the set of scenarios to 
execute, including those that provide insight into the sensitivities and uncertainties associated 
with the scenarios.  Often times, the execution of a model takes on a life of its own, with learning 
and adjustments to scenarios occurring in the moment.  It is important in all cases to ensure 
either all executions are conducted within the permissible limits of operation or the results 
placarded for executions outside the permissible limits [M&S 26]. 
 
Another task to accomplish during the course of Model Use, initially discussed in Considerations 
in Model Verification (section 5.5.2.2b), is Solution Verification.  This is similar to what is 
accomplished in verification testing, but for the model’s current use.  Solution Verification is 
used to detect human errors, e.g., typographical errors or other incorrect/inadvertent interactions 
with the software, as well as determine the numerical accuracy of the solution. One common 
method is the echoing of all input data, including selections made by a mouse or other input 
devices, to a log file for comparison with the intended inputs. Confirmation that this or other 
methods were employed is advisable when reviewing M&S results. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

84 of 157 

As such an environment can be very dynamic, it is very valuable to carefully keep track of the 
versions of the various execution results in association with the scenarios that generated them 
(NASA-STD-7009A, section 4.3.2 f). 
 
Warning or error messages that come about during model execution are to be documented and 
explained [M&S 27], and all failure modes, points of failure and associated messages should be 
documented and explained (NASA-STD-7009A, section 4.3.2 h). 
 
5.6.2.3  
Sensitivity Studies 

 
As RWSs in operation can deviate from nominal operating conditions, sensitivity studies with a 
model of the RWS can be quite valuable.  Knowing where a model, and by analogy a RWS, is 
sensitive to changes in operating conditions or parameters provides valuable insight into how 
strictly controls or mitigations must be pursued.  Conversely, studying and analyzing these 
sensitivities also leads to an understanding of model, and, by analogy, RWS robustness (material 
in NASA/SP-2010-576 on robustness is instructive).  It is equally important, during sensitivity 
studies, to stay within the permissible uses of the model (unless such excursions are 
appropriately placarded). 
 
While execution of the model occurs in this sub-phase, the analysis to determine how variation in 
the output of an M&S can be apportioned to different sources of variation in the model input and 
parameters occurs after actual model execution and gathering of data from execution. Variations 
in model input and parameters are best kept within the boundaries of permissible use of the 
model when performing the sensitivity studies. 
 
Documenting the extent and results of sensitivity studies is required [M&S 30], assessed as one 
of the operational factors of results credibility [M&S 31], and reported [M&S 35]. 
 
5.6.3 Model Post-Use 
 
After completing M&S execution, two major steps remain in the Model Use Phase:  
 

a. Results analysis.  
b. Results assessment and reporting.  

 
One major purpose of using an M&S is to generate data to support decisions concerning the 
represented RWS.  Before even proceeding with data analysis, it is prudent to ascertain any 
conditions that may render the results moot.  These potential caveats to analyzing, let alone 
accepting, M&S results are shown in Table 8, Potential Caveats to MS Results.  The existence of 
any of these caveats are to be reported with the M&S results per requirement [M&S 32].  
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

85 of 157 

Table 8—Potential Caveats to M&S Results 

7009 
Requirement 

Reporting Requirement
Do any of 
the following 
exist? (Yes / 
No)

If yes, 
what are 
they? 

Rationale for 
proceeding with 
the reported 
information

[M&S 32]
Caveats

(1)
Unachieved Acceptance Criteria.

(2)
Violation of any Assumptions.

(3)
Violation of the Limits of 
Operation.

(4)
Execution Warning and Error 
Messages.

(5)
Unfavorable outcomes from the 
proposed use assessments.

(6)
Unfavorable outcomes from 
Setup/Execution Assessments.

(7)
Waivers to Requirements.

 
One method to ensure analysis caveats are noted adequately is to add placards to the results 
(Figure 13, Example Placard) per [M&S 26] (2). 
 

 

Figure 13—Example Placard 

 
Another example is to note vehicle configuration differences between the M&S, defined analysis 
scenarios, and the RWS in the caveats. 
 
5.6.3.1 
Analyze Data 

 
Producing results is the most obvious task in any modeling and simulation effort.  However, 
rarely can data from the M&S be used directly in making such decisions, and so the output data 
is analyzed, statistically or otherwise, to support specific decisions.  This analysis of a set or sets 
of data gathered from use of the M&S directly depends on the M&S and the type of information 
needed for application to a RWS.  Clearly understanding, and conveying, what the results 
represent is important (e.g., minimum, most likely, maximum).  The additional tasks of solution 
verification, uncertainty characterization, and sensitivity analysis provide supplemental 
qualifying information. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

86 of 157 

5.6.3.1.1 Uncertainty Characterization 
 
Uncertainty Characterization is the process of identifying sources of uncertainty and describing 
their relevant qualities (qualitatively or quantitatively) in all models, simulations, and 
experiments (inputs and outputs).  The basic premise is that models are abstractions of actual or 
proposed RWSs, which necessarily induce some uncertainty in the model’s ability to replicate 
system behavior.  Uncertainty characterization and quantification are difficult parts of 
understanding any system or model of a system.  Deterministic analyses leave the uncertainties 
unaddressed and provide incomplete or misleading, if not incorrect, results.  Even a 
deterministic, static, model would benefit from a qualitative analysis of uncertainty.  Note:  This 
topic was originally introduced in section 5.2.1.3.3, Nondeterministic Specifications, and 
illustrated in Figure 5. 
 
A synopsis for reporting uncertainty characterization is shown in Table 9. 
 

Table 9—Uncertainty Characterization Synopsis 

7009 Req't
Reporting Req't
Do any of 
the 
following 
exist? (Yes / 
No)

If yes, 
what are 
they? 

Rationale for 
proceeding with 
the reported 
information 

[M&S 33]
Uncertainty in Results

(1)
Quantitative Estimate.

(2)
Qualitative Description.

(3)
No estimate or description 
given.

[M&S 34]
Uncertainty Processes
Processes for obtaining 
Uncertainties in M&S Input.
Processes for obtaining 
Uncertainties in M&S 
Results.
Processes for obtaining 
Uncertainties in Quantities 
Derived from M&S Results.

 
Uncertainty comes in many forms and may present itself in a variety of places relevant to the 
analysis, including the following: 
 

a. System understanding:  How well the system is known. 
 
b. Model building:  What is and is not included in the model. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

87 of 157 

c. Input:  The amount of good, i.e., attributable or authoritative, data available and the 
form the data takes. 

 
d. Running the models:  The setup and initialization parameters for running the model. 
Do they meet the breadth of analyses required?  Are the simulation model scenarios 
accomplished with a well-considered design of experiments?  Are the numerical errors 
sufficiently small? 

 
e. Output analysis:  Does the form of the output portray the breadth of the results 
obtained?  

 
f. Uncertainties are often classified into two separate types: 

 

(1) Epistemic: A lack of knowledge of the quantities or processes identified with the 
system, i.e., subjective, reducible, and may be identified with model uncertainty.  
If the system could be studied more closely, it may be possible to reduce the 
magnitude of the uncertainty. 

 
(2) Aleatory:  The inherent variation in the physical system, i.e., stochastic or 
irreducible.  Systems have inherent differences in their characteristics, which 
may change on a day-to-day (or moment-by-moment) basis. 

 
There are many potential sources of uncertainty in a model, with typical sources listed in Figure 
14, Sources of Model Uncertainty, (Oberkampf, et al., 2002). This figure was made from the 
perspective of models based on PDEs; other types of models will not have some of these sources 
and yet have other sources of uncertainty. The A and E notations in Figure 14 refer to whether 
the uncertainty source is aleatory or epistemic. Furthermore, this figure distinguishes between 
epistemic uncertainties, aleatory uncertainties, and errors; however, errors are a form of 
epistemic uncertainty whether they are quantified or not.  
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

88 of 157 

. 

Figure 14—Sources of Model Uncertainty 

Identifying, quantitatively expressing and correctly classifying uncertainties is often the most 
difficult part of uncertainty characterization. This is because uncertainty is everywhere and many 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

89 of 157 

people are going to have different opinions on uncertainty sources.  Epistemic uncertainty in 
particular is difficult because often times the uncertainty source is not well understood. 
Quantifying epistemic uncertainty is often difficult simply due to the nature of the uncertainty. 
Even SMEs may have varying opinions on the amount of uncertainty present in a particular 
source.  However, when epistemic sources of uncertainty can be identified and their impact on 
M&S results can be quantified, important decisions can be made regarding the mitigation or even 
reduction of these uncertainties.  Proper detail and adequate attention should be given to 
epistemic uncertainties to most effectively guide decision making based on M&S results. 
 
Aleatory uncertainty is typically more straightforward in that variations in physical systems are 
usually obvious and well understood. The only challenge with aleatory uncertainty is actually 
having enough information to support a claim that a particular uncertainty source can be actually 
classified as aleatory (i.e., irreducible). In some cases extensive data taken over very large time 
scales may be necessary to fully understand the uncertainty. Consider variations in atmospheric 
wind profiles. Years of data at even a single, geographical location are needed to glean even 
some sense of the variability. Practitioners are encouraged to use caution when claiming an 
uncertainty source is aleatory. This is typically the easier route in terms of propagating the 
uncertainty and interpreting the results, but incorrect classification and, therefore, treatment of 
uncertainty can produce very misleading results.  
 
Note:  Uncertainty in M&S results may occur in many ways (Table 10).  Generally, M&S results 
uncertainties either come from the model or the input to the model, not necessarily both.  A 
deterministic model with nondeterministic inputs can produce nondeterministic results.  A 
nondeterministic model will always produce nondeterministic results.   
 

Table 10—Uncertainty in M&S Results 

  
Deterministic 

Model

Nondeterministic 

Model

Deterministic 

Inputs

Deterministic 

Results.

Nondeterministic 

Results.

Nondeterministic 

Inputs

Nondeterministic 

Results.

Nondeterministic 

Results.

 
 
On the other hand, with the inevitable analysis of model output, post-processing can produce either 
deterministic or nondeterministic results. 
 
The significance of uncertainty in the results depends on how the results are to be applied in a 
decision situation.  The uncertainty in a given result may not matter in some situations, while in 
others it may imply that the nominal or best estimate result is suboptimal or even questionable.  
In the latter case, if the decision stakes are high enough, additional analysis or testing may be 
appropriate to invest in to reduce the uncertainty.  
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

90 of 157 

The following information should be considered when reporting results uncertainty. For large 
models, it may become necessary to focus on key sources of uncertainty or break the model up 
into components and give “system level” summary of the uncertainty. 
 

a. How were the uncertainties determined? 

 

b. How thoroughly were the uncertainties identified and evaluated? 

 

c. Are the sources documented? 

 

d. What are the sources of the uncertainties? 

 

(1) In the system? 
(2) Included in the model? 
(3) Type of each source (i.e., aleatory vs. epistemic)? 
(4) How well is the uncertainty known? 
(5) Excluded from the model that induces uncertainty? 
(6) In the data for, the parameters of, and the input to the model? 
(7) In the results/calculations of the M&S and analysis? 

 
e. What method(s) were used to quantify uncertainty (e.g., Monte Carlo, test data, or 
Kriging-model-based survey data) including how uncertainty propagates through the model to the 
results? 
 

f. What is the impact of the uncertainty (e.g., on performance metrics)? 

 

g. Is there an Uncertainty Mitigation Plan? 

 
Uncertainty is characterized throughout the life of an M&S.  The model user should understand 
the uncertainties identified during the M&S development process (as identified in NASA-STD-
7009A, section 4.2.7) and document uncertainties introduced during the application of the M&S. 
 
Documentation of uncertainties consists of two parts:  First is the explanation of how 
uncertainties are identified and characterized: 
 

[M&S 28] Shall document any processes and rationale for characterizing uncertainty in: 
(1) The input to an M&S. (2) The results from an M&S. (3) The quantities derived from 
M&S results 

 
The process for characterizing uncertainty could range from very quantitative (i.e., B-Basis 
allowable for a material property) to much more qualitative (such as a rule of thumb Model 
Uncertainty Factor (MUF) applied to analysis results).  Explaining why a particular method of 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

91 of 157 

uncertainty characterization was used informs the overall credibility of the M&S results and may 
also point to ways that uncertainty could be reduced by using other methods of characterization. 
 
The second part of documenting uncertainty is to describe and quantify those particular 
uncertainties: 
 

[M&S 29] Shall document any uncertainties (qualitatively described or quantitative) in: 
(1) The input to an M&S. (2) The results from an M&S. (3) The quantities derived from 
M&S results. 

 
Note that for model use, uncertainty can be found in the inputs to the M&S, the results of the 
M&S, and also items derived from the M&S results.  For example: 
 
A structural analyst is using a FEM to performing an analysis to determine stresses in a structure 
due to thermal loads.  The thermal loads input to the FEM have some uncertainty.  The resulting 
stress values produced from the FEM may have uncertainties due to uncertainties in material 
properties for coefficient of thermal expansion.  Ultimately, the stress results are used to 
calculate margins of safety (MOS) for the structure.  Those derived MOS values could also have 
uncertainty if, for example, the allowable material yield or ultimate stresses are not well 
quantified. 
 
Responsible parties should document any significant physical processes, effects, scenarios, or 
environments not considered in the uncertainty characterization analysis (NASA-STD-7009A, section 
4.3.4 a). 
 
5.6.3.1.2 Sensitivity Analysis 
 
Sensitivity analysis is the study of an M&S’s response to variations in input parameters to 
determine which parameters are key drivers to the M&S’s results.  This analysis is undertaken 
with the results obtained from the sensitivity studies accomplished during the actual execution 
(use) of the M&S.  If the response is negligible, then the M&S (at least in the experimental 
domain), and by inference the RWS, is considered insensitive to those parameters.   
Understanding the sensitivity to input parameters is key to determining the robustness the M&S 
(see Results Robustness factor in NASA-STD-7009A, Appendix E).  On the other hand, if the 
response is not negligible, particularly to minor variations of the input parameters, the M&S is 
considered sensitive and the responsible parameters are key drivers to the model results. 
 
The Results Robustness credibility factor is concerned with how thoroughly the sensitivities of 
the current M&S results are known, with some of these variables and parameters intrinsic to the 
RWS and others intrinsic to the M&S.  Since the model is used to understand how changes in the 
various parameters may impact the RWS, the sensitivities of the model should be similar to the 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

92 of 157 

sensitivities of the RWS (see Note 2 below).  The justification for the evaluation and any 
technical review of Results Robustness is to be documented. 
 
Notes: 
 

(1) NASA-STD-7009A defines sensitivity analysis but only references robustness in 
terms of sensitivity.  This can lead to confusion about both terms, so some 
clarification is provided here.  With respect to systems and models, sensitivity and 
control robustness are opposites.  If a system is sensitive to changes in controlled 
operating parameters or conditions, then it is not considered robust.  On the other 
hand, if the system is found to be insensitive to changes in controlled operating 
parameters or conditions, then the system is considered robust.  Sensitivity analysis is 
the technique that can be used to better understand system robustness. 

 

(2) The closeness of a model’s response to the system’s response should be part of the 
M&S validation effort.  The Results Robustness credibility assessment factor focuses 
on the degree to which sensitivity analyses were accomplished.  If documentation is 
provided comparing the sensitivity of model results to the sensitivity of the RWS, 
then the requirement of NASA-STD-7009A is met. 

 

(3) Sensitivity analysis can also be used early in the RWS life cycle, when limited 
validation data are available, to determine the boundaries for stable system 
performance.  This is also useful when good referent data are not available.  If system 
instability is indicated, then more attention is required to the affected portions of the 
system as it progresses in development (Kelton, et al., 2004).  If system performance 
is adequately stable, i.e., insensitive to small changes in operating parameters, then 
margin may be available as the system design matures. 

 
Additional considerations with respect to these key questions are: 
 

a. What are the significant sensitivities of the M&S results?  

  

(1) Which parameters, when varied, have the largest impacts on the results?   
(2) Do they match the sensitivities of the RWS? 

 

b. How thoroughly are the sensitivities known?   

 

(1) What percentage of parameters have had their sensitivities evaluated? 
(2) How much testing was performed to characterize the sensitivity fully? 

 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

93 of 157 

5.6.3.2 Assessing and Reporting Results 
 
At this point in the M&S life cycle, the results from M&S use are analyzed and ready for 
reporting.  However, merely reporting the results presents an incomplete picture, at best.  The 
requirements and recommendations of NASA-STD-7009A also require the assessment of the 
results as to their credibility and potential risks of accepting them as they are.  Everything that 
has occurred during the M&S life cycle has the potential to impact the acceptability (credibility) 
of the final results of M&S use and risk for the object (i.e., the RWS) of M&S-based analysis.  
Additionally, the reporting of technical review results (Table 11), qualifications of the 
developers, testers, users, and analysts (Table 12), and supporting documentation (Table 13) is 
required. 
 

Table 11—Technical Review Synopsis 

7009 Req't
Reporting Req't
Do any of 
the 
following 
exist? (Yes / 
No)

If yes, 
what are 
they? 

Rationale for 
proceeding with 
the reported 
information 

[M&S 36]
Technical Review
Review
- What was reviewed?
- Depth of Review.
- Formality of Review.
- Currency of Review.
Reviewers
- Expertise.
- Independence.

 
 

Table 12—People Qualifications Synopsis 

7009 Req't
Reporting Req't
Do any of 
the 
following 
exist? (Yes / 
No)

If yes, 
what are 
they? 

Rationale for 
proceeding with 
the reported 
information 

[M&S 37]
People Qualifications
Developers.
Testers.
Users (Operators).
Analysts.

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

94 of 157 

Table 13—Documentation Synopsis 

7009 Req't
Reporting Req't
Do any of 
the 
following 
exist? (Yes / 
No)

If yes, 
what are 
they? 

Rationale for 
proceeding with 
the reported 
information 

[M&S 38]
M&S Documentation 
(Synopsis)

[M&S 6]
Criticality Assessment.

[M&S 7]
M&S in Scope of 7009.

[M&S 9]
Technical Reviews.

[M&S 10]
Relevant Characteristics of 
RWS for M&S Development.

[M&S 11]
Assumptions & Abstractions.

[M&S 12]
Structure & Math of M&S.

[M&S 13]
Limits of Operation.

[M&S 14]
Permissible Uses.

[M&S 16]
Domain of Verification.

[M&S 18]
Domain of Validation.

[M&S 19]
Processes for Characterizing 
Uncertainty in Referent Data.

[M&S 20]
Methods of Uncertainty 
Propagation in M&S.

[M&S 21]
Incorporated Uncertainties.

[M&S 22]
Proposed Uses.

[M&S 23]
Use Assessment.

[M&S 24]
Input Data.

[M&S 25]
Setup & Execution Rationale.

[M&S 27]
Warning or Error Messages.

[M&S 28]
Processes for Characterizing 
Uncertainty in Input, Results, 
Derived Results.

[M&S 29] 
(1)

Uncertainties in Input

[M&S 29] 
(2)

Uncertainties in Results.

[M&S 29] 
(3)

Uncertainties in Derived 
Results.

[M&S 30]
Sensitivity Analyses.

 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

95 of 157 

5.6.3.2.1 Results Credibility Assessment  
 
The credibility of M&S results is influenced by all the activities in an M&S life cycle.  While 
credibility is not something that can be assessed directly, the factors influencing overall 
credibility (as defined in NASA-STD-7009A per requirement [M&S 31]) are more readily 
assessed. 
 
Following are notes about the NASA-STD-7009A credibility factors: 
 

a. They are considered a minimum set that are applicable to all types of M&S. 
b. They are essentially independent of each other. 
c. For a particular type or application of M&S, additional factors may prove useful. 

 
Additional assistance in achieving the assessed credibility levels for each factor is provided in 
Appendix D. 
 
In addition to assessing the level of credibility for each factor, as a matter of practice, it is also 
recommended for responsible parties to set threshold levels for each factor for the M&S effort to 
attain (NASA-STD-7009A, section 4.3.7 a).  These are best set as early as possible in 
development or use, so as to help the developers or users, respectively, work towards the targeted 
level.  This also supports the insight provided by comparison of the preferred threshold and 
achieved credibility factor levels (NASA-STD-7009A, section 4.3.7 c).  Justification and 
documentation for the assessed levels of each of these factors (NASA-STD-7009A, section 4.3.7 
b) provide the needed evidence. 
 
5.6.3.2.2 M&S Risk Assessment 
 
From an M&S perspective, a risk exists in the potential shortfalls in the M&S with respect to 
sufficiently representing the RWS.  The topic of risk is sprinkled throughout NASA-STD-
7009A, whose primary purpose is to “reduce the risks associated with M&S-influenced decisions.”  
This starts with the assessment of criticality [M&S 6], which is not an element of risk, but does 
provide an understanding of the influence the M&S has on the RWS and consequences of 
inadequate RWS representation.   
 
The reporting of M&S associated risks usually occurs at the end of the Use Phase; however, an 
effective assessment of risk is best considered during each phase of the M&S life cycle (further 
explanations are in Appendix E).  With the potential for incurring M&S risks anywhere in the 
M&S life cycle, it is necessary to assess and report them whenever the results of an M&S-based 
analysis are given.  Several of the requirements and recommendations of NASA-STD-7009A are 
inherently risk oriented.  In particular, the reporting of any caveats from M&S use [M&S 32] and 
the assessed level of credibility for each of the defined factors (this NASA Technical Handbook, 
Appendix D; NASA-STD-7009A, Appendix E) are to be part of any M&S risk assessment. 
   
In addition, each of the following items, if they exist, may improve the risk posture of the M&S: 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

96 of 157 

 

a. Developer/Use Qualifications. 
b. Technical Reviews. 
c. Development/Use Documentation. 

 
While these do not guarantee lower M&S risk, having good developer/user qualifications, 
technical reviews, and documentation improves the chances of adequate M&S representation of 
the RWS than if they were less so. 
 
Table 14 provides a synopsis of potential M&S risk elements with rationales and references. 
 

Table 14—M&S Risk Elements 

Major Risk 
Element 

Rationale
NASA-STD-
7009A 
Reference

NASA-HDBK-
7009A 
Reference

Caveats
Communicates areas that may lead to 
problems or concerns with the M&S 
results.

[M&S 32]
Section 5.6.3
Table 8 

Uncertainty
Communicates that M&S results are 
estimates with a potential range.

[M&S 33]
[M&S 34]

Section 5.6.3.1.2
Table 9

Credibility
Communicates factor assessments 
that impact the believability of the 
M&S results.

[M&S 35]
Appendix E 
Tables 3 – 6

Appendix D

Technical 
Review 

Provides independent assessment of 
various aspects of the development 
or use of the M&S.

[M&S 36]
Table 11

People 
Qualifications 

Provides an understanding of the 
education and experience of the 
people developing and using the 
M&S.

[M&S 37]
Table 12

M&S 
Documentation 

Ensures clear evidence of what was 
actually accomplished in M&S 
development and use. 

[M&S 38], plus 
all of the 
documentation 
R/r’s

Table 13

 
These elements are also part of section 5.6.3.2.3, Table 15, M&S Reporting Synopsis, as 
potential areas for incurring or mitigating potential M&S risks, which are to be considered in the 
context of criticality.  Further background and explanations of these M&S risk related topics are 
in Appendix E. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

97 of 157 

When an M&S is applied by its use to a particular RWS, any associated risks are to become part 
of the RWS risk management system. 
 
Not all caveats, uncertainties, credibility factor assessments, technical reviews, developer and 
user qualifications, or documentation adequacies necessarily introduce M&S risk.  Each of them 
are to be evaluated (and reported) as to whether or not they introduce a risk to the adequacy of 
the M&S results, i.e., introduce unacceptable inadequacies to representing the RWS. 
 
5.6.3.2.3 Reporting 
 
Reporting the results of an M&S goes without saying, but there can be a lot of information 
qualifying those results.  The purpose for the reporting requirements ([M&S 32] through [M&S 
39]) in NASA-STD-7009A is to promote a more complete understanding of the results, and the 
models and processes leading to those results.  A synopsis of reporting information is provided in 
Table 15, which is supported by a more detailed coverage of each item in the following portions 
of this section. 
 

Table 15—M&S Reporting Synopsis 

NASA-STD-
7009A 
Requirement 

Reporting Requirement
Does risk 
exist 
w.r.t. this 
item? 
(Yes / No)

If yes, 
describe 
the 
risk(s). 

If yes, provide the 
rationale for 
proceeding with 
the risk(s). 

[M&S 32]
Caveats.

[M&S 33]
Uncertainty in Results.

[M&S 34]
Uncertainty Processes.

[M&S 35]
Credibility Assessment.

[M&S 36]
Technical Reviews.

[M&S 37]
People Qualifications.

[M&S 38]
M&S Documentation.

[M&S 39]
M&S Risk Assessment.

 
5.6.4 Products and Expected Outcomes of the Model Use Phase 
 
Final products for the model and its use(s) are to be collected and appropriately archived, and 
includes, but are not limited to, the following: 
 

a. Criticality Assessment Results (pertaining to M&S Use). 
b. Use Assessment Results. 
c. Scenarios Used. 
d. M&S Setup (& Calibrations). 
e. Credibility Assessment Results. 
f. M&S Use Results (Raw & Processed). 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

98 of 157 

g. As-Run Procedure from M&S Use. 
h. Results Uncertainties. 
i. Results Sensitivities. 
j. Caveats. 
k. M&S Use Documentation. 
l. Risk Assessment. 
m. Data to update M&S Validation (if any) from use. 

 
5.7 
Model and Analysis Archiving (Phase F) 

 
The NASA-STD-7009A requirements and recommendations applicable to the Model and 
Analysis Archiving phase of the M&S life cycle are found in Appendix A. 
 
Model/Analysis Archiving is the process of storing and cataloging all M&S, including 
designated development and use artifacts for retrieval and use.  The concepts of archiving are 
integrally bound to configuration management (CM), which establishes, tracks, and controls the 
officially accepted M&S and all relevant artifacts throughout the M&S life cycle.  The relevant 
artifacts include the objectives and requirements best defined, per [M&S 8](6), early in the 
development and use life-cycle phases and included in any M&S development, use, or retirement 
plans (NASA-STD-7009A, section 4.1.2 a).  The NASA Standard for CM is Configuration 
Management Requirements for NASA Enterprises (EIA-649-2). 
 
M&S efforts should identify, manage, process, deliver, control, and archive all M&S-related 
technical data and products, including the M&S and tools, information, and data used in 
development and use of the M&S as an integral part of work product management (NASA-STD-
7009A, section 4.1.2c).  Recommended practices for M&S archival should be identified, 
documented (NASA-STD-7009A, section 4.1.3a), and considered for use, along with a method 
for adherence tracking (NASA-STD-7009A, section 4.1.3b(2)), and included as part of training 
for the M&S (NASA-STD-7009A, section 4.1.4b(1)B and section 4.1.4b(1)C).  This includes 
establishing and documenting initial baselines and versioning of controlled items, such as 
designs, test procedures, test reports, and model correlation reports (comparing RWS 
measurements/observations to equivalent model outputs).  Changes to established baselines are 
to be evaluated, justified, authorized, and implemented with traceability to unique version 
identifiers.  Once Development is completed, the model is officially released with all products 
and development artifacts archived.   
 
Whenever M&S results are obtained from use, they should be placed in the M&S’s CM system 
(NASA-STD-7009A, section 4.3.9c). 
 
Table 16 shows examples of products, documents, or artifacts that may require controlling or 
archiving in each phase of the M&S life cycle. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

99 of 157 

Table 16—Example Archival Products in the M&S Life Cycle 

Phase
Pre-A
A
B
C
D
E
F

Name
Model 
Initiation 

Model 
Concept 

Model Design
Model 
Construction 

Model Test
Model Use
Model & 
Analysis 
Archival

Archival 
Item 

RWS Sub-
System, 
Element, or 
Aspect 
Information 
under 
consideration.
 
Initial 
Statement of 
M&S 
Intended Use. 

M&S 
Development 
Plan. 
 
M&S System 
Architecture. 
 
M&S Concept 
Diagrams. 
 
M&S 
Requirements 
& 
Specifications. 
 
M&S Testing 
Requirements. 

M&S Design.

 
Conceptual 
Validation 
Documentation 
& Results. 

The M&S.
Verification 
Plans & 
Procedures. 
 
Validation 
Plans & 
Procedures. 
 
Documented 
domain of 
Permissible 
Use. 
 
The 
Released 
M&S. 
 
User's 
Guide 

Use Plans 
& 
Procedures. 
 
Proposed 
Use. 
 
Use 
Assessment 
& Results. 
 
M&S 
Setup & 
Input 
Scenarios. 
 
M&S 
Output. 
 
Output 
Results. 
 
Reporting.

All 
associated 
M&S 
baselined 
products 
from 
previous 
phases is 
included. 

 
It is up to the programs/projects/individual M&S efforts to determine the type of storage media 
and follow the NASA Records Management Program Requirements (NPR 1441.1). 
 

6. 
WORKSHEET 

 
The worksheet accessible at nasa-hdbk-7009a_-_worksheet.xlsx is intended to assist in the 
planning, development, and use of M&S, including the reporting of results from use of the M&S.  
Many, but not all, requirements and recommendations of NASA-STD-7009A are referenced.  
The information and questions included in this Worksheet are meant to induce a spirit of general 
M&S inquiry, which is by no means all-inclusive or mandatory in all cases.  The intent is to help 
gain a greater depth of understanding of the M&S-based analysis, per the requirements and 
recommendations of NASA-STD-7009A. 
 
Use of NASA-STD-7009A, NASA-HDBK-7009, or the Worksheet may be limited to specific 
phases of the M&S life cycle, or particular organizations developing or using the M&S, for a 
variety of reasons: 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

100 of 157 

 

a. An M&S development organization may choose to follow the precepts of NASA-
STD-7009A, this NASA Technical Handbook, or Worksheet (e.g., for a broadly applicable 
M&S), while an M&S user (organization) may not choose to follow. 

 
b. An M&S user (organization) may choose to follow the precepts of NASA-STD-
7009A, this NASA Technical Handbook, or Worksheet (e.g., for a specifically defined use of an 
M&S) when using an M&S that was not developed or documented according to NASA-STD-
7009A practices. 
 
For these or any other variety of possible reasons, the Worksheet is organized to allow the 
relevant sections to be used when needed.  Such tailoring is expected depending on the particular 
development or application, so long as it is clearly understood (if not officially documented, 
justified, and accepted). 
 
The Worksheet in this NASA Technical Handbook is organized similarly to NASA-STD-7009A, 
with relevant contextual information (Table 17, Worksheet Organization).  The M&S life cycle 
is defined in NASA-STD-7009A, Appendix F, and discussed in this NASA Technical 
Handbook, section 4.6. 
 

Table 17—Worksheet Organization 

Worksheet 

Section

Worksheet Section Title
Worksheet Section Description

6.1
Header.
Contextual information about the RWS and the model 
representing the RWS, including pictorial renderings of 
the criticality and credibility assessments.

6.2
M&S Planning.
Overarching concepts applicable to planning the M&S 
development and use (necessarily encompassing all 
phases of the M&S Life Cycle).

6.3
M&S Development.
Questions and STD references applicable to the phases 
and key processes of M&S development 

6.4
M&S Use.
Questions and STD references applicable to the key 
processes of M&S Use.

 
6.1 
Header 

 
Figure 15, Worksheet Header, is largely similar to the version found in the baseline of this 
NASA Technical Handbook, but reorganized to mirror similar concepts between the RWS and 
the M&S.   
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

101 of 157 

Figure 15—Worksheet Header 

 
The graphics at the top left and right are reminders of two important elements when developing 
and applying an M&S:  The criticality of the situation under the purview of the M&S, and the 
credibility of the M&S results. 
 
The left side of the header requests information relative to the system, sub-system, or aspect of 
the system pertinent to the analysis at hand, along with the system’s life-cycle phase and the key 
responsible parties.  The System Life-Cycle Phase follows the life cycle defined for NASA 
programs and projects. 
 
The right side of the header requests information relative to the M&S, the topic area of the M&S-
based analysis (use), the M&S’s life-cycle phase (as defined in NASA-STD-7009A, Appendix 
F), and the key M&S responsible parties. 
 
Note for sections 6.2, 6.3, and 6.4:  The tables in these sections contain the following: 
 

a. Items to cover. 
 
b. References to NASA-STD-7009A. 
 
c. Key questions for each item. 
 
d. A check column (for use in a checklist manner, if desired). 
 
e. Data entry area for resources, comments, notes, references, links, or other pertinent 
information. 
 
All of the columns are shown in Figure 16, Worksheet Example of All Columns, for the M&S 
Planning section as a reference.  In the sections that follow, only the first three columns will be 
shown for improved readability. 
 

Date:

NASA-STD-7009A

M&S Life-Cycle Worksheet

System:
M&S:

Sub-System, Element, or Aspect of System Under Analysis:
Topic of Analysis (e.g., Production, Ground Ops, Flight, Mission, Entry, Descent, Landing):

Responsibility Chain:  P/P Mgt & Tech Authority
M&S Responsible Party:  Developers, Users, Analysts

System Life-Cycle Phase:   Pre-A    A    B    C    D    E    F
M&S Life-Cycle Phase:   Pre-A    A    B    C    D    E    F


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

102 of 157 

 

Figure 16—Worksheet Example of All Columns 

 
6.2 
M&S Planning Section 

The M&S Planning section (Table 18, Worksheet – M&S Planning) includes overarching 
concepts applicable to the whole life cycle of an M&S, including: 

 

a. Criticality assessment. 
b. Planning. 
c. Use of Best Practices. 

 
Accomplishment of training for all those involved with M&S development and use (and 
potentially even the customers of the M&S). 
 

Table 18—Worksheet – M&S Planning 

Item
STD Ref
Questions

M&S Planning

Criticality 
Assessment [M&S 6] 

What method was used to perform the criticality assessment for 
this M&S?
What were the results of the Criticality Assessment?

Life-Cycle 
Planning 
4.1.2 a 

What are the plans for acquisition / development of this M&S?
What are the plans for Use / Maintenance / Retirement of this 
M&S?

Best 
Practices 
4.1.3 a, b 
What best practices were identified for this M&S?
How were these best practices applied to this M&S?

Training 
4.1.4 a, b 

What training was required for M&S developers and operators?
What training was accomplished for M&S developers and 
operators?

 
Each of the items in this section could easily be considered or accomplished during development 
and, either be reviewed or re-accomplished during M&S use. 
 
 
 

Item
STD Ref
Questions


What method was used to perform the 
criticality assessment for this M&S?
What were the results of the Criticality 
Assessment?
What are the plans for acquisition / 
development of this M&S?
What are the plans for Use / Maintenance / 
Retirement of this M&S?
What best practices were identified and 
applied to this M&S?
How were these best practices applied to 
this M&S?
What training was required for M&S 
developers and operators?
What training was accomplished for M&S 
devleopers and operators?

Responses, Comments, Notes, References, Links

M&S Planning

Best Practices
4.1.3 a, b

Training
4.1.4 a, b

Criticality Assessment
[M&S 6]

Life Cycle
Planning
4.1.2 a


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

103 of 157 

6.3 
M&S Development Section 

 
The M&S development section (Table 19, Worksheet – M&S Development) includes questions 
and references to the requirements and recommendations of NASA-STD-7009A for the 
applicable phases and key processes of M&S development, including: 
 

a. Model Initiation (Pre-Phase A). 
b. Model Concept Development (Phase A). 
c. Model Design, including Conceptual Validation (Phase B). 
d. Model Construction (Implementation) (Phase C). 
e. Model Testing, including both Verification and (Empirical) Validation (Phase D). 
f. Model Release (Phase D). 

 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

104 of 157 

Table 19—Worksheet – M&S Development 

Item 
STD Ref 
Questions 

M&S Development 

M&S Initiation 

[M&S 10] 

What is the RWS? 

What is the RWS environment? 

What is the RWS problem/decision/situation for the M&S? 

What is the RWS Intended Use? 

[M&S 8] (2) 
What is the M&S Intended Use in relation to the RWS Problem/ Decision/ 
Situation?

Model Concept 
Development 

[M&S 11], 
[M&S 12]

What is the M&S approach? (Is it known how to model what is to be 
modeled?)

[M&S 12]
What's included in the M&S, including model environment influences?

[M&S 11] 

Is there anything significant to this analysis not included in the M&S or 
scenarios?
What assumptions & abstractions are included in the M&S and Analysis? 

Model Design 

[M&S 20], 
[M&S 21]
What uncertainties are included in the M&S? 

[M&S 8] 
What are the Requirements or Specifications for the model? 

[M&S 12] 
What are the Implementation Mechanisms (e.g., Math Models)? 

4.2.2 m 
What is the Implementation Architecture (e.g., Platform-Software)? 

Conceptual 
Validation 
[M&S 17] 
Have the Model Design and Architecture been Conceptually Validated? (e.g,. 
Reviewed by SMEs, both RWS and M&S)? 

Implementation
What is the implementation status of the M&S?

Verification 

4.1.2 a
4.1.3 b (3) 
4.2.4 a

What are the verification practices, methods, and requirements? 

[M&S 15]
Has the model construction been verified? (i.e., Code Verification)?

  
Has the model operation or output been verified? (i.e., Solution Verification)? 

4.1.2 c
What artifacts (evidence) of verification are available?

Empirical 
Validation 

4.1.2 a
4.1.3 b (3) 
4.2.6 a

What are the validation practices, methods, and requirements? 

4.1.2 c 
What artifacts (evidence) of validation are available?
Who reviewed/verified the RWS (Referent System) data?

[M&S 8] (1), 
(3), (4)

What is the accuracy, precision, sensitivity, uncertainty, and bias of the model? 
Does it satisfy the requirements?

[M&S 20], 
[M&S 21]

What uncertainties are characterized in the model and how do they compare to 
the RWS Uncertainties?

4.2.8 a 
What uncertainties are not characterized in the model and what are those 
uncertainties in the RWS?

  
What are the model sensitivities?
How do they compare to Sensitivities of the RWS?

Permissible 
Use
[M&S 14] 
What are the Permissible Uses of the M&S? 

Model Release 

4.1.2 c 
What version of the model is released for use? 

4.1.2 c 
Where are the model and its development artifacts archived? 

4.2.2 e 
Was a User's Guide produced and formally released with the model? 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

105 of 157 

 
6.4 
M&S Use Section 

 
The M&S Use section (Table 20, Worksheet – M&S Use) includes questions and references to 
the requirements and recommendations of NASA-STD-70009A or the M&S Use phase and the 
key processes of M&S Use, including: 
 

a. Use Processes. 
b. Use assessment, comparing the proposed and permissible uses of the M&S. 
c. M&S Setup, scenarios for use, and use (execution) of the M&S. 
d. Analysis of M&S results. 
e. Uncertainty Characterization. 
f. Sensitivity Analysis. 
g. Reporting of results, including: 
 

(1) Caveats 
(2) Requirements compliance. 
(3) M&S Results Credibility. 
(4) Technical reviews. 
(5) People Qualifications. 
(6) M&S-based Risk 

 

h. M&S Product Archiving. 

Table 20—Worksheet – M&S Use 

Item
STD Ref
Questions

M&S Use

Use 
Processes 

4.3.2 e
What are the processes for using the model? 

4.2.2 e
Is a User's Guide available?

Proposed 
Use
[M&S 22] 
What is the Proposed Use for the Model? 

Use 
Assessment 
[M&S 23] 

Does the M&S type & purpose of match the proposed use?
Do the modeling methods (abstractions, assumptions, mechanisms) 
provide the needed fidelity (level of detail, accuracy, precision, & 
uncertainty)?
Is the proposed range of use within the permissible model limits?
Are the expected M&S outputs (results) appropriate & within the 
needed accuracy, precision, and uncertainty?

Scenarios
[M&S 24]
What are the Scenarios for model use?

Setup
[M&S 25]
What are the model setups?

Execution
What is the execution status for the use?

Analysis 
[M&S 28] 
(3)
How was the output (data) analyzed? 

M&S Results
What are the best-estimate results provided by the analysis?


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

106 of 157 

Item
STD Ref
Questions

M&S Use

How well (how directly) do the analysis results address the problem 
statement?

Uncertainty
in Estimate
[M&S 29] 
What are the uncertainties in the results of this analysis? 

Sensitivities
[M&S 30]
What are the Sensitivities in the results of this analysis?

Caveats 

[M&S 32] 
(1)
Unachieved Acceptance Criteria? 

[M&S 32] 
(2)
Violation of Assumptions? 

[M&S 32] 
(3)
Violation of Limits of Operation? 

[M&S 32] 
(4)
Warning or Error Messages? 

[M&S 32] 
(5)
Unfavorable Propose Use Assessments? 

[M&S 32] 
(6)
Unfavorable Setup/Execution Assessments? 

[M&S 32] 
(7)
Waivers to Requirements? 

Requirements
Compliance

[M&S 32] 
(1)

Give details on non-compliances with all M&S requirements and their 
consequences.

Credibility 
Assessment 

[M&S 31] 
 
4.3.7 a, b, c 

Data Pedigree.
Verification.
Validation.
Input Pedigree.
Uncertainty Characterization.
Results Robustness.
M&S History.
M&S Process / Product Management.

Technical 
Reviews
[M&S 36] 
Provide a summary of the Technical Reviews performed on this 
M&S/Analysis. 

People 
Qualification
[M&S 37] 
What are the qualifications & experience of the people developing, 
testing, & using this M&S?

M&S Risk
[M&S 39]
What are the risks of basing this decision on the M&S-based analysis?

Results 
Archiving
4.3.9 c 
Were the M&S results (and related artifacts) archived? 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

107 of 157 

APPENDIX A 

 

REQUIREMENTS AND RECOMMENDATIONS PER  

LIFE-CYCLE PHASE 

 

 
A.1 
Purpose  

 
This appendix provides guidance as to which M&S life-cycle phase each NASA-STD-7009A 
requirement and recommendation is likely accomplished. 
  
A.2 
When to Achieve Each Requirement and Recommendation 

 
While some of the requirements and recommendations in NASA-STD-7009 are inherently 
accomplished (satisfied) in one life-cycle phase, there are many that may be accomplished 
(satisfied) in one or more phases.  Additionally, there are times in the M&S life cycle where the 
requirements and recommendations are best accomplished, but may be accomplished at a later 
time.  There are also instances where a R/r is to be accomplished both from M&S Development 
and M&S Use.  If a requirement or recommendation is not accomplished in the indicated phase, 
it becomes incumbent on the subsequent phases to make up that shortfall.  Note there are some 
broad R/r’s applicable to all phases of the M&S life cycle. 
 
The primary table in this appendix (Table 22, R/r per M&S Life-Cycle Phase [accessible at nasa-
std-7009a_reqts_and_recs_per_life_cycle_phase.xlsx]) indicates when the requirements and 
recommendations of NASA-STD-7009A are best to be accomplished, with abbreviated 
designations defined in Table 21, R/r M&S Life-Cycle Phase Designations. 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

108 of 157 

 

Table 21—R/r M&S Life-Cycle Phase Designations 

Designation
Description

- 

Indicates the results of R/r satisfaction may be updated from earlier results 
(this may be true for many requirements, but is particularly so for between 
R/r’s between Be and Bnlt phase designations).

B
The M&S life-cycle phase where the R/r is best accomplished.

Be
The earliest M&S life-cycle phase where the R/r is best accomplished.

Bnlt
The latest M&S life-cycle phase where the R/r may be accomplished.

C-Val
Conceptual Validation (Credibility Factor)

Dev 
The development phase of the M&S life cycle where the R/r is best 
accomplished.

DP
Data Pedigree (Credibility Factor)

E-Val
Empirical Validation (Credibility Factor)

Hist
M&S History (Credibility Factor)

I 
R/r’s that provide information for planning purposes (in M&S Development) 
but are not necessarily required until the Use Phase.

IP
Input Pedigree (Credibility Factor)

Mgt
Process/Product Management (Credibility Factor)

RR
Results Robustness (Credibility Factor)

T
R/r’s that are satisfied by test of the M&S.

UC
Uncertainty Characterization (Credibility Factor)

Ver
Verification (Credibility Factor)

 
For the credibility factor abbreviated designations, the actual reporting of credibility is not 
required until late in the Use Phase for the M&S.  However, at least the initial (baseline) 
assessment of the development focused factors (i.e., data pedigree, verification, and validation) 
are best accomplished during the phase in which they occur. 


NASA-HDBK-7009A 

 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED 
 

109 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

Section 

#
Section Title 
 
 
 
 
 
 
 
 
 
 
 
 

4.1.1
General M&S Programmatics

a 
[M&S 6] Shall perform and document the 
criticality assessment for the M&S. 

B 
(Dev) 

 
 
 
 
 
 
 
B 
(Use) 

 
 
 

b 
[M&S 7] Shall identify and document if the M&S 
is in scope of this NASA Technical Standard. 

 
B 
 
 
 
 
 
 
B 
 
 
 

c 

[M&S 8] Shall define the objectives and 
requirements for M&S products including the 
following:

 
B 
 
 
 
 
 
 
 
 
 
 

  
(1) The acceptance criteria for M&S products, 
including any endorsement for the M&S.  

 
B 
 
 
 
 
 
 
B 
(Use) 

 
 
 

  
(2) Intended use. The intended uses may be 
updated throughout the model development.  
B 
 
 
 
 
 
 
 
 
 
 
 

  
(3) Metrics (programmatic and technical).  
 
B 
 
 
 
 
 
 
B 
(Use) 

 
 
 

  

(4) Verification, validation, and uncertainty 
characterization (see [M&S 15-16], [M&S 17-
18], [M&S 19-21]). 

 
B 
 
 
 
 
 
 
B 
(UC only) 

 
 
 

  
(5) Reporting of M&S information for critical 
decisions (see [M&S 32-39]).  

 
I 
 
 
 
 
 
 
B 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

110 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

  
(6) Configuration management (CM) 
(artifacts, timeframe, processes) of M&S. 

 
B 
(Dev) 

 
 
 
 
 
 
B 
(Use) 

 
 
 

d 

[M&S 9] Shall document any technical reviews 
accomplished in regard to the development, 
management (control), and use of the M&S. 

 
B 
B 
B 
B 
B 
B 
B 
B 
B 
B 
 

4.1.2 
General M&S Programmatic 
Recommendations

 
 
 
 
 
 
 
 
 
 
 
 

a 

Should develop a plan (including identifying the 
responsible organization(s)) for the acquisition, 
development, operation, maintenance, or 
retirement of the M&S. 

B 
(Dev) 

 
 
 
 
 
 
 
B 
(Use) 

 
 
 

b
Should document M&S waiver processes
B

c 

Should document the extent to which an M&S 
effort exhibits the characteristics of work 
product management, process definition, 
process measurement, process control, process 
change, and continuous improvement, including 
CM and M&S support and maintenance 

 
B 
B 
B 
B 
B 
B 
B 
B 
B 
B 
B 

4.1.3
M&S Best Practices Recommendations

a 

Should identify and document any 
recommended practices that apply to M&S for 
the program/project.

 
B 
(Dev) 

 
 
 
 
 
 
B 
(Use) 

 
 
 

b 
At a minimum, recommended practices for the 
following should be considered: 
  
  
  
  
  
  
  
  
  
  
  
  


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

111 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

  
(1) Data and M&S input verification, validation, 
and pedigree.  

 
B 
(Data) 

 
 
 
 
 
 
B 
(Input) 

 
 
 

  
(2) An auditing method of tracking adherence to 
recommended practices. 

 
B 
 
 
 
 
 
 
B 
 
 
 

  
(3) Verification and validation processes for the 
M&S.  

 
 
 
B 
(C-Val.) 

 
B 
(Ver.) 

B 
(E-Val.) 

 
 
 
 
 

  
(4) Uncertainty characterization methods for the 
M&S. 

 
 
B 
B 
B 
B 
B 
 
B 
 
 
 

(5) Sensitivity analysis methods for the M&S. 
B
B

  
(6) Understanding of the disciplines 
incorporated in the M&S. 

 
B 
 
 
 
 
 
 
B 
 
 
 

  

(7) Analyzing and interpreting the M&S results, 
including documentation of inference guidelines 
and statistical processes used. 

 
 
 
 
 
 
 
 
B 
 
 
 

  
(8) Recognizing and capturing the need for any 
changes or improvements in the M&S.  

 
 
 
 
B 
B 
B 
 
B 
 
 
 

(9) Reporting procedures for results. 
I
B

  

(10) Best practices for user interface design to 
constrain the operation of the M&S to within its 
limits of operations.

 
 
B 
 
B 
 
 
 
 
 
 
 

4.1.4
M&S Training Recommendations

a 

Should determine the depth of required training 
or equivalent experience (i.e., qualifications) for 
developers, operators, and analysts. 

 
B 
 
 
 
 
 
 
B 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

112 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

b
Should document the following:

  

(1) Training topics required for developers, 
operators, and analysts of M&S, which should 
include the following:

  
  
  
  
  
  
  
  
  
  
  
  

  
A. The limits of operation for M&S, with 
implications and rationale. 

 
B 
 
 
 
 
 
 
B 
 
 
 

  
B. CM requirements.  
 
B 
(Dev) 

 
 
 
 
 
 
B 
(Use) 

 
 
 

  

C. Documentation requirements and 
recommendations as specified in this NASA 
Technical Standard. 

 
B 
 
 
 
 
 
 
B 
 
 
 

  
D. How to recognize unrealistic results from 
simulations. 

 
 
 
 
 
B 
B 
 
B 
 
 
 

  

E. Feedback processes to improve M&S 
processes and results, including providing 
feedback for results that are not credible, are 
unrealistic, or defy explanation.  

 
 
 
 
 
 
 
 
B 
 
 
 

F. Sensitivity analysis. 
B
B

G. Uncertainty characterization. 
B
B

  
H. Verification and validation.  
 
 
 
B 
(C-Val.) 

 
B 
(Ver.) 

B 
(E-Val.) 

 
 
 
 
 

  
I. How to report simulation results to decision 
makers. 

 
 
 
 
 
 
 
 
B 
 
 
 

J. Statistics and probability
B
B


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

113 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

  

K. Discipline-specific recommended practices. 
Other applicable Agency policy, procedural 
requirements, and standards. 

 
B 
 
 
 
 
 
 
B 
 
 
 

  
L. Basic modeling structures, mathematics, 
assumptions, and abstractions. 

 
B 
 
 
 
 
 
 
B 
 
 
 

  
(2) Process and criteria for verifying that training 
requirements are met. 

 
B 
 
 
 
 
 
 
B 
 
 
 

4.2.1
General M&S  Development

a 

[M&S 10] Shall document the relevant 
characteristics, including data, about the RWS 
used to develop the model, including its 
pedigree (see Data Pedigree in Appendix E). 

B 
 
 
 
 
 
 
 
 
 
 
 

b 

[M&S 11] Shall document the assumptions and 
abstractions underlying the M&S, including their 
rationales.

 
B 
 
 
 
 
 
 
 
 
 
 

c 

[M&S 12] Shall document the basic structure 
and mathematics of the model (e.g., equations 
solved, behaviors modeled, and conceptual 
models). 

 
B 
B 
 
B 
 
 
 
 
 
 
 

d 
[M&S 13] Shall document the limits of operation 
(e.g., boundary conditions) of models. 

 
B 
B 
 
B 
T 
T 
 
 
 
 
 

e 
[M&S 14] Shall document the permissible uses 
of the M&S.

 
 
 
 
 
 
 
Bnlt 
 
 
 
 

4.2.2 
General M&S Development 
Recommendations

 
 
 
 
 
 
 
 
 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

114 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

a 
Should document data sets and any supporting 
software used in model development 

 
B 
 
 
 
 
 
 
 
 
 
 

b 

Should document units and vector coordinate 
frames (where applicable) for all input/output 
variables in the M&S

 
B 
 
 
 
T 
 
 
 
 
 
 

c 

Should document any methods of uncertainty 
characterization and the uncertainty in any data 
used to develop the model or incorporated into 
the model. 

 
B 
B 
 
B 
 
 
 
 
 
 
 

d 

M&S should be designed and constructed so 
that, in the event of a failure, messages 
detailing the failure mode and point of failure 
are provided. 

 
 
B 
 
B 
T 
 
 
 
 
 
 

e 
Should document guidance on proper use of 
the M&S.

 
 
B 
 
B 
T 
T 
Bnlt 
 
 
 
 

f 
Should document any parameter calibrations 
and the domain of calibration. 

 
 
 
 
B 
T 
T 
 
 
 
 
 

g 

Should document updates of the model (e.g., 
solution adjustment, change of parameters, 
calibration, and test cases) and assign unique 
version identifier, description, and the 
justification for the updates.

 
 
 
 
B 
 
 
 
 
 
 
B 

h 

CM records should contain test cases that span 
the limits of operation for the M&S defined by 
the program or project.

 
 
 
 
 
B 
(Ver. Cases) 

B 
(Val. 

Cases)

 
 
 
 
B 

i 
Should document obsolescence criteria and 
obsolescence date of the model. 

 
B 
 
 
 
 
 
 
 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

115 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

j 

Should provide a feedback mechanism for 
users to report unusual results to model 
developers or maintainers.

 
 
 
 
B 
 
 
 
 
 
 
 

k 

Should maintain (conceptual, mathematical, 
and computational) models and associated 
documentation in a controlled CM system.

 
B 
B 
 
B 
 
 
B 
 
 
 
B 

l 

Should maintain the data sets and supporting 
software referenced in Rec. “a” of this section 
and the associated documentation in a 
controlled CM system. 

 
Be 
- 
- 
- 
- 
- 
Bnlt 
 
 
 
B 

m 

Should document any unique computational 
requirements (e.g., support software, main 
memory, disk capacities, processor, and 
compilation options). 

 
B 
 
 
Bnlt 
 
 
 
 
 
 
B 

n 

Developers should convey serious concerns 
about M&S to project managers (and decision 
makers, if appropriate) as soon as they are 
known. 

 
B 
B 
B 
B 
B 
B 
Bnlt 
 
 
 
 

4.2.3
M&S Verification

a
[M&S 15] Shall verify all models
B

b 
[M&S 16] Shall document the domain of 
verification of all models.

 
 
 
 
 
B 
 
 
 
 
 
 

4.2.4
M&S Verification Recommendations

a 
Should document any verification techniques 
used.

 
 
 
 
 
B 
 
 
 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

116 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

b 

Should document any numerical error estimates 
(e.g., numerical approximations, insufficient 
discretization, insufficient iterative convergence, 
finite-precision arithmetic) for the results of the 
computational model. 

 
 
 
 
 
B 
 
 
 
 
 
 

c 

Should document the verification status of 
(conceptual, mathematical, and computational) 
models.

 
 
 
 
 
B 
 
 
 
 
 
 

d 
Should document any aspects of M&S that 
have not been verified.

 
 
 
 
 
B 
 
 
 
 
 
 

4.2.5
M&S Validation

a 
[M&S 17] Shall validate all models. 
 
 
 
B

(C-Val)

 
 
B

(E-Val)

 
 
 
 
 

b 
[M&S 18] Shall document the domain of 
validation of all models.

 
 
 
 
 
 
B 
 
 
 
 
 

4.2.6
M&S Validation Recommendations

a 

Should document any techniques used to 
validate the M&S for its intended use, including 
the experimental design and analysis.

 
 
 
 
 
 
B 
 
 
 
 
 

b 

Should document any validation metrics and 
referents, and data sets used for model 
validation.

 
 
 
 
 
 
B 
 
 
 
 
 

c 
Should document any studies conducted and 
results of model validation. 

 
 
 
 
 
 
B 
 
 
 
 
 

d 
Should document any aspects of M&S that 
have not been validated.

 
 
 
B 

(C-Val) 

 
 
B 

(E-Val) 

 
 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

117 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

4.2.7 
Uncertainty Characterization in M&S 
Development

 
 
 
 
 
 
 
 
 
 
 
 

a 

[M&S 19] Shall document any processes and 
rationale for characterizing uncertainty in the 
referent data.

 
B 
 
 
 
 
 
 
 
 
 
 

b 

[M&S 20] Shall explain and document any 
mechanisms or constructs related to the 
incorporation or propagation of uncertainty in 
the model. 

 
 

B 
(as 
designe
d) 

 
B 
(as built) 

 
 
 
 
 
 
 

c 

[M&S 21] Shall document any uncertainties 
(qualitatively described or quantitative) 
incorporated into the M&S. 

 
 

B 
(as 
designe

d)

 
B 
(as built) 

 
 
 
 
 
 
 

4.2.8 
Uncertainty Characterization in M&S 
Development Recommendation 

 
 
 
 
 
 
 
 
 
 
 
 

a 

The responsible party should document any 
significant physical processes, effects, 
scenarios, or environments not considered in 
the uncertainty characterization analysis. 

 
 
B 
 
 
 
 
 
 
 
 
 

4.3.1
M&S Use Requirements

a 
[M&S 22] Shall document the proposed use(s) 
of the M&S.

 
 
 
 
 
 
 
 
B 
 
 
 

b 

[M&S 23] Shall perform and document an 
assessment of the appropriateness of the M&S 
relative to its proposed use.

 
 
 
 
 
 
 
 
B 
 
 
 

c 

[M&S 24] Shall document data used as input to 
the M&S, including its pedigree (see Input 
Pedigree in Appendix E).

 
 
 
 
 
 
 
 
B 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

118 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

d 

[M&S 25] Shall document the rationale for the 
setup and execution of the simulation and 
analysis.

 
 
 
 
 
 
 
 
 
B 
 
 

e
[M&S 26] Shall do either of the following:

  

(1) Ensure that simulations and analyses are 
conducted within the limits of operation of the 
models, or

 
 
 
 
 
 
 
 
 
B 
 
 

  

(2) Placard the simulation and analysis results 
with a warning that the simulation may have 
been conducted outside the limits of operation 
and include the type of limit that may have been 
exceeded, the extent that the limit might have 
been exceeded, and an assessment of the 
consequences of this action on the M&S 
results. 

 
 
 
 
 
 
 
 
 
B 
 
 

f 

[M&S 27] Shall document and explain any 
observed warning and error messages resulting 
from the execution of the computational M&S. 

 
 
 
 
 
 
 
 
 
B 
 
 

4.3.2
M&S Use Recommendations

a 

Should document the relevant characteristics of 
the system that is the subject of the M&S-based 
analysis.

 
 
 
 
 
 
 
 
B 
 
 
 

b 

Should document which computational models 
were used (including revision numbers) in the 
simulation/analysis.

 
 
 
 
 
 
 
 
 
B 
 
 

c 
Should document any parameter calibrations 
and the domain of calibration 

 
 
 
 
 
 
 
 
 
B 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

119 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

d 
Should document data sets and any supporting 
software used in input preparation. 

 
 
 
 
 
 
 
 
B 
 
 
 

e 

Should document the processes for conducting 
simulations and analyses for generating results 
reported to decision makers.

 
 
 
 
 
 
 
 
Bnlt 

 
 
 

f
Should document the versions of M&S results.
B

g 

Should document any use history of M&S, in 
the same or similar applications, which are 
relevant for establishing the credibility of the 
current M&S application (see Appendix E.4.3.1, 
M&S History Factor). 

 
 
 
 
 
 
 
 
 
B 
 
 

h 

Should document and explain all failure modes, 
points of failure, and messages indicating such 
failures.

 
 
 
 
 
 
 
 
 
B 
 
 

4.3.3
Uncertainty Characterization in M&S Use

a 
[M&S 28] Shall document any processes and 
rationale for characterizing uncertainty in: 
  
  
  
  
  
  
  
  
  
  
  
  

(1) The input to an M&S. 
B

(2) The results from an M&S. 
B

(3) The quantities derived from M&S results.
B

b 
[M&S 29] Shall document any uncertainties 
(qualitatively described or quantitative) in: 
  
  
  
  
  
  
  
  
  
  
  
  

(1) The input to an M&S. 
B

(2) The results from an M&S. 
B


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

120 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

(3) The quantities derived from M&S results.
B

4.3.4 
M&S Uncertainty Characterization 
Recommendation

 
 
 
 
 
 
 
 
 
 
 
 

a 

Responsible parties should document any 
significant physical processes, effects, 
scenarios, or environments not considered in 
the uncertainty characterization analysis. 

 
 
 
 
 
 
 
 
B 
 
 
 

4.3.5
M&S Sensitivity Analysis

a 

[M&S 30] The responsible party shall document 
the extent and results of any sensitivity 
analyses performed with the M&S.

 
 
 
 
 
 
 
 
 
B 
 
 

4.3.6
M&S Results Credibility Assessment 

a 

[M&S 31] The responsible party shall assess 
the credibility of M&S results for each of the 
factors described in Appendix E.

 
 
B 
(DP) 

B 
(C-Val.) 

 
B 
(Ver.) 

B 
(E-Val.) 

 
B 
(IP) 

 
B 
 

4.3.7 
M&S Results Credibility Assessment 
Recommendations

 
 
 
 
 
 
 
 
 
 
 
 

a 

Should set credibility sufficiency threshold 
levels for each factor as described in Appendix 
E.5. 

 
B 
(DP, Ver., 
Val.) 

 
 
 
 
 
 

B 
(IP, UC. 
RR, Hist, 
Mgt) 

 
 
 

b 

Should justify and document the credibility 
assessment for each of the factors referenced 
in [M&S 31].

 
 
B 
(DP) 

B 
(C-Val.) 

 
B 
(Ver.) 

B 
(E-Val.) 

 
B 
(IP) 

 
B 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

121 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

c 

Should gain additional insight into the credibility 
of M&S results by applying the process in 
Appendix E.5 to determine and report any gaps 
between the achieved scores and the 
program/project-defined threshold scores for 
each of the factors.

 
 
 
 
 
 
 
 
 
 
B 
 

4.3.8
M&S Results Reporting 

a 

[M&S 32] Shall include explicit warnings for any 
of the following occurrences, accompanied by 
at least a qualitative estimate of the impact of 
the occurrence: 

  
  
  
  
  
  
  
  
  
  
  
  

  
(1) Any Unachieved Acceptance Criteria (as 
specified in [M&S 8] (1)).

 
 
 
 
 
 
 
 
 
 
B 
 

  
(2) Violation of any assumptions of any model 
(as specified in [M&S 11]). 

 
 
 
 
 
 
 
 
 
 
B 
 

  
(3) Violation of the limits of operation (as 
specified in [M&S 13]). 

 
 
 
 
 
 
 
 
 
 
B 
 

  
(4) Execution warning and error messages (see 
[M&S 27]). 

 
 
 
 
 
 
 
 
 
 
B 
 

  
(5) Unfavorable outcomes from the proposed 
use assessments (described in [M&S 23]). 

 
 
 
 
 
 
 
 
 
 
B 
 

  

(6) Unfavorable outcomes from any 
setup/execution assessments (described in 
[M&S 25]). 

 
 
 
 
 
 
 
 
 
 
B 
 

  
(7) Waivers to any of the requirements in this 
NASA Technical Standard. 

 
 
 
 
 
 
 
 
 
 
B 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

122 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

b 

[M&S 33] Shall include an estimate of results 
uncertainty, as defined in [M&S 29 (1)-(3)], in 
one of the following ways:

  
  
  
  
  
  
  
  
  
  
  
  

  
(1) A quantitative estimate of the uncertainty in 
the M&S results, or 

 
 
 
 
 
 
 
 
 
 
B 
 

  
(2) A qualitative description of the uncertainty in 
the M&S results, or 

 
 
 
 
 
 
 
 
 
 
B 
 

  

(3) A clear statement that no quantitative 
estimate or qualitative description of uncertainty 
is available

 
 
 
 
 
 
 
 
 
 
B 
 

c 

[M&S 34] Shall include a description of any 
processes used to obtain the estimate of 
uncertainty as defined in [M&S 28 (1)-(3)].

 
 
 
 
 
 
 
 
 
 
B 
 

d 

[M&S 35] Shall include the assessment of 
credibility for the M&S results for each factor 
specified in [M&S 31].

 
 
 
 
 
 
 
 
 
 
B 
 

e 

[M&S 36] Shall include the findings from any 
technical reviews accomplished in regard to the 
development, management (control), and use of 
the M&S. 

 
 
 
 
 
 
 
 
 
 
B 
 

f 

[M&S 37] Shall include the qualifications of the 
developers of the M&S and the users, 
operators, or analysts involved in producing the 
results from the M&S, including, but not limited 
to, their relevant education, training, and 
experience.

 
 
 
 
 
 
 
 
 
 
B 
 

g 

[M&S 38] Shall show what aspects of modeling 
and simulation are documented, as shown in 
Appendix A.

 
 
 
 
 
 
 
 
 
 
B 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

123 of 157 

Table 22—R/r per M&S Life-Cycle Phase

Phase -->
Pre-A
A
B
C
D
E
F

 
Phase Name --> 
Model 

Initiation 

Model 

Concept 

Development

Model Design 
Model 

Construction 
Model Testing 
Model Use (Ops) 

Model / 
Analysis 
Archiving

 
Sub-Phase --> 
  
  
Design 
Conceptual 
Validation 
  
Verification 
Empirical 
Validation 
Release 
Pre-Ops 
Use 
(Ops) 
Post-Ops 
  

h 

[M&S 39] Shall include an assessment of and 
rationale for the risks associated with the use of 
the M&S-based analysis.

 
 
 
 
 
 
 
 
 
 
B 
 

4.3.9
M&S Results Reporting Recommendations

a 

Should include concluding remarks stating 
whether the M&S results are credible enough 
for the actual use.

 
 
 
 
 
 
 
 
 
 
B 
 

b 

Should identify how to access more detailed 
backup material, including high-level 
descriptions of the models used and key 
assumptions for limits of validity. 

 
 
 
 
 
 
 
 
 
 
B 
 

c
Should place M&S results in the CM system.
B

d 
Should summarize deviations from established 
recommended practices. 

 
 
 
 
 
 
 
 
 
 
B 
 

e 

Should include dissenting technical opinions 
regarding the credibility of the results or any 
recommended actions

 
 
 
 
 
 
 
 
 
 
B 
 

f 

Should convey serious concerns about M&S or 
its use to project managers (and decision 
makers, if appropriate) as soon as they are 
known. 

 
 
 
 
 
 
 
 
B 
B 
B 
 

 

 

 


NASA-HDBK-7009A 

 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED 
 

124 of 157 

APPENDIX B 

 

QUALITY OF REFERENT DATA USED IN EMPIRICAL 
VALIDATION 

 
 
B.1 
Purpose  

 
This appendix provides guidance on the quality of referent data used in empirical validation. 
 
B.2 
Quality of Referent Data 

 
An important and often overlooked item with regard to the quality of the referent data acquired 
and used to validate an M&S is the assurance that all sources of error, especially those that are 
difficult to detect, are eliminated or mitigated to acceptable levels.  Understanding and 
accounting for the differences between the referent and RWS is essential, but equally essential is 
that data obtained from the referent, and the methodologies used to acquire these data, are 
compatible with, or convertible to, data needed to correctly validate an M&S.  More often than 
not, the referent is either:  
 

a. An experiment that is designed to simulate or replicate a RWS or a portion thereof. 
 
b. An operating or prototype RWS equipped with instrumentation and data acquisition 
systems to assure its safe, reliable, and proper operation and maintenance.   
 
The instrumentation, data acquisition systems, and the methodologies used to obtain data from a 
referent are often different from those needed to properly validate an M&S.  Generally, 
instrumentation used to provide data for physical systems has the purpose of monitoring system 
health, preventing unsafe operating conditions, or predicting the need for preventative 
maintenance or repairs.  More often than not, these data are often different, where many 
differences are subtle and can easily remain undetected, or have higher allowed 
errors/uncertainties when compared with data that is needed for M&S validation. 
 
Additionally, errors in instrumentation measurements and data obtained from these 
measurements are common whenever a high level of rigor, similar to the level of rigor applied to 
M&S verification, is not exercised to assure all possible sources of error are identified and taken 
into account or reduced to acceptable levels.  Examples of unresolved/uncorrected empirical data 
acquisition errors and their root causes include: 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

125 of 157 

 

(1) Pressure sense line taps being positioned/configured such that true static (or 
stagnation) pressure is not measured. 
 

(2) Unaccounted effects of head pressures due to elevation differences. 

 

(3) High frequency and amplitude pressure oscillations in the system coupled with 
measurement response time delays causing false readings. 

 

(4) Measurement response time delays masking out transients that need to be 
measured. 

 

(5) Nearby or contacting heat sinks or sources skewing thermocouple (or other 
types of temperature instrument) readings. 

 

(6) Instruments themselves in the flow stream/passages altering flow 
characteristics. 

 

(7) Data transmission rates (number of readings per unit of time) from instrument 
measurements exceeding limits of data processing equipment. 

 
In a number of instances, facility environments also contribute significant thermal, mechanical, 
optical or other forms of background “noise” to the critical measurements required for model 
validation.  Left unchecked, these noise sources limit the domain of validation, requiring 
extrapolation of the model for predictions applied in the actual RWS environment.  
Alternatively, facility noise sources may be attenuated through the use of specially-designed test 
fixtures, but these must then be included in the model when replicating ground testing and often 
complicate or add uncertainty to model validation efforts.  These are then removed when 
replicating flight (mission) conditions. 
 
An example would be the use of mechanical isolation systems to mitigate vibrations generated 
by facility machinery, such as vacuum and fluid pumps.  The isolation system would have to be 
added to the appropriate (e.g., structural, thermal, optical) models of the RWS (or portion 
thereof) under test, followed by careful identification and separation of its contribution to 
measurements obtained during the test. 
 
To further compound these problems and work against the likelihood of them being corrected, 
the M&S developers are generally working in organizations that are separate and independent of 
the organizations where experimental systems and RWS designers and operators work.  Such 
separate and independent organizations do not always communicate effectively, especially when 
large and complex systems, or large quantities of detailed information and data, are involved.  
Added to this situation are the budgetary and schedule constraints, universal to all projects and 
programs, where decision-makers can be strongly influenced or driven to use data obtained from 
past (historical) experiments and RWSs, where incorrect assumptions of data compatibility are 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

126 of 157 

made.  (Oberkampf, W.L.; Roy, C.J. (2010), Chapters 10 and 11, provide further details and a 
substantiating case study.)  Therefore, the referent data and the methodologies to obtain these 
data are to be checked for compatibility with data needed for M&S validation, and the 
verification of referent data is to be performed with the same rigor and level of scrutiny as the 
verification of an M&S prior to validation of the M&S. 
 
The concept of “model builder’s risk” (or type 1 error) and “model user’s risk” (or type 2 error) 
(discussed in Oberkampf, W.L.; Roy, C.J. (2010), Chapter 12, Section 12.2.2) also need to be 
understood and addressed during M&S validation.  “Model builder’s risk” is the problem where 
the validity of an M&S is rejected when it is actually valid.  “Model user’s risk” is the opposite, 
an M&S being accepted as valid when it is not.  Type 1 errors can lead to recalibrating or tuning 
an M&S to provide acceptable agreement with invalid referent data; likely to result in continued 
and expanded use and acceptance of (and reliance upon) an invalid M&S for subsequent 
applications and projects/programs.  Type 2 errors are potentially the most dangerous because 
errors in the referent data can result in acceptable (good to excellent) agreement with data from 
an invalid M&S.  When this occurs, there is little or no incentive to pursue and uncover 
undetected errors and biases with the net result being a false sense of security (that is until a 
major mishap or catastrophe occurs).  This is depicted in Table 23, M&S vs. Referent 
Data/Results Relationship. 
 
Table 23 is a simple 2x2 matrix of conditions and outcomes that includes type 1 and type 2 
errors.  While not similarly labeled, the upper-right quadrant also represents a type of error. 
Here, the model and referent do not agree, but the consensus is that the referent is valid. 
Assuming the model was verified before the comparison to the referent was made, the 
conclusion is then that the conceptual model (or its architecture, requirements and other inputs to 
the Model Design Phase) are not valid. 
 
The best remedy to mitigate or prevent “model builder’s risk” and “model user’s risk” is 
complete, effective, and fully transparent communications between M&S developers and the 
designers and operators of the experiment, test article, prototype, or RWS to be used as the 
referent for M&S validation.  While the M&S and data from the referent are separately and 
independently verified, the M&S developer or validator needs to fully understand the referent 
and how data is acquired.  Additionally, the designers and operators of the systems used as a 
referent need to fully understand the types of data and data acquisition requirements needed by 
the M&S developers.  However, proper validation still requires that no transfer/communication 
of actual data and results between people performing verification of the M&S and those 
performing verification of data from the referent prior to M&S validation. 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

127 of 157 

Table 23—M&S versus Referent Data/Results Relationship 

 
 
 

 
M&S Data/Results

Valid 
Invalid 

Referent (Empirical) Data/Results 

Valid 

M&S is Correctly Validated * 

M&S Data/Results and Referent Data/ 
Results being in Agreement is not possible.* 

 

If M&S Data/Results and Referent Data/ 
Results are not in Agreement, M&S to be 
corrected or replaced and then re-verified  

Invalid 

M&S Data/Results and Referent Data/ 
Results being in Agreement is not possible * 

 

M&S Data/Results and Referent Data/ 
Results are not in Agreement, 

Type 1 Error exists; and 

Source(s) of referent data/results need to 
be corrected or replaced and then re-
verified ** 

If M&S Data/Results and Referent Data/ 
Results are in Agreement, 

Type 2 Error exists. 

 

Whether or not M&S Data/Results and 
Referent Data/Results are in Agreement, 
M&S needs to be corrected or replaced 
and then re-verified and source(s) of 

referent data/results need to be corrected 
or replaced and then re-verified ** 

Notes: 

∗ 
Domain of M&S verification is within domain of referent data verification and all verifications 
have been done correctly 
 

   **  Sources of referent data having unacceptably high errors can be the result of: 

 

1. The source(s) of referent data; e.g., prototype of system, experimental system or setup, 
simulation of RWS, RWS being tested in different operating environment; is not a 
sufficiently correct representation of RWS being modeled. 
 

2. Unknown and undiscovered phenomena are acting on and skewing data and results 
obtained from the source(s) of referent data. 
 

3. The instrumentation, the way instrumentation is connected/installed into the RWS or 
system representing/simulating the RWS, or methods that data is acquired are not 
compatible with data required to validate the M&S. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

128 of 157 

APPENDIX C  

 

M&S USER’S GUIDE OUTLINE 

 
 
C.1 
Purpose  

 
This appendix provides guidance on the content of an M&S user’s guide, but the content and 
organization of this appendix are only suggestions and not intended as a prescription. 
 
C.2 
M&S User’s Guide 

 
Development of a User’s Guide for an M&S is a recommendation of NASA-STD-7009A, 
section 4.2.2e:  Should document guidance on proper use of the model. 
 
C.3 
M&S User’s Guide Content 

 
The content listed should be located somewhere in the User’s Guide and easily found by Table of 
Contents or indices. 
 

1. General Information 

 

a. Table of Contents, Figures, and Tables. 
b. User’s Guide Revision History. 
c. Model applicable glossary. 
d. Model applicable acronyms. 
e. Model applicable references. 

 

2. Model Identification 

 

a. Official model name (or designator). 
b. Applicable revision. 
c. Description of model. 
d. Location of the model and relevant artifacts repository. 

 

3. Intended Use (see section 5.1.1.2 of this NASA Technical Handbook) 

 

a. What the model is. 
b. What the model is used for (i.e., its purpose). 
c. What the model should not be used for. 

 

4. M&S Conceptual Diagram (Conceptual Model) 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

129 of 157 

a. Model Contents. 
b. Sequence of Processes & Computations (as needed). 
c. Description of Model Capabilities. 
d. Sources and General Description of Key Equations and Systems of Equations to 
use (or used) in the model; especially those most critical to modeling the RWS or 
those that could prove difficult to implement. 
 

5. Technical Background of How the Model Works 

 

a. M&S Architectural Diagram.  
b. Primary Governing Concepts (possibly equations and systems of equations), 
along with their pedigree of use. 

c. M&S Abstractions & Assumptions. 
d. How uncertainties are handled in 

i. The construction of the model. 
ii. The use of the model. 

1. In the Input. 
2. In the Output. 

e. Technical Metrics 

i. Accuracy and Precision of the Released Model. 
ii. Model Setup criteria to obtain desired level of accuracy or precision. 

f. User Interface. 

 

6. Permissible Uses of the Model, as constrained by 

 

a. The Intended Use. 
b. Limits of Operation (boundary conditions for model use): 

i. As Designed, determined by: 

1. Abstractions. 
2. Assumptions. 
3. Modeling choices. 

ii. As Verified. 
iii. As Validated. 

 

c. Include Obsolescence Criteria. 

 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

130 of 157 

7. Processes for Model Use 

 

a. Model Use/Analysis Plan. 

 
Suggestions from a “model perspective” of what to include in the Use/Analysis 
Plan, with the Developer’s Scope of Use in mind. 
 

b. Use Assessment. 

 

c. Setup. 

 

i. M&S Architectural Diagram.  
ii. Requirements and Instructions for setting up (installing) the model for use. 

 

d. Inputs.  

 

i. What all the inputs are. 
ii. What the permissible range for each input is. 

 

e. User Interface. 

 

f. Use. 

 

8. Expected Results from Use 

 

a. Example Results (Samples). 

 

b. Comparison with referent empirical data. 

 
Provide examples of results with good and poor comparison to referent data. 
 

c. Uncertainties with upper and lower bounds in the overlay of plotted data. 

 

i. Associated input uncertainties with their pedigree. 

 

d. Potential Areas of Sensitivity. 

 

9. Other M&S Development Information Relevant to M&S Use 

 

a. Potential Caveats. 

 

i. Unachieved Acceptance Criteria. 
ii. Waivers to Development Requirements. 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

131 of 157 

 

b. Development Related Credibility Factors 

 

i. Data Pedigree. 
ii. Verification. 
iii. Validation. 
iv. M&S (Revision) History. 
v. M&S Process/Product Management. 

 

c. Potential areas of Risk. 

 

d. Findings from Technical Reviews. 

 

e. Where to find Development Artifacts. 

 

10. Operator/User/Analyst Requirements/Recommendations 

 

a. Education. 
b. Experience. 
c. Training. 

 

11. Developer Qualifications 

 

12. Help 

 

a. Where to go for help. 

 
Include website or info location where there are FAQs, etc., that may also lead a 
user to a CM/repository system (section 2d) where the files are stored. 
 

b. Who to Contact for Help, Comment, or Suggestions. 

 

i. M&S Developer. 
ii. Configuration Manager. 

 

 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

132 of 157 

APPENDIX D  

 

ASSESSING AND INFLUENCING  

M&S RESULTS CREDIBILITY 

 
 
D.1 
Purpose  

 
This appendix provides guidance for performing the M&S results credibility assessment and 
provides information on how each M&S life-cycle phase may affect each of the credibility 
factors.  
 
D.2 
Overall M&S Credibility 

 
M&S Results Credibility is a key tenet of NASA-STD-7009A.  The idea is challenging, as it may 
take on a variety of meanings depending on the context of the M&S, but it is a natural part of any 
decision-making process.  As credibility cannot be measured directly, the methodology 
developed as part of NASA-STD-7009A formalizes this assessment with a minimum set of 
criteria contributing to M&S-based analysis credibility. 
 
Details to consider as to the credibility of the results of an M&S-based analysis are included in 
sections 4.3.6, 4.3.7, and Appendix E of NASA-STD-7009A, which addresses key development, 
usage, and supporting aspects of an M&S activity.   
 

a. When assessing M&S Results Credibility, consider the following:  

 

(1) There may be other key aspects to a particular type of M&S that are not included 
in this credibility assessment.  Including those additional aspects along with the 
more broadly applicable credibility factors defined in NASA-STD-7009A is 
acceptable and encouraged.  The factors included in NASA-STD-7009A’s 
credibility assessment are considered to be a minimal set for a majority of M&S.  
If, however, a factor is not considered relevant to a particular M&S, tailoring is 
permitted, with the approval of the program/project delegated Technical 
Authority.  (See section 1.3 of NASA-STD-7009A.) 

 

(2) There is no correlation between compliance with the requirements of 
NASA-STD-7009A and the achievement of particular levels for the various 
factors in the credibility assessment.  Attaining the various levels of credibility 
relate to the technical aspects and are defined on a case-by-case basis. 

 
M&S Results Credibility is also affected by each phase in the M&S life cycle.  Perhaps with the 
exception of input pedigree, all credibility factors are affected by more than one of the life-cycle 
phases.  Table 24, M&S Life-Cycle Phase Affects M&S Results Credibility Factors, is an 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

133 of 157 

overview of when in the life cycle these influences occur.  Explanations for how each life-cycle 
phase affects each credibility factor are included in subsequent sections of this appendix. 
 

Table 24—M&S Life-Cycle Phase Affects M&S Results Credibility Factors 

Phase
Pre-A
A
B
C
D
E
F

Name 
Model 
Initiation 

Model 
Concept 

Model 
Design 

Model 
Construction 

Model 
Test 

Model 
Use 

Model & 
Analysis 
Archival

Data Pedigree 
X 
X 
X 
X 
 
 
 

Verification 
 
X 
X 
X 
X 
 
 

Validation 
 
X 
X 
X 
X 
 
 

Input Pedigree 
 
 
 
 
 
X 
 

Uncertainty 
Characterization 

 
X 
X 
X 
X 
X 
 

Results Robustness 
 
 
 
 
X 
X 
 

M&S History 
 
 
X 
X 
X 
X 
 

M&S 
Product/Process 
Mgt

X 
X 
X 
X 
X 
X 
X 

 

b. The acceptable level for the overall credibility and contributing factors is determined 
by the program/project management in association with the delegated Technical Authority 
(NASA-STD-7009A, section 4.3.7), as appropriate for the current state of the RWS and the 
M&S and the criticality of the decision being made.  The expectation for analyses is that they 
improve as: 
 

(1) The system development matures. 
(2) Data become available from relevant phases of the program/project. 
(3) The M&S matures and is used. 

 

c. The assessment of overall M&S results credibility should include the following: 
 

(1) A tabular or graphical display of all of the credibility factors. 
 
(2) The role of the person/team performing the credibility assessment in the 
development, operation, or analysis using the M&S. 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

134 of 157 

(3) A summary of the evidence and supporting rationale.  (A reference to another 
document may suffice.) 

 
An example for reporting a synopsis of the credibility assessment is shown in Figure 17, 
Credibility Assessment Synopsis. 
 

     
 

a. Bar Chart 
 
 
 
 
  b.  Spider (Radar) Plot 

 

Figure 17—Credibility Assessment Synopsis 

 
Note:  The scaling of levels are intended to depict a range of possible assessments from nothing 
(zero) to perfect or nearly so (four).  It is only possible for an M&S to achieve an assessed 
credibility Level 4 with considerable effort in M&S development and use, and with adequate 
data from the RWS.  For example, many NASA scientific missions consist of a single flight 
vehicle.  The only way to attain a Level 4 assessment for validation is by comparison with results 
from the actual RWS; therefore, any time before the first mission, an assessment of Level 3 is the 
highest possible for validation.  The purpose for such an assessment is to discuss the factors 
influencing the credibility of the analysis results.  It is the decision maker’s responsibility, in 
conjunction with the delegated Technical Authority, to ascertain the acceptability of this 
information. 
 
D.3  
Data Pedigree 

 
The Data Pedigree factor strives to address the adequacy and quality of the data (or information) 
used to develop the model, including their completeness, breadth, and accuracy.  The central idea 
is to communicate clearly the credibility of the data used in developing the model.   
 
The following attributes are to be considered for all data used to develop an M&S: 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

135 of 157 

a. Source of the data.  

 
(1) SME. 
(2) Document. 
(3) Database. 
 

b. Quality of the source. 

 
(1) Notional. 
(2) Informed. 
(3) Specified. 
(4) Derived. 
(5) Measured. 
(6) Similarity of analogous data source. 

 
c. Diversity of the data source; greater is often better, but not always. 

 
(1) Single values, e.g., a minimum, maximum, or average from a particular source. 
(2) A set of historical values for this input from a number of sources. 
(3) Single versus multiple instances. 

 
d. Quantity of source data.  

 
(1) A single value. 
(2) A set of values. 
 

e. Form of the data used. 

 
(1) Deterministic. 
(2) Deterministic with spread. 
(3) Probability distribution or stochastic data. 

 
Determining the credibility level for the data used to develop an M&S is interdependent on the 
attributes discussed above. These details of data pedigree are to be considered in determining the 
overall data pedigree credibility level. 
 
Table 25, Data Pedigree Credibility Achievement, is to be read from the bottom up (like the 
credibility assessment), with the general idea that improvement is achieved when ascending the 
table.  Note that these sub-factors for data pedigree are not strictly ordered and should be 
considered as part of the discussion in the overall assessment of data pedigree.  

 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

136 of 157 

Table 25—Data Pedigree Credibility Achievement 

Source1
Quality2
Diversity/Quantity3
Form of Input4

RWS
Official

Another 
Model/Analysis 

Analogous
Stochastic (pdf) or 
Empirical Function

Analogous 
System 

Historical
Variety of Process 
Iterations

Average with Spread

SME
Unofficial
Variety of Instances
Range of Values

None
Notional
Amount of Data
Deterministic

 
Notes: 
 
1. Source:  The data obtained from an analogous real-world source may be better than that 
obtained from another model or analysis; however, the reverse can also be true. 
 

2. Quality:  The data quality from an analogous source may be as good as data quality from the 
historical system. 
 

3. Diversity/Quantity:  Having data from a variety of instances, e.g., Orbiter tail numbers, may 
be as good as having data from one instance over many process flows. 
 

4. Form of Data:  Form, correct units, and appropriateness to scenario. 
 
NASA-STD-7009A, Table 4, Level Definitions for Factors in the M&S Development Category, 
provides guidance for achieving the various credibility levels for the data pedigree factor.  
 
Table 26, Life-Cycle Phase Influence on Data Pedigree, shows how data pedigree is affected by 
the various M&S life-cycle phases. 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

137 of 157 

Table 26—Life-Cycle Phase Influence on Data Pedigree 

Phase
Name
Data Pedigree is affected by

Pre-A
Model Initiation
•
The initial information gathered to direct model development.

A
Model Concept
Development 

•
The additional/supplemental data is gathered to support the 
conceptualization of the model and establish requirements for 
model fidelity and performance. 

• 
The data supporting (justifying) the use of specific modeling 
methods, e.g., methods used on similar problems, can substantiate 
the use specific methods over others.

B
Model Design
•
Any remaining RWS data not previously gathered to allow the 
completion of Model Design.

C
Model Construction
•
The actual data, including its form, used in the model.

 

D
Model Test

 

E
Model Use

 

F
Model & Analysis 
Archival 
 

 
D.4  
Verification 

 
The process of verification ensures the computational model (or simulation model) is correctly 
implemented. Verification does not ensure the M&S matches the RWS or addresses the problem 
of interest.   
 

a. The M&S can be considered verified when the following two conditions are satisfied: 

 

(1) The M&S meets its specifications.  These specifications start with the 
conceptual/mathematical model and include additional requirements for 
functions, e.g., user interfaces and data I/O. 

 
(2) All significant sources of numerical errors inherent in the implementation are 
identified, quantified, and within assigned upper bounds. 

 
b. A review should examine the documented evidence relating to these two aspects of 
verification and address questions, including: 

 

(1) What actions demonstrated the model functions exactly as intended, as specified 
by the conceptual model or other model requirements?  What were the results of 
these actions? 

 
(2) What process was used to quantify numerical errors resulting from any 
algorithms, and what were the results? 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

138 of 157 

(3) What process was used to quantify numerical errors resulting from factors such 
as sampling or quantization, the step size chosen for the numerical integration of 
differential equations in a time-domain simulation, and the methods and intervals 
used for interpolation of model parameters; what were the results? 

 
NASA-STD-7009A, Table 4, Level Definitions for Factors in the M&S Development Category, 
provides guidance for achieving the various credibility levels for the verification factor. 
 
Table 27 shows how verification is affected by the various M&S life-cycle phases.  While 
verification does not occur until Phase D, information that helps establish model design, which is 
the basis for Verification, is influential.  As Model Initiation typically only gathers preliminary 
information, it is not included as formally influential to verification. 
 

Table 27—Life-Cycle Phase Influence on Verification 

Phase
Name
Verification is affected by

Pre-A
Model Initiation

A
Model Concept 
Development 

•
As RWS & modeling concepts mature, requirements for the 
model are determined to scope and guide subsequent phases 
of development, which are checked in Verification.

B
Model Design
•
The design of the model is the basis upon which the model is 
implemented and verified.

C
Model Construction
•
This phase produces the model, based on the design 
requirements of Phase B, which is checked in Verification. 

• 
As implementation choices are made during model 
construction, specifics for verification planning and 
procedures are determined.

D
Model Test
•
The 1st part of this Phase is Verification.

• 
The goals of attaining the various credibility levels of 
verification are achieved. 

E
Model Use

 

F
Model & Analysis 
Archival 
 

 
 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

139 of 157 

D.5  
Validation 

 
The process of validation ensures the M&S is an acceptably accurate representation of the real 
world from the perspective of the intended uses of the M&S.  The complete handling of 
validation occurs in two distinct parts:  Validation of the M&S design (conceptual validation) 
and validation of the implemented M&S (empirical validation). 
 
Note:  It is advantageous to accomplish verification before empirical validation.  Accomplishing 
verification before empirical validation precludes the discovery of M&S implementation issues 
while trying to ascertain the accuracy or fidelity of the M&S with respect to the RWS.  
Validating an unverified M&S assumes the model is working as designed.  NASA-STD-7009A, 
Table 4, Level Definitions for Factors in the M&S Development Category, provides guidance for 
achieving the various credibility levels for the Validation Factor. 
 
Table 28 shows how validation is affected by the various M&S life-cycle phases.  While 
validation does not occur until Phase B (Conceptual/Design Validation) and Phase D (Model 
Validation), information that helps establish model design, which is the basis for validation, is 
influential.  As Model Initiation typically only gathers preliminary information, it is not included 
as formally influential to validation. 
 

Table 28—Life-Cycle Phase Influence on Validation 

Phase
Name
Validation is affected by

Pre-A
Model Initiation

A
Model Concept 
Development 

•
RWS Conceptual Elements to include in the model design 
are determined, which are checked in Conceptual Validation 
(end of Phase B). 

• 
Potential scenarios for use of the model may be determined 
in this Phase, which are checked in Validation (Phase D).

B
Model Design
•
The design of the model may incorporate aspects of the 
RWS or features to allow specified scenarios to be run, 
which will be implemented and validated.

C
Model Construction
•
This phase produces the model to run specific types of 
scenarios that will be validated. 

D
Model Test
•
The 2nd part of this Phase is Validation, which tests against 
RWS scenarios. 

• 
The goals of attaining the various credibility levels of 
Validation are achieved.

E
Model Use

F
Model & Analysis 
Archival 
 

 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

140 of 157 

D.6  
Input Pedigree 

 
The input pedigree factor strives to address the adequacy and quality of the inputs to the model 
during use, including their completeness, breadth, and accuracy for use in a particular simulation, 
and the eventual analysis recommendations.  Models are generally considered as encapsulations 
of certain system characteristics to which a set of data is applied for a specific analysis.  The 
input to a model broadly refers to the data used to obtain simulation and analysis results.  The 
input does not address the model mathematics or structure, the processing of information within 
the model, or statements of uncertainty accompanying the results.  The data can, however, 
include specific modifying parameters, with or without uncertainty, to the model or be used to 
set up and initialize the model. 
 
The attributes to consider for each input are the same as those for Data Pedigree in section D.3, 
but with respect to M&S input data.  Refer to those attributes in section D.3 through Table 25 
and its accompanying notes. 
 
NASA-STD-7009A, Table 5, Level Definitions for Factors in the M&S Use (Operations) 
Category, provides guidance for achieving the various credibility levels for the input pedigree 
factor. 
 
Table 29, Life-Cycle Phase Influence on input pedigree, shows how validation is affected by the 
various M&S life-cycle phases.  As mentioned earlier, input pedigree is perhaps the only 
credibility factor not affected by more than one life-cycle phase. 
 

Table 29—Life-Cycle Phase Influence on Input Pedigree 

Phase
Name
Input Pedigree is affected by

Pre-A
Model Initiation

A
Model Concept 
Development

B
Model Design

C
Model Construction

 

D
Model Test

E
Model Use
•
Data to analyze for model setup and input is gathered.

•
Model Input is used to produce Model Output & Results.

F
Model & Analysis 
Archival 
 

 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

141 of 157 

D.7  
Uncertainty Characterization 

 
Uncertainty Characterization is the process of identifying sources of uncertainty and describing 
their relevant qualities (qualitatively or quantitatively) in all models, simulations, and 
experiments (inputs and outputs).   
 

a. Characterizing the uncertainty of M&S results can be accomplished qualitatively or 
quantitatively depending on: 
 

(1) The maturity of the RWS. 
(2) The availability of RWS data. 
(3) The fidelity of the M&S. 
(4) The time and resources available to characterize the uncertainty. 

 

b. Details associated with the types of information needed to more fully understand 
uncertainty in M&S, include the following, which can be tracked using a table similar to 
Table 30, Sample Table for the Uncertainties of a Process: 

 

(1) Name:  Uniquely identifying an uncertainty. 

 

(2) Sources:  Listing what is not known or not fully known in an M&S is a 
beginning.  Each item can then be enhanced with some qualifying information.   

 
(3) Location:  Knowing where uncertainties are located in the RWS aids in 
understanding it and also in determining whether or not these uncertainties 
should be included in the model, e.g., if the magnitude of an uncertainty is small 
relative to other parameters in the system or inconsequential to the outcome, then 
it may not be needed.  Knowing the architecture of the M&S and the locations of 
the uncertainties can help understand how uncertainty propagates through the 
model to the results. 
 

(4) Inclusion in the M&S:  Indicating whether or not the (RWS) uncertainty is 
included in the M&S. 
 

(5) Type:  Classifying the type of uncertainty (e.g., epistemic or aleatory). 
 
(6) How well known:  An analyst may know there is something not known about a 
part or parameter of the RWS, but not know anything else.  Conversely, much 
may be known about a given part or parameter of a RWS with a lot of supporting 
data. 

 
(7) Magnitude:  The magnitude of an uncertainty may be given in qualitative or 
quantitative form.  If little is known about a particular system, then knowing a 
parameter may vary in a small or large way is useful.  For example, knowing the 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

142 of 157 

clearance height of a high-value satellite processing facility door requires more 
than qualitative specification. 

 
(8) Uncertainty Mitigation Plan:  For critical parameters with uncertainty, it may be 
useful to develop a plan for reducing that uncertainty. 

 

Table 30—Sample Table for the Uncertainties of a Process 

Name1
Source2
Location3
Included 
in M&S?4 

Type5
How 
Well 

Known6

Magnitude7
Mitigation 

Plan8 

 
The amount of uncertainty analysis is dependent on the criticality of the situation, though the 
exact amount is not generically determinable.  As with the other credibility assessment factors, 
this is accomplished on a case-by-case basis.  Uncertainties may be identified and analyzed or 
assessed in data/information from the RWS or in the methods of modeling various aspects of the 
model. 
 
NASA-STD-7009A, Table 5, Level Definitions for Factors in the M&S Use (Operations) 
Category, provides guidance for achieving the various credibility levels for the Uncertainty 
Characterization Factor. 
 
Table 31 shows how Uncertainty Characterization is affected by the various M&S life-cycle 
phases. 
 

Table 31—Life-Cycle Phase Influence on Uncertainty Characterization 

Phase
Name
Uncertainty Characterization is affected by

Pre-A
Model Initiation

A
Model Concept 
Development 

•
Uncertainties from the RWS are identified, analyzed, and 
assessed for inclusion in the model. 

•
Uncertainties induced from particular modeling methods.

B
Model Design
•
The model is designed to incorporate (or allow the 
incorporation of) uncertainties. 

• 
The design of the model will also solidify uncertainties 
induced by modeling methods.

C
Model Construction
•
Capabilities to incorporate uncertainties, or modeling 
methods that induce uncertainties, are built into the model. 

D
Model Test
•
Uncertainties are characterized in the model under test 
conditions.

E
Model Use
•
Uncertainties from model use are characterized and reported.

F
Model & Analysis 
Archival 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

143 of 157 

 
D.8  
Results Robustness 

 
The robustness of model results is determined from the analysis of model sensitivities.  These 
inherent sensitivities may first be assessed during model testing to characterize the sensitivity of 
the model (in other words, to characterize the robustness of model response).  The ideal outcome 
from sensitivity analysis are results that indicate the model sensitivities are the same as that of 
the RWS.  When the model is operationally used, sensitivities are again analyzed to determine 
the specific robustness of the model results to the scenarios undertaken. 
 
NASA-STD-7009A, Table 5, Level Definitions for Factors in the M&S Use (Operations) 
Category, provides guidance for achieving the various credibility levels for the Results 
Robustness Factor. 
 
Table 32, Life-Cycle Phase Influence on Results Robustness, shows how Results Robustness is 
affected by the various M&S life-cycle phases. 
 

Table 32—Life-Cycle Phase Influence on Results Robustness 

Phase
Name
Results Robustness is affected by

Pre-A
Model Initiation

A
Model Concept 
Development 
 

B
Model Design

C
Model Construction

 

D
Model Test
•
Sensitivities are first assessed during model testing to 
characterize the sensitivity of the model (in other words, to 
characterize the robustness of model response).  The ideal 
outcome from sensitivity analysis are results that indicate the 
model sensitivities are the same as that of the RWS.

E
Model Use
•
Sensitivities are analyzed with respect to the specific 
scenarios used to determine the specific robustness of the 
model results.

F
Model & Analysis 
Archival 
 

 
D.9  
M&S History 

 
The M&S History Credibility Factor includes two distinct parts:  The change history and the use 
history of the M&S.  The M&S change history is how new or how recently changed the M&S is, 
while the use history is how the M&S was used.  When comparing current uses of the M&S with 
past uses, the change or revision history of the M&S is also to be considered. 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

144 of 157 

While model development begins with Pre-Phase A and Phase A, the actual model design is not 
established until Phase B; after which, formal Change History is preferred, if not required. 
 
NASA-STD-7009A, Table 6, Level Definitions for Factors in the Supporting Evidence Category, 
provides guidance for achieving the various credibility levels for the M&S History Factor. 
 
Table 33, Life-Cycle Phase Influence on M&S History, shows how M&S History is affected by 
the various M&S life-cycle phases. 
 

Table 33—Life-Cycle Phase Influence on M&S History 

Phase
Name
M&S History is affected by

Pre-A
Model Initiation

A
Model Concept 
Development

B
Model Design
•
The baseline of the original model’s design establishes the 
beginning of the “real” model.

C
Model Construction
•
When model implementation is complete, change tracking is 
established. 

D
Model Test
•
Successful model testing (both verification & validation) 
substantiates the model baseline for use.

E
Model Use
•
Use of the model provides real-world application of the 
model that can further substantiate model validation and 
support use on similar RWSs or similar RWS scenarios.

F
Model & Analysis 
Archival 
 

 
D.10  M&S Process/Product Management 
 
M&S Process/Product Management conveys the extent to which an M&S effort exhibits the 
characteristics of work product management, process definition, process measurement, process 
control, process change, continuous improvement, including CM and M&S support and 
maintenance.  There is the potential for any process or product in the entire M&S life cycle to be 
formally managed or controlled. 
 
NASA-STD-7009A, Table 6, Level Definitions for Factors in the Supporting Evidence Category, 
provides guidance for achieving the various credibility levels for the M&S History Factor. 
 
Table 34, Life-Cycle Phase Influence on M&S Product/Process Management, shows how M&S 
Product/Process Management is affected by the various M&S life-cycle phases. 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

145 of 157 

 

Table 34—Life-Cycle Phase Influence on M&S Product/Process Management 

Phase
Name
M&S Product/Process Mgt is affected by

Pre-A
Model Initiation
•
RWS info/data is gathered to support model development.

A
Model Concept 
Development 

•
RWS info/data.

•
Modeling concepts chosen.

B
Model Design
•
Official baseline model design is established.

C
Model Construction
•
Official baseline model is established.

 

D
Model Test
•
Plans, procedures, & scenarios for testing (verification or 
validation) are established to accept the model. 

• 
Documentation of permissible uses and user documentation 
(e.g., User’s Guide) is formally established. 

•
The “accepted” model is deemed ready for use.

E
Model Use
•
Proposed Uses, Use Assessments, & outcomes.

• 
Scenarios for model use and definition of model setup 
established for the specific use. 

•
Output and Results obtained & reported.

F
Model & Analysis 
Archival 

•
Processes & products are defined at specific collection 
points throughout the M&S life cycle. 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

146 of 157 

APPENDIX E  

 

M&S RISK ASSESSMENT 

 
 
E.1 
Purpose  

 
This appendix provides guidance for assessing M&S risks.  
 
E.2 
M&S Risk 

 
The discussion of M&S risk is usually focused on the RWS the M&S is representing.  One major 
reason for developing or using an M&S is to accomplish RWS analyses using a surrogate for the 
RWS, thus, removing risk from the RWS.  Due to expense, availability, or cost of performing an 
analysis on the RWS, using a surrogate is often preferred.  Such surrogates are often non-
operational replicants, test fixtures, emulators, analysis systems, and, increasingly, M&S.  These 
surrogates potentially remove many, most, or all of the risks to the RWS. 
 
The RWS situation (i.e., operations or processes) are then performed using the M&S (as a 
surrogate), with the risks experienced on the surrogate instead of the RWS.  What becomes a 
concern, then, is the ability of the surrogate to fully (completely and accurately) represent the 
RWS.  If the M&S is insufficient for a proposed use, the implications indicated from the use of 
an M&S (e.g., analysis) may not be useful (or directly transferrable) to the RWS.  M&S risk is, 
therefore, a measure of the potential inability of an M&S to correctly represent the RWS.  Given 
the M&S risk, the decision maker ascertains the risk to the RWS.  This inability is necessarily 
associated with how the M&S is used to represent the RWS, the likelihood that the 
representation will be inadequate, and the consequences if it occurs. 
 

M&S risks are discussed throughout NASA-STD-7009A (Table 35, Risk Related Topics in 
NASA-STD-7009A) and may be introduced during any phase of the M&S life cycle (Table 36, 
Examples of Possible Risks throughout the M&S Life Cycle). 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

147 of 157 

Table 35—Risk-Related Topics in NASA-STD-7009A 

7009 Topic
Addressed …
Location in STD

Credibility
… to reduce risk …
1.1

Definition of 
Margin 

… to account for uncertainties and risks
3.2

Definition of 
Risk 

… the probability a program or project will 
experience an undesired event; and the 
consequences 

3.2

Credibility 
Factors 

… to reduce, assess, and communicate risk
4

Assumptions & 
Abstractions  

introduces risks
4.2.1 [M&S 11] Rationale

Unexplained 
Warning or Error 
Messages 

increase risk
4.3.1 [M&S 27] Rationale

More than just 
the Results 

… the risks associated with accepting the 
results  

4.3.8

M&S-based 
Analysis 

… assessment of and rationale for the risks
associated  

4.3.8 [M&S 39]

Prog/Proj Risk
… inform program/project risk management 
processes 

4.3.8 [M&S 39] Rationale

M&S Risk 
Assessment 

These risks may be due to factors inherent to 
the M&S, or associated with the specific 
application or use of the M&S

4.3.8 [M&S 39]
Expl. Note 

Criticality 
Assessment 

to mitigate potential risks
[M&S 6] & Appendix D

 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

148 of 157 

Table 36—Examples of Possible Risks throughout the M&S Life Cycle 

Model Phase

Examples of Influence on Risk 

Designator
Name

Pre-A
Model Initiation
• 
Amount & Quality of RWS Info Available. 

A 
Model Concept 

• 
Amount of Time, Money, & Resources Available for 
Model Development. 

B 
Model Design 
• 
Trades in Model Design that Affect Fidelity. 

C 
Model Construction 

•
Choices in Model Implementation that Affect RWS 
Representation. 

D 
Model Test 

•
Completeness in Verification.

• 
Completeness in Validation. 

E 
Model Use 

• 
Appropriateness of Proposed Use to Permissible Use. 

• 
Amount & Quality of Input Data Available. 

• 
Completeness in Model Use to discover accuracy, 
uncertainties, & sensitivities. 

• 
Warning or Errors during Model Use. 

• 
Correct & Complete post-use analysis of data. 

F 
Model & Analysis 
Archival 

• 
Adherence to Work Product Mgt. 

• 
Understanding Model Change History & Past Uses. 

 
While risks incurred in either development or use of the M&S are best understood and mitigated 
when they occur, any M&S risks having implications to the RWS are to be assessed and reported 
with the results of any M&S-based results [M&S 39].  These M&S risks are then to inform the 
applicable program/project risk management processes and procedures (refer to NPR 8000.4) for 
risk-informed decision making (Figure 18, NASA RIDM Process) and continuous risk 
management (CRM) (Figure 19, NASA CRM Process). 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

149 of 157 

 

Figure 18—NASA RIDM Process 

 

Figure 19—NASA CRM Process 

 
Additional guidelines for the entire NASA risk management approach are found in NASA/SP-
2011-3422, NASA Risk Management Handbook, and NASA SP-2010-576, NASA Risk-
Informed Decision Making Handbook. 
 
 

Risk-Informed Decision Making (RIDM)  

Analysis of Alternatives
Conduct Integrated Analysis of Risk of Each 
Alternative; Develop the Technical Basis for 
Deliberation 

Risk-informed Alternative Selection 
Deliberate; Select an Alternative and Accept the 
Associated Risk Informed by Risk Analysis Results, 
and Document the Decision and its Rationale 

Identification of Alternatives
Formulate Objectives and Performance Measures; 
Formulate Decision Alternatives, Recognizing both 
Risks and Opportunities

TO CRM

Continuous Risk Management 
(CRM) 

From RIDM

Control

Track

Plan

Analyze

Identify

Communicate
Document


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

150 of 157 

E.3 
Aspects of M&S Risk 

 
While the emphasis is on RWS risk, the M&S practitioner is to identify what risks are incurred 
during M&S development and use. 
 
Most, if not all, of the R/r’s in NASA-STD-7009A may relate to some aspect of (M&S) risk, 
either by: 
 

a. Identification of the risk element. 
 
b. Description of the context (of the situation the M&S is representing). 
 
c. Understanding the influence of the specific risk element (to the M&S results and, in 
turn, the RWS). 

 
d. Clearly communicating risk elements when reporting the results from an M&S-based 
use. 
 
These aspects of risk, as contained in NASA-STD-7009A, are shown in this NASA Technical 
Handbook’s section 5.6.3.2.2, Table 14.  While these elements may not be critical to the correct 
functioning of the M&S (i.e., the ability of the M&S to produce acceptable or useful results), 
having them can provide greater clarity than if they were not addressed.  The NASA-STD-
7009A requirements (including their rationale statements) and recommendations provide 
additional information as to what is needed to more fully understand each element and Table 11 
(Technical Review), Table 12 (People Qualifications), and Table 13 (Documentation) in this 
NASA Technical Handbook. 
 
A detailed listing of the elements and sub-elements of M&S risk are consolidated in Table 37 for 
convenience. 
 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

151 of 157 

 

Table 37—Detailed M&S Risk Elements 

7009 Req't
Reporting Req't
Does risk 
exist w.r.t. 
this item? 
(Yes / No)

If yes, 
describe 
the 
risk(s).

If yes, provide the 
rationale for 
proceeding with 
the risk(s).

[M&S 31]
Credibility Assessment
Data Pedigree
Verification
Validation
Input Pedigree
Uncertainty Characterization
Results Robustness
M&S History
M&S Process/Product Mgt

[M&S 32]
Caveats

(1)
Unachieved Acceptance Criteria

(2)
Violation of any Assumptions

(3)
Violation of the Limits of 
Operation

(4)
Execution Warning and Error 
Messages

(5)
Unfavorable outcomes from the 
proposed use assessments

(6)
Unfavorable outcomes from 
Setup/Execution Assessments

(7)
Waivers to Requirements

[M&S 33]
Uncertainty in Results

(1)
Quantitative Estimate

(2)
Qualitative Description

(3)
No estimate or description given

[M&S 34]
Uncertainty Processes
Processes for obtaining 
Uncertainties in M&S Input
Processes for obtaining 
Uncertainties in M&S Results
Processes for obtaining 
Uncertainties in Quantities 
Derived from M&S Results


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

152 of 157 

7009 Req't
Reporting Req't
Does risk 
exist w.r.t. 
this item? 
(Yes / No)

If yes, 
describe 
the 
risk(s).

If yes, provide the 
rationale for 
proceeding with 
the risk(s).

 

[M&S 36]
Technical Review
Review
- What was reviewed?
- Depth of Review
- Formality of Review
- Currency of Review
Reviewers
- Expertise
- Independence

[M&S 37]
People Qualifications
Developers
Testers
Users (Operators)
Analysts

[M&S 38]
M&S Documentation 
(Synopsis)

[M&S 6]
Criticality Assessment

[M&S 7]
M&S in Scope of 7009

[M&S 9]
Technical Reviews

[M&S 10]
Relevant Characteristics of RWS 
for M&S Development

[M&S 11]
Assumptions & Abstractions

[M&S 12]
Structure & Math of M&S

[M&S 13]
Limits of Operation

[M&S 14]
Permissible Uses

[M&S 16]
Domain of Verification

[M&S 18]
Domain of Validation

[M&S 19]
Processes for Characterizing 
Uncertainty in Referent Data

[M&S 20]
Methods of Uncertainty 
Propagation in M&S

[M&S 21]
Incorporated Uncertainties

[M&S 22]
Proposed Uses


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

153 of 157 

7009 Req't
Reporting Req't
Does risk 
exist w.r.t. 
this item? 
(Yes / No)

If yes, 
describe 
the 
risk(s).

If yes, provide the 
rationale for 
proceeding with 
the risk(s).

[M&S 23]
Use Assessment

[M&S 24]
Input Data

[M&S 25]
Setup & Execution Rationale

[M&S 27]
Warning or Error Messages

[M&S 28]
Processes for Characterizing 
Uncertainty in Input, Results, 
Derived Results

[M&S 29] (1)
Uncertainties in Input

[M&S 29] (2)
Uncertainties in Results

[M&S 29] (3)
Uncertainties in Derived Results

[M&S 30]
Sensitivity Analyses

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

154 of 157 

APPENDIX F  

 

REFERENCES 

 

 
F.1 
Purpose  

 
This appendix provides guidance in the form of additional reference documentation not named in 
the body of the text but that may provide supplementary information to the reader. 
 
F.2 
Reference Documents 

 
F.2.1 Government Documents 
 

DoD 

VV&A Recommended Practices Guide Glossary. Retrieved May 
20, 2011.  
http://vva.msco.mil/Mini_Elabs/VVtech-informal.htm#inf3

 
Los Alamos National Laboratory 
 
LA-14167-MS
Thacker, B.H.; Doebling, S.W.; Hemez, F.M.; Anderson, M.C.; 
Pepin, J.E.; and Rodriguez, E.A. (October 2004). Concepts of 
Model Verification and Validation.

 
NASA 
 
NASA-HDBK-
8739.19-3

Measurement Uncertainty Analysis Principles and Methods
NASA Measurement Quality Assurance Handbook – ANNEX 3

RP-08-118
NASA Standard for Models and Simulations (M&S):  Development 
Process and Rationale

Bolognese, J. (2009). The FEMCI Book. Retrieved February 21, 
2018. http://femci.gsfc.nasa.gov/femcibook.html

JWST-PLAN-006165
 

James Webb Space Telescope (JWST) System Modeling and 
Analysis and JWST Models Validation, Verification and 
Calibration Plan (SE-18), D42916 Rev. B

JWST-REF-002290
James Webb Space Telescope Math Models Guidelines Document 
(SE16), September 19, 2007, D36124 Rev. C

 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

155 of 157 

National Institute of Standards and Technology (NIST) 

 
 

 
 

 
Sandia National Laboratories 
 
SAND2005-4302
Oberkampf, W.; Barrone, M. (August 2005). Measures of 
Agreement Between Computation and Experiment: Validation 
Metrics.

SAND2007-0853
Oberkampf, W.; Trucano, T. (February 2007). Verification and 
Validation Benchmarks. 

SAND2013-8051
Richard G. Hills, Walter R. Witkowski, William J. Rider, Timothy 
G. Trucano, Angel Urbina (September 2013). Development of a 
Fourth Generation Predictive Capability Maturity Model.

SAND2016-6465 TR
How to PIRT (July 2016)

SAND2016-6466 TR
What is PIRT? (July 2016)

 
F.2.2 Non-Government Documents 
 

AIAA. AIAA Guide to Assessing Experimental Uncertainty - Supplement to S-071A-1999  
(G-045-2003e). 

 
ANSI/NCSL Z540 2-1997 (R2012). (1997). U.S. Guide to the Expression of Uncertainty 
in Measurement. 

 
SAE EIA-649-2, Configuration Management Requirements for NASA Enterprises. 

 

Bedford, T.J.; Cooke, R.M. (2001). Probabilistic Risk Analysis: Foundations and 
Methods. Cambridge, England: Cambridge University Press. 

 
Briggs, C. (April 2007). Managing Analysis Models in the Design Process. Paper AIAA-
2007-2286 presented at the 48th AIAA/ASME/ASCE/AHS/ASC Structures, 
Structural Dynamics, and Materials Conference. Honolulu, HI.  

 
Cloud, D.; Rainey, L.B. (1998).  Applied Modeling and Simulation. New York:  
McGraw-Hill. 

 
Cooke, R.M. (1991). Experts in Uncertainty: Opinion and Subjective Probability in 
Science. New York: Oxford University Press. 

 

NIST Technical Note 
1297

Taylor, B.N.; Kuyatt, C.E. (1994). Guidelines for Evaluating and 
Expressing the Uncertainty of NIST Measurement Results.


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

156 of 157 

Cullen, A.C.; Frey, H.C. (1999). Probabilistic Techniques in Exposure Assessment: A 
Handbook for Addressing Variability and Uncertainty in Models and Inputs. New 
York: Springer-Verlag.  

 
Evans, M.; Hastings, H.; and Peacock, B. (2000). Statistical Distributions Third Edition.  
Hoboken: John Wiley & Sons, Inc.   

 
ISO/IEC Guide 98-3:2008, Uncertainty of measurement -- Part 3: Guide to the expression 
of uncertainty in measurement (GUM:1995). 

 
ISO/IEC/IEEE 24765:2010 Systems and software engineering—Vocabulary. 
 
Law, A.M. (2006). Simulation Modeling and Analysis 4th Edition. Boston: McGraw-Hill. 
 
Muheim, D.M.; Menzel, M.; Mosier, G.; Howard, J.; Irish, S.; Maghami, P.; Mehalick, 
K.; Parrish, K.; Pitman, J.; Thomson, S.; Asuquo, C.; Blaurock, C.; Congedo, C.; 
Ha, K.; Holmes, N.; Liu, F.; McGinnis, M.; Mariconti, S.; May, C.; Russell, B.; 
Sanders, J.; Shiri, S.; Smith, J.; and Skelton, D. (August 2010). An Update on the 
Role of Systems Modeling in the Design and Verification of the James Webb 
Space Telescope.  Paper presented at Modeling, Systems Engineering, and Project 
Management for Astronomy IV. SPIE 7738. San Diego, CA.  

 
Oberkampf, W.L.; Roy, C.J.  (2009). Verification and Validation in Computational 
Simulation. Cambridge, England: Cambridge University Press. 

 
Rainey, L.B. (2004). Space Modeling and Simulation - Roles and Applications 
throughout the System Life Cycle. El Segundo, CA: The Aerospace Press and the 
American Institute of Aeronautics and Astronautics. 

 
Saltelli, Andrea. (2005). “Global Sensitivity Analysis: An Introduction.” In Kenneth M. 
Hanson and François M. Hemez, Eds., Sensitivity Analysis of Model Output.  27-
43. Los Alamos National Laboratory, NM. 

 
Sargeant, R.G.  (2007). Verification and Validation of Simulation Models. Paper 
presented at the 2007 Winter Simulation Conference.  Washington, D.C. 

 
Steele, M., Dimensions of Credibility in Models and Simulations, Paper 08E-SIW-076 
presented at the European Simulation Interoperability Workshop 2008. 
Edinburgh, Scotland. 

 
Suter, G.W., ed. (2006). Ecological Risk Assessment. Boca Raton: CRC Press. 
 
Vose, D. (2008). Risk Analysis: A Quantitative Guide. West Sussex, England: John Wiley 
& Sons, Ltd. 

 
 


NASA-HDBK-7009A 
 

APPROVED FOR PUBLIC RELEASE – DISTRIBUTION IS UNLIMITED  

157 of 157 

APPENDIX G 

 

TECHNICAL WORKING GROUP 

 
 
G.1 Purpose  
 
This appendix provides guidance in a list of the individuals in the TechnicalWorking Group who 
drafted this NASA Technical Handbook and can provide additional guidance, as necessary for 
implementing the practices in NASA-STD-7009A or this NASA Technical Handbook  
 
G.2 Technical Working Group  
 
Name
Center

Martin Steele, Ph.D.
(Office of Primary Responsibility Designee) 
Kennedy Space Center 

Wei Lin 
Ames Research Center  

Trong Bui, Ph.D. 

Seung Y. Yoo, Ph.D. 

Manuel Castro 

Armstrong Flight Research Center 

Jerry Myers, Ph.D. 
Glenn Research Center 

Gary Mosier 

Jeffrey Bolognese, Ph.D. 
Goddard Space Flight Center 

Steven Cornford, Ph.D. 
Jet Propulsion Laboratory 

Paul Bielski 
Johnson Space Center 

Thomas West, Ph.D. 
Langley Research Center 

Timothy Barth, Ph.D.  
NASA Engineering and Safety Center 
(Kennedy Space Center) 

Kenneth Johnson  
NASA Engineering and Safety Center 
(Marshall Space Flight Center) 

Laurence de Quay, Ph.D.
Stennis Space Center

 

For further questions or guidance in the use of this NASA Technical Handbook, contact the 
Office of Primary Responsibility or other Center representatives listed above. 


