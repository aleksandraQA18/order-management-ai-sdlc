---
name: micro-requirements-analysis
description: Minimal analysis of business intent for micro-story. Clarifies Story Core, refines Acceptance Criteria, and identifies missing information or ambiguity without expanding scope or introducing technical details.
argument-hint: "[BA Story Slice]"
---

# Micro Requirements Analysis

Use this skill to perform minimal business analysis for micro-stories.

## Analysis Flow (lightweight)

1. Clarify the actor (As a).
2. Clarify the capability (I want).
3. Clarify the business value (So that).
4. Refine Acceptance Criteria (max 3) into clear, observable business behavior.
5. Identify missing information (OPEN).
6. Identify ambiguity (OPEN).

## Requirement Quality

Each element must be:

- clear and unambiguous;
- observable from a business perspective;
- testable without knowing implementation;
- minimal and proportional to the micro-story.

## Acceptance Criteria

Acceptance Criteria must:

- describe business behavior, not technical implementation;
- be independently understandable;
- avoid API, database or architectural details;
- remain within the scope of the Story Core.

## Scope Rules

IN SCOPE:

- business intent;
- business outcome;
- minimal business rules.

OUT OF SCOPE:

- architecture;
- API design;
- database structure;
- implementation details;
- UI/UX invention.

## Ambiguity & Missing Information

Mark unclear or missing information as:

- [OPEN] Missing Information
- [OPEN] Ambiguity

Do not resolve ambiguity.  
Do not invent missing business behavior.

## Output

The skill produces:

- clarified Story Core;
- refined Acceptance Criteria;
- list of OPEN issues (missing information, ambiguity).
