#!/usr/bin/env python3

import os
import sys
import pandas as pd

def generate_summary(portfolio_file):
    """Reads the portfolio CSV and prints a simplified summary to the console."""

    if not os.path.exists(portfolio_file):
        print(f"Error: Portfolio file '{portfolio_file}' not found. Run 'make Update_Portfolio' first.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)

    if df.empty:
        print("Portfolio is empty. Nothing to summarize.")
        return

    # Extract binder number from the index for grouping (assuming it's the first digit)
    df['binder_name'] = df['index'].astype(str).str[0].astype(int)

    # Summary Calculations
    total_portfolio_value = df['card_market_value'].sum()
    binder_values = df.groupby('binder_name')['card_market_value'].sum().reset_index()

    # Most Valuable Card (based on per-card market value)
    most_valuable_card = df.loc[df['card_market_value'].idxmax()]

    # Get binder values (assuming only binders 1 and 2 exist for simplicity)
    binder_1_value = binder_values[binder_values['binder_name'] == 1]['card_market_value'].iloc[0] if 1 in binder_values['binder_name'].values else 0.0
    binder_2_value = binder_values[binder_values['binder_name'] == 2]['card_market_value'].iloc[0] if 2 in binder_values['binder_name'].values else 0.0


    # Print Summary Report
    print(f"Total Value: ${total_portfolio_value:,.2f}")
    print(f"Binder 1 Value: ${binder_1_value:,.2f}")
    print(f"Binder 2 Value: ${binder_2_value:,.2f}")
    print(f"Most Valuable Card: Name: {most_valuable_card['card_name']}, Card ID: {most_valuable_card['card_id']}, Value: ${most_valuable_card['card_market_value']:,.2f}")


def main():
    """Runs the report on the production file."""
    generate_summary('card_portfolio.csv')

def test():
    """Runs the report on the test file."""
    generate_summary('test_card_portfolio.csv')


if __name__ == "__main__":
    # Check for a specific argument to trigger production mode from Makefile
    if len(sys.argv) > 1 and sys.argv[1] == 'main':
        main()
    else:
        test()
