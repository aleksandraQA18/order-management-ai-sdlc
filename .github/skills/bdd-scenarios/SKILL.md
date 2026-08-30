---
name: bdd-scenarios
description: Convert selected QA verification targets into concise, business-readable BDD scenarios that remain traceable to Acceptance Criteria and risks.
argument-hint: "[Verification Target or Story]"
---

# BDD Scenarios Skill

Use this skill to produce clear, minimal BDD scenarios for verification targets identified by QA.  
This skill explains _how to choose_ behavior that needs scenario-level specification and _how to express_ it as business-readable examples without prescribing implementation.

> "BDD scenarios describe observable system behavior using examples."  
> "Use the standard structure: Feature; Scenario; Given; When; Then."

## Inputs

- Approved Acceptance Criteria
- QA Analysis output (Verification Targets)
- System Analyst analysis (for affected components and boundaries)
- Relevant UI design artifact when applicable

## Purpose

- Clarify expected behavior for stakeholders.
- Provide concrete, observable examples that are traceable to Acceptance Criteria and identified risks.
- Support handoff to developers and testers without prescribing test implementation.

## Selection Rules

- Create scenarios only for verification targets explicitly identified by QA.
- Prioritize:
  - **critical business behavior**
  - **high-risk rules**
  - **meaningful negative cases**
  - **boundary conditions**
  - **cross-component behavior**
- Do not create scenarios to inflate test counts or for out-of-scope behavior.

## Scenario Structure and Style

- Use this exact structure for each scenario:

Feature: [business capability]

Scenario: [specific behavior]
Given [initial context]
And [additional context when needed]
When [action or event]
Then [observable outcome]
And [additional outcome when needed]

- Use **business language** only; avoid implementation details (classes, DB rows, selectors).
- Keep scenarios focused on a single behavior; avoid multiple unrelated actions.
- Prefer explicit scenarios over Scenario Outline unless multiple examples materially improve clarity.

## Traceability

- Every scenario must include traceability metadata:
