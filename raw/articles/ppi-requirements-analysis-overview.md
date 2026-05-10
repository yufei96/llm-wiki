 

 
Page 1 of 6 

PPI-006100-13 
© Copyright and all Other Rights Reserved Project Performance (Australia) Pty Ltd 2024 

REQUIREMENTS ANALYSIS OVERVIEW 

By Robert J. Halligan FIE Aust CPEng IntPE(Aus) 
 
Project Performance International Pty Ltd 
P.O Box 2385 
Ringwood VIC 3134 Australia 
Ph: 61-3-9876-7345 
Email: rhalligan@ppi-int.com 

 
 
1. Objectives of Requirements Analysis  

The usual criterion for adequacy of a set of requirements is that, if the requirements set is satisfied, the level of risk 
associated with failing to satisfy the needs of relevant stakeholders is low – typically an expected loss of value of two 
or three percent, or less.  

To this basic criterion can be added the dimension of time. Requirements change with time due to the problem space 
genuinely changing, and due to “what is possible in technology” triggering perfectly valid new requirements. So, 
requirements analysis must be an ongoing activity, to a lesser or greater degree. 

 
2. Techniques of Requirements Analysis  

The requirements analysis process used and recommended by the author is illustrated in Figure 1.  

 

Figure 1:  An Effective Requirements Analysis Process 
 

PPI-006248-5
© Copyright Project Performance (Australia) Pty Ltd 1994-2024

www.ppi-int.com

Legend:

REQUIREMENTS ANALYSIS
(CAPTURE AND VALIDATION)
METHODOLOGY

SRA System Requirements Analysis
S/H Stakeholder
DEV Development
OCD Operational Concept Description (CONUSE)
ERA Entity Relationship Attribute
 
Perform only if there are initial specifed 
requirements as an input to the analysis.
*

• specifed requirements
• verifcation requirements
• value model
• description of intended use

Output:

• problem domain information
Input:

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

SOLICIT
REQUIREMENTS
VIA AI

DESIGN
REQUIREMENTS
ANALYSIS

OTHER
CONSTRAINTS
SEARCH

VERIFICATION
REQUIREMENTS
DEV.

OCD/CONUSE
DEVELOPMENT
S/H
VALUE
ANALYSIS

*

*

*

SUPPORT
AUTHORING
WITH AI


 

 
Page 2 of 6 

PPI-006100-13 
© Copyright and all Other Rights Reserved Project Performance (Australia) Pty Ltd 2024 

The set of techniques which combine to comprise a very effective and efficient requirements analysis methodology 
is described below:  

a. Stakeholder Identification. The objective of stakeholder identification is to identify stakeholders who are 
potential “owners” of requirements, or who can facilitate effective communication relating to requirements. These 
stakeholders are subsequently encouraged to make input into the definition of the requirements, are consulted 
regarding requirements issues, and are invited to “sign-off” on their subsets of requirements. 

b. Document Review. Documents, if any, which contain or relate to intended use, requirements, and goals are 
examined, with a view to identifying key issues that should be resolved with stakeholders before requirements 
analysis proceeds too far. This review provides input into the planning for conduct of the requirements analysis. 

c. Context Flow Analysis. This analysis tracks the state of the world outside of the system on a whole of life basis, 
from system cradle to system grave. All requirements of the system originate in these contexts, with one class of 
exception. Stakeholders are mapped to the contexts, often resulting in the identification of additional 
stakeholders. The main work product of this analysis is subsequently used to structure analysis work, checks and 
dialog with stakeholders. See Figure 2. 

 

 

 

Figure 2:  Context Flow Diagram 

 

 
 

BEING 
PRODUCED

BEING 
TESTED

BEING 
DELIVERED

BEING INSTALLED

BEING USED
BEING 
SUPPORTED
HAVING 
WASTE 
REMOVED

BEING 
DISPOSED OF

BEING TESTED

Conditions of existence: 

“states of the world external to the 
system” 

Associate stakeholders with the 
context(s) in which they have an 
interest. 

Look for additional stakeholders in 
each context. 

 

All requirements (with one 
class of exception) come 
from those contexts. 
 

PPI-008479-1 


 

 
Page 3 of 6 

PPI-006100-13 
© Copyright and all Other Rights Reserved Project Performance (Australia) Pty Ltd 2024 

d. Context Analysis. This analysis identifies/validates mainly external interface requirements. The analysis also 
contributes to environmental requirements. Context analysis helps identify additional stakeholders in the system: 
owners of interoperating systems; individuals who will interact with the system; and organizational entities with 
which the system will interface. Context analysis sets the foundation for subsequent capture and validation of 
required functionality. See Figure 3. 

 

 

 

 

 

 
 
 
 
 
 
 
 
 
 
Figure 3:  Context Diagram 
 

e. States and Modes Analysis. This is a high ROI analysis, which establishes the big-picture dynamics required of 
the system, expressed in terms of states & modes. States and modes analysis often identifies major requirements 
issues. The analysis also establishes preconditions for subsequent precise and concise specification of the 
requirements captured in other analyses. See Figure 4. 

Figure 4:  States Transition Diagram 

Legend:

P 
  Permissive guidance (”may”) statement
TX 
  Time Expired
 
  Required transition
 
  Permitted but not required transition
 
  Prohibited transition
Unconnected arrow : Default state or mode
                  Event(s) that are to cause transition
 
  External response (if any) as a direct
 
  consequence of the transition having  
 
  occurred
                 

Armed
State

Safe
State

Misfire
State
TX
State

Detonating
State

Detonated
State

© Copyright Project Performance (Australia) Pty Ltd 2012-2018

Example State Transition Diagrams

P

(P)

(P)

PPI-008223-1 

PPI-008481-1 


 

 
Page 4 of 6 

PPI-006100-13 
© Copyright and all Other Rights Reserved Project Performance (Australia) Pty Ltd 2024 

f. Functional Analysis. This analysis is conducted within a modeling boundary which encapsulates enough of the 
problem, including functional aspects of operational scenarios, to capture and validate the required system 
functional and performance requirements. The result is a set of functional and performance requirements which 
is sufficiently complete and is at precisely the correct level of abstraction, neither too broad nor at a level of 
abstraction which directs the implementation of the system, as opposed to capturing the need. Use cases are a 
basic form of functional analysis; more robust functional modeling techniques can be used for more demanding 
applications. 

 

Figure 5:  Functional Flow Block Diagram 
 

g. Rest of Scenario Analysis. This analysis, conducted iteratively with functional analysis, identifies/validates 
environmental requirements, physical requirements, resource requirements and contributes additional content 
to external interface requirements. 

h. Entity Relationship Attribute Analysis. ERA analysis provides input to capture/validation of additional 
information content of external interface requirements, and some aspects of functional requirements. The 
analysis is most relevant to data-oriented systems. 

 
Figure 6:  Entity Relationship Attribute Diagram 

A

OR

L
L

A

3
Introduce
Capability into
Service

5Perform Airlift
Capability
Upgrade

4.2.1.1
Perform
Mission
Briefng

4.2.1.4
Perform
Paratrooping
Activity

4.2.1.5

4.2.1.2

Fly to Target
Area

4.2.1.3
Perform
Paratroop
Preparation
Activities

OR

A
A
Perform Target
Area Egress

4.2.1.7

Defeat Threat
Laydown 1

L
L

4.2.1.7

Defeat Threat
Laydown n

PPI-005642-3

4.2.1.6
Perform Aircraft
Home Base
Recovery
Activities


 

 
Page 5 of 6 

PPI-006100-13 
© Copyright and all Other Rights Reserved Project Performance (Australia) Pty Ltd 2024 

i. 
Parsing Analysis. Parsing analysis is a text analysis technique for identification of errors, incompleteness, 
inconsistency, lack of clarity, ambiguity, lack of verifiability, and infeasibility, in textually stated requirements. The 
basis of the technique is illustrated in Figure 7:  

 

Figure 7:  Parsing Template 

 

The parsing template also provides an excellent aid to writing good requirements the first time, and for rewriting 
defective requirements. 

 

j. 
Out-of-Range analysis. This analysis captures and validates any requirements that relate to defective inputs or 
outputs or abnormal conditions of use/support/disposal. The requirements from this analysis can make the 
difference between a system that will be effective in the real world, and a system that could be effective only in 
the ideal world. 

k. Other Constraints Search. This activity looks for requirements which are ordained from on high (such as from 
statute law, applicable regulations, policy, governing standards, directives). 

l. 
Clean-Up. This activity verifies the refined requirements set, looking for residual defects in the work products of 
the analysis. Keyword searching is used in combination with specific verification criteria. 

 
 
 


 

 
Page 6 of 6 

PPI-006100-13 
© Copyright and all Other Rights Reserved Project Performance (Australia) Pty Ltd 2024 

3. Conclusion 
 

Figure 8:  Approach to Requirements Analysis 

 

Methods exist to perform requirements capture and validation both efficiently and very effectively. The methods rely, 
not on requirements elicitation per se (which is neither efficient nor effective), but on elicitation of responses from 
stakeholders to specific requirements issues identified mainly through effective analysis of the problem domain.  

 

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
system requirements specifcation

VM: 
 
value (or system/software efectiveness) model

VRS:  
verifcation requirements specifcation

PPI-005499-4

is a restatement of
traces to/from


