import os
import sys
import pandas as pd

def generate_summary(portfolio_file):
    """
    Reads the card portfolio and prints total value and top card.
    """
    # Check if the file exists
    if not os.path.exists(portfolio_file):
        print(f"Error: File '{portfolio_file}' not found.", file=sys.stderr)
        sys.exit(1)

    # Load the CSV
    df = pd.read_csv(portfolio_file)

    # Check if DataFrame is empty
    if df.empty:
        print("Portfolio file is empty. Nothing to summarize.")
        return

    # Total portfolio value
    total_portfolio_value = df['card_market_value'].sum()

    # Most valuable card
    most_valuable_index = df['card_market_value'].idxmax()
    most_valuable_card = df.loc[most_valuable_index]

    # Print report
    print("\n📊 Portfolio Summary Report")
    print("-" * 40)
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")
    print(f"Most Valuable Card:")
    print(f"   - Name: {most_valuable_card['card_name']}")
    print(f"   - ID: {most_valuable_card['set_id']}-{most_valuable_card['card_number']}")
    print(f"   - Market Value: ${most_valuable_card['card_market_value']:,.2f}")
    print("-" * 40)

def main():
    """Run summary using production data."""
    generate_summary("card_portfolio.csv")

def test():
    """Run summary using test data."""
    generate_summary("test_card_portfolio.csv")

if __name__ == "__main__":
    print("Running Summary in TEST mode...", file=sys.stderr)
    test()