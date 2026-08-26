---
name: test-design
description: Design risk-based verification and choose the lowest effective test level for a Story.
argument-hint: "[Story or QA Contract]"
---

# Test Design

1. Start from risks and acceptance criteria.
2. Select the lowest effective test level.
3. Define representative data.
4. Cover positive, negative and boundary behavior where relevant.
5. Remove duplicate coverage.
6. Define expected evidence.

Guidance:
- unit: isolated logic
- integration: component interaction
- API: service behavior and contracts
- E2E: critical user journeys
- exploratory/manual: unknowns and changing behavior

Do not prescribe unnecessary E2E coverage.
