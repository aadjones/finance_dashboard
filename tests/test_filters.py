import datetime

import pandas as pd
import pytest

from src.app.filters import apply_date_filter


@pytest.fixture
def sample_df():
    # Create a DataFrame with known signup dates.
    data = {
        "signup_date": pd.to_datetime(["2025-01-01", "2025-01-05", "2025-02-10", "2025-03-01", "2025-03-15"]),
        "channel": ["ads", "social", "ads", "referral", "email"],
    }
    return pd.DataFrame(data)


def test_apply_date_filter_within_range(sample_df):
    # Define a date range that includes some of the data.
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 2, 15)

    filtered_df = apply_date_filter(sample_df, start_date, end_date)

    # Expected to include the rows with dates 2025-01-01, 2025-01-05, 2025-02-10
    expected_dates = pd.to_datetime(["2025-01-01", "2025-01-05", "2025-02-10"])
    pd.testing.assert_series_equal(
        filtered_df["signup_date"].reset_index(drop=True), pd.Series(expected_dates), check_names=False
    )


def test_apply_date_filter_empty(sample_df):
    # Define a date range that excludes all dates.
    start_date = datetime.date(2026, 1, 1)
    end_date = datetime.date(2026, 12, 31)

    filtered_df = apply_date_filter(sample_df, start_date, end_date)
    assert filtered_df.empty
