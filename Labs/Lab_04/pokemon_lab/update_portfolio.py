import os
import json
import pandas as pd

def _load_lookup_data(lookup_dir):
    """
    Load and clean card data from JSON files in the lookup directory.
    Returns a combined DataFrame with relevant market info.
    """
    all_lookup_df = []

    # Expected columns for a lookup dataframe; used as a fallback when no valid
    # lookup files are present so downstream code can safely reference columns.
    required_cols = [
        'card_id', 'card_name', 'card_number',
        'set_id', 'set_name', 'card_market_value'
    ]

    for filename in os.listdir(lookup_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(lookup_dir, filename)

            # Load JSON
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, OSError) as e:
                # Skip files that aren't valid JSON or cannot be read
                print(f"\u26a0 Skipping invalid lookup file {filename}: {e}", file=sys.stderr)
                continue

            # Ensure the JSON has the expected 'data' key containing a list
            if not isinstance(data, dict) or 'data' not in data or not isinstance(data['data'], list):
                print(f"\u26a0 Skipping lookup file {filename}: missing or invalid 'data' array", file=sys.stderr)
                continue

            # Flatten JSON data
            df = pd.json_normalize(data['data'])

            # Add card_market_value column if possible; fall back to 0.0 when missing
            try:
                holo = df.get('tcgplayer.prices.holofoil.market')
                normal = df.get('tcgplayer.prices.normal.market')
                # If the columns exist, coalesce them, otherwise fill with 0.0
                if holo is not None:
                    card_market = holo.fillna(normal) if normal is not None else holo.fillna(0.0)
                elif normal is not None:
                    card_market = normal.fillna(0.0)
                else:
                    card_market = 0.0
                df['card_market_value'] = card_market
            except Exception:
                df['card_market_value'] = 0.0

            # Rename relevant columns
            df = df.rename(columns={
                'id': 'card_id',
                'name': 'card_name',
                'number': 'card_number',
                'set.id': 'set_id',
                'set.name': 'set_name'
            })

            # Keep only relevant columns
            required_cols = [
                'card_id', 'card_name', 'card_number',
                'set_id', 'set_name', 'card_market_value'
            ]

            # Append clean df to list
            all_lookup_df.append(df[required_cols].copy())

    # If no valid lookup files were read, return an empty DataFrame with the
    # expected columns so callers can merge without error.
    if not all_lookup_df:
        return pd.DataFrame(columns=required_cols)

    # Combine all dataframes
    lookup_df = pd.concat(all_lookup_df, ignore_index=True)

    # Sort and drop duplicate card IDs, keeping the highest-value one
    lookup_df = lookup_df.sort_values(by='card_market_value', ascending=False)
    lookup_df = lookup_df.drop_duplicates(subset=['card_id'], keep='first')

    return lookup_df


def _load_inventory_data(inventory_dir):
    """
    Load and process inventory CSVs from the given directory.
    Returns a combined DataFrame with a unified card_id.
    """
    inventory_data = []

    for filename in os.listdir(inventory_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(inventory_dir, filename)
            df = pd.read_csv(filepath)
            inventory_data.append(df)

    # If no CSVs found, return an empty DataFrame
    if not inventory_data:
        return pd.DataFrame()

    # Combine all inventory CSVs into one DataFrame
    inventory_df = pd.concat(inventory_data, ignore_index=True)

    # Create card_id: set_id + '-' + card_number
    inventory_df['card_id'] = (
        inventory_df['set_id'].astype(str) + '-' + inventory_df['card_number'].astype(str)
    )

    return inventory_df


import sys
from pathlib import Path


def update_portfolio(inventory_dir, lookup_dir, output_file):
    """
    Main ETL function: loads, merges, cleans, and saves the card portfolio.
    """
    # If relative paths are provided, resolve them relative to this script's dir
    base_dir = Path(__file__).resolve().parent
    inventory_dir = Path(inventory_dir)
    lookup_dir = Path(lookup_dir)
    if not inventory_dir.is_absolute():
        inventory_dir = (base_dir / inventory_dir).resolve()
    if not lookup_dir.is_absolute():
        lookup_dir = (base_dir / lookup_dir).resolve()

    # Load data
    lookup_df = _load_lookup_data(str(lookup_dir))
    inventory_df = _load_inventory_data(str(inventory_dir))

    # Handle empty inventory
    if inventory_df.empty:
        print("❌ Error: Inventory is empty. No portfolio created.", file=sys.stderr)
        headers = [
            'card_name', 'set_id', 'set_name', 'card_number',
            'card_market_value', 'binder_name', 'page_number',
            'slot_number', 'index'
        ]
        pd.DataFrame(columns=headers).to_csv(output_file, index=False)
        return

    # Merge dataframes on 'card_id'. Inventory CSVs already include a 'card_name'
    # which would cause pandas to create suffixed columns (e.g. card_name_x, card_name_y).
    # Use explicit suffixes, then coalesce into a single 'card_name' preferring
    # the lookup (official) name when available, otherwise fall back to the
    # inventory's name.
    merged_df = pd.merge(
        inventory_df,
        lookup_df[['card_id', 'card_name', 'set_name', 'card_market_value']],
        on='card_id',
        how='left',
        suffixes=('_inv', '_lookup')
    )

    # Prefer lookup name when present, otherwise use inventory name
    if 'card_name_lookup' in merged_df.columns or 'card_name_inv' in merged_df.columns:
        merged_df['card_name'] = merged_df.get('card_name_lookup').fillna(merged_df.get('card_name_inv'))

    # Clean missing values
    merged_df['card_market_value'] = merged_df['card_market_value'].fillna(0.0)
    merged_df['set_name'] = merged_df['set_name'].fillna('NOT_FOUND')

    # Create location index
    merged_df['index'] = (
        merged_df['binder_name'].astype(str) + "-" +
        merged_df['page_number'].astype(str) + "-" +
        merged_df['slot_number'].astype(str)
    )

    # Drop intermediate suffixed name columns if they exist
    for col in ('card_name_inv', 'card_name_lookup'):
        if col in merged_df.columns:
            merged_df.drop(columns=[col], inplace=True)

    # Final column order
    final_cols = [
        'card_name', 'set_id', 'set_name', 'card_number',
        'card_market_value', 'binder_name', 'page_number',
        'slot_number', 'index'
    ]

    # Sanity-check final columns exist; if not, fill with defaults to avoid KeyError
    missing = [c for c in final_cols if c not in merged_df.columns]
    if missing:
        # Fill any missing columns with sensible defaults
        for c in missing:
            if c == 'card_name':
                merged_df[c] = ''
            elif c in ('card_market_value',):
                merged_df[c] = 0.0
            else:
                merged_df[c] = 'NOT_FOUND'

    # Write to output
    merged_df[final_cols].to_csv(output_file, index=False)
    print(f"✅ Portfolio written to {output_file}")


def main():
    """
    Run portfolio update in production mode.
    """
    update_portfolio(
        inventory_dir="./card_inventory",
        lookup_dir="./card_set_lookup",
        output_file="card_portfolio.csv"
    )


def test():
    """
    Run portfolio update in test mode using test data directories.
    """
    update_portfolio(
        inventory_dir="./card_inventory_test",
        lookup_dir="./card_set_lookup_test",
        output_file="test_card_portfolio.csv"
    )


if __name__ == "__main__":
    print("🔍 Starting ETL pipeline in TEST mode...", file=sys.stderr)
    test()