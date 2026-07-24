from dataclasses import dataclass
from typing import List


PHQ9_ITEM_COUNT = 9
MIN_ITEM_SCORE = 0
MAX_ITEM_SCORE = 3
MAX_TOTAL_SCORE = 27


@dataclass
class PHQ9Assessment:
    """
    PHQ-9 screening assessment.

    This is a symptom-screening instrument.
    It does not diagnose depression or predict imminent risk.

    Item 9 is represented separately as a safety-response flag.
    """

    item_scores: List[int]

    @property
    def total_score(self) -> int:
        return sum(self.item_scores)

    @property
    def item_9_positive(self) -> bool:
        return self.item_scores[8] > 0

    @property
    def severity_category(self) -> str:
        score = self.total_score

        if score <= 4:
            return "minimal"
        elif score <= 9:
            return "mild"
        elif score <= 14:
            return "moderate"
        elif score <= 19:
            return "moderately_severe"
        else:
            return "severe"


def validate_phq9_items(item_scores: List[int]) -> List[str]:
    """
    Validate the nine PHQ-9 item scores.

    Each item must be scored from 0 to 3.
    """

    errors: List[str] = []

    if len(item_scores) != PHQ9_ITEM_COUNT:
        errors.append("PHQ-9 requires exactly 9 item scores.")
        return errors

    for index, score in enumerate(item_scores, start=1):
        if not isinstance(score, int):
            errors.append(
                f"PHQ-9 item {index} score must be an integer."
            )
        elif score < MIN_ITEM_SCORE or score > MAX_ITEM_SCORE:
            errors.append(
                f"PHQ-9 item {index} score must be between 0 and 3."
            )

    return errors


def assess_phq9(item_scores: List[int]) -> PHQ9Assessment:
    """
    Create a PHQ-9 assessment after validating the item scores.

    Raises:
        ValueError: if the item scores are invalid.
    """

    errors = validate_phq9_items(item_scores)

    if errors:
        raise ValueError("; ".join(errors))

    return PHQ9Assessment(item_scores=item_scores)