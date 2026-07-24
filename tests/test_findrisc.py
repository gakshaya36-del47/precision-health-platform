import pytest

from core.instruments.findrisc import (
    FINDRISCInput,
    assess_findrisc,
    calculate_findrisc_score,
    classify_findrisc_score,
)


def test_low_risk_profile_scores_zero():
    inputs = FINDRISCInput(
        age=40,
        bmi=24,
        waist_circumference_cm=79,
        physical_activity=True,
        daily_fruit_vegetable_intake=True,
        antihypertensive_medication=False,
        history_of_elevated_blood_glucose=False,
        family_history_of_diabetes=False,
    )

    assert calculate_findrisc_score(inputs) == 0


def test_highest_possible_score_is_26():
    inputs = FINDRISCInput(
        age=70,
        bmi=32,
        waist_circumference_cm=100,
        physical_activity=False,
        daily_fruit_vegetable_intake=False,
        antihypertensive_medication=True,
        history_of_elevated_blood_glucose=True,
        family_history_of_diabetes=True,
    )

    assert calculate_findrisc_score(inputs) == 26


def test_score_categories():
    assert classify_findrisc_score(0) == "Low"
    assert classify_findrisc_score(7) == "Slightly elevated"
    assert classify_findrisc_score(12) == "Moderate"
    assert classify_findrisc_score(15) == "High"
    assert classify_findrisc_score(21) == "Very high"


def test_complete_assessment_returns_score_and_category():
    inputs = FINDRISCInput(
        age=60,
        bmi=28,
        waist_circumference_cm=90,
        physical_activity=False,
        daily_fruit_vegetable_intake=False,
        antihypertensive_medication=True,
        history_of_elevated_blood_glucose=False,
        family_history_of_diabetes=True,
    )

    result = assess_findrisc(inputs)

    assert result.score == 18
    assert result.category == "High"