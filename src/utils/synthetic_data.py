# src/utils/synthetic_data.py

import datetime
import random

import pandas as pd

# Define a list of possible acquisition channels
CHANNELS = ["ads", "social", "referral", "organic", "email"]


def generate_random_date(start_date: datetime.date, end_date: datetime.date) -> datetime.date:
    """
    Generate a random date between start_date and end_date.
    """
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)


def generate_synthetic_users(num_users: int, start_date: datetime.date, end_date: datetime.date) -> pd.DataFrame:
    """
    Generate synthetic user data as a pandas DataFrame.

    Each user has:
      - 'signup_date': a random date between start_date and end_date.
      - 'channel': a random acquisition channel.

    Args:
        num_users: Number of synthetic users to generate.
        start_date: The earliest signup date.
        end_date: The latest signup date.

    Returns:
        A pandas DataFrame with synthetic user data.
    """
    data = {
        "signup_date": [generate_random_date(start_date, end_date) for _ in range(num_users)],
        "channel": [random.choice(CHANNELS) for _ in range(num_users)],
    }

    df = pd.DataFrame(data)
    # Convert signup_date to datetime (if not already)
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    return df


if __name__ == "__main__":
    # Quick test: generate 10 synthetic users
    start = datetime.date(2025, 1, 1)
    end = datetime.date(2025, 3, 31)
    sample_df = generate_synthetic_users(10, start, end)
    print(sample_df)
