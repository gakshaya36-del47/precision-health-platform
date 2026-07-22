# Evidence Database Schema

Planned structure for `evidence/*.json` (not yet populated beyond this schema).

## genes.json
```json
{
  "gene_id": "FTO",
  "full_name": "Fat mass and obesity-associated gene",
  "susceptibility_or_response": "susceptibility",
  "notes": "Common variant studied for obesity-risk interaction with diet; not deterministic."
}
```

## nutrients.json
```json
{
  "nutrient_id": "saturated_fat",
  "category": "macronutrient",
  "notes": "..."
}
```

## disease_domains.json
```json
{
  "domain_id": "obesity",
  "display_name": "Obesity and metabolic health",
  "output_language": ["profile", "risk indicator", "modifiable priority"],
  "disallowed_language": ["diagnosis", "guaranteed outcome"]
}
```

## relationships.json
```json
{
  "relationship_id": "FTO_satfat_obesity_001",
  "gene": "FTO",
  "nutrient_or_exposure": "saturated_fat",
  "domain": "obesity",
  "biological_pathway": "appetite regulation / energy homeostasis (hypothalamic signaling)",
  "outcome": "altered weight-gain response to high-saturated-fat diet",
  "evidence_strength": "Moderate",
  "population": "primarily European-ancestry cohorts",
  "study_type": "review-cited association studies",
  "source": "Barrea et al. 2020, Int J Obes Suppl, PMC7371677",
  "limitations": "Effect sizes and population generalizability need to be verified against primary studies before being surfaced with a numeric weight."
}
```

## evidence_levels.json
```json
{
  "levels": [
    "High evidence",
    "Moderate evidence",
    "Limited evidence",
    "Emerging evidence",
    "Research-only"
  ],
  "definitions": {
    "High evidence": "Multiple independent studies, ideally meta-analyzed, consistent direction of effect.",
    "Moderate evidence": "Several studies with generally consistent findings, some heterogeneity.",
    "Limited evidence": "Few studies or mixed findings.",
    "Emerging evidence": "Early-stage research, small samples, not yet replicated.",
    "Research-only": "Included for completeness/education; not yet sufficiently evidenced for any user-facing weighting."
  }
}
```

## Rules
- Every relationship record must cite a real source — placeholders must be
  explicitly labeled `"source": "PLACEHOLDER - not yet sourced"`, never a
  fabricated citation.
- No relationship implies genetic determinism; `outcome` fields describe
  differential response, not fixed fate.
