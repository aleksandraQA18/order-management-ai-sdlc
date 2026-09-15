---
name: qa-heuristics
description: Apply focused QA heuristics to identify meaningful negative, boundary, state, integration, and data risks for the current Story.
argument-hint: "[Story]"
---

# QA Heuristics

Use these heuristics selectively to improve verification quality.

## Check

Consider only heuristics relevant to the Story:

- invalid input;
- missing required data;
- boundary values;
- zero/empty values;
- state transitions;
- duplicate operations;
- persistence and data integrity;
- API contract behavior;
- integration failures;
- consistency between created and retrieved data;
- existing regression impact.

## Existing Tests

Compare these risks against existing tests.

Prefer:
- extending an existing test when it already exercises the relevant path;
- adding a focused test when the behavior is missing;
- updating an existing test when the approved Story changes expected behavior.

## Avoid

Do not:
- generate exhaustive edge cases without evidence they matter;
- repeat the same risk in multiple QA sections;
- turn generic testing advice into Story-specific requirements;
- prescribe implementation details;
- require manual testing when automation provides sufficient evidence.

## Output

Use the heuristics to improve the QA Analysis. Do not add a separate heuristics section to the Story.
