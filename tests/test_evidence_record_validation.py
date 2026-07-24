import json
from pathlib import Path

from core.evidence.record_validation import validate_evidence_record


RECORD_PATH = (
    Path(__file__).parents[1]
    / "evidence"
    / "records"
    / "example_metabolic_association.json"
)


def load_record():
    with RECORD_PATH.open() as file:
        return json.load(file)


def test_verified_evidence_record_has_no_validation_errors():
    record = load_record()

    errors = validate_evidence_record(record)

    assert errors == []


def test_missing_required_field_is_rejected():
    record = load_record()
    record.pop("source")

    errors = validate_evidence_record(record)

    assert "Missing required field: source" in errors


def test_predictive_fields_are_rejected():
    record = load_record()
    record["risk_score"] = 12

    errors = validate_evidence_record(record)

    assert (
        "Evidence records must not contain predictive field: risk_score"
        in errors
    )


def test_invalid_status_is_rejected():
    record = load_record()
    record["status"] = "predictive_model"

    errors = validate_evidence_record(record)

    assert "Invalid evidence record status." in errors