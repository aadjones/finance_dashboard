# src/app/dashboard.py

import datetime

import pandas as pd
import streamlit as st

from business.user_acquisition import (
    acquisition_channel_breakdown,
    calculate_cpa,
    count_new_users,
)
from utils.synthetic_data import generate_synthetic_users


# -----------------------------------------------------------------------------
# Data Loading with Caching
# -----------------------------------------------------------------------------
@st.cache_data
def load_synthetic_data(num_users: int, start_date: datetime.date, end_date: datetime.date) -> pd.DataFrame:
    """
    Load synthetic user data as a pandas DataFrame.
    This function is cached so that the data remains constant during a session
    unless its input parameters change.
    """
    return generate_synthetic_users(num_users, start_date, end_date)


def get_data() -> tuple[pd.DataFrame, float]:
    """
    Gets the synthetic data and marketing spend from sidebar inputs.
    Uses st.session_state to store the data across interactions.
    """
    # Sidebar settings
    st.sidebar.header("Dashboard Settings")
    marketing_spend = st.sidebar.slider(
        "Total Marketing Spend",
        min_value=0.0,
        max_value=1000.0,
        value=100.0,
        step=10.0,
    )

    num_users = st.sidebar.slider("Number of Synthetic Users", min_value=10, max_value=500, value=100)

    # Define a fixed date range for the session
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 3, 31)

    # Load and cache synthetic data if not already present or if num_users changed
    if "df" not in st.session_state or st.session_state.get("num_users") != num_users:
        st.session_state.df = load_synthetic_data(num_users, start_date, end_date)
        st.session_state.num_users = num_users

    return st.session_state.df, marketing_spend


# -----------------------------------------------------------------------------
# Metric Calculations
# -----------------------------------------------------------------------------
def calculate_metrics(df: pd.DataFrame, marketing_spend: float) -> tuple:
    """
    Calculate key metrics from the data.
    """
    total_new_users = len(df)
    cpa = calculate_cpa(marketing_spend, total_new_users)
    daily_counts = count_new_users(df, period="day")
    channel_breakdown = acquisition_channel_breakdown(df)
    return total_new_users, cpa, daily_counts, channel_breakdown


# -----------------------------------------------------------------------------
# Dashboard Layout
# -----------------------------------------------------------------------------
def display_dashboard(
    total_new_users: int, cpa: float, daily_counts: pd.Series, channel_breakdown: dict, df: pd.DataFrame
):
    """
    Display the dashboard metrics and visualizations.
    """
    st.title("Business Model Dashboard")
    st.write("## User Acquisition Metrics")
    st.write(f"**Total New Users:** {total_new_users}")
    st.write(f"**Cost Per Acquisition (CPA):** ${cpa:.2f}")

    st.write("### New Users by Day")
    st.line_chart(daily_counts)

    st.write("### Acquisition Channels Breakdown")
    st.bar_chart(pd.Series(channel_breakdown))

    st.write("### Raw Synthetic Data")
    st.dataframe(df)


# -----------------------------------------------------------------------------
# Main Execution Flow
# -----------------------------------------------------------------------------
def main():
    df, marketing_spend = get_data()
    total_new_users, cpa, daily_counts, channel_breakdown = calculate_metrics(df, marketing_spend)
    display_dashboard(total_new_users, cpa, daily_counts, channel_breakdown, df)


if __name__ == "__main__":
    main()
