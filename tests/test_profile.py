from core.profile import (
    Anthropometrics,
    FamilyHistory,
    LifestyleProfile,
    UserProfile,
)
from core.validation import validate_user_profile


def test_valid_user_profile_has_no_validation_errors():
    profile = UserProfile(
        age=25,
        sex="female",
        country_or_region="India",
        anthropometrics=Anthropometrics(
            height=165,
            height_unit="cm",
            weight=60,
            weight_unit="kg",
            waist_circumference=75,
            waist_unit="cm",
        ),
        lifestyle=LifestyleProfile(
            physical_activity_frequency="regular",
            dietary_pattern="mixed",
            sleep_duration_hours=7,
            perceived_stress="moderate",
        ),
        family_history=FamilyHistory(
            diabetes="no",
            cardiovascular_disease="no",
        ),
    )

    errors = validate_user_profile(profile)

    assert errors == []


def test_invalid_age_is_rejected():
    profile = UserProfile(age=150)

    errors = validate_user_profile(profile)

    assert "Age must be between 18 and 120 years." in errors


def test_negative_weight_is_rejected():
    profile = UserProfile(
        anthropometrics=Anthropometrics(weight=-5)
    )

    errors = validate_user_profile(profile)

    assert "Weight must be greater than zero." in errors


def test_invalid_sleep_duration_is_rejected():
    profile = UserProfile(
        lifestyle=LifestyleProfile(sleep_duration_hours=30)
    )

    errors = validate_user_profile(profile)

    assert "Sleep duration must be between 0 and 24 hours." in errors