# AI SDLC Operating Rules

## Principle

AI is an implementation accelerator, not the authority on product
correctness.

## Agents

### BA Agent

Owns business intent.

### Architect Agent

Owns architecture constraints.

### SA Agent

Owns system behavior.

### QA Agent

Owns quality strategy, risks, verification targets and quality gates.

### Developer Agent

Owns implementation and implementation-level automated tests.

### QA Review

Validates the evidence and challenges assumptions.

## Context Discipline

An agent should receive: - project context required for the current
story, - the current story, - relevant architecture/system
constraints, - relevant QA quality contract.

Do not send the entire project history when it is not needed.

## Human-in-the-Loop

Human review is required when: - requirements conflict, - architecture
trade-offs are material, - security risk is high, - quality gate
exceptions are proposed, - AI output changes business behavior.

## AI Experiment Log

For important stories record: - what AI generated, - what was
accepted, - what was changed, - what AI got wrong, - which review or
test caught it.

The experiment should measure where AI helps and where human judgment
remains necessary.
