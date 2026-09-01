---
name: qa-heuristics
description: Perform targeted heuristic risk discovery for a Story and map material findings to QA risks and Verification Targets.
argument-hint: "[Story]"
---

# QA Heuristics

Use only when additional heuristic discovery can reveal material risk not already covered by QA Analysis.

## Inputs

- approved Acceptance Criteria;
- approved BA/SA analysis;
- relevant UI artifact;
- relevant implementation evidence.

## Selection

Select only relevant families:
- Input & Boundary
- State & Lifecycle
- Workflow
- Integration
- Data
- Authorization
- Concurrency & Timing
- Error Handling
- Regression

Do not run the checklist mechanically.

## Method

`Heuristic → focused question → evidence → Finding → Risk → Verification Target`

Record a finding only when it materially affects quality.

## Evidence

Use:
- `FACT` — directly supported by evidence;
- `INFERENCE` — reasonable deduction;
- `PROPOSAL` — suggested verification, not a requirement.

Never convert a proposal into a business requirement.

## Risk

Use `HIGH`, `MEDIUM`, or `LOW` based on impact and likelihood. Keep rationale short.

## Verification Target

Use:

`VT-XX: [observable behavior]`

Do not generate test cases or implementation instructions.

## Output

Produce exactly:

```text
# Heuristic Findings

## Findings
- H-01: [FACT/INFERENCE/PROPOSAL] [finding] | Risk: [LOW/MEDIUM/HIGH] | VT: [VT-XX]

## Questions / OPEN
- [material unresolved question, or None]
```

Do not duplicate existing QA Analysis findings unless new evidence materially changes the assessment.
