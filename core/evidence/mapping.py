from dataclasses import dataclass
from typing import Optional


@dataclass
class EvidenceMapping:
    """
    Structured representation of an evidence relationship.

    This object records an evidence association only.
    It does not calculate disease risk, probability, or a composite score.
    """

    factor: str
    biological_domain: str
    outcome: str

    evidence_type: str
    direction: str

    source: str
    population_context: Optional[str] = None
    evidence_strength: Optional[str] = None

    notes: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.factor.strip():
            raise ValueError("Factor cannot be empty.")

        if not self.biological_domain.strip():
            raise ValueError("Biological domain cannot be empty.")

        if not self.outcome.strip():
            raise ValueError("Outcome cannot be empty.")

        if not self.evidence_type.strip():
            raise ValueError("Evidence type cannot be empty.")

        if not self.direction.strip():
            raise ValueError("Direction cannot be empty.")

        if not self.source.strip():
            raise ValueError("Source cannot be empty.")

    def is_predictive_score(self) -> bool:
        """
        Evidence mappings are not predictive scores.
        """
        return False

    def has_numeric_risk_output(self) -> bool:
        """
        Evidence mappings do not generate numerical risk outputs.
        """
        return False