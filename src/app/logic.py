import datetime

import pandas as pd
import streamlit as st

from business.user_acquisition import (
    acquisition_channel_breakdown,
    calculate_cpa,
    count_new_users,
)
from utils.synthetic_data import generate_synthetic_users


@st.cache_data
def load_synthetic_data(num_users: int, start_date: datetime.date, end_date: datetime.date) -> pd.DataFrame:
    """
    Load synthetic user data as a pandas DataFrame.
    Cached so data remains constant during a session unless inputs change.
    """
    return generate_synthetic_users(num_users, start_date, end_date)


def get_data() -> tuple[pd.DataFrame, float]:
    """
    Gets synthetic data and marketing spend from sidebar inputs.
    Uses st.session_state to store data across interactions.
    """
    st.sidebar.header("Dashboard Settings")
    marketing_spend = st.sidebar.slider(
        "Total Marketing Spend for Entire Period ($)", min_value=0.0, max_value=1000.0, value=100.0, step=10.0
    )
    num_users = st.sidebar.slider("Number of Synthetic Users", min_value=10, max_value=500, value=100)

    # Define a fixed generation range for synthetic data
    generation_start = datetime.date(2025, 1, 1)
    generation_end = datetime.date(2025, 3, 31)

    # Generate/cached data
    if "df" not in st.session_state or st.session_state.get("num_users") != num_users:
        st.session_state.df = load_synthetic_data(num_users, generation_start, generation_end)
        st.session_state.num_users = num_users

    return st.session_state.df, marketing_spend


def calculate_metrics(df: pd.DataFrame, marketing_spend: float) -> tuple:
    """
    Calculate key metrics from the data.
    """
    total_new_users = len(df)
    cpa = calculate_cpa(marketing_spend, total_new_users)
    daily_counts = count_new_users(df, period="day")
    channel_breakdown = acquisition_channel_breakdown(df)
    return total_new_users, cpa, daily_counts, channel_breakdown
