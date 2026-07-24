import pytest

from core.classification.anthropometrics import (
    calculate_bmi,
    calculate_waist_to_height_ratio,
    classify_bmi_asian_action_point,
    classify_bmi_standard,
    classify_waist_to_height_ratio,
)


def test_bmi_calculation():
    bmi = calculate_bmi(
        weight_kg=60,
        height_cm=165,
    )

    assert bmi == 22.04


def test_standard_bmi_classification():
    assert classify_bmi_standard(22.0) == "healthy_range"
    assert classify_bmi_standard(27.0) == "overweight"
    assert classify_bmi_standard(32.0) == "obesity"


def test_asian_bmi_action_point_classification():
    assert classify_bmi_asian_action_point(22.0) == "lower_risk_range"
    assert (
        classify_bmi_asian_action_point(24.0)
        == "increased_risk_action_point"
    )
    assert (
        classify_bmi_asian_action_point(28.0)
        == "high_risk_action_point"
    )


def test_waist_to_height_ratio():
    ratio = calculate_waist_to_height_ratio(
        waist_cm=75,
        height_cm=165,
    )

    assert ratio == 0.45


def test_waist_to_height_classification():
    assert (
        classify_waist_to_height_ratio(0.45)
        == "below_0.5_boundary"
    )

    assert (
        classify_waist_to_height_ratio(0.50)
        == "at_or_above_0.5_boundary"
    )


def test_invalid_measurements_are_rejected():
    with pytest.raises(ValueError):
        calculate_bmi(
            weight_kg=-60,
            height_cm=165,
        )

    with pytest.raises(ValueError):
        calculate_waist_to_height_ratio(
            waist_cm=75,
            height_cm=0,
        )