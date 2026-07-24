from dataclasses import dataclass
from typing import Optional


@dataclass
class BMIResult:
    """
    Result of BMI calculation and classification.

    BMI is an anthropometric classification measure.
    It is not a diagnosis or an individual disease-risk prediction.
    """

    value: float
    classification: str
    population_context: str


@dataclass
class WaistToHeightResult:
    """
    Result of waist-to-height ratio calculation.

    The ratio is an anthropometric assessment measure.
    """

    value: float
    classification: str


def calculate_bmi(
    weight_kg: float,
    height_cm: float,
) -> float:
    """
    Calculate body mass index.

    BMI = weight (kg) / height (m)^2

    Parameters
    ----------
    weight_kg:
        Body weight in kilograms.

    height_cm:
        Height in centimetres.

    Returns
    -------
    float
        BMI rounded to two decimal places.
    """

    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")

    if height_cm <= 0:
        raise ValueError("Height must be greater than zero.")

    height_m = height_cm / 100

    return round(weight_kg / (height_m ** 2), 2)


def classify_bmi_standard(bmi: float) -> str:
    """
    Classify BMI using standard adult BMI categories.

    These categories are classifications, not diagnoses.
    """

    if bmi < 18.5:
        return "underweight"

    if bmi < 25:
        return "healthy_range"

    if bmi < 30:
        return "overweight"

    return "obesity"


def classify_bmi_asian_action_point(
    bmi: float,
) -> str:
    """
    Classify BMI using Asian population action points.

    These thresholds are provided as population-contextual
    assessment categories and should not be interpreted as
    universal diagnostic thresholds.
    """

    if bmi < 18.5:
        return "underweight"

    if bmi < 23:
        return "lower_risk_range"

    if bmi < 27.5:
        return "increased_risk_action_point"

    return "high_risk_action_point"


def calculate_waist_to_height_ratio(
    waist_cm: float,
    height_cm: float,
) -> float:
    """
    Calculate waist-to-height ratio.

    Ratio = waist circumference / height

    Both measurements must use the same unit.
    """

    if waist_cm <= 0:
        raise ValueError("Waist circumference must be greater than zero.")

    if height_cm <= 0:
        raise ValueError("Height must be greater than zero.")

    return round(waist_cm / height_cm, 2)


def classify_waist_to_height_ratio(
    ratio: float,
) -> str:
    """
    Classify waist-to-height ratio using a 0.5 boundary.

    This is an anthropometric assessment classification.
    It is not a diagnosis or a prediction of future disease.
    """

    if ratio < 0.5:
        return "below_0.5_boundary"

    return "at_or_above_0.5_boundary"