#!/usr/bin/env python3

import os
import sys
import pandas as pd

def generate_summary(portfolio_file):
    """Reads the portfolio CSV and prints a simplified summary to the console."""

    if not os.path.exists(portfolio_file):
        print(f"Error: Portfolio file '{portfolio_file}' not found. Run the update step first.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)

    if df.empty:
        print("Portfolio is empty. Nothing to summarize.")
        return

    # Summary Calculations
    total_portfolio_value = df['card_market_value'].sum()

    # Most Valuable Card (based on per-card market value)
    most_valuable_card = df.loc[df['card_market_value'].idxmax()]

    # Print Simplified Summary Report
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print(f"Most Valuable Card: Name: {most_valuable_card['card_name']}, Card ID: {most_valuable_card['card_id']}, Value: ${most_valuable_card['card_market_value']:,.2f}")


# --- Public Interface Functions ---

def main():
    """Public function: Runs the report on the production file (card_portfolio.csv)."""
    generate_summary('card_portfolio.csv')

def test():
    """Public function: Runs the report on the test file (test_card_portfolio.csv)."""
    generate_summary('test_card_portfolio.csv')


if __name__ == "__main__":
    # If called directly, default to the test function
    test()
