# tests/test_synthetic_data.py

import datetime

import pandas as pd

from src.utils.synthetic_data import generate_synthetic_users


def test_generate_synthetic_users_count():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 3, 31)
    num_users = 50
    df = generate_synthetic_users(num_users, start_date, end_date)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == num_users


def test_generate_synthetic_users_date_range():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 3, 31)
    df = generate_synthetic_users(20, start_date, end_date)
    # Ensure all signup dates are within the provided range.
    assert df["signup_date"].min().date() >= start_date
    assert df["signup_date"].max().date() <= end_date


def test_generate_synthetic_users_channels():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 3, 31)
    df = generate_synthetic_users(20, start_date, end_date)
    allowed_channels = {"ads", "social", "referral", "organic", "email"}
    assert set(df["channel"]).issubset(allowed_channels)
