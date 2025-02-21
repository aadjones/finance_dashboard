import pandas as pd
import streamlit as st


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
