# AI-SDLC Agent Contract

## Purpose

Operating rules for the AI-SDLC workflow used in this repository.

AI agents support analysis, reasoning, documentation and implementation.

AI is not the decision maker.

## Human-Owned UI Design

When a Story introduces or changes user-facing UI, the Human must provide an approved UI Design Artifact before BA analysis starts.

Agents must not invent UI/UX behavior when a required UI Design Artifact is missing.

The UI Design Artifact is part of the Story input and must be treated as a source of UI requirements.

Changes to the approved UI/UX require Human review and approval.

## Backlog

Stories are Human-created work items.

The canonical Story structure is defined in:

`backlog/story-template.md`

Agents must process Stories according to this structure and must not
silently invent missing requirements or decisions.

## Global Rules

1. Do not invent requirements.
2. Missing information is `OPEN`.
3. Do not silently resolve conflicts.
4. Work only within the current Story.
5. Prefer simple, maintainable solutions.
6. Preserve traceability: Business Requirement → Story → Risk → Verification → Implementation → Evidence.
7. Every Story requires a QA Quality Contract.
8. Every merge requires CI and required quality gates.
9. An agent must not approve its own work.
10. Quality gates are risk-based.
11. Do not create automation just to increase test count.
12. Prefer the lowest effective test level.
13. Never expose or commit secrets.
14. Do not change business behavior without updating the relevant specification.
15. Do not hide failures by weakening assertions or using unlimited retries.
16. AI output is reviewed when it affects behavior, architecture, security, or quality gates.
17. Do not silently change an approved API, data, system or business contract.
18. If implementation reveals information that affects an approved decision, stop and request human review.

## Agent Ownership

| Agent            | Ownership                                                                             |
| ---------------- | ------------------------------------------------------------------------------------- |
| Business Analyst | business intent and acceptance criteria                                               |
| System Analyst   | system behavior, technical specification, architectural impact and Implementation Map |
| QA               | risks, verification strategy and QA Quality Contract                                  |
| FE Developer     | frontend implementation and frontend unit/component tests                             |
| BE Developer     | backend/service implementation and backend unit tests                                 |

Agents may identify issues outside their ownership, but must not make decisions
belonging to another role.

## Human-in-the-Loop

The human is the final decision maker.

Agents may:

- analyze;
- challenge assumptions;
- identify risks;
- identify ambiguities and conflicts;
- propose solutions;
- present alternatives;
- recommend an option.

Agents must not independently approve decisions.

Every major agent analysis requires human review before the Story proceeds to
the next stage.

Human approval is required for decisions affecting:

- product scope;
- business behavior;
- architecture;
- system behavior;
- API or data contracts;
- security;
- quality gates;
- significant implementation decisions.

Recommendation does not constitute approval.

## Agent Workflow

The default workflow is:

```text
Business Requirements
        ↓
Business Analyst
        ↓
Human Review
        ↓
System Analyst
        ↓
Human Review
        ↓
QA
        ↓
Human Review
        ↓
Implementation
   ┌────┴────┐
   ↓         ↓
FE Developer  BE Developer
   └────┬────┘
        ↓
Human Review
```
