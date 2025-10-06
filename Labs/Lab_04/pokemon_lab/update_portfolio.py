#!/usr/bin/env python3

import os
import sys
import json
import pandas as pd

def _load_lookup_data(lookup_dir):
    """Loads and consolidates all card set JSONs into a single, clean lookup DataFrame."""
    all_lookup_df = []
    for filename in os.listdir(lookup_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(lookup_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

                df = pd.json_normalize(data['data'], errors='ignore')
                df['card_market_value'] = df['tcgplayer.prices.holofoil.market'].fillna(df['tcgplayer.prices.normal.market']).fillna(0.0)

                df = df.rename(columns={'id': 'card_id', 'set.id': 'set_id', 'set.name': 'set_name', 'number': 'card_number', 'name': 'card_name'})

                required_cols = ['card_id', 'card_name', 'card_number', 'set_id', 'set_name', 'card_market_value']
                all_lookup_df.append(df[required_cols].copy())

    lookup_df = pd.concat(all_lookup_df, ignore_index=True)

    # Keep the highest market value for duplicates
    return lookup_df.sort_values(by='card_market_value', ascending=False).drop_duplicates(
        subset=['card_id'], keep='first'
    )

def _load_inventory_data(inventory_dir):
    """Loads and consolidates all inventory CSV files, and calculates the card_id."""
    inventory_data = []
    for filename in os.listdir(inventory_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(inventory_dir, filename)
            df = pd.read_csv(filepath)
            inventory_data.append(df)

    if not inventory_data:
        return pd.DataFrame()

    inventory_df = pd.concat(inventory_data, ignore_index=True)

    # NEW: Calculate card_id = set_id-card_number
    inventory_df['card_id'] = inventory_df['set_id'].astype(str) + '-' + inventory_df['card_number'].astype(str)

    return inventory_df

def update_portfolio(inventory_dir, lookup_dir, output_file):
    """Loads data, merges, calculates index, and writes to CSV."""

    lookup_df = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)

    if inventory_df.empty:
        print("No inventory data found. Outputting empty file.", file=sys.stderr)
        pd.DataFrame(columns=['index', 'card_id', 'card_name', 'card_number', 'set_id', 'set_name', 'card_market_value']).to_csv(output_file, index=False)
        return

    # Merge Inventory with Lookup Data (SIMPLIFIED MERGE KEY)
    merged_df = pd.merge(
        inventory_df, 
        lookup_df[['card_id', 'set_name', 'card_market_value']], 
        on=['card_id'], 
        how='left'
    )

    # Final Calculations and Index Creation
    merged_df['card_market_value'] = merged_df['card_market_value'].fillna(0.0)
    merged_df['set_name'] = merged_df['set_name'].fillna('NOT_FOUND')

    # Index field name change
    merged_df['index'] = merged_df['binder_name'].astype(str) + \
                         merged_df['page_number'].astype(str) + \
                         merged_df['slot_number'].astype(str)

    # Select and Write to CSV
    final_cols = ['index', 'card_id', 'card_name', 'card_number', 'set_id', 'set_name', 'card_market_value']

    merged_df[final_cols].to_csv(output_file, index=False)
    print(f"Portfolio update complete. Data saved to {output_file}.")


def main():
    """Runs the production pipeline using the normal folders."""
    update_portfolio(
        inventory_dir='./card_inventory/', 
        lookup_dir='./card_set_lookup/', 
        output_file='card_portfolio.csv' # PRODUCTION OUTPUT
    )

def test():
    """Runs the test pipeline using the dedicated test folders."""
    update_portfolio(
        inventory_dir='./card_inventory_test/', 
        lookup_dir='./card_set_lookup_test/', 
        output_file='test_card_portfolio.csv' # TEST OUTPUT
    )


if __name__ == "__main__":
    # Check for a specific argument to trigger production mode from Makefile
    if len(sys.argv) > 1 and sys.argv[1] == 'main':
        print("--- Running Update Portfolio (Production Mode) ---", file=sys.stderr)
        main()
    else:
        # Default behavior (running ./script.py or 'make Test') is the test function
        print("--- Running Update Portfolio (Test Mode) ---", file=sys.stderr)
        test()
