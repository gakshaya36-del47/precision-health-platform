# Roadmap

Each phase should end at a clean, working checkpoint. Do not start a phase
before the previous one is stable and documented.

### Phase 0 — Existing project audit
N/A for this build — there was no pre-existing codebase, only literature and
a planning document. Skipped; starting directly at Phase 1.

### Phase 1 — Codebase stabilization
Project skeleton, docs, dependency management, `.gitignore`. (In progress.)

### Phase 2 — Core platform architecture
`UserProfile` and `LifestyleProfile` data structures. No UI yet. Unit tests
for structure validation (e.g. plausible ranges for age, BMI inputs).

### Phase 3 — Obesity module refinement
BMI/waist-circumference-based indicators, modifiable vs. non-modifiable
factor split, first pass at the genetic layer (FTO, MC4R, PPARG) using
evidence from Barrea et al. 2020.

### Phase 4 — Depression and mental well-being module refinement
Validated-screening-style questionnaire structure (e.g. PHQ-9-like item
shape — using our own item wording, not copyrighted instruments verbatim,
until licensing is confirmed), safety-message handling.

### Phase 5 — Type 2 diabetes risk
Age, BMI, family history, lifestyle, and (if available) biomarker inputs.

### Phase 6 — Cardiovascular risk
Lipid/BP-based inputs, APOE/FADS1 genetic layer.

### Phase 7 — Shared-factor engine
Cross-domain modifiable-factor scoring ("Shared-Factor Priority Score").

### Phase 8 — Evidence database
Structured `evidence/*.json` files with evidence-level grading.

### Phase 9 — Genetic interaction layer
Gene → nutrient/lifestyle → pathway → biomarker → outcome chains with
uncertainty annotations.

### Phase 10 — Explainability engine
Consistent contributing-factor breakdown for every module output.

### Phase 11 — What-if intervention simulator
Baseline vs. scenario comparison UI + underlying diff logic.

### Phase 12 — Biological pathway visualization
Interactive diagrams for diet/sleep/stress → pathway → outcome.

### Phase 13 — Validation framework
Content, technical, model, explainability, usability validation (see
`docs/VALIDATION_PLAN.md`).

### Phase 14 — Usability and accessibility
Responsive layout, accessible color/contrast, plain-language toggle.

### Phase 15 — Research documentation
Finalize RESEARCH_NOTES.md, LITERATURE_MAP.md, MODEL_ASSUMPTIONS.md for
manuscript prep.

### Phase 16 — Manuscript preparation
Draft methods/results sections from the validation data collected in Phase 13.

---
We are not implementing all phases at once. Current focus: Phase 1 → Phase 2.
