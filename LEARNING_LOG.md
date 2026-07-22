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

## 22 July 2026 — Day 1

### Technical milestone

Successfully installed the Python dependencies and launched the Streamlit prototype locally.

### What I learned

- The project uses Python and Streamlit.
- The application can be launched using:
  `python3 -m streamlit run app/main.py`
- The current project is a scaffold rather than a completed health prediction system.
- The existing application currently contains no biomedical calculation logic.

### Scientific understanding

The planned platform will explore interconnected health domains rather than treating each condition in isolation. Obesity, depression-related mental well-being, type 2 diabetes, and cardiovascular risk share several potentially important factors, including lifestyle, anthropometrics, clinical biomarkers, family history, and genetic susceptibility.

### Current limitation

The platform currently represents a software scaffold and does not yet produce clinical risk estimates or diagnostic outputs.

### Next learning goal

Understand how to design a transparent shared data model and evidence structure for a multi-domain biomedical research prototype.