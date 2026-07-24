from dataclasses import dataclass
from typing import Optional


@dataclass
class FINDRISCInput:
    """
    Inputs for the later expanded 0–26 point FINDRISC structure.

    This instrument is a screening tool.
    It is not a diagnosis and does not independently establish
    diabetes status.
    """

    age: int
    bmi: float
    waist_circumference_cm: float
    physical_activity: bool
    daily_fruit_vegetable_intake: bool
    antihypertensive_medication: bool
    history_of_elevated_blood_glucose: bool
    family_history_of_diabetes: bool


@dataclass
class FINDRISCResult:
    score: int
    category: str


def calculate_findrisc_score(inputs: FINDRISCInput) -> int:
    """
    Calculate the 0–26 point FINDRISC score.

    Point values follow the adopted expanded FINDRISC structure.
    No coefficients are reconstructed or recalibrated.
    """

    score = 0

    # Age
    if inputs.age < 45:
        score += 0
    elif inputs.age < 55:
        score += 2
    elif inputs.age < 65:
        score += 3
    else:
        score += 4

    # BMI
    if inputs.bmi < 25:
        score += 0
    elif inputs.bmi < 30:
        score += 1
    else:
        score += 3

    # Waist circumference
    if inputs.waist_circumference_cm < 80:
        score += 0
    elif inputs.waist_circumference_cm < 88:
        score += 3
    else:
        score += 4

    # Physical activity
    if not inputs.physical_activity:
        score += 2

    # Daily fruit and vegetable intake
    if not inputs.daily_fruit_vegetable_intake:
        score += 1

    # Antihypertensive medication
    if inputs.antihypertensive_medication:
        score += 2

    # History of elevated blood glucose
    if inputs.history_of_elevated_blood_glucose:
        score += 5

    # Family history of diabetes
    if inputs.family_history_of_diabetes:
        score += 5

    return score


def classify_findrisc_score(score: int) -> str:
    """
    Categorize the total FINDRISC score.

    Category labels are screening categories, not diagnoses.
    """

    if score < 7:
        return "Low"
    elif score < 12:
        return "Slightly elevated"
    elif score < 15:
        return "Moderate"
    elif score < 21:
        return "High"
    else:
        return "Very high"


def assess_findrisc(inputs: FINDRISCInput) -> FINDRISCResult:
    """
    Calculate and classify a FINDRISC screening score.
    """

    score = calculate_findrisc_score(inputs)

    return FINDRISCResult(
        score=score,
        category=classify_findrisc_score(score),
    )