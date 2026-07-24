import pytest

from core.research.analysis import ExploratoryAnalysis


def test_valid_exploratory_analysis_can_be_created():
    analysis = ExploratoryAnalysis(
        hypothesis_id="HYP-001",
        observed_exposure="Low physical activity",
        observed_outcome_factor="Elevated cardiometabolic risk marker",
        interpretation=(
            "The observed profile contains factors that may be relevant "
            "to cardiometabolic health."
        ),
        limitations=[
            "This analysis does not establish causation.",
            "This analysis is not a clinical diagnosis.",
            "Individual outcomes may vary."
        ]
    )

    assert analysis.hypothesis_id == "HYP-001"
    assert analysis.observed_exposure == "Low physical activity"
    assert analysis.is_non_predictive() is True


def test_analysis_is_not_a_clinical_prediction():
    analysis = ExploratoryAnalysis(
        hypothesis_id="HYP-002",
        observed_exposure="Short sleep duration",
        observed_outcome_factor="Poor metabolic health indicator",
        interpretation="The factors may be relevant to metabolic health.",
        limitations=["This is an exploratory interpretation."]
    )

    assert analysis.is_non_predictive() is True


def test_empty_hypothesis_id_is_rejected():
    with pytest.raises(ValueError):
        ExploratoryAnalysis(
            hypothesis_id="",
            observed_exposure="Low physical activity",
            observed_outcome_factor="Metabolic marker",
            interpretation="Exploratory interpretation.",
            limitations=["Not diagnostic."]
        )


def test_empty_exposure_is_rejected():
    with pytest.raises(ValueError):
        ExploratoryAnalysis(
            hypothesis_id="HYP-001",
            observed_exposure="",
            observed_outcome_factor="Metabolic marker",
            interpretation="Exploratory interpretation.",
            limitations=["Not diagnostic."]
        )


def test_empty_outcome_factor_is_rejected():
    with pytest.raises(ValueError):
        ExploratoryAnalysis(
            hypothesis_id="HYP-001",
            observed_exposure="Low physical activity",
            observed_outcome_factor="",
            interpretation="Exploratory interpretation.",
            limitations=["Not diagnostic."]
        )


def test_empty_interpretation_is_rejected():
    with pytest.raises(ValueError):
        ExploratoryAnalysis(
            hypothesis_id="HYP-001",
            observed_exposure="Low physical activity",
            observed_outcome_factor="Metabolic marker",
            interpretation="",
            limitations=["Not diagnostic."]
        )


def test_empty_limitations_are_rejected():
    with pytest.raises(ValueError):
        ExploratoryAnalysis(
            hypothesis_id="HYP-001",
            observed_exposure="Low physical activity",
            observed_outcome_factor="Metabolic marker",
            interpretation="Exploratory interpretation.",
            limitations=[]
        )