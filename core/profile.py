from dataclasses import dataclass
from typing import Optional


@dataclass
class Anthropometrics:
    """
    Self-reported or measured body measurements.

    These values are stored as inputs only.
    No disease risk or diagnosis is calculated here.
    """

    height: Optional[float] = None
    height_unit: Optional[str] = None

    weight: Optional[float] = None
    weight_unit: Optional[str] = None

    waist_circumference: Optional[float] = None
    waist_unit: Optional[str] = None


@dataclass
class LifestyleProfile:
    """
    Lifestyle and behavioural context.

    These fields are stored for future evidence mapping
    or validated instruments. They do not independently
    produce a disease-risk score.
    """

    physical_activity_frequency: Optional[str] = None
    dietary_pattern: Optional[str] = None
    smoking_status: Optional[str] = None
    alcohol_status: Optional[str] = None
    sleep_duration_hours: Optional[float] = None
    perceived_stress: Optional[str] = None


@dataclass
class FamilyHistory:
    """
    Self-reported family-history context.
    """

    diabetes: Optional[str] = None
    cardiovascular_disease: Optional[str] = None


@dataclass
class ClinicalContext:
    """
    Limited clinical/contextual information.

    These fields are stored for future validated instruments.
    They do not independently produce a diagnosis or risk score.
    """

    blood_pressure_medication: Optional[str] = None
    history_of_elevated_blood_glucose: Optional[str] = None


@dataclass
class UserProfile:
    """
    Structured user profile for the research prototype.

    This class stores validated input data only.
    It does not diagnose disease, calculate composite risk,
    or generate unsupported predictive scores.
    """

    age: Optional[int] = None
    sex: Optional[str] = None
    country_or_region: Optional[str] = None

    anthropometrics: Optional[Anthropometrics] = None
    lifestyle: Optional[LifestyleProfile] = None
    family_history: Optional[FamilyHistory] = None
    clinical_context: Optional[ClinicalContext] = None