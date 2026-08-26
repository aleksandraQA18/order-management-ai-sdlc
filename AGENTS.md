# AI SDLC Agent System — Order Management

## Purpose
Operating model for the Order Management AI SDLC experiment.

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

## Agent Ownership
| Agent | Ownership |
|---|---|
| BA | business intent and acceptance criteria |
| Architect | architecture and constraints |
| System Analyst | system behavior and technical specification |
| QA | risks, verification strategy, quality contract |
| Developer | implementation and implementation-level tests |
| DevOps | delivery infrastructure and CI/CD |

## Human Approval
Required for conflicting requirements, blocking questions, material architecture changes, significant security risk, quality-gate exceptions, business-behavior changes, or uncertain release readiness.

## Context Discipline
Normally provide an agent only:
- this `AGENTS.md`,
- current Story,
- relevant business context,
- relevant architecture/system context,
- QA Quality Contract when applicable.

## Status Model
`BACKLOG → READY → IN_ANALYSIS → READY_FOR_DEVELOPMENT → IN_DEVELOPMENT → READY_FOR_REVIEW → QA_REVIEW → READY_FOR_MERGE → DONE`

Any stage may become `BLOCKED`.

## Handoff
Every handoff contains:
- Story ID
- status
- completed work
- decisions
- open questions
- artifacts
- next action

## AI Experiment Log
For important Stories record what AI generated, what was accepted/changed, what AI got wrong, what caught the problem, and which guardrail was added if needed.
