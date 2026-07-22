# Explainable Multi-Domain Precision Health Platform (research prototype)

## Status: early scaffold — Phase 1 (codebase stabilization) in progress

## Scientific motivation
Obesity, depression-related mental well-being, type 2 diabetes, and cardiovascular
risk share overlapping modifiable drivers — sleep, diet, physical activity, stress —
and, to a lesser and much more uncertain degree, overlapping genetic susceptibility.
Most consumer tools treat these four domains as isolated calculators. This project
explores whether a shared, explainable computational model can surface which
modifiable factors matter across domains for a given person, without pretending to
diagnose disease or predict the future with certainty.

## Problem statement
Build a research-grade, explainable software prototype that:
- estimates domain-level risk indicators (not diagnoses) for obesity/metabolic
  health, depression-related well-being, type 2 diabetes, and cardiovascular risk,
- represents gene–diet–lifestyle relationships with explicit evidence grading and
  uncertainty, never as deterministic gene→disease claims,
- explains every output in terms of the factors that produced it,
- lets a user simulate "what if I changed X" scenarios and see model-based
  (not guaranteed) directional changes across domains.

## What this is NOT
- Not a diagnostic tool.
- Not a clinically validated risk calculator (validation plan is in
  `docs/VALIDATION_PLAN.md`, to be built out — nothing here has been validated yet).
- Not a source of genetic determinism — genetic contributions are modeled as
  susceptibility modifiers with explicit evidence levels, never as fate.

## Platform architecture (planned, see ROADMAP.md for phasing)
- **User Profile** — age, sex, anthropometrics, family history, smoking/alcohol.
- **Lifestyle Profile** — diet, physical activity, sleep, stress.
- **Domain modules** — obesity/metabolic, depression-related well-being,
  type 2 diabetes, cardiovascular risk.
- **Shared-factor engine** — cross-domain modifiable-factor scoring.
- **Evidence database** — structured, evidence-graded gene/nutrient/lifestyle/
  outcome relationships (see `EVIDENCE_DATABASE_SCHEMA.md`).
- **Explainability engine** — every output ships with its contributing factors.
- **What-if simulator** — baseline vs. scenario comparison across domains.

## Tech stack
- **Python** for all core logic (calculations, evidence data, explainability),
  chosen because it keeps the scientific/computational core directly reusable in
  Jupyter notebooks for later manuscript figures and statistical validation —
  the same functions power the app and the research analysis.
- **Streamlit** for the interactive front end — minimal boilerplate, good fit for
  a research-facing data app, easy to deploy for demos/portfolio purposes.
- **pandas / numpy** for data handling; **pytest** for testing core calculations.

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage
```bash
streamlit run app/main.py
```
(App is currently a placeholder — see PROJECT_STATUS.md for what's implemented.)

## Evidence framework
Every gene/nutrient/lifestyle/outcome relationship in `evidence/` carries an
evidence-strength label (High / Moderate / Limited / Emerging / Research-only),
a population note, and stated limitations. No relationship is presented as
deterministic. See `EVIDENCE_DATABASE_SCHEMA.md`.

## Explainability approach
Outputs are only allowed to show numeric weights/percentages if the underlying
model is a transparent, inspectable weighted model — no invented numbers.
Modifiable and non-modifiable factors are always separated.

## Validation plan
See `docs/VALIDATION_PLAN.md` (content, technical, model, explainability, and
usability validation layers) — this is a plan, not a completed validation.

## Limitations
- No clinical validation has been performed at this stage.
- Evidence base is being built incrementally; many relationships are currently
  placeholders labeled "research-only" pending literature review.
- Genetic susceptibility variants included are common, well-studied ones (e.g.
  FTO, MC4R, PPARG) — this is not a comprehensive polygenic risk model.

## Ethical considerations
- No real personal health or genetic data is used in development (synthetic/demo
  data only).
- The platform must never claim to diagnose disease or guarantee outcomes.
- Mental well-being module includes safety-message handling for concerning
  responses (see MODULE_B docs once implemented).

## Roadmap
See `ROADMAP.md`.

## Citation
Citation information will be added once the platform reaches a stage suitable for
manuscript preparation (see `RESEARCH_NOTES.md` and `LITERATURE_MAP.md`).
