---
name: system-analysis
description: Perform system-level analysis for the Story. Identify current and required system behavior, affected components, API/data impact, architecture impact, risks, documentation impact, and unresolved decisions.
argument-hint: "[Story]"
---

# System Analysis Skill

Use this skill to produce the content required by the System Analyst Template Contract.

The skill defines HOW the analysis is performed.  
The System Analyst Agent fills the Template Contract using the results of this skill.

## Analysis Flow

Follow this sequence:

1. **Current System Behavior**
   - Inspect current system state using available evidence:
     - architecture context
     - system documentation
     - source code
     - existing APIs
     - existing tests
   - Describe observable behavior relevant to the Story.
   - Distinguish:
     FACT: confirmed behavior  
     INFERENCE: derived from evidence  
     CONTRADICTION: behavior conflicting with BA requirements

2. **Required System Behavior**
   - Translate approved Acceptance Criteria into required system behavior.
   - Describe:
     - required inputs/outputs
     - required state changes
     - required validation
     - required error behavior
   - Do not invent behavior not present in BA.

3. **Components Affected**
   - Identify components affected by the required behavior:
     - frontend
     - backend service
     - API
     - persistence
     - integration
     - shared components
   - For each component:
     - why it is affected
     - what behavior must change
     - whether change is required or optional
   - Mark uncertain components as:
     OPEN

4. **Data & API Impact**
   - Identify required changes to:
     - API behavior
     - request/response data
     - validation rules
     - persistence
     - data relationships
     - state transitions
   - Distinguish:
     REQUIRED_CHANGE  
     ASSUMPTION  
     OPEN_DECISION

5. **Architecture Impact**
   - Assess whether the current architecture supports the required behavior.
   - Classify:
     NO_CHANGE  
     CHANGE_REQUIRED  
     OPEN
   - When change is required:
     - describe affected components
     - propose reasonable alternatives
     - identify risks and trade-offs

6. **Implementation Map**
   - Define the implementation boundary for FE and BE Developers.
   - Use the structure:
     | Component | Required change | Developer | Dependencies |
   - Identify:
     - WHAT changes
     - WHERE it changes
     - WHO implements it (FE / BE)
     - WHICH dependencies matter
   - Mark unknowns as:
     OPEN

7. **Risks & Trade-offs**
   - Identify system-level risks:
     - coupling
     - dependencies
     - data consistency
     - backward compatibility
     - scalability
     - maintainability
     - operational impact
   - Do not turn hypothetical concerns into requirements.

8. **Documentation Impact**
   - Identify affected system or process documentation.
   - Describe required updates.
   - Do not document unapproved decisions.

9. **OPEN ISSUES**
   - Mark missing or ambiguous information as:
     OPEN
   - For each OPEN:
     - describe the question
     - why it matters
     - alternatives
     - recommendation
