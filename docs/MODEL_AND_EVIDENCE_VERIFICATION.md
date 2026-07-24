## FINDRISC Version Selection

The project will implement the later 0–26 point FINDRISC version, not the original 0–20 point Diabetes Risk Score published by Lindström & Tuomilehto (2003).

The selected version must have its complete scoring table verified from an authoritative source before implementation.

The following must not be conflated:

- Original 2003 Diabetes Risk Score: 0–20 points, seven variables.
- Later 0–26 FINDRISC versions: expanded/modified scoring structure, including family history.

Implementation status: NOT YET CLEARED.

No FINDRISC code will be written until the exact adopted version and all scoring categories are documented and verified.# Model and Evidence Verification

Status: planning/verification document. Supplements
`docs/MODEL_AND_EVIDENCE_INVENTORY.md`. No application code has been written
or modified as a result of this document.

Every proposed Version 1 instrument or framework below is labeled as one of:
- **VALIDATED SCREENING INSTRUMENT**
- **CLASSIFICATION/ASSESSMENT**
- **EVIDENCE MAPPING**
- **EXPLORATORY RESEARCH HYPOTHESIS**

---Verification update:

The 0–26 point FINDRISC scoring structure has been cross-checked against the original Lindström & Tuomilehto (2003) Diabetes Risk Score citation and multiple direct reproductions of the original scoring table. The adopted implementation uses the eight-variable 0–26 structure: age, BMI, waist circumference, physical activity, daily fruit/vegetable/berry intake, antihypertensive medication, history of high blood glucose, and family history of diabetes.

The original 2003 paper reports the underlying seven-variable Diabetes Risk Score with a 0–20 range. The 0–26 structure used by this project is the later expanded FINDRISC form that includes family history. These versions are explicitly treated as distinct and will not be conflated.

Implementation status: CLEARED FOR IMPLEMENTATION.

The implementation must preserve the published category boundaries and integer point values. No coefficients will be reconstructed, recalibrated, or modified. Original Finnish-cohort absolute-risk percentages must not be presented as individually calibrated predictions for platform users.

## A. FINDRISC — Verification Table

**Label: VALIDATED SCREENING INSTRUMENT** (explicitly a screening tool for
future risk, not a diagnostic test — it identifies who should get a glucose/
HbA1c test, it does not diagnose diabetes itself).

| # | Field | Detail |
|---|---|---|
| 1 | Instrument/model name | Finnish Diabetes Risk Score (FINDRISC / FINDRISK) |
| 2 | Exact original citation | Lindström J, Tuomilehto J. "The Diabetes Risk Score: A Practical Tool to Predict Type 2 Diabetes Risk." *Diabetes Care.* 2003;26(3):725–731. |
| 3 | DOI / authoritative source | DOI: 10.2337/diacare.26.3.725 |
| 4 | Intended purpose | Identify, without any laboratory test, individuals at increased 10-year risk of developing (drug-treated) type 2 diabetes, so they can be directed toward lifestyle counselling and/or glucose testing. It is explicitly a screening tool, not a diagnostic test. |
| 5 | Required inputs | Age (band), BMI (band), waist circumference (sex-specific band), daily physical activity ≥30 min (yes/no), daily fruit/vegetable/berry consumption (yes/no), history of antihypertensive medication use (yes/no), history of previously measured high blood glucose (yes/no), family history of diabetes (none / 2nd-degree relative / 1st-degree relative). |
| 6 | Scoring method / classification rules | Point sum across the 8 items, derived originally from multivariate logistic regression coefficients converted to integer scores by the original authors. Published/widely reproduced point values: age <45=0, 45–54=2, 55–64=3, >64=4; BMI <25=0, 25–30=1, >30=3; waist circumference (men <94cm=0, 94–102cm=3, >102cm=4; women <80cm=0, 80–88cm=3, >88cm=4); physical activity yes=0/no=2; daily fruit/veg/berries yes=0/no=1; antihypertensive medication no=0/yes=2; prior high blood glucose no=0/yes=5; family history none=0, grandparent/aunt/uncle/cousin=3, parent/sibling/child=5. Total range 0–26. Commonly reported risk-category bands: low <7 (~1% 10-yr risk), slightly elevated 7–11 (~4%), moderate 12–14 (~17%), high 15–20 (~33%), very high >20 (~50%). **These exact point values and percentages must be checked against the primary 2003 paper's tables directly before being hard-coded** — the values above are consistently reproduced across many secondary clinical sources but this project has not yet obtained and re-verified them against the original journal PDF. |
| 7 | Intended population | General adult population screening in primary care / pharmacy / community settings, originally ages 35–64. |
| 8 | Validation population | Derived from two Finnish population cohorts, >9,000 adults aged 35–64, followed 10 years, new diabetes cases ascertained via Finland's National Drug Registry. Since then, externally validated (with varying performance) in Germany, Hungary, Norway, Turkey, Indonesia, Peru, Poland, several Latin American cohorts, and NHANES (US) data, generally reporting AUC/C-statistic in the ~0.7–0.85 range in the original and closely related populations. |
| 9 | Known limitations | (a) Original absolute risk percentages (1/4/17/33/50%) do not transfer reliably to other populations — e.g. a large Norwegian 10-year follow-up (HUNT study) found only 13.5% cumulative incidence among people scoring ≥15, versus the ~33% implied by the original Finnish bands, showing the *ranking* (higher score = higher risk) held up but the *absolute percentages* did not. (b) Multiple external validations recommend recalibration/reweighting before use in a new population. (c) Weaker discrimination reported in people over 65. (d) Does not include ethnicity-specific adjustment despite well-documented differences in diabetes risk at a given BMI across ethnic groups. |
| 10 | Suitable for implementation in this prototype? | Yes, as a screening instrument only — provided absolute risk percentages are either omitted or clearly labeled "as reported in the original Finnish cohort, not calibrated to this platform's users," and the score itself (not a diagnosis) is the primary output. |
| 11 | Can it be implemented without reconstructing missing coefficients? | Yes — the scoring is a simple integer point sum with publicly reproduced values (no proprietary/regression coefficients need to be estimated or invented), but the exact values must be pulled from the primary 2003 paper (or a direct, citable reproduction of it) before being hard-coded, not assembled from memory of secondary sources. |
| 12 | Required safety considerations | None safety-critical (no self-harm-adjacent items), but must not present the output as a diagnosis, and must recommend an actual glucose/HbA1c test and clinician follow-up at moderate-or-higher scores rather than implying certainty. |

---

## B. PHQ-9 — Verification Table

**Label: VALIDATED SCREENING INSTRUMENT** (explicitly a screening/severity
measure; the original validation paper itself distinguishes it from a
clinical diagnostic interview — a positive screen still requires clinical
confirmation).

| # | Field | Detail |
|---|---|---|
| 1 | Instrument/model name | Patient Health Questionnaire-9 (PHQ-9); ultra-brief 2-item version PHQ-2 available as an optional pre-screen. |
| 2 | Exact original citation | Kroenke K, Spitzer RL, Williams JBW. "The PHQ-9: Validity of a Brief Depression Severity Measure." *J Gen Intern Med.* 2001;16(9):606–613. |
| 3 | DOI / authoritative source | DOI: 10.1046/j.1525-1497.2001.016009606.x. Instrument itself is public domain — the official PHQ Screeners materials state no permission is required to reproduce, translate, display, or distribute it (originally developed with an educational grant from Pfizer Inc.; Pfizer's copyright restrictions on this content were later lifted). |
| 4 | Intended purpose | Screen for and measure the severity of depressive symptoms over the prior two weeks, mapped to the 9 DSM diagnostic criteria for major depressive disorder. Multipurpose: can support screening, severity monitoring over time, and treatment-response tracking — but a diagnosis still requires clinical evaluation. |
| 5 | Required inputs | 9 items (interest/pleasure, mood, sleep, energy, appetite, self-worth/guilt, concentration, psychomotor change, thoughts of self-harm/death), each scored 0 ("not at all") to 3 ("nearly every day") for the past 2 weeks; an optional 10th item asks how much these symptoms have affected daily functioning. |
| 6 | Scoring method / classification rules | Simple sum of the 9 item scores, range 0–27, no reverse-keyed items. Published severity bands from the original validation: 0–4 minimal, 5–9 mild, 10–14 moderate, 15–19 moderately severe, 20–27 severe. A score ≥10 is the standard clinically-significant threshold, reported at 88% sensitivity / 88% specificity for major depressive disorder against independent structured clinical interview in the original validation. |
| 7 | Intended population | Adult primary-care patients (general and OB-GYN clinics), for use as a self-administered screener before or during a clinical visit. |
| 8 | Validation population | Original PHQ studies: ~6,000 US adult patients across 8 family-practice and 7 obstetrics-gynecology clinics (Spitzer et al. 1999 PRIME-MD studies; Kroenke et al. 2001 validation), validated against independent structured mental-health-professional interviews. Since then, translated and re-validated across many countries/languages, consistently used as a screening (not diagnostic) tool. |
| 9 | Known limitations | Self-report only, cannot replace a clinical interview; performance varies somewhat by population/language version; a positive screen (≥10) is not itself a diagnosis and requires follow-up; item 9 (thoughts of self-harm) requires special handling regardless of the total score — see column 12. |
| 10 | Suitable for implementation in this prototype? | Yes, as a screening instrument, contingent on the safety-response design (below) being built and tested *before* this module ships. |
| 11 | Can it be implemented without reconstructing missing coefficients? | Yes — scoring is an unweighted sum with fixed, published severity bands; no coefficients need to be invented or estimated. |
| 12 | Required safety considerations | **Non-negotiable prerequisite.** Any non-zero response to item 9 (thoughts of self-harm or being better off dead) must trigger an immediate, direct, supportive response and crisis-resource information, independent of the total score — this must be built, tested, and reviewed before the scoring feature ships, not added afterward. The module must never present its output as a diagnosis, and must state this explicitly on the same screen as the result. |

---

## C. Obesity and Metabolic Health — Verification Table

Three separate items are covered here since obesity/metabolic health does
not have one single validated instrument the way T2D (FINDRISC) or
depression (PHQ-9) do.

### C1. BMI classification

**Label: CLASSIFICATION/ASSESSMENT** (a universally used anthropometric
convention, not a predictive model).

| # | Field | Detail |
|---|---|---|
| 1 | Instrument/model name | WHO BMI classification (standard) and WHO Asian-population BMI action points |
| 2 | Exact original citation | WHO Expert Consultation. "Appropriate body-mass index for Asian populations and its implications for policy and intervention strategies." *Lancet.* 2004;363(9403):157–163. |
| 3 | DOI / authoritative source | DOI: 10.1016/S0140-6736(03)15268-3 |
| 4 | Intended purpose | Classify current body weight status (underweight/normal/overweight/obese) as a population-health convention — not a prediction of future disease. |
| 5 | Required inputs | Height, weight → BMI = weight(kg) / height(m)². |
| 6 | Scoring method / classification rules | Standard WHO cutoffs: <18.5 underweight, 18.5–24.9 normal, 25–29.9 overweight, ≥30 obese. The 2004 WHO Expert Consultation additionally proposed Asian-population action points at BMI 23.0 (increased risk), 27.5, 32.5, and 37.5 kg/m², after finding that the observed-risk cutoff for cardiometabolic disease fell in the 22–25 kg/m² range across various Asian cohorts — i.e., meaningfully lower than the standard 25 kg/m² threshold. The consultation deliberately did **not** replace the international cutoffs, only added population-specific "public health action points." |
| 7 | Intended population | Standard cutoffs: general/international, originally calibrated mainly on European-ancestry data. Asian action points: adults of Asian ancestry, reviewed across more than 25 Asian-population cohort studies. |
| 8 | Validation population | As above — a WHO expert consultation synthesis of existing published cohort evidence, not a single new validation study. |
| 9 | Known limitations | BMI does not distinguish fat mass from muscle mass, does not capture fat distribution, and (per the very rationale for the Asian action points) the same BMI value corresponds to different metabolic risk in different populations. This project's likely user base (India) falls under the Asian action-point guidance, which must be reflected in the classification shown, not the standard European-calibrated cutoffs alone. |
| 10 | Suitable for implementation in this prototype? | Yes — it's simple, well-documented, and both cutoff sets are equally implementable; the only judgment call is which cutoff set (or both, labeled) to show. |
| 11 | Can it be implemented without reconstructing missing coefficients? | Yes — no coefficients, just published threshold values. |
| 12 | Required safety considerations | None safety-critical; must avoid language implying a moral judgment about body weight, and must state that BMI is a screening/classification convention, not a diagnosis of metabolic disease. |

### C2. Waist circumference

**Label: CLASSIFICATION/ASSESSMENT.**

| # | Field | Detail |
|---|---|---|
| 6 | Scoring / classification rules | Widely used sex-specific thresholds for increased cardiometabolic risk (e.g. the same thresholds embedded in FINDRISC: men ≥94cm elevated / ≥102cm high; women ≥80cm elevated / ≥88cm high) — these trace back to WHO/IDF central-obesity guidance, the same evidence base FINDRISC itself draws on. |
| 9 | Known limitations | Like BMI, population-specific cutoffs exist and are not universally agreed; measurement technique (exact anatomical landmark) varies across studies, which can shift results by a few centimeters. |
| 10 | Suitable for V1? | Yes, reusing the same FINDRISC-aligned thresholds keeps the platform internally consistent. |

### C3. Waist-to-height ratio (WHtR) — included as requested

**Label: CLASSIFICATION/ASSESSMENT** (proposed as a screening heuristic, not
a diagnostic model).

| # | Field | Detail |
|---|---|---|
| 1 | Instrument/model name | Waist-to-Height Ratio (WHtR), boundary value 0.5 |
| 2 | Exact original citation | Ashwell M, Gibson S. "A proposal for a primary screening tool: 'Keep your waist circumference to less than half your height'." *BMC Med.* 2014;12:207. |
| 3 | DOI / authoritative source | DOI: 10.1186/s12916-014-0207-1 |
| 4 | Intended purpose | Simple, ethnicity-independent proxy for central adiposity and cardiometabolic risk, summarized as the public-health message "keep your waist circumference to less than half your height." |
| 5 | Required inputs | Waist circumference, height (same units). |
| 6 | Scoring / classification rules | WHtR = waist circumference / height. A commonly cited banding (from later secondary sources building on Ashwell's work, not the 2014 paper itself) is roughly: <0.4 possibly underweight risk, 0.4–0.5 healthy range, 0.5–0.6 increased risk, >0.6 high risk — the single boundary value of 0.5 is the one with the strongest direct support from the cited paper and meta-analyses; the finer 0.4/0.6 sub-bands should be sourced independently before being hard-coded, as they were not directly verified in this review. |
| 7/8 | Population | Reviewed across UK (Health Survey for England, National Diet and Nutrition Survey) and international meta-analytic evidence; explicitly proposed as suitable across ethnic groups and across adults and children, addressing the exact ethnicity problem that BMI cutoffs have. |
| 9 | Known limitations | The 0.5 cutoff is a pragmatic, simplicity-driven boundary rather than a precisely fitted statistical threshold for any one outcome; some pediatric/regional studies find slightly different optimal cutoffs (e.g. ~0.49 in some child cohorts). |
| 10 | Suitable for V1? | Yes, as an optional additional/complementary classification alongside BMI and waist circumference — it directly addresses the ethnicity-cutoff problem flagged for BMI in C1. |
| 11 | Coefficients needed? | No — single ratio, single published boundary value. |
| 12 | Safety considerations | Same body-neutral framing requirement as BMI. |

### C4. What can and cannot be called "obesity staging"

- **Can** call it "BMI/waist-circumference/WHtR classification" — these are
  established, cited, anthropometric conventions.
- **Cannot** call this "the Edmonton Obesity Staging System" unless the
  actual EOSS clinical criteria (comorbidity severity, functional limitation,
  psychopathology, all clinically assessed — see prior inventory Section 2)
  are implemented; a subset of self-reportable items must be labeled
  "a simplified, partial adaptation inspired by EOSS categories," not "EOSS,"
  if lab-based criteria aren't actually being applied. This distinction must
  be visible in the UI copy, not just in this document.

---

## D. Cardiovascular Risk — Why No Numeric Model in V1

**Label for any V1 cardiovascular feature: EVIDENCE MAPPING**, not a
prediction model.

Reasoning, consolidated from the prior inventory and unchanged by this
verification pass:

1. Both candidate validated prediction models — the 2013 ACC/AHA Pooled
   Cohort Equations (Goff et al., *Circulation* 2014;129(25 Suppl 2):S49–S73)
   and the 2023 AHA PREVENT equations (Khan et al., *Circulation*
   2023;148(24):1982–2004, DOI: 10.1161/CIRCULATIONAHA.123.067626) — publish
   their coefficients in appendices/supplements that this project has not
   yet obtained and independently verified. Implementing either from a
   secondary description would risk exactly the kind of reconstructed,
   unverified coefficient this Day-2 correction explicitly prohibits.
2. The Pooled Cohort Equations were derived and validated only in White and
   Black US adults aged 40–79; current guidance explicitly acknowledges this
   likely **underestimates risk in South Asian populations** when the
   "White" equation is used as a substitute — directly relevant given this
   platform's likely user base.
3. PREVENT is US-derived from a more diverse cohort and deliberately excludes
   race as a variable, which is a meaningful equity improvement, but it has a
   much shorter external-validation track record outside the US than the
   older PCE, and no validation in a South Asian population has been
   identified in this review.
4. Given both the coefficient-sourcing gap and the population-applicability
   gap, no numeric CVD risk percentage should be computed or shown in
   Version 1.

**What CAN be shown instead (evidence mapping, no computed percentage):**
- The named risk factors used by both PCE and PREVENT (age, sex, total/HDL
  cholesterol, systolic blood pressure, blood-pressure treatment, smoking
  status, diabetes status; PREVENT additionally: BMI, kidney function/eGFR)
  and their documented direction of effect — presented as "these are the
  factors clinical cardiovascular risk models consider, and this is the
  general direction in which each moves risk," with citations, and no
  synthesized number.
- A plain statement that a numeric 10-year risk estimate is intentionally not
  provided in this version, with the reasons above shown to the user in
  simplified form (transparency about the gap, not a hidden limitation).

---

## E. Shared-Factor Engine — Verification

**Label: EXPLORATORY RESEARCH HYPOTHESIS.** This is the one area of the
platform that is *not* an implementation of a published instrument, and it
must never be presented as if it were.

- **Evidence mapping vs. prediction, explicitly distinguished:** the
  individual associations behind this feature (e.g. poor sleep and obesity,
  poor sleep and depression, physical inactivity and T2D, chronic stress and
  cardiovascular risk) are each independently documented in the literature
  and can be shown as **evidence-mapping** statements with citations, exactly
  like Section D above.
- **What must NOT be built:** a composite numeric "Shared-Factor Priority
  Score" that adds/weights these associations into one number. No such
  composite exists in the literature reviewed for this platform, and
  assigning weights ourselves — even with good intentions — would be
  inventing coefficients, which this Day-2 correction explicitly forbids.
- **What CAN be built, if desired, later:** a purely qualitative, non-scored
  view — e.g. a table or diagram showing which documented associations touch
  which domains (the earlier "Factor × Domain" table already sketched in the
  original master prompt) — with every cell traceable to a specific citation,
  and no aggregation into a single score. If this is ever built, every
  instance of it in the UI must carry a visible label such as "exploratory,
  not a validated score" — this is a hard requirement, not a suggestion.

---

## Version 1 Evidence Freeze

This is the authoritative, frozen list for Version 1. Nothing outside this
list may be implemented as a live, user-facing calculation without a new
verification entry being added to this document first.

### Approved for implementation in Version 1

| Feature | Label | Basis |
|---|---|---|
| Type 2 diabetes screening | VALIDATED SCREENING INSTRUMENT | FINDRISC (Lindström & Tuomilehto 2003) — point values re-verified against the primary paper before coding, absolute risk % shown only with an explicit "Finnish-cohort-derived, not calibrated to you" caveat |
| Depression-related well-being screening | VALIDATED SCREENING INSTRUMENT | PHQ-9 (Kroenke, Spitzer, Williams 2001), full item set and scoring, with the safety-response pathway for item 9 built and tested first |
| BMI classification (standard + Asian action points) | CLASSIFICATION/ASSESSMENT | WHO 2004 Expert Consultation |
| Waist circumference classification | CLASSIFICATION/ASSESSMENT | WHO/IDF central-obesity thresholds, aligned with FINDRISC's own thresholds |
| Waist-to-height ratio (0.5 boundary) | CLASSIFICATION/ASSESSMENT | Ashwell & Gibson 2014 |
| Partial, self-reportable EOSS-inspired staging | CLASSIFICATION/ASSESSMENT | Sharma & Kushner 2009, explicitly labeled "simplified/partial, not full clinical EOSS" |
| Cardiovascular risk factors and direction of effect | EVIDENCE MAPPING | Named variables from PCE/PREVENT literature, no computed percentage |
| Gene–diet associations (FTO, MC4R, PPARG, APOE/APOA, ADRB, PLIN, FADS1, CLOCK, MTHFR) | EVIDENCE MAPPING | Barrea et al. 2020 (already logged in `LITERATURE_MAP.md`) |
| Cross-domain factor associations, shown individually with citations, no composite score | EVIDENCE MAPPING | Per-domain literature already gathered; no aggregation |

### Explicitly excluded from Version 1

| Feature | Reason |
|---|---|
| Any numeric 10-year cardiovascular risk percentage (PCE or PREVENT) | Coefficients not yet sourced from primary appendix/supplement; population-applicability gap for likely (South Asian-inclusive) users |
| Any composite "Shared-Factor Priority Score" or similar aggregated cross-domain number | No validated model exists; would require inventing weights, which is explicitly prohibited |
| Any polygenic or composite genetic risk score | No single validated, broadly-applicable score identified as appropriate for direct-to-consumer, non-clinical use |
| Full clinical Edmonton Obesity Staging System (lab-based criteria) | Requires HbA1c/lipids/clinician-diagnosed comorbidities not reliably self-reportable |
| QRISK3, QDiabetes, ADA Diabetes Risk Test | Licensing terms not yet reviewed (QRISK3), and/or population-specific/duplicative of FINDRISC without added validated value for V1 |

No code changes have been made as part of this document. Next step, when
requested, is to translate only the "Approved for implementation" table above
into `MODEL_ASSUMPTIONS.md` entries before any corresponding code is written.## FINDRISC Version Selection

The project will implement the later 0–26 point FINDRISC version, not the original 0–20 point Diabetes Risk Score published by Lindström & Tuomilehto (2003).

The selected version must have its complete scoring table verified from an authoritative source before implementation.

The following must not be conflated:
- Original 2003 Diabetes Risk Score: 0–20 points, seven variables.
- Later 0–26 FINDRISC versions: expanded/modified scoring structure, including family history.

Implementation status: NOT YET CLEARED.

No FINDRISC code will be written until the exact adopted version and all scoring categories are documented and verified.