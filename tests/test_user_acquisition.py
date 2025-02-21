# tests/test_user_acquisition.py

import datetime

import pytest

from src.business.user_acquisition import (
    acquisition_channel_breakdown,
    calculate_cpa,
    count_new_users,
    create_users_dataframe,
)

# Sample data: list of user dicts
SAMPLE_USERS = [
    {"signup_date": datetime.date(2025, 1, 1), "channel": "ads"},
    {"signup_date": datetime.date(2025, 1, 1), "channel": "social"},
    {"signup_date": datetime.date(2025, 1, 2), "channel": "ads"},
    {"signup_date": datetime.date(2025, 1, 8), "channel": "referral"},
    {"signup_date": datetime.date(2025, 2, 15), "channel": "ads"},
]


@pytest.fixture
def users_df():
    return create_users_dataframe(SAMPLE_USERS)


def test_count_new_users_day(users_df):
    counts = count_new_users(users_df, period="day")
    # Check that the count for Jan 1, 2025 is 2, Jan 2 is 1, etc.
    assert counts.loc["2025-01-01"] == 2
    assert counts.loc["2025-01-02"] == 1


def test_calculate_cpa():
    cpa = calculate_cpa(100, 5)
    assert cpa == 20

    cpa = calculate_cpa(100, 0)
    assert cpa == float("inf")


def test_acquisition_channel_breakdown(users_df):
    breakdown = acquisition_channel_breakdown(users_df)
    expected = {"ads": 3, "social": 1, "referral": 1}
    for channel, count in expected.items():
        assert breakdown[channel] == count
