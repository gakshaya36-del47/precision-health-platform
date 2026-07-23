from typing import List

from .profile import UserProfile


def validate_user_profile(profile: UserProfile) -> List[str]:
    """
    Validate basic input plausibility.

    Returns a list of validation errors.
    An empty list means no basic validation errors were found.

    This is input validation only.
    It is not clinical validation and does not diagnose disease.
    """

    errors: List[str] = []

    if profile.age is not None:
        if not isinstance(profile.age, int):
            errors.append("Age must be an integer.")
        elif profile.age < 18 or profile.age > 120:
            errors.append("Age must be between 18 and 120 years.")

    if profile.sex is not None:
        allowed_values = {"female", "male", "intersex", "prefer_not_to_say"}
        if profile.sex not in allowed_values:
            errors.append(
                "Sex must be one of: female, male, intersex, "
                "prefer_not_to_say."
            )

    if profile.anthropometrics is not None:
        anthropometrics = profile.anthropometrics

        if anthropometrics.height is not None:
            if anthropometrics.height <= 0:
                errors.append("Height must be greater than zero.")

        if anthropometrics.weight is not None:
            if anthropometrics.weight <= 0:
                errors.append("Weight must be greater than zero.")

        if anthropometrics.waist_circumference is not None:
            if anthropometrics.waist_circumference <= 0:
                errors.append(
                    "Waist circumference must be greater than zero."
                )

    if profile.lifestyle is not None:
        lifestyle = profile.lifestyle

        if lifestyle.sleep_duration_hours is not None:
            if (
                lifestyle.sleep_duration_hours < 0
                or lifestyle.sleep_duration_hours > 24
            ):
                errors.append(
                    "Sleep duration must be between 0 and 24 hours."
                )

    return errors