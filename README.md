# AI-Powered SDLC & QA Engineering

A hands-on project where I’m exploring what software development looks like when AI agents become part of the SDLC — not as one all-purpose assistant, but as a team of specialized roles.

The project combines **software development, QA engineering and AI-assisted workflows**.

## What am I building?

I’m building a small order management application and using it as a playground for an AI-powered SDLC.

The workflow is split between specialized agents:

```text
Human
  ↓
Business Analyst
  ↓
System Analyst
  ↓
QA
  ↓
FE / BE Developer
  ↓
PR
  ↓
Dev / QA Review
```

Each agent has a defined responsibility, dedicated skills and clear boundaries. Human decisions remain part of the process — especially where requirements, design or technical decisions need judgement.

## My focus

My primary focus in this project is **QA Engineering and test automation**, not becoming an expert software developer.

I’m building the application with the help of AI. The code may therefore contain mistakes, imperfect design decisions or implementation issues — and that is part of the experiment rather than something I’m trying to hide.

My goal is to build a working MVP, understand the development process around it, and then use testing, reviews, CI, logs and metrics to see how effectively those problems can be detected.

I will personally implement the **API, integration and E2E tests** as part of my learning process.

## Why?

I want to understand AI-assisted software engineering in practice, rather than just using AI to generate code.

I’m particularly interested in questions like:

- Can specialized AI agents improve the development process?
- Can they maintain traceability from requirements to implementation and testing?
- How well can AI identify risks and review implementation?
- Where does AI help, and where is Human judgement still necessary?

## The interesting part comes later

Once the MVP is working, I’ll intentionally introduce **known defects** into the application.

The goal is to turn the project into a controlled experiment:

```text
Known defect
    ↓
AI-SDLC
    ↓
Tests / Reviews / CI / Logs
    ↓
Was it detected?
    ↓
Where and when?
    ↓
Evidence
```

This will let me measure things such as defect detection rate, escaped defects, time to detect, false positives and the effectiveness of AI reviewers.

In other words, the application is only part of the project.

**The real subject of the experiment is the development process itself.**

## What’s in the repository?

- `/.github/agents` — AI agents and their responsibilities
- `/.github/skills` — reusable skills used by agents
- `/docs` — project and experiment documentation
- Application source code
- Tests and supporting artifacts

## Project roadmap

- [x] Design the AI-SDLC agent and skill architecture
- [ ] Build the MVP
- [ ] Add automated PR reviews
- [ ] Introduce controlled defects
- [ ] Collect evidence from tests, CI, GitHub and logs
- [ ] Analyse results and build quality metrics
- [ ] Document what worked, what failed and what I learned

## What I’m learning

This project is helping me explore the intersection of:

**QA Engineering · Software Development · AI Agents · SDLC · Test Automation · CI/CD · Observability · Quality Metrics**
