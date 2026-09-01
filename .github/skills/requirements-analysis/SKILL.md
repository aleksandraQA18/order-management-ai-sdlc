---
name: requirements-analysis
description: Minimal analysis of business intent for micro-stories. Clarifies Story Core, refines Acceptance Criteria, and identifies only material missing information or ambiguity without expanding scope or introducing technical details.
argument-hint: "[Story]"
---

# Micro Requirements Analysis

Use this skill to perform minimal business analysis for micro-stories.

## Analysis Flow

1. Read the Story and provided artifacts.
2. Clarify the actor (As a).
3. Clarify the capability (I want).
4. Clarify the business value (So that).
5. Refine Acceptance Criteria (maximum 3) into clear, observable business behavior.
6. Identify only material missing information or ambiguity.
7. Mark unresolved issues as OPEN.

## Source of Truth

- Treat the Story and provided artifacts as the only source of business requirements.
- Preserve valid requirements from the input; refine wording only when needed for clarity or testability.
- If provided sources conflict, do not resolve the conflict; report it as OPEN.
- Do not use assumptions or general domain knowledge to fill missing business behavior.

## Requirement Quality

Each Story Core element and Acceptance Criterion must be:

- clear and unambiguous;
- observable from a business perspective;
- testable without knowing implementation;
- minimal and proportional to the micro-story.

## Acceptance Criteria

Acceptance Criteria must:

- describe business behavior or business rules, not technical implementation;
- be independently understandable;
- avoid API, database, architecture, or implementation details;
- remain within the scope of the Story Core;
- include only criteria supported by the Story and provided artifacts;
- contain no more than 3 criteria.

Do not invent an additional criterion to reach the maximum of 3.

## Scope Rules

IN SCOPE:

- business intent;
- business outcome;
- minimal business rules required to understand or accept the Story.

OUT OF SCOPE:

- architecture;
- API design;
- database structure;
- implementation details;
- UI/UX invention.

Do not expand the Story scope.

## Ambiguity & Missing Information

Report an issue only when the missing information or ambiguity affects:

- acceptance of the Story;
- expected business behavior;
- implementation of the required behavior;
- testability of the Story.

Use:

- `[OPEN] Missing Information`
- `[OPEN] Ambiguity`

Do not resolve OPEN issues or turn assumptions into requirements.

If no material issue exists, do not invent one.

## Output

Produce:

- clarified Story Core;
- refined Acceptance Criteria;
- material OPEN issues under Missing Information and Ambiguity.

Keep the analysis minimal and proportional to the Story. Do not provide technical recommendations or additional sections.
