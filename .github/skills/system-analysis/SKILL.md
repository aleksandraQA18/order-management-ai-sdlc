---
name: system-analysis
description: Perform minimal system-level analysis for a Story. Map approved business requirements to current and required system behavior, affected components, relevant API/data impact, architecture impact, material risks, and unresolved decisions.
argument-hint: "[Story]"
---

# System Analysis Skill

Use this skill to perform minimal system-level analysis for the Story.

The approved BA Analysis defines WHAT the business requires. This skill defines HOW to assess what the existing system must change to support it.

## Analysis Flow

1. **Current System Behavior**
   - Inspect only evidence relevant to the Story:
     - source code
     - existing APIs
     - existing tests
     - architecture/system context
     - relevant documentation, if available
   - Describe observable current behavior.
   - Classify evidence as:
     - `FACT` — directly confirmed by repository evidence;
     - `INFERENCE` — derived from available evidence;
     - `CONTRADICTION` — current behavior conflicts with approved BA requirements.
   - Do not present unsupported behavior as fact.

2. **Required System Behavior**
   - Translate approved Acceptance Criteria into system behavior.
   - Identify only behavior required to satisfy the approved BA Analysis.
   - Describe relevant:
     - inputs and outputs;
     - state changes;
     - validation;
     - error behavior.
   - Do not invent behavior or redefine Acceptance Criteria.

3. **Components Affected**
   - Identify only components relevant to the required behavior.
   - Consider, when applicable:
     - frontend;
     - backend/service;
     - API;
     - persistence;
     - integrations;
     - shared components.
   - For each affected component, state why it is affected and what system-level behavior must change.
   - Mark uncertain impact as `OPEN`.
   - Do not identify file-, class-, or function-level implementation details.

4. **Data & API Impact**
   - Identify only relevant changes to:
     - API behavior;
     - request/response data;
     - validation;
     - persistence;
     - data relationships;
     - state transitions.
   - Distinguish:
     - `REQUIRED_CHANGE` — supported by approved requirements and system evidence;
     - `ASSUMPTION` — necessary inference, not confirmed;
     - `OPEN_DECISION` — unresolved and requiring human decision.
   - Do not prescribe implementation details.

5. **Architecture Impact**
   - Assess whether the current architecture supports the required behavior.
   - Classify:
     - `NO_CHANGE` — current architecture supports the Story;
     - `CHANGE_REQUIRED` — an architectural/component-level change is necessary;
     - `OPEN` — evidence is insufficient to decide.
   - If `CHANGE_REQUIRED`, describe the affected architectural areas and material trade-offs.
   - Propose alternatives only when multiple viable approaches materially affect architecture, risk, or scope.

6. **Implementation Map**
   - Define the minimum implementation boundary for Developers at component level.
   - Use:
     | Component | Required change | Developer | Dependencies |
     | --------- | --------------- | --------- | ------------ |
   - State WHAT component behavior must change and WHERE at system/component level.
   - Use `FE` or `BE` for Developer where applicable.
   - Mark unknowns as `OPEN`.
   - Do not prescribe classes, functions, files, algorithms, or code structure.

7. **Risks & Trade-offs**
   - Report only material risks or trade-offs introduced or affected by the Story.
   - Consider when relevant:
     - coupling;
     - dependencies;
     - data consistency;
     - backward compatibility;
     - scalability;
     - maintainability;
     - operational impact.
   - Do not turn hypothetical concerns into requirements.
   - If no material risks are identified, state that none were identified.

8. **OPEN ISSUES**
   - Report only unresolved information, ambiguity, contradiction, or decision that materially affects implementation, acceptance, architecture, or testability.
   - For each issue:
     - state the question/problem;
     - state why it matters.
   - Do not silently resolve it.
   - Do not automatically provide alternatives or recommendations unless they are necessary for a meaningful human decision.

## Scope Rules

IN SCOPE:

- current observable system behavior;
- required system behavior derived from approved BA Analysis;
- affected system components;
- relevant API and data impact;
- system-level architecture impact;
- minimum implementation boundary;
- material risks and trade-offs;
- material OPEN issues.

OUT OF SCOPE:

- business requirement definition;
- redefining Acceptance Criteria;
- detailed solution design;
- classes, functions, files, algorithms, or code structure;
- implementation instructions;
- documentation analysis;
- unrelated refactoring;
- hypothetical requirements.

## Output

Produce only the content required by the System Analyst Template Contract:

- Current System Behavior
- Required System Behavior
- Components Affected
- Data & API Impact
- Architecture Impact
- Implementation Map
- Risks & Trade-offs
- OPEN ISSUES

Keep the analysis minimal and proportional to the Story. Do not add sections or analysis that does not materially help Developers or QA proceed safely.
