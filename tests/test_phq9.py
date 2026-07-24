import pytest

from core.instruments.phq9 import (
    assess_phq9,
    validate_phq9_items,
)


def test_zero_score_is_minimal():
    assessment = assess_phq9([0, 0, 0, 0, 0, 0, 0, 0, 0])

    assert assessment.total_score == 0
    assert assessment.severity_category == "minimal"
    assert assessment.item_9_positive is False


def test_maximum_score_is_27():
    assessment = assess_phq9([3, 3, 3, 3, 3, 3, 3, 3, 3])

    assert assessment.total_score == 27
    assert assessment.severity_category == "severe"
    assert assessment.item_9_positive is True


def test_item_9_positive_is_flagged_separately():
    assessment = assess_phq9([0, 0, 0, 0, 0, 0, 0, 0, 1])

    assert assessment.total_score == 1
    assert assessment.item_9_positive is True


def test_item_9_zero_is_not_flagged():
    assessment = assess_phq9([0, 0, 0, 0, 0, 0, 0, 0, 0])

    assert assessment.item_9_positive is False


def test_invalid_number_of_items_is_rejected():
    errors = validate_phq9_items([0, 1, 2])

    assert errors


def test_item_scores_outside_valid_range_are_rejected():
    errors = validate_phq9_items([0, 0, 0, 0, 0, 0, 0, 0, 4])

    assert errors


def test_invalid_scores_raise_value_error():
    with pytest.raises(ValueError):
        assess_phq9([0, 0, 0, 0, 0, 0, 0, 0, 4])