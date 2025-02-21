import pandas as pd
import pytest

from src.app.logic import calculate_metrics


# We'll use a small synthetic DataFrame to test metric calculations.
@pytest.fixture
def sample_df():
    # Create a simple DataFrame with fixed dates and channels.
    data = {
        "signup_date": pd.to_datetime(["2025-01-01", "2025-01-01", "2025-01-02", "2025-01-08", "2025-02-15"]),
        "channel": ["ads", "social", "ads", "referral", "ads"],
    }
    return pd.DataFrame(data)


def test_calculate_metrics(sample_df):
    # Suppose we have a marketing spend of $100
    marketing_spend = 100.0

    total_new_users, cpa, daily_counts, channel_breakdown = calculate_metrics(sample_df, marketing_spend)

    # Check total new users
    assert total_new_users == len(sample_df)

    # Check that CPA is calculated correctly (100 / number of users)
    expected_cpa = marketing_spend / len(sample_df)
    assert cpa == pytest.approx(expected_cpa)

    # Check daily counts
    # Expected: Jan 1:2, Jan 2:1, Jan 8:1, Feb 15:1
    expected_daily = {
        pd.Timestamp("2025-01-01"): 2,
        pd.Timestamp("2025-01-02"): 1,
        pd.Timestamp("2025-01-08"): 1,
        pd.Timestamp("2025-02-15"): 1,
    }
    # Convert Series to dict for comparison
    assert daily_counts.to_dict() == expected_daily

    # Check channel breakdown
    expected_breakdown = {"ads": 3, "social": 1, "referral": 1}
    assert channel_breakdown.to_dict() == expected_breakdown
