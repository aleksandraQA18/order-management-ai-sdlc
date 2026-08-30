---
name: qa-heuristics
description: Apply context-driven QA heuristics to discover risks, edge cases, failure modes and verification targets; produce concise findings for the QA Analysis skill.
argument-hint: "[Story]"
---

# QA Heuristics Skill

Use this skill to _discover_ meaningful risks and verification targets that the QA Analysis will evaluate.  
This skill explains _how to think_ with heuristics: which questions to ask, how to convert findings into risks, and how to produce a concise, machine-friendly findings output.

## Inputs

- Approved Acceptance Criteria
- System Analyst analysis
- BA analysis
- Relevant UI design artifact when applicable
- Any available implementation evidence (optional)

## Heuristic Selection

- Choose heuristics relevant to the Story type and affected components (e.g., input/boundary for CRUD, workflow/state for payments).
- Do not run the full checklist mechanically; prefer a targeted subset that is likely to produce meaningful findings.
- Prioritize heuristics that map to high-impact or uncertain areas identified in BA/SA.

## How to apply heuristics (method)

- For each selected heuristic:
  1. Formulate a focused question the heuristic raises.
  2. Inspect evidence (BA/SA, code, tests, design) for signals that answer the question.
  3. If evidence reveals a concern, record a concise Finding and map it to a Verification Target.
  4. Classify the resulting Risk (LOW / MEDIUM / HIGH) with a short rationale.
- Use the reasoning chain: **Heuristic → Question → Finding → Risk → Verification Target**.
- Tag statements as **FACT** (evidence-backed), **INFERENCE** (reasonable deduction), or **PROPOSAL** (suggested verification).
- Ignore heuristics that produce no meaningful finding.

## Typical heuristic families (pick relevant ones)

- **Input & Boundary**: empty/null, min/max, invalid format, large input, duplicates, encoding.
- **State & Lifecycle**: repeated operation, invalid transition, partial completion, expiry.
- **Workflow**: retries, timeouts, interruptions, alternate paths.
- **Integration**: dependency unavailable, slow/invalid response, contract mismatch.
- **Data**: duplicate/stale/missing data, concurrent modification, partial update.
- **Authorization**: unauthenticated, unauthorized, wrong owner.
- **Concurrency & Timing**: race conditions, duplicate submissions, ordering issues.
- **Error Handling**: safe failure, actionable messages, recoverability.
- **Regression**: shared components, changed APIs, previous defects.

## Output Contract

Produce the following structured artefact exactly.
