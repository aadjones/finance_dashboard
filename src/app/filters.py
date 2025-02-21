import datetime

import pandas as pd
import streamlit as st


def apply_date_filter(df: pd.DataFrame, start_date: datetime.date, end_date: datetime.date) -> pd.DataFrame:
    """
    Filters the DataFrame based on the provided start_date and end_date.
    Returns only rows where signup_date is within [start_date, end_date].
    """
    if start_date > end_date:
        st.warning("Start date is after end date. Adjusting filter range automatically.")
        start_date, end_date = end_date, start_date

    # Convert to pandas Timestamps for safe comparison
    mask = (df["signup_date"] >= pd.to_datetime(start_date)) & (df["signup_date"] <= pd.to_datetime(end_date))
    return df.loc[mask]


def get_filter_dates(default_start: datetime.date, default_end: datetime.date) -> tuple[datetime.date, datetime.date]:
    """
    Displays two date inputs in the Streamlit sidebar and returns the chosen start_date and end_date.
    """
    st.sidebar.subheader("Date Range Filter")
    start_date_filter = st.sidebar.date_input("Start Date", default_start)
    end_date_filter = st.sidebar.date_input("End Date", default_end)
    return start_date_filter, end_date_filter
