<!-- Page 1 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Connecting Requirements to 
Test Execution with MBSE and MBT
Presented by Andrew Pollner and Katherine Pilat
ALP International Corporation
5425 Wisconsin Avenue
Suite 600
Chevy Chase, MD 20815
(301) 654-9200
Software Engineering Institute 
Model-Based Systems Engineering (MBSE) in Practice 
August 21, 2025


<!-- Page 2 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Introduction to ALPI
●Provides DoD T&E consulting services (DOT&E, DTE&A, DOD CIO, USAF)
■Focus on test process improvement (MBSE, MBT) 
■Leverage automation strategies for testing
■Develop test automation frameworks
■Deliver accredited ISTQB certification training (AI Testing, Model-Based Testing)
■Development, Implementation, and Training of DevSecOps tools
■Support T&E policy and guidance through best practices and whitepapers
●Formed in 1993
●Locations: DC-Metro and Greater Boston Area
2


<!-- Page 3 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Software Testing Challenges
Understanding the Domain
Ensuring Rigor in Test Design
Ensuring Repeatability in Test Execution
3


<!-- Page 4 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Understanding Model-Based Testing (MBT)
●What is MBT?
■An approach to testing that leverages MBSE to generate test artifacts and improve 
program integrity through enhanced test design and test execution 
●Why Use MBT?
■Provides comprehensive and efficient verification and validation of a system 
■Enables traceability of requirements through the digital thread from system to test
►Identifies gaps in requirements and coverage
■Establishes repeatability in testing and reduces maintenance costs
4


<!-- Page 5 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Elements of Model-Based Testing (MBT)
●Three elements of MBT:
■Model
■Automated Test Design/Generation
■Automated Test Execution
●Programs can use any or all elements
■Implementation can be in stages depending on program maturity
►New programs may implement the process starting from the System model
►Existing programs in production can start with Test Model and Test Design 
5


<!-- Page 6 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Models
●System Models represent the system, informed by Stakeholder Inputs, 
Customer Objectives, Mission Capabilities, Mission Requirements, Trade 
Studies, etc.
■Describes the internal workings of the system 
●Test Models represent the system from the test perspective
■Contains inputs for testing, reuses system model elements
■Contains Verification Architecture and V&V information (e.g., test approaches, 
equipment, etc.) 
●Contains Requirements linked to activities, interfaces, use cases, etc.
6


<!-- Page 7 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Automated Test Design
●Generate Test Cases from the Test Model
■Using Automated Test Design Tools, a model is evaluated and test cases are 
generated
■Generated based on criteria, such as “full requirements coverage” or “least amount 
of test cases required to hit all model paths”
■Provides Continuous Testing and Decision Point Evaluation
TC1
TC2
TC3
Test Design Example 
Tools:
o Yest
o Conformiq Designer
o MBTSuite
o Etc.
7


<!-- Page 8 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Automated Test Execution
●Execute Test Cases
■Test Execution Tools take manual or automatically generated test cases and 
execute them, providing data and pass/fail results
■Execute on Models for a baseline expectation of results
■Execute on System and compare to baseline
Test Execution Example Tools
o Conformiq Transformer
o Cameo Systems Modeler + Simulation Toolkit + 
Jenkins
o Tosca
o Selenium
o Etc.
8


<!-- Page 9 -->
WWW.ALPI.COM
© ALP International Corporation 2025
MBT Prototype
Prototype: Generic Radar
■Use Cases: (1) Search and (2) Interrogation
■System Model
►One detailed activity diagram for each Use Case
►Linked to requirements
■Test Model
►One higher level activity diagram for each Use Case
►Reuses elements from System Model
►Linked to requirements
►Function calls to the tactically representative code
►Basis for the Test Cases 
■Tactically Representative Code
►Python code of the Use Cases that is executed by Model-Based Testing
9


<!-- Page 10 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Search Use Case
   System Model
10


<!-- Page 11 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Search Use Case
    Test Model
11


<!-- Page 12 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Interrogation Use Case – System Model
12


<!-- Page 13 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Interrogation Use Case
          Test Model
13


<!-- Page 14 -->
WWW.ALPI.COM
© ALP International Corporation 2025
14


<!-- Page 15 -->
WWW.ALPI.COM
© ALP International Corporation 2025
15


<!-- Page 16 -->
WWW.ALPI.COM
© ALP International Corporation 2025
MBT Steps
1.
Import Test Model into MBT Tool (e.g., MBTSuite)
2.
MBT Tool creates Test Cases based on the paths in the Test Model
3.
Export the Test Cases into code (e.g., python)
4.
Execute Test Case code to run the tactically representative code
16


<!-- Page 17 -->
WWW.ALPI.COM
© ALP International Corporation 2025
1. Import Model into MBTSuite
IFF Use Case
Search Use 
Case
17


<!-- Page 18 -->
WWW.ALPI.COM
© ALP International Corporation 2025
2. MBTSuite creates Test Cases based on paths in Test Model
Different Strategies create different number of Test Cases
 - Strategies: Guided Path, Shortest Path, Random
Statistics shown on 
the created Test Cases
18


<!-- Page 19 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Exportable Test Case in MBTSuite
Test Case #1 – Ignore Detection
19


<!-- Page 20 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Test Case #2 
- Valid Detection
- Manual Mode
- Foe
20


<!-- Page 21 -->
WWW.ALPI.COM
© ALP International Corporation 2025
3. Export the Test Cases into code (e.g., python)
21


<!-- Page 22 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Test Cases Translated into Python
Test Case 1
Test Case 2
22


<!-- Page 23 -->
WWW.ALPI.COM
© ALP International Corporation 2025
4. Tactically Representative Code - Run by the Test Cases
23


<!-- Page 24 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Test Cases Results
• Currently manually recorded
• Next step would be automated P/F
Test 
Case
Test Condition
Result
1
The detection is not above the noise floor, ignore.
Pass
2
There is a real detection, radar is in manual mode, and 
the detection is a foe
Pass
3
There is a real detection, radar is in manual mode, and 
the detection is a friend
Pass
4
There is a real detection, radar is in auto mode, and the 
detection is a foe.
Pass
5
There is a real detection, radar is in auto mode, and the 
detection is a friend.
Pass
6
The validation check returns a detection that is not 
above the noise floor.
Pass
24


<!-- Page 25 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Challenges in MBT Implementation
●Tools that can import models vs only create models
●Tools that generate scripts vs automated testing solutions
●Limited availability of STAT (e.g., combinatorial methods)
●ATO in Government cloud environments
●Challenges with non-deterministic models (e.g. generative AI)
25


<!-- Page 26 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Summary and Conclusions
Model-Based Testing:
●Illustrates a value-added approach to improving T&E with MBSE
●Allows for end-to-end testing providing traceability and rigor
●Is achieved with the right set of tools and techniques
●Improves the testing practice through shift left
●Practical solution to bridge theory and program success
26


<!-- Page 27 -->
WWW.ALPI.COM
© ALP International Corporation 2025
Q&A
27
