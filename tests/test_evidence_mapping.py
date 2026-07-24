import pytest

from core.evidence.mapping import EvidenceMapping


def test_valid_evidence_mapping_can_be_created():
    mapping = EvidenceMapping(
        factor="Physical inactivity",
        biological_domain="Metabolic health",
        outcome="Type 2 diabetes",
        evidence_type="Observational association",
        direction="Higher exposure associated with higher outcome risk",
        source="Example primary study",
        population_context="Adult population",
        evidence_strength="Moderate",
    )

    assert mapping.factor == "Physical inactivity"
    assert mapping.outcome == "Type 2 diabetes"


def test_evidence_mapping_is_not_a_predictive_score():
    mapping = EvidenceMapping(
        factor="Dietary pattern",
        biological_domain="Metabolic health",
        outcome="Type 2 diabetes",
        evidence_type="Systematic review",
        direction="Association",
        source="Example review",
    )

    assert mapping.is_predictive_score() is False
    assert mapping.has_numeric_risk_output() is False


def test_empty_factor_is_rejected():
    with pytest.raises(ValueError):
        EvidenceMapping(
            factor="",
            biological_domain="Metabolic health",
            outcome="Type 2 diabetes",
            evidence_type="Review",
            direction="Association",
            source="Example source",
        )


def test_empty_source_is_rejected():
    with pytest.raises(ValueError):
        EvidenceMapping(
            factor="Physical inactivity",
            biological_domain="Metabolic health",
            outcome="Type 2 diabetes",
            evidence_type="Review",
            direction="Association",
            source="",
        )