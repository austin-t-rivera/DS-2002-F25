#!/usr/bin/env python3

import os
import sys
import json
import pandas as pd

# --- Helper Functions ---

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
    inventory_df['card_id'] = inventory_df['set_id'].astype(str) + '-' + inventory_df['card_number'].astype(str)

    return inventory_df

def update_portfolio(inventory_dir, lookup_dir, output_file):
    """Orchestrates the ETL process using specified directories and writes to the output file."""

    lookup_df = _load_lookup_data(lookup_dir)
    inventory_df = _load_inventory_data(inventory_dir)

    if inventory_df.empty:
        cols = ['index', 'card_id', 'card_name', 'card_number', 'set_id', 'set_name', 'card_market_value']
        pd.DataFrame(columns=cols).to_csv(output_file, index=False)
        print("No inventory data found. Outputting empty file.", file=sys.stderr)
        return

    merged_df = pd.merge(
        inventory_df,
        lookup_df[['card_id', 'set_name', 'card_market_value']],
        on=['card_id'],
        how='left'
    )

    merged_df['card_market_value'] = merged_df['card_market_value'].fillna(0.0)
    merged_df['set_name'] = merged_df['set_name'].fillna('NOT_FOUND')

    merged_df['index'] = merged_df['binder_name'].astype(str) + \
                         merged_df['page_number'].astype(str) + \
                         merged_df['slot_number'].astype(str)

    final_cols = ['index', 'card_id', 'card_name', 'card_number', 'set_id', 'set_name', 'card_market_value']
    merged_df[final_cols].to_csv(output_file, index=False)
    print(f"Portfolio update complete. Data saved to {output_file}.")


# --- Public Interface Functions ---

def main():
    """Public function: Runs the production pipeline using the normal folders."""
    update_portfolio(
        inventory_dir='./card_inventory/',
        lookup_dir='./card_set_lookup/',
        output_file='card_portfolio.csv'
    )

def test():
    """Public function: Runs the test pipeline using the dedicated test folders."""
    update_portfolio(
        inventory_dir='./card_inventory_test/',
        lookup_dir='./card_set_lookup_test/',
        output_file='test_card_portfolio.csv'
    )


if __name__ == "__main__":
    # If called directly, default to the test function
    print("--- Running Update Portfolio (Test Mode) ---", file=sys.stderr)
    test()
