# Learning Log

## Entry 1 — Project scaffold

**What I implemented**
Initial folder structure, documentation set, dependency choices.

**What scientific concept it uses**
None yet — this is project setup.

**What computational concept I learned**
Separation of concerns from the start: keeping domain logic (to be built in
`app/` and a future `core/` package) importable independently of the UI layer,
so the same code can later run inside a Jupyter notebook for manuscript
analysis without duplicating logic.

**What I should study next**
Python dataclasses and basic `typing` (Optional, Literal) — needed for
Phase 2's `UserProfile`/`LifestyleProfile` structures.

## Day 2 — Evidence Verification and Version 1 Scope Freeze

### Objective
Establish a scientifically defensible evidence foundation before implementing any health assessment or prediction functionality.

### Work completed
- Reviewed candidate validated screening instruments and health assessment frameworks.
- Distinguished validated screening instruments from classification/assessment tools, evidence mapping, and exploratory research hypotheses.
- Identified FINDRISC as the candidate validated screening instrument for type 2 diabetes risk screening, pending final primary-source verification before implementation.
- Identified PHQ-9 as the candidate validated screening instrument for depression-related symptoms, with a mandatory safety-response pathway for Item 9 before implementation.
- Restricted obesity and metabolic health to transparent classification and assessment measures such as BMI and appropriately verified anthropometric measures.
- Restricted cardiovascular functionality in Version 1 to evidence mapping rather than an unsupported numerical percentage risk prediction.
- Restricted shared-factor relationships to citation-linked evidence mapping rather than an arbitrary composite score.
- Excluded genetic risk scoring from Version 1.
- Created a Version 1 Evidence Freeze defining which features are approved for implementation and which are explicitly excluded.

### Scientific principles established
1. A screening instrument is not a diagnosis.
2. An association is not automatically causation.
3. A numerical score should not be created without a scientifically justified and documented model.
4. A validated model should not be assumed to transfer perfectly across populations.
5. Evidence strength and population applicability must be documented.
6. Safety requirements must be designed before implementing mental-health screening functionality.

### Current Version 1 direction
The platform will combine:
- transparent anthropometric assessment,
- a verified diabetes screening instrument,
- a validated mental-health screening instrument with an appropriate safety pathway,
- citation-linked cross-domain evidence mapping,
- cardiovascular factor evidence mapping,
- explainable outputs with limitations.

### Day 2 outcome
The Version 1 scientific scope has been frozen before application implementation begins.

### Next milestone
Day 3: design the structured data model and validation architecture for the approved Version 1 features.
