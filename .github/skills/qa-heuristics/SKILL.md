---
name: qa-heuristics
description: Apply context-driven QA heuristics to discover risks, missing scenarios, edge cases, and failure modes without mechanically generating tests.
argument-hint: "[Story]"
---

# QA Heuristics

Use this skill during QA analysis to challenge assumptions, discover relevant risks, and identify behavior that may require verification.

## Purpose

Heuristics are prompts for investigation, not automatic test cases.

Apply only heuristics relevant to the current Story, system behavior, architecture, and identified risks.

Do not run the full heuristic set mechanically.

The goal is to discover meaningful risks with the smallest effective amount of analysis and verification.

## Workflow

1. Understand the approved business behavior.
2. Review the System Analyst analysis and affected components.
3. Identify the main risk areas.
4. Select relevant heuristics.
5. Ask the questions raised by those heuristics.
6. Record meaningful findings.
7. Convert findings into risks or verification targets when justified.
8. Ignore heuristics that produce no relevant risk.
9. Do not create a test scenario unless the finding requires verification.

Use the following reasoning chain:

Heuristic
→ Question
→ Finding
→ Risk
→ Verification Target

A heuristic that produces no meaningful finding does not require further action.

## Input and Boundary Heuristics

Consider when the Story accepts or transforms input:

- empty value;
- null or missing value;
- minimum value;
- maximum value;
- value just below a boundary;
- value just above a boundary;
- invalid format;
- unexpected type;
- unusually large input;
- duplicate input;
- leading/trailing whitespace;
- case sensitivity;
- special characters;
- unexpected encoding.

Ask:

- What are the valid equivalence classes?
- Where are the meaningful boundaries?
- What happens when required input is missing?
- What happens when input is syntactically valid but semantically invalid?
- What happens when input is repeated?

Do not create separate tests for every invalid value when one representative example covers the risk.

## State and Lifecycle Heuristics

Consider when the Story changes or depends on state:

- initial state;
- valid state transition;
- invalid state transition;
- repeated operation;
- already completed operation;
- cancelled operation;
- expired state;
- partially completed state.

Ask:

- Can the operation be performed more than once?
- What happens when the entity is already in the target state?
- Can the system enter an invalid state?
- What happens after cancellation or expiration?
- Are state transitions atomic and consistent?

## Workflow Heuristics

Consider the complete business flow:

- happy path;
- alternate path;
- rejection;
- cancellation;
- retry;
- timeout;
- interruption;
- partial completion;
- recovery.

Ask:

- What can happen between the start and successful completion?
- What happens when the user retries?
- What happens when an intermediate step fails?
- Can the process be safely resumed?
- Can partial completion leave inconsistent state?

## Integration Heuristics

Consider dependencies between components or external systems:

- dependency unavailable;
- timeout;
- slow response;
- invalid response;
- unexpected response;
- duplicate response;
- dependency failure after local state change;
- contract mismatch.

Ask:

- What happens if the dependency is unavailable?
- What happens if it responds too slowly?
- What happens if the response is syntactically valid but unexpected?
- Can retries create duplicate effects?
- Can local and remote state become inconsistent?

## Data Heuristics

Consider persistence and data integrity:

- duplicate data;
- stale data;
- missing data;
- inconsistent data;
- invalid relationship;
- concurrent modification;
- persistence failure;
- partial update.

Ask:

- Can two operations modify the same data concurrently?
- What happens when persisted data is missing or inconsistent?
- Can a partial update leave invalid state?
- Is the operation idempotent where it needs to be?
- Can duplicate records or effects be created?

## Authorization Heuristics

Consider when access or ownership is relevant:

- unauthenticated user;
- authenticated but unauthorized user;
- wrong resource owner;
- insufficient role;
- expired authorization;
- direct access to another user's resource.

Ask:

- Who is allowed to perform the operation?
- Who owns the affected resource?
- What happens when the user has authentication but insufficient authorization?
- Can a user access or modify another user's data?

This is QA security awareness, not a full security assessment.

Do not perform a dedicated OWASP assessment unless explicitly requested or assigned as a separate security activity.

## Concurrency and Timing Heuristics

Consider when operations can overlap or timing matters:

- simultaneous requests;
- duplicate submission;
- race condition;
- timeout;
- delayed response;
- stale client state;
- ordering of events.

Ask:

- What happens when the same operation is submitted twice?
- What happens when two users modify the same resource?
- Does operation order affect the final state?
- Can delayed responses overwrite newer state?

## Error Handling Heuristics

Consider:

- validation error;
- business rule rejection;
- unexpected failure;
- dependency failure;
- timeout;
- retry;
- recovery.

Ask:

- Does the system fail safely?
- Is the user given an actionable outcome?
- Is the system left in a valid state?
- Can the operation be retried safely?
- Is the failure observable through appropriate evidence?

## Regression Heuristics

Consider:

- shared components;
- reused business rules;
- common APIs;
- changed data models;
- existing critical journeys;
- areas with previous defects.

Ask:

- What existing behavior could this change unintentionally affect?
- Which consumers depend on the changed behavior?
- Which critical paths use the changed component?
- Are there existing defects or regression-prone areas nearby?

Regression scope should be proportional to risk.

## Heuristic Selection by Story Type

Use relevant heuristics based on the change.

Examples:

Registration:
- input and boundary;
- state and lifecycle;
- authorization;
- integration;
- error handling;
- duplicate submission.

Payment:
- workflow;
- state and lifecycle;
- integration;
- concurrency and timing;
- data integrity;
- error handling.

CRUD:
- input and boundary;
- state;
- duplicate data;
- authorization;
- concurrency;
- regression.

Do not assume that the same heuristic set applies to every Story.

## Findings

Record meaningful findings in a concise form:

| Heuristic | Question | Finding | Risk | Verification Target |
|---|---|---|---|---|
| | | | | |

Only populate the table when the heuristic produces a relevant finding.

## Boundary

This skill helps discover:

- risks;
- missing behavior;
- edge cases;
- failure modes;
- regression concerns;
- verification needs.

It does not:

- invent requirements;
- redefine business behavior;
- automatically generate test cases;
- prescribe implementation;
- replace risk-based QA analysis;
- perform a full security assessment.

All findings remain subject to human review where they affect requirements, scope, architecture, or quality gates.
