# src/business/user_acquisition.py

import pandas as pd


def create_users_dataframe(users: list) -> pd.DataFrame:
    """
    Converts a list of user dicts into a pandas DataFrame.

    Each user dict should have:
      - 'signup_date': a datetime.date or datetime.datetime object.
      - 'channel': a string indicating the acquisition channel.
    """
    df = pd.DataFrame(users)
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    return df


def count_new_users(df: pd.DataFrame, period: str = "day") -> pd.Series:
    """
    Counts new users grouped by a specified period: 'day', 'week', or 'month'.

    Returns a pandas Series with the period as index and counts as values.
    """
    df = df.copy()
    df.set_index("signup_date", inplace=True)

    if period == "day":
        counts = df.resample("D").size()
    elif period == "week":
        counts = df.resample("W").size()
    elif period == "month":
        counts = df.resample("M").size()
    else:
        raise ValueError("Period must be 'day', 'week', or 'month'.")

    return counts


def calculate_cpa(total_cost: float, new_users: int) -> float:
    """
    Calculate Cost Per Acquisition (CPA).
    """
    if new_users == 0:
        return float("inf")
    return total_cost / new_users


def acquisition_channel_breakdown(df: pd.DataFrame) -> pd.Series:
    """
    Returns a breakdown of user acquisitions by channel.
    """
    return df["channel"].value_counts()
