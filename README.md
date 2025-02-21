# Finance Dashboard

A Streamlit-based dashboard for exploring financial and business model metrics using synthetic data. This project is designed as an analysis tool that computes key metrics—such as user acquisition, cost per acquisition (CPA), and channel breakdowns—while allowing you to interactively filter data by date range and adjust parameters like marketing spend.

## Features

- **Synthetic Data Generation:** Generates random user data with configurable parameters.
- **User Acquisition Metrics:** Calculates total new users, daily sign-ups, and CPA.
- **Channel Breakdown:** Visualizes user acquisition channels.
- **Interactive Filtering:** Use date range filters and sliders to customize the view.
- **Modular Design:** Clean separation between data logic, filtering, and layout.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/finance_dashboard.git
   cd finance_dashboard
   ```

2. **Install dependencies:**

   ```bash
   make setup
   ```

3. **Activate the virtual environment:**

   ```bash
   source env/bin/activate  # On Windows use: .\env\Scripts\activate
   ```

4. **Run the app:**

   ```bash
   make run
   ```

## License

This project is licensed under the MIT License.
