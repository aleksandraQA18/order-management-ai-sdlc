# AI SDLC — Engineering Environment Setup Guide

## Cel
Zbudować krok po kroku środowisko dla Order Management, oddzielone od specyfikacji samego produktu.

Docelowo:
`Local → PR CI → Ephemeral Test → Merge → Staging → Release Gate → Production Simulation`

Nie zaczynamy od AWS/Kubernetes. Najpierw Git/GitHub, Docker, GitHub Actions, Playwright, PostgreSQL, quality gates i izolowane środowiska.

---

## 0. Prerequisites

Zainstaluj:
- Git
- GitHub account
- Docker Desktop
- Node.js LTS
- Python 3.x
- VS Code
- GitHub CLI — opcjonalnie

Sprawdź:
```bash
git --version
docker --version
docker compose version
node --version
npm --version
python --version
```

Docs:
- https://git-scm.com/doc
- https://docs.docker.com/get-started/
- https://docs.docker.com/compose/
- https://nodejs.org/en/docs
- https://docs.python.org/3/

**Checkpoint:** wszystkie narzędzia działają lokalnie.

---

## 1. GitHub Repository

Repo:
`order-management-ai-sdlc`

Nie pracujemy bezpośrednio na `main`.

Przykładowe branche:
```text
feature/ORD-003-create-order
feature/ORD-004-validation
fix/ORD-005-total
test/ORD-006-api
```

Docs:
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://docs.github.com/en/get-started/using-github/github-flow

**Checkpoint:** lokalny projekt można wypchnąć do GitHub.

---

## 2. Initial repository structure

```text
order-management-ai-sdlc/
├── frontend/
├── backend/
├── tests/
├── qa/
├── docs/
├── .github/
│   └── workflows/
├── .gitignore
├── README.md
└── docker-compose.yml
```

Nie twórz wszystkich przyszłych folderów na zapas.

---

## 3. Local Docker Environment

Cel:
```bash
docker compose up --build
```

Usługi:
```text
frontend
backend
postgres
```

Naucz się:
- image
- container
- Dockerfile
- ports
- environment variables
- volume
- network
- healthcheck
- dependencies
- Docker Compose

Docs:
- https://docs.docker.com/build/concepts/dockerfile/
- https://docs.docker.com/compose/gettingstarted/
- https://docs.docker.com/reference/compose-file/

**Checkpoint:** świeży clone uruchamia aplikację jedną udokumentowaną komendą.

---

## 4. Environment Configuration

Dodaj `.env.example`.

Nigdy nie commituj prawdziwych sekretów.

Docelowe środowiska:
```text
local
test
staging
production
```

Preferuj konfigurację zamiast kodu zależnego od środowiska.

---

## 5. Database Strategy

PostgreSQL.

### Local
Może mieć persistent volume.

### CI/Test
Świeża baza dla każdego runu/job:
```text
CI
 ↓
PostgreSQL
 ↓
migrations
 ↓
seed
 ↓
tests
 ↓
destroy
```

### Staging
Oddzielna baza.

### Production simulation
Oddzielna baza.

Nigdy nie kopiujemy danych produkcyjnych do testów.

Dane testowe powinny być:
- deterministic,
- isolated,
- resettable,
- minimalne.

---

## 6. Reproducible Test Execution

Zdefiniuj komendy działające lokalnie, np.:
```bash
npm run lint
npm run typecheck
npm run test
```

Backend analogicznie.

CI ma używać tych samych logicznych komend co lokalny development.

**Checkpoint:** testy da się odtworzyć z czystego checkoutu.

---

## 7. GitHub Actions — PR CI

Utwórz:
```text
.github/workflows/ci-pr.yml
```

Trigger:
```yaml
on:
  pull_request:
    branches:
      - main
```

Początkowy pipeline:
```text
checkout
 ↓
install dependencies
 ↓
lint
 ↓
typecheck
 ↓
build
 ↓
tests
 ↓
report
```

Docs:
- https://docs.github.com/en/actions/get-started/quickstart
- https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions

**Checkpoint:** otwarcie PR uruchamia CI.

---

## 8. Playwright in CI

Po dodaniu Playwright:
```text
install browsers
 ↓
run tests
 ↓
upload HTML report
 ↓
upload trace/screenshots for failures
```

Docs:
- https://playwright.dev/docs/ci-intro
- https://playwright.dev/docs/test-reporters
- https://playwright.dev/docs/trace-viewer

Nie używaj nieograniczonych retries do ukrywania flaky tests.

---

## 9. Branch Protection / Rulesets

Chcemy:
```text
PR
 ↓
required checks
 ↓
PASS → merge allowed
FAIL → merge blocked
```

Na początku wymagaj tylko istotnych checków:
- build/checks
- API tests, gdy istnieją
- E2E tests, gdy istnieją

Docs:
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets

**Ćwiczenie:** celowo zepsuj check i sprawdź, czy merge zostanie zablokowany.

---

## 10. Pull Request Workflow

Każda Story:
```text
Story
 ↓
branch
 ↓
implementation
 ↓
tests
 ↓
PR
 ↓
CI
 ↓
QA review
 ↓
merge
```

PR powinien zawierać:
- co się zmieniło,
- business behavior,
- tests,
- risks,
- evidence,
- known limitations.

---

## 11. Ephemeral Test Environment

Cel: każdy CI run ma izolowane środowisko.

Przykład:
```text
PR #42
 ├── backend container
 ├── postgres container
 ├── frontend if needed
 └── test runner
       ↓
     tests
       ↓
    destroy
```

Dzięki temu równoległe PR-y nie współdzielą stanu.

Docs:
- https://docs.github.com/en/actions/using-containerized-services/about-service-containers
- https://docs.docker.com/build/ci/

**Checkpoint:** dwa CI runs nie wpływają na siebie danymi testowymi.

---

## 12. Staging

Po merge:
```text
main
 ↓
build artifact/image
 ↓
deploy staging
 ↓
smoke
 ↓
full regression
```

Staging może początkowo być osobnym Docker Compose. Nie musi być publiczny.

Ma mieć:
- oddzielną konfigurację,
- oddzielną bazę,
- production-like ustawienia,
- reprezentatywne dane,
- brak swobodnego eksperymentowania.

---

## 13. Production Simulation

Osobne środowisko:
```text
production/
├── frontend
├── backend
└── postgres
```

Z:
- oddzielną bazą,
- konfiguracją,
- sekretami,
- kontrolowanym deploymentem.

Preferowany model:
**build once, promote the same artifact**.

Czyli nie budujemy „innego kodu” na production.

---

## 14. Release Flow

Docelowo:
```text
feature
 ↓
PR
 ↓
PR CI
 ↓
quality gate
 ↓
merge
 ↓
main CI
 ↓
staging
 ↓
smoke
 ↓
regression
 ↓
release gate
 ↓
production simulation
```

Na początku production może wymagać manual approval.

---

## 15. Quality Gates

### PR Gate
```text
lint              PASS
typecheck         PASS
build             PASS
critical API      PASS
critical E2E      PASS
```

### Staging Gate
```text
full API regression       PASS
E2E regression            PASS
critical risks covered   PASS
no blocker defect         PASS
```

### Release Gate
```text
staging healthy
regression green
security checks green
evidence available
approval received
```

Nie używaj arbitralnego „90% testów musi przejść”. Gate powinien wynikać z ryzyka.

---

## 16. Test Reports / Evidence

CI powinno przechowywać:
- Playwright HTML report,
- screenshots,
- traces,
- JUnit-compatible results, jeśli skonfigurowane,
- istotne logi.

Nie commituj wygenerowanych raportów do repo.

Cel:
> Po failu wiadomo co, gdzie i dlaczego się zepsuło.

---

## 17. Secrets

Nigdy nie commituj:
- passwords
- API keys
- tokens
- private keys
- production credentials

Używaj GitHub Actions Secrets/Variables.

Docs:
https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions

---

## 18. Rollback Exercise

Po uruchomieniu deploymentu wykonaj eksperyment:
```text
v0.1.0 → healthy
v0.2.0 → intentional defect
rollback → v0.1.0
```

Następnie:
```text
incident
 ↓
root cause analysis
 ↓
bug
 ↓
regression test
 ↓
fix
 ↓
v0.2.1
```

To jest celowo praktyczne ćwiczenie QA + DevOps.

---

## 19. Monitoring — później

Na początku wystarczy:
- application logs,
- health endpoint,
- CI results,
- deployment history.

Dopiero później:
- Prometheus,
- Grafana,
- OpenTelemetry,
- structured logging.

Nie dokładamy observability zanim podstawowy delivery pipeline nie działa.

---

## 20. Security Pipeline — późniejsza faza

Po stabilnym CI/CD dodaj:
- dependency audit,
- secret scanning,
- SAST, jeśli ma sens,
- security smoke tests,
- OWASP-focused tests.

Nie zaczynaj od security tooling.

---

## 21. Kubernetes — opcjonalny advanced phase

Nie zaczynamy od Kubernetes.

Najpierw:
```text
Docker
 ↓
Compose
 ↓
CI/CD
 ↓
Environments
 ↓
Quality Gates
```

Dopiero później pytamy:
> Jakie problemy rozwiązuje Kubernetes, których Docker Compose nie rozwiązuje?

Docs:
- https://kubernetes.io/docs/tutorials/kubernetes-basics/
- https://kind.sigs.k8s.io/
- https://minikube.sigs.k8s.io/docs/

---

# 22. Recommended implementation order

### Phase 1 — Local
- tools
- GitHub repo
- structure
- Docker Compose
- frontend/backend/PostgreSQL

### Phase 2 — Local quality
- lint
- typecheck
- tests
- Playwright
- reproducible commands

### Phase 3 — PR CI
- GitHub Actions
- build
- checks
- API tests
- E2E
- reports

### Phase 4 — Quality gates
- protect main
- required checks
- intentionally fail a check
- verify merge is blocked

### Phase 5 — Ephemeral test environment
- isolated PostgreSQL
- migrations
- seed data
- tests
- cleanup

### Phase 6 — Staging
- artifact/image
- deployment
- smoke
- regression

### Phase 7 — Production simulation
- separate config
- separate DB
- deployment
- release gate

### Phase 8 — Operations
- rollback
- incident
- RCA
- regression from incident

### Phase 9 — Security
- dependency/security checks
- application security tests

### Phase 10 — Optional Kubernetes
Only after the above works.

---

# 23. Environment Definition of Done

- [ ] fresh clone works
- [ ] Docker Compose starts local stack
- [ ] frontend reaches backend
- [ ] backend reaches PostgreSQL
- [ ] tests run locally
- [ ] PR triggers CI
- [ ] CI produces evidence
- [ ] failed required check blocks merge
- [ ] merge triggers main pipeline
- [ ] test environment is isolated
- [ ] staging can be deployed
- [ ] staging regression runs
- [ ] production simulation exists
- [ ] release gate exists
- [ ] rollback has been tested
- [ ] secrets are not committed

---

# 24. Learning Method

For every infrastructure task answer:

### What?
What did I configure?

### Why?
What problem does it solve?

### Failure?
What happens when it fails and how do I diagnose it?

Do not copy configuration without understanding it.

The goal is not to memorize Docker or GitHub Actions syntax. The goal is to understand the delivery system well enough to make QA and engineering decisions inside it.
