# Literature Map

| Topic | Key paper | Finding (paraphrased) | Relevance to app | Limitation | Feature it supports |
|---|---|---|---|---|---|
| Nutrigenetics, obesity & CVD | Barrea L, Annunziata G, Bordoni L, Muscogiuri G, Colao A, Savastano S (OPERA Group). "Nutrigenetics—personalized nutrition in obesity and cardiovascular diseases." *Int J Obes Suppl.* 2020;10(1):1–13. PMCID: PMC7371677 | Obesity and cardiovascular disease arise from interacting genetic and environmental (largely dietary) factors; people on similar diets show variable CVD outcomes, which the authors attribute partly to genetic polymorphisms affecting nutrient response. The review summarizes genes with documented diet-interaction evidence in obesity/CVD, including FTO, MC4R, PPARG, APOE/APOA, ADRB, PLIN, FADS1, CLOCK, and MTHFR. | Primary seed source for the genetic-interaction layer of the Obesity and Cardiovascular modules. Confirms which gene-diet relationships have enough published attention to be worth including at "Moderate"+ evidence level rather than as placeholders. | Single review paper — summarizes primary literature but is not itself a primary study; specific effect sizes and population details need to be pulled from the primary sources it cites before going into the evidence database. | Evidence database (genes.json), Genetic interaction layer, Obesity module, Cardiovascular module |

## Notes on use
- This table only paraphrases findings — no verbatim text from the paper is
  reproduced here or elsewhere in the project, per copyright practice.
- Before promoting any gene-diet relationship from this paper into
  `evidence/relationships.json`, trace it to the primary study(ies) it cites
  and record evidence strength independently — don't inherit the review's
  framing as evidence strength.
