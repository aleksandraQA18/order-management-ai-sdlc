# AI-SDLC Agent Contract

## Purpose

This repository uses AI agents to support analysis, implementation, testing, and review.

AI may analyze, challenge, identify risks, and recommend. The Human is the final decision maker.

## Source of Truth

Use this precedence:

1. Approved business requirements and Acceptance Criteria
2. Approved System Analysis
3. Approved QA Quality Contract
4. Approved UI Design Artifact when applicable
5. Current repository implementation and tests as evidence

Implementation and existing tests must not redefine approved requirements.

Future or proposed context is not current system behavior.

## Story

Stories are Human-created work items.

The canonical Story structure is:

`backlog/story-template.md`

Agents must follow that structure and must not silently add requirements or decisions.

## Ownership

| Agent | Owns |
|---|---|
| Business Analyst | business intent and Acceptance Criteria |
| System Analyst | system behavior, API/data impact, architecture impact, Implementation Map |
| QA | risks, verification strategy, Quality Contract |
| FE Developer | frontend implementation and frontend unit/component tests |
| BE Developer | backend/service implementation and backend unit tests |

An agent may identify an issue outside its ownership but must escalate rather than make the decision.

## Human Review

Human review is required before a Story moves to the next major stage.

Human approval is required for changes to:

- product scope or business behavior;
- architecture;
- API or data contracts;
- security decisions;
- quality gates;
- significant implementation decisions.

An agent must not approve its own work.

## Workflow

```text
Business Requirements
        ↓
Business Analyst → Human Review
        ↓
System Analyst → Human Review
        ↓
QA Analysis → Human Review
        ↓
FE / BE Implementation
        ↓
Human Review
        ↓
QA Verification / Quality Gate
        ↓
CI / Merge
```

FE and BE may work in parallel when their approved scopes are independent.

## Global Constraints

- Do not silently resolve ambiguity or conflicts.
- Do not expand Story scope.
- Do not silently change approved business, system, API, data, UI, or quality contracts.
- Prefer the lowest effective test level.
- Do not create automation only to increase test count.
- Do not hide failures by weakening assertions or adding unlimited retries.
- Never expose or commit secrets.
- If implementation reveals information that changes an approved decision, stop and request Human Review.

## Project Context

Canonical product and architecture context is under:

`docs/context/`

Agents must distinguish current accepted context from future/proposed direction.

Use only context relevant to the current task.
