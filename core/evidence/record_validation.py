from typing import Any, Dict, List


REQUIRED_FIELDS = {
    "id",
    "factor",
    "biological_domain",
    "outcome",
    "evidence_type",
    "direction",
    "population_context",
    "evidence_strength",
    "source",
    "interpretation",
    "status",
}


FORBIDDEN_PREDICTIVE_FIELDS = {
    "risk_score",
    "predicted_probability",
    "individual_risk",
    "composite_score",
}


def validate_evidence_record(record: Dict[str, Any]) -> List[str]:
    """
    Validate the structure of an evidence-mapping record.

    This validates metadata structure only.
    It does not validate the scientific truth of the evidence itself.
    """

    errors: List[str] = []

    missing_fields = REQUIRED_FIELDS - set(record.keys())

    for field in sorted(missing_fields):
        errors.append(f"Missing required field: {field}")

    forbidden_fields = FORBIDDEN_PREDICTIVE_FIELDS.intersection(record.keys())

    for field in sorted(forbidden_fields):
        errors.append(
            f"Evidence records must not contain predictive field: {field}"
        )

    if "source" in record and not isinstance(record["source"], dict):
        errors.append("Source must be a structured object.")

    if "status" in record:
        allowed_statuses = {
            "evidence_record_template",
            "verified_evidence_record",
        }

        if record["status"] not in allowed_statuses:
            errors.append("Invalid evidence record status.")

    return errors