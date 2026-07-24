from dataclasses import dataclass
from typing import List


@dataclass
class ExploratoryAnalysis:
    """
    Represents a transparent, non-predictive analysis of an exploratory hypothesis.

    This object does not diagnose disease, calculate individual disease risk,
    or generate a clinical prediction.
    """

    hypothesis_id: str
    observed_exposure: str
    observed_outcome_factor: str
    interpretation: str
    limitations: List[str]

    def __post_init__(self):
        if not self.hypothesis_id.strip():
            raise ValueError("Hypothesis ID cannot be empty.")

        if not self.observed_exposure.strip():
            raise ValueError("Observed exposure cannot be empty.")

        if not self.observed_outcome_factor.strip():
            raise ValueError("Observed outcome factor cannot be empty.")

        if not self.interpretation.strip():
            raise ValueError("Interpretation cannot be empty.")

        if not self.limitations:
            raise ValueError("At least one limitation must be provided.")

        if any(not limitation.strip() for limitation in self.limitations):
            raise ValueError("Limitations cannot contain empty values.")

    def is_non_predictive(self) -> bool:
        """
        Confirms that this object represents exploratory analysis,
        not clinical prediction.
        """
        return True