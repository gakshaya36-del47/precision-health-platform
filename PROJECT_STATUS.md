# Project Status

## Current phase
Phase 1 — Codebase stabilization (initial scaffold just created; no calculation
logic yet).

## Overall completion
~2% — documentation and folder scaffold only. No working app yet.

## Completed
- [x] Chose stack: Python + Streamlit + pandas/numpy, pytest for tests.
- [x] Created project skeleton (`app/`, `evidence/`, `tests/`, `docs/`).
- [x] Created README, ROADMAP, LEARNING_LOG, CHANGELOG, RESEARCH_NOTES,
      LITERATURE_MAP, MODEL_ASSUMPTIONS, EVIDENCE_DATABASE_SCHEMA skeletons.
- [x] Logged first literature source (Barrea et al. 2020, nutrigenetics review)
      into LITERATURE_MAP.md.
- [x] Added `.gitignore` and `.env.example`.

## Currently working on
- [ ] Nothing mid-flight — this is a clean checkpoint.

## Next milestone
- [ ] Phase 2: Define the core `UserProfile` and `LifestyleProfile` data
      structures (plain Python dataclasses), with unit tests, before any UI.

## Known bugs
- [ ] None yet (no functional code exists).

## Scientific decisions made
- Genetic layer will only include variants with at least "Moderate" evidence
  per our own grading scale, sourced from literature review, starting with the
  genes covered in Barrea et al. 2020 (FTO, MC4R, PPARG, APOE/APOA, ADRB, PLIN,
  FADS1, CLOCK, MTHFR).
- All disease-domain outputs will use screening/risk-estimation language, never
  diagnostic language.

## Technical decisions made
- Python chosen over a JS framework so the same functions used by the app can
  be imported directly into Jupyter notebooks for manuscript analysis later.
- Streamlit chosen over Flask/FastAPI+React for now to minimize UI boilerplate
  while the scientific core is still being designed; can be swapped later
  without touching the core logic if a richer UI is needed.

## Research questions currently being studied
- [ ] How to represent evidence strength + population applicability in a way
      that's both machine-readable and human-explainable.

## Bioinformatics/computational concepts learned
- [ ] (log entries go in LEARNING_LOG.md as features are built)

## Papers and resources to read
- [ ] Barrea et al. 2020, "Nutrigenetics—personalized nutrition in obesity and
      cardiovascular diseases," Int J Obes Suppl. (logged, not yet deeply mined
      for the evidence database)

## GitHub commits completed
- [ ] None yet — repo not initialized.

## LinkedIn progress update opportunities
- [ ] Not yet — wait until Phase 2 produces something demonstrable.

## What I should learn next
- [ ] Python dataclasses / typing basics if not already comfortable, since the
      next milestone builds directly on them.


# Project Status

## Current Version

v0.1 — Initial Working Scaffold

## Date

22 July 2026

## Current State

The initial Streamlit application has been successfully launched locally.

## Technology Stack

- Python
- Streamlit

## Current Functionality

The application currently provides:

- A working Streamlit interface
- A research prototype landing page
- Scope definition for a multi-domain precision-health platform
- A clear statement that the platform is not a diagnostic tool

## Planned Health Domains

- Obesity and metabolic health
- Depression-related mental well-being
- Type 2 diabetes
- Cardiovascular risk

## Planned Shared Factors

- Diet
- Physical activity
- Sleep
- Stress
- Anthropometric variables
- Clinical biomarkers
- Family history
- Selected genetic susceptibility factors

## Current Calculations

No biomedical calculations or risk scores have been implemented yet.

## Current Limitations

- No disease-specific models
- No shared-factor engine
- No evidence database integration
- No intervention simulation
- No validation dataset

## Next Milestone

Design and implement the scientific data model and evidence structure before building individual health-domain modules.

## Status

🟢 Working scaffold
