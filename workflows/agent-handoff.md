# Agent Handoff Protocol

## Required Format

```text
Story:
Status:

Completed:
- ...

Decisions:
- ...

Artifacts:
- ...

Open Questions:
- ...

Risks:
- ...

Next Agent:
...

Expected Action:
...
```

## Valid Handoffs
BA → SA
SA → QA
QA → Developer
Developer → QA Review
QA Review → Merge
DevOps → CI/Release

## Rules
1. Do not hand off incomplete work without declaring it.
2. Do not hide open questions.
3. Do not silently overwrite another role's artifact.
4. Keep scope tied to the Story.
5. If the next agent cannot proceed safely, use `BLOCKED`.
