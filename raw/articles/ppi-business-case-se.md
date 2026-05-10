P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 1 of 48

THE BUSINESS CASE FOR 
SYSTEMS ENGINEERING

10 March 2018 

Robert J Halligan, FIE Aust CPEng


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 2 of 48

Robert J Halligan, FIE Aust CPEng

Managing Director
Project Performance International 

Content Contributor
to EIA/IS-632, EIA 632, IEEE 1220, 
ISO/IEC 15288 SE standards

Past INCOSE Head Of Delegation
to ISO/IEC SC7 on Software and
Systems Engineering

Past Member of the INCOSE 
Board of Directors

Past President
Systems Engineering Society of 
Australia

Consultant/Trainer
to BAE Systems, Mitsubishi, 
Airbus, Thales, Raytheon, General 
Electric, Boeing, Lockheed, 
General Dynamics, OHB, Nokia, 
AREVA,  BHP Billiton, Rio Tinto, 
Embraer, Halliburton and many 
other leading enterprises on six 
continents

rhalligan@ppi-int.com


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 3 of 48

SEI/AESS/NDIA 2012 STUDY RESULTS

http://resources.sei.cmu.ed
u/asset_files/specialreport/
2012_003_001_34067.pdf

Driver
Relationship to Performance 
(Gamma)

All Projects
Lower challenge
Higher challenge

SEC-Total – total deployed SE
+0.49
+0.34
+0.62

SEC-PP – project planning
+0.46
+0.16
+0.65

SEC-REQ – reqts. developt. & mgmt.
+0.44
+0.36
+0.50

SEC-VER – verification
+0.43
+0.27
+0.60

SEC-ARCH – product architecture
+0.41
+0.31
+0.49

SEC-CM – configuration management
+0.38
+0.22
+0.53

SEC-TRD – trade studies
+0.38
+0.29
+0.43

SEC-PMC – project monitor & control
+0.38
+0.27
+0.53

SEC-VAL – validation
+0.33
+0.23
+0.48

SEC-PI – product integration
+0.33
+0.23
+0.42

SEC-RSKM – risk management
+0.21
+0.18
+0.24

SEC-IPT – integrated product teams
+0.18
-0.12
+0.40

Gamma
Relationship

-0.2 <| Gamma | ≤  0
Weak negative

0 ≤ | Gamma | < 0.2 
Weak positive

0.2 ≤ | Gamma | < 0.3 
Moderate

0.3 ≤ | Gamma | < 0.4 
Strong

0.4 ≤ | Gamma | 
Very strong

Source: “The Business Case for Systems Engineering Study: Results of the Systems 
Engineering Effectiveness Survey”, CMU/SEI-2012-SR-009, November 2012


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 4 of 48

OUR JOURNEY:

• What are our challenges?
• What is systems engineering?
• Why systems engineering?
• Studies on the value of systems engineering
• ROI for one facet: Requirements Analysis


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 5 of 48

KICK-OFF EXERCISE:

In groups of 3-4 people, consider the question 
“what are the greatest challenges that we (you) 
face in your engineering”? List as many 
challenges as you can, in the time designated.


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 6 of 48

WHERE WE HAVE COME FROM
– OOPS GOT THAT WRONG!


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 7 of 48

TODAY, AND NOT JUST IN KABUL!


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 8 of 48

THE PROBLEM IN GENERAL:

Standish Group study of 8380 IT-based projects
See also Morris and Hough, “The Anatomy of Major Projects”


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 9 of 48

Average cost 
overrun: 89%

For “challenged” 
and cancelled 
projects:

% of 
Projects

Average cost 
overrun: 89%

Standish Group study of 8380 IT-based projects

For “challenged” 
and cancelled 
projects:

% of 
Projects

% of Cost Overrun

THE PROBLEM – COST:


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 10 of 48

% of 
Project
s

Standish Group study of 8380 IT-based projects

For “challenged” 
and cancelled projects:

% of 
Projects

% Schedule Overrun

Average schedule
overrun: 122%

THE PROBLEM – SCHEDULE:


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 11 of 48

THE PROBLEM – QUALITY:

Average missing
features: 39%

For “challenged” 
projects:

% of 
Project
s

Average missing
features: 39%

For “challenged” 
projects:

% of 
Projects

% of Missing Features

Standish Group study of 8380 IT-based projects


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 12 of 48

SYSTEMS THINKING – A FOUNDATION

•

leads to

leads to

Outward and Upward Looking View
(part of one or more bigger systems)

System Views

Object View
(object with required and desired 
characteristics)

Inward Looking View
(seeing the system destined to become a set 
of interacting objects, the properties of the 
whole coming from the objects and their 
interactions)

PPI-005918-4

Requirements

+

Goals


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 13 of 48

WHAT IS SYSTEMS ENGINEERING?


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 14 of 48

INTEGRATE VERIFICATION & VALIDATION

WEDGE
MODEL

e.g. test
RSA

S

SE

SE

SE

S

SE

SE

SE

(e.g., Aircraft, 
Air Traffic Control
System)

(e.g., Propulsion 
System, Airframe)

(e.g., Engine, 
Fuel Pump)

S R A

time
trend

DESIGN
BUILD

Verification:
Is the work product correct-meets requirements?         
Validation:
Does the work product satisfy the need for the work product?         

O T & E

S R A , S R R , A D R , D D R

Legend :
A Build, increment, etc.
ADR
Architectural Design Review
DDR
Detailed Design Review
HWITLS  
Hardware in the Loop Simulation
OT&E
Operational Test & Evaluation
PCA
Physical Configuration Audit
PITLS
People in the Loop Simulation
RSA (FCA)
Requirements Satisfaction Audit
S
Top-Level System
SE
System Element
SRA
System Requirements Analysis
SRR
System Requirements Review
SWITLS 
Software in the Loop Simulation

PPI-006003-9
© Copyright Project Performance (Australia) Pty Ltd 2007 - 2017

™

PCA

PCA

PCA
S R R
A D R A D R

D D R
D D R

trend
time

HWITLS
PITLS
SWITLS

time

Needs
Information

PROJECT PERFORMANCE

INTERNATIONAL

www.ppi-int.com


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 15 of 48

THE ESSENCE OF SE:

•
ensure adequate problem definition

•
define possible solution alternatives

•
qualify solution alternatives for feasibility & effectiveness

•
develop qualified alternatives

•
use logical design as an aid in developing physical
design (model-based design)

•
design through levels of abstraction – architecture and
detail

•
maintain a clear distinction between problem and solution


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 16 of 48

AND MORE …

•
conduct trade-off studies and optimization to maximize
overall effectiveness

•
specify solution elements to objective adequacy

•
integrate engineering specialties with technology expertise

•
verify work products (correct – the product right)

•
validate work products (needed – the right product)

•
employ configuration management

•
do only work that adds value

•
manage the engineering – plan, organize, inspire, assess,
control.


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 17 of 48

WHEN IS SYSTEMS ENGINEERING 
APPLIED?

• Solution development phase

• New Systems/Products
• Families of Products

• Solution build/production phase

• To correct design deficiencies

• Sustainment/operations and support phase

• Modifications to track changing need
• Incremental/competitive improvements for business 
reasons

• Response to obsolescence


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 18 of 48

WHAT IS SYSTEMS ENGINEERING 
APPLIED TO?

• The enterprise

• Capability/business/enterprise systems
• End-use products

• Production systems

• Maintenance systems
• Training systems

• Project systems
• Engineering systems

• Anything else for which a solution does not already exist, and is sought!


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 19 of 48

PPI-005332-6

© Copyright Project Performance (Australia) Pty Ltd 2007-2014

0

1000

Benefit to Company - e.g. ∆ NPV 

Benefit to Customer
        (external or internal)
Optimum
solution for the
company

1:1 Customer/Contractor
      Business Model

Internet Scam
Company
Business 
Model

Product-Oriented
Free Market Place
Business Model

Trade Off: Interests of Secondary Stakeholder (Customer) versus Primary Stakeholder (company)

Optimum
solution for 
the company
0

+

-

origin on x axis represents a 
threshold of acceptability.

Internal Project

(Net Present Value)

IN WHAT BUSINESS MODELS?


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 20 of 48

INDICATORS OF EFFECTIVE SE 
– PRODUCT-ORIENTED ENTERPRISE:

•
On, under, or close to development budget

•
On, ahead of, or close to development schedule

•
High Return on Sales

•
Market leadership

•
Low warranty costs

•
Repeat business is the norm

•
High staff satisfaction and retention


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 21 of 48

INDICATORS OF EFFECTIVE SE 
– CONTRACT-ORIENTED ENTERPRISE:

•
On, under, or close to development budget

•
On, ahead of, or close to development schedule

•
High contract gross margin

•
High customer satisfaction

•
Low warranty costs

•
Repeat business is the norm

•
High staff satisfaction and retention


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 22 of 48

INDICATORS OF EFFECTIVE SE 
– INTERNAL PROJECTS:

• On, under, or close to development budget

• On, ahead of, or close to development schedule
• High internal customer satisfaction

• No desire to outsource

• High staff satisfaction and retention


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 23 of 48

INDICATORS OF EFFECTIVE 
SYSTEMS ENGINEERING 
MANAGEMENT:

•
Effective systems engineering

•
Harnessing of creativity

•
A learning environment

•
Growing intellectual capital within the enterprise

•
High staff satisfaction and retention

•
Shared vision of the outcome and a related focus on quality, cost, time


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 24 of 48

INDICATORS OF NO SE OR 
INEFFECTIVE SE:

• Milestones missed
• Significant dispute with stakeholders over requirements

• Many problems and delays occuring during system integration
• Significant dispute with customers over testing

• Significant problems occuring in released or fielded systems/products

• Engineering effort tends to be back-end loaded during development


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 25 of 48

WHERE DOES THE MONEY GO?

Cost component
Ideal %
Actual %

What proportion of development cost is spent 
due to genuine system requirements changes? 
There is no 
ideal.
?

What proportion of development cost is spent 
due to defective system requirements? 
0%
?

What proportion of development cost is spent 
due to system design errors undetected in design 
reviews? 
0%
?

What proportion of development cost is spent 
due to system design errors undetected in 
system testing? 
0%
?

What proportion of cost in a system integration 
phase is spent on system integration as opposed 
to rework?

Close 
to100%
?


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 26 of 48

McKINSEY STUDY (1)


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 27 of 48

McKINSEY STUDY (2)

5
C
S
OPTIMISING
U
E
S
R
4
T
V
MEASURED
O
I
3
M
C
DEFINED
E
E
R

3
C
DEFINED
>20
<4.0
<3.0
O
2
E
R

MANAGED
R
R
R
E
1
O
C
PERFORMED
<20
>4.0
>3.0
R
T
0
I
INITIAL
O
N

<0.8
<0.5

<2.0
<2.0

>35

>25

Service 
Quality
Maturity Level

Design Quality
Market Share %

Process Quality

Scrap%          Rework%

Quality Benefits

Equivalent to SMI

SOURCE: Excellence in Quality Management, McKinsey & Company, Inc. 

CMMI


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 28 of 48

OTHER OLD CLAIMS

1. Improved Quality of Designs

• Resulted in reduced Change Orders (> 50%)

2. Product Development Cycle

• Reduced as much as 40-60% by concurrent rather than sequential 
design of products and processes

3. Manufacturing Costs

• Reduced by as much as 30-40% by having integrated product teams 
integrate product and process designs

4. Scrap & Rework

• Reduced by as much as 75% through product and process design 
optimization

Data based on a study of 14 companies that had applied concurrent 
engineering - Institute for Defense Analysis (IDA), 'The Role of Concurrent 
Engineering in Weapons System Acquisition’, December 1988


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 29 of 48

NASA AND THE VALUE OF SE


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 30 of 48

INCOSE STUDY - COST 

SE Effort = SE Quality * (SE Cost/Actual Cost) 


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 31 of 48

INCOSE STUDY - SCHEDULE 

SE Effort = SE Quality * (SE Cost/Actual Cost) 


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 32 of 48

MCPM – MATURITY BY PROJECT 
CATEGORY MODEL, BRAZIL

Archibald & Prado, “PM Maturity 2006 Research –Maturity and Success in IT”, March, 2007


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 33 of 48

CMU/NDIA 2007 STUDY RESULTS

Source: “A Survey of Systems Engineering Effectiveness”, CMU/SEI-2008-SR-034, December 2008 


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 34 of 48

PROJECT ENGINEERING MATURITY 
MATRIX

Feedback: 
Process Continuously 
Improved

Quantitative:
Process Measured
Focus on metrics

Qualitative:
Process defined and
institutionalized

Focus on process org.

Intuitive:
Process depends on
individuals

Ad hoc/chaotic:
Unpredictable

System problem prevention
Technology innovation
Process management

Process mapping/variation
Process improvement database
Quantitative quality plans

Enterprise process definition
Education and training
Review and testing
Interdisciplinary teamwork
Life cycle engineering
Integrated systems management

System requirements mgmt
Project planning and tracking
System configuration mgmt
Quality management
System risk management

Increased
Customer
and
Producer
Satisfaction

Increased
Risk

5 OPTIMIZING

4 MANAGED

3 DEFINED

2 REPEATABLE

1

Maturity Level          Characteristics               Key Process Areas     


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 35 of 48

SEI/AESS/NDIA 2012 
STUDY RESULTS (1)

Source: “The Business Case for Systems Engineering Study: Results of the Systems Engineering 
Effectiveness Survey”, CMU/SEI-2012-SR-009, November 2012 

52%

29%
20%

33%

47%

24%

15%
24%

57%

0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
100%

Lower SEC (n=48)
Middle SEC (n=49)
Higher SEC (n=51)

Project Performance (Perf)

Total Systems Engineering Capability (SEC-Total)

Gamma = 0.49         p-value < 0.001

All Projects

Higher 
Perf

Middle 
Perf

Lower 
Perf


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 36 of 48

SEI/AESS/NDIA 2012 
STUDY RESULTS (2)

Legend: PC  Project Challenge

Source: “The Business Case for Systems Engineering Study: Results of the Systems Engineering 
Effectiveness Survey”, CMU/SEI-2012-SR-009, November 2012 

32%
19%
12%

45%
58%

36%

23%
23%

52%

0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
100%

Lower SEC
(n=22)
Middle SEC
(n=26)
Higher SEC
(n=25)

Low PC

Gamma = 0.34         p-value = 0.029

69%

39%
27%

23%

35%

12%

8%
26%

62%

0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
100%

Lower SEC
(n=26)
Middle SEC
(n=23)
Higher SEC
(n=26)

High PC

Gamma = 0.62         p-value < 0.001


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 37 of 48

SEI/AESS/NDIA 2012 
STUDY RESULTS (3)

http://resources.sei.cmu.ed
u/asset_files/specialreport/
2012_003_001_34067.pdf

Driver
Relationship to Performance 
(Gamma)

All Projects
Lower challenge
Higher challenge

SEC-Total – total deployed SE
+0.49
+0.34
+0.62

SEC-PP – project planning
+0.46
+0.16
+0.65

SEC-REQ – reqts. developt. & mgmt.
+0.44
+0.36
+0.50

SEC-VER – verification
+0.43
+0.27
+0.60

SEC-ARCH – product architecture
+0.41
+0.31
+0.49

SEC-CM – configuration management
+0.38
+0.22
+0.53

SEC-TRD – trade studies
+0.38
+0.29
+0.43

SEC-PMC – project monitor & control
+0.38
+0.27
+0.53

SEC-VAL – validation
+0.33
+0.23
+0.48

SEC-PI – product integration
+0.33
+0.23
+0.42

SEC-RSKM – risk management
+0.21
+0.18
+0.24

SEC-IPT – integrated product teams
+0.18
-0.12
+0.40

Gamma
Relationship

-0.2 <| Gamma | ≤  0
Weak negative

0 ≤ | Gamma | < 0.2 
Weak positive

0.2 ≤ | Gamma | < 0.3 
Moderate

0.3 ≤ | Gamma | < 0.4 
Strong

0.4 ≤ | Gamma | 
Very strong

Source: “The Business Case for Systems Engineering Study: Results of the Systems Engineering 
Effectiveness Survey”, CMU/SEI-2012-SR-009, November 2012


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 38 of 48

SEI/AESS/NDIA 2012
STUDY RESULTS (4)

Source: “The Business Case for Systems Engineering Study: Results of the Systems Engineering 
Effectiveness Survey”, CMU/SEI-2012-SR-009, November 2012 

Driver 
Relationship to Performance 

All projects 
Lower challenge 

projects 

Higher challenge 

projects 

PC – Project challenge 
-0.26 � Moderate 
negative 
-0.26 � Moderate 
negative 
-0.23 � Moderate 
negative 

EXP – Prior experience 
+0.36 � Strong 
positive 
+0.51 � Very strong
positive 
+0.19� Weak 
positive 

 


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 39 of 48

A Look at Return on Investment
for One Facet of Systems Engineering: 
Requirements Analysis


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 40 of 48

Initial (Originating)
Stakeholder
Requirements (if any) 
- e.g. user.
(SyRS, e.g. URS)

Other Info

AND

1

2

3

4

AND

5

AND

6

Ref.
Ref.
AND

4.2.1

4.2.2

4.2.3

4.2.4

OR
OR
LP
LP

3
5

SyRS-Refined

VRS

OCD

VM
Analytical work products

OCD:  
operational concept description (CONUSE)

URS:  
SyRS of user requirements

SyRS:  
system requirements specification

VM: 
 
value (or system/software effectiveness) model

VRS:  
verification requirements specification

PPI-005499-4

is a restatement of
traces to/from


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 41 of 48

Legend:

IDENTIFY
STAKEHOLDERS

STATES &
MODES
ANALYSIS

READ &
ASSESS
INPUTS

PLAN
THE SRA

CONTEXT
ANALYSIS

FUNCTIONAL
ANALYSIS

REST OF
SCENARIO
ANALYSIS

PARSING
ANALYSIS

OUT-OF-RANGE
ANALYSIS

ERA
ANALYSIS

CLEAN-UP

MEASURE
REQUIREMENTS
QUALITY

DESIGN
REQUIREMENTS
ANALYSIS

OTHER
CONSTRAINTS
SEARCH

VERIFICATION
REQUIREMENTS
DEV.

OCD
DEVELOPMENT
S/H
VALUE
ANALYSIS

*

*

*

PPI-006248-2

REQUIREMENTS ANALYSIS
(CAPTURE AND VALIDATION)
METHODOLOGY

SRA System Requirements Analysis
S/H Stakeholder
DEV Development
OCD Operational Concept Description (CONUSE)
ERA Entity Relationship Attribute
 
Perform only if there are initial specified 
* requirements as an input to the analysis.


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 42 of 48

REQUIREMENTS QUALITY AND 
REQUIREMENTS ANALYSIS EFFORT

Have
Need
Number of Requirements
Skills
Tech-Environment
Access & Cooperation)

0
0

 .3

1
1

Risk M 

Risk H

Have
0.5

WORK = f(

 0.85-0.98

Need
0.9

WORK!
(SRA)

P007-004138-4

Risk L


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 43 of 48

Organization/Project 
Overruns Attributed to 
Requirements Problems 

NASA over two decades (Werner 
Gruhl) 

70% of overruns  

U.S. Census Bureau project 2009 
80% cost overrun locked in solely due to 
poor requirements 

Marine One Helicopter Program 
83% cost overrun attributed by Lockheed 
to requirements problems 

Schwaber, 2006; Weinberg, 1997; 
Nelson et al, 1999 

“Requirements errors are the single 
greatest source of defects and quality 
problems”  

Hofmann and Lehner, 2001  
“Deficient requirements are the single 
biggest cause of software project failure” 

Standish Group, The Chaos Report on 
8300 IT projects 

60.9% of an average 89% cost overrun 

 

IMPACT OF REQUIREMENTS DEFECTS


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 44 of 48

Parameter 
Value 

Contract value 
$4B 

Requirements on the Ship 
27,000, only fair in quality 

Consequence if uncorrected 
At least 20% loss of capability, costing at 
least $800M; or 
Rework costs exceeding 20% 

Cost of fixing the requirements 
$8M (0.2% of contract value) 

Return on Investment 
Approximately 100:1 

 

REQUIREMENTS ANALYSIS ROI TO 
CUSTOMER


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 45 of 48

Paramater 
Value 

% Sales spent on marketing 
12.5% 

% Sales spent on bidding 
9-10% 

Win ratio for the more successful 
companies 

1 in 2 to 1 in 4 

Typical cost/bid, % Total Contract Value 
2-3% TCV 

Cost of winning business from a new 
customer vis-à-vis a satisfied existing 
customer 

5:1 

Cost of preserving customer satisfaction 
through requirements analysis 

0.2% TCV 

 

REQUIREMENTS ANALYSIS ROI FOR A 
CONTRACTOR

TCV: Total Contract Value


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 46 of 48

CONCLUSIONS:

1.
The practice of engineering can be immature
• Sometimes ad hoc and chaotic – that is destructive to success via  
satisfaction of users and other stakeholders.

2.
The evidence is now compelling that the practice of systems 
engineering contributes to enterprise success in terms of: 
• reduced costs
• shorter timeframes
• increased value achieved in using the system.


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 47 of 48

CHALLENGES – HOW DID WE GO?

We will review the list of challenges 
from earlier, and the contributions 
made by "a systems approach to the 
engineering of systems".


P1314-005216-3 
© Copyright Project Performance (Australia) Pty Ltd 1998-2018

Page 48 of 48

THE QUESTION IS NO LONGER, “SHOULD WE BE 
PRACTICING SYSTEMS ENGINEERING?” 
"YES" IS BEYOND DOUBT.

TODAY'S QUESTION IS,
“HOW BEST DO WE DO IT?”

Robert J. Halligan
Email: rhalligan@ppi-int.com


