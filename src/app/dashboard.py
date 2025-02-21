import datetime

from app.filters import apply_date_filter, get_filter_dates
from app.layout import display_dashboard

# Local imports from our refactored modules
from app.logic import calculate_metrics, get_data


def main():
    # 1. Load the data and marketing spend
    df, marketing_spend = get_data()

    # 2. Apply a date range filter
    default_start = datetime.date(2025, 1, 1)
    default_end = datetime.date(2025, 3, 31)
    start_date_filter, end_date_filter = get_filter_dates(default_start, default_end)
    df_filtered = apply_date_filter(df, start_date_filter, end_date_filter)

    # 3. Calculate metrics on the filtered data
    total_new_users, cpa, daily_counts, channel_breakdown = calculate_metrics(df_filtered, marketing_spend)

    # 4. Display the final dashboard
    display_dashboard(total_new_users, cpa, daily_counts, channel_breakdown, df_filtered)


if __name__ == "__main__":
    main()
