# AI SDLC Agent System v2 — Setup

## 1. Copy to repository root

Copy the contents of this package so that `.github/agents` and `.github/skills` are directly under the repository root.

Target:

```text
repo/
├── AGENTS.md
├── .github/
│   ├── copilot-instructions.md
│   ├── agents/
│   └── skills/
└── ...
```

## 2. Reload VS Code

After copying the files:
- reopen the workspace if needed,
- open Copilot Chat in Agent mode,
- check the agent dropdown.

Custom agents are defined in `.github/agents` and use `.agent.md` files.

## 3. Verify skills

In Copilot Chat, use `/skills` or open Configure Chat → Skills.

Project skills live in `.github/skills/<skill-name>/SKILL.md`.

## 4. First smoke test

Select the `QA` custom agent and ask:

> Analyze the current repository configuration and explain which files define your role, which skills are available to you, and what you would need before analyzing ORD-001. Do not modify files.

Expected behavior:
- it reads `AGENTS.md`,
- it identifies its role,
- it identifies relevant skills,
- it does not invent ORD-001 details,
- it asks for the Story if it is not present.

## 5. Second smoke test

Once ORD-001 exists:

> Analyze ORD-001 as QA. Produce the QA Quality Contract only. Do not modify application code.

Review whether the output contains:
- risks,
- verification targets,
- test levels,
- automation strategy,
- regression impact,
- security considerations,
- quality gate.

## 6. Important

Do not give every agent unrestricted autonomy immediately.

Start with read-only analysis where possible. Give edit/execute permissions only where the role actually needs them.

The purpose of this setup is to evaluate AI behavior, not to maximize autonomy.
