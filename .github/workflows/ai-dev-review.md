---
name: AI Dev Reviewer
description: Run the repository Dev Reviewer on pull requests and publish a non-blocking GitHub review.
on:
  pull_request:
    types: [opened, synchronize, reopened]

engine:
  id: codex

model: gpt-5.4

permissions:
  contents: read
  pull-requests: read

imports:
  - .github/agents/dev-reviewer.agent.md

safe-outputs:
  submit-pull-request-review:
    max: 1
    allowed-events: [COMMENT]
  create-pull-request-review-comment:
    max: 10
---

# Dev Reviewer CI

Review the current pull request using the imported Dev Reviewer agent.

## Review Context

Treat the following as the primary review evidence:

1. The current pull request diff.
2. The Story being implemented.
3. Approved Acceptance Criteria.
4. Approved System Analysis and Implementation Map.
5. Relevant source code and existing tests.
6. Available CI/test evidence.

The repository is the source of truth for locating the relevant Story and approved analysis artifacts.

Do not infer missing requirements. If required context cannot be found, report an evidence gap rather than inventing it.

## Output Rules

- This is a non-blocking review.
- Never approve the pull request.
- Never request changes.
- Submit at most one GitHub review with event `COMMENT`.
- Create inline comments only for meaningful findings tied to changed lines.
- Do not create comments for stylistic preferences or speculative issues.
- Keep the review concise and actionable.
- Use the severity and finding structure defined by the imported Dev Reviewer agent.
- If there are no meaningful findings, say so explicitly in the review summary.
