---
name: qa-analysis
description: Perform focused QA analysis for a Story and produce a concise, actionable QA Analysis output used by the QA Agent.
argument-hint: "[Story]"
---

# QA Analysis Skill

Use this skill to perform a focused, methodical QA analysis that produces the artefacts required by the QA Agent.  
This skill explains _jak myśleć_ o jakości: co sprawdzić, jak klasyfikować ryzyko, jak ocenić pokrycie i jak sformułować minimalny, ryzykiem uzasadniony Quality Contract.

## Inputs

- Approved Acceptance Criteria
- BA analysis
- System Analyst analysis
- Relevant UI design artifact when applicable
- Available implementation evidence (code diffs, tests, CI results) when present

## Analysis Guidance

- **Start od wymagań**: mapuj każdy punkt Acceptance Criteria na możliwe zachowanie systemu i potencjalne ryzyka.
- **Używaj dowodów**: traktuj kod i testy jako _evidence_, nie jako ostateczne źródło prawdy.
- **Klasyfikuj ryzyko** według wpływu i prawdopodobieństwa:
  - **HIGH** — krytyczny biznesowo lub może spowodować poważne uszkodzenie danych lub przerwanie usługi.
  - **MEDIUM** — zauważalny wpływ na użytkownika lub integracje; możliwy do wykrycia w testach automatycznych.
  - **LOW** — kosmetyczne, rzadkie lub niskiego wpływu.
- **Ocena pokrycia**:
  - Zidentyfikuj istniejące testy powiązane z każdym Verification Target.
  - Oceniaj ich skuteczność: deterministyczne, szybkie, niezależne.
  - Wskaż luki: brak testu; test nie pokrywa scenariusza negatywnego; test jest flaky.
- **Regresja**:
  - Określ minimalny zakres regresji oparty na zmianach komponentów i zależnościach.
  - Preferuj selektywny regres testów o wysokim prawdopodobieństwie wpływu.
- **Quality Contract**:
  - Powinien być proporcjonalny do ryzyka.
  - Zawiera wymagane weryfikacje, automatyzację, manualne kroki i kryterium bramki jakości.

## Output Contract

Produce the following structured artefact exactly.
