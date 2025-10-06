# Lab 4: Building a Data Pipeline with Bash and Python

**Objective:** In this lab, you will build a robust, multi-stage data pipeline that orchestrates **Bash scripts** (for API calls and file management) and **Python scripts** (for data transformation and reporting) using a central **Makefile**. You will integrate JSON (card details) and CSV (inventory) to create a unified final report.

---

<img width="250" height="342" alt="image" src="https://github.com/user-attachments/assets/ae3823f6-c73b-4f0e-a761-32c68d4e3caf" />
<img width="250" height="342" alt="image" src="https://github.com/user-attachments/assets/35d56fc3-35c1-41c4-b29a-095aa643aa42" />
<img width="250" height="342" alt="image" src="https://github.com/user-attachments/assets/194cfb72-a392-4e19-9cd5-d0d3a9238afc" />

---

Before starting the lab, I encourage you to spend a few minutes exploring the data so you know what you will be looking at:
- [Sample JSON](https://docs.pokemontcg.io/api-reference/cards/card-object#sample-json)
- [Sample Curl Cards Code](https://docs.pokemontcg.io/api-reference/cards/search-cards#code-samples)
- [Sample CURL Sets Code](https://docs.pokemontcg.io/api-reference/sets/search-sets#code-samples)
- [Sample End Product on Trading Site](https://www.tcgplayer.com/product/42346/pokemon-base-set-alakazam?page=1&Language=English)

<br>

---

## Step 0. Setup 

### Update your `main` branch and open up a new Codespace in GitHub

1.  Go to **your** forked `DS-2002-F25` repo in GitHub and make sure you are looking at your `main` branch.

2.  To open your Codespace, to the right, you can click on `<> Code`, then `Codespaces`, and lastly **open the codespace that you created for Lab 5**.
    - If you do not have a codespace for main, click `Create codespace on main` or the `+` to do so.
    - NOTE: You are now in your VS Code Codespace! This is a container that is built for you to work in that has essentially all of the functionality of a high-powered IDE, in this case VS Code, but is also fully integrated into your GitHub!

4.  Within your Codespace, in the Terminal (bottom center), run the `update_repo.sh` file to update your `main` branch. (OPTIONAL: Follow the prompts in the script to update your other branches if you'd like!)

5.  Use `cd` to navigate to your `/Labs/Lab_04` directory, where you should see this file `Lab_04_Python_Scripting.md` if everything is up-to-date.

6.  Create and move into a new branch called `Lab_4` by running `git checkout -b Lab_4`.

7.  To ensure you have the `pandas` library installed for the Python scripts by running	`pip install pandas`.

<br>

### Create Lab Directories
1.  Create a new directory for this project, within the `Labs/Lab_04/` directory, and navigate into it:
    ```bash
    mkdir pokemon_lab && cd pokemon_lab
    ```
2.  Within `pokemon_lab`, create two directories where you will be storing data.
	```bash
	mkdir card_set_lookup card_inventory
	```

<br>

### Store Data

Create the following test files. The test_set.json file should be placed in the root pokemon_lab directory, and the test_binder.csv should go into the card_inventory/ directory.

1.  `test_set.json` (Root Directory). This file simulates the JSON response from the Pokemon TCG API for a small set of cards.
```JSON
{
  "data": [
    {
      "id": "base1-1",
      "name": "Alakazam",
      "number": "1",
      "set": { "id": "base1", "name": "Base Set" },
      "tcgplayer": { "prices": { "holofoil": { "market": 65.50 } } }
    },
    {
      "id": "base1-4",
      "name": "Charizard",
      "number": "4",
      "set": { "id": "base1", "name": "Base Set" },
      "tcgplayer": { "prices": { "holofoil": { "market": 250.75 } } }
    },
    {
      "id": "base1-58",
      "name": "Pikachu",
      "number": "58",
      "set": { "id": "base1", "name": "Base Set" },
      "tcgplayer": { "prices": { "normal": { "market": 5.15 } } }
    },
    {
      "id": "base1-4",
      "name": "Charizard",
      "number": "4",
      "set": { "id": "base1", "name": "Base Set" },
      "tcgplayer": { "prices": { "holofoil": { "market": 250.75 } } }
    }
  ]
}
```

2.  `card_inventory/test_binder.csv` (Inventory Directory). This CSV file represents a small sample of your inventory.
```
card_name,set_name,card_number,binder_number,binder_page_number
Alakazam,Base Set,1,1,1
Charizard,Base Set,4,1,2
Pikachu,Base Set,58,1,3
Pikachu,Base Set,58,1,3
```

3.  Real Inventory Files - within the Lab_4 assignment in Canvas, there should be two files to download. Download and place them into your Inventory Directory.
    - `card_inventory/binder_1.csv`
    - `card_inventory/binder_2.csv`

<br>

---

## Step 1: Bash Scripts for API and File Management
Create these files in the root directory (`pokemon_lab/`) and remember to make them executable: `chmod +x <filename>`.

<br>

### Scenario
Building off of what we did in Activity 4, you still want to understand the value of your inheretance, a binder (or two?!) of Pokémon cards from your older cousin Austin! Because you want to simplify and automate this process, you are building an application to track the market prices of your new Pokémon cards. Your first task is to create a reliable and repeatable data pipeline that can pull card data from an API, process it, and output the results to a CSV file.

<br>

### 1.1 `add_card_set.sh` (Interactive Fetch)
This script prompts the user for a set ID and fetches the corresponding card data using `curl`, saving it to the `card_set_lookup/` directory.
1.  Add an appropriate shebang.
2.  Use `read` to prompt the user for the "TCG Card Set ID" (e.g., base1, base4), and save their response as a local variable called `SET_ID`.
3.  Add this `if` statement to ensure an error is thrown if the `$SET_ID` provided is empty:
```
if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi
```
4.  Use `echo` to provide a helpful output to let the user know we are fetching the data. Must use the `$SET_ID` variable in your message.
5.  Use `curl` and the `"$SET_ID"` to call the Pokemon TCG API, grabbing all the cards for our specified set and outputting it into the `card_set_lookup` directory as a JSON named exclusively by the `$SET_ID`.

<br>

### 1.2 `refresh_card_sets.sh` (Batch Fetch)
This script loops through all existing JSON files in the lookup directory and re-runs the API call to update the data, ensuring prices are current.
1.  Add an appropriate shebang.
2.  Use `echo` to provide a helpful output to let the user know we are refreshing all card sets in card_set_lookup/.
3.  Start a `for` loop that will go through every `.json` `FILE` in `card_set_lookup/`.
4.  In that `for` loop:
    - Create a local variable called `SET_ID` using this: `SET_ID=$(basename "$FILE" .json)`
    - Use `echo` to let the user know we are updating that set. (Must use the new local variable.)
    - Use `curl` and the `"$SET_ID"` to call the Pokemon TCG API and save the file as `"$FILE"`.
    - Use `echo` to let the user know the data was written to that file. (Must use the file variable.)
5.  End the `for` loop with `done`
6. Use `echo` to let the user know that all card sets have been refreshed.

<br>

---

## Step 2: Python Scripts for Data Processing and Reporting
Create these files in the root directory (`pokemon_lab/`) and remember to make them executable: `chmod +x <filename>`.

<br>

### `update_portfolio.py` (ETL)
```
#!/usr/bin/env python3

import os
import sys
import json
import pandas as pd

def _load_lookup_data(lookup_dir):
    """Loads and consolidates all card set JSONs into a single, clean lookup DataFrame."""
    lookup_data = []
    for filename in os.listdir(lookup_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(lookup_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                for card in data.get('data', []):
                    prices = card.get('tcgplayer', {}).get('prices', {})
                    # Prioritize holofoil then normal market price
                    market_value = prices.get('holofoil', {}).get('market') or prices.get('normal', {}).get('market') or 0.0
                    
                    lookup_data.append({
                        'card_id': card.get('id', 'N/A'),
                        'card_name': card.get('name'),
                        'card_number': str(card.get('number')),
                        'set_id': card.get('set', {}).get('id', 'N/A'),
                        'set_name': card.get('set', {}).get('name'),
                        'card_market_value': market_value
                    })

    lookup_df = pd.DataFrame(lookup_data)
    # Remove duplicates, keeping the highest market value for a given card/set/number combination
    lookup_df = lookup_df.sort_values(by='card_market_value', ascending=False).drop_duplicates(
        subset=['card_name', 'set_name', 'card_number'], keep='first'
    )
    return lookup_df

def _load_inventory_data(inventory_dir):
    """Loads and consolidates all inventory CSV files, then groups by card details to get quantities."""
    inventory_data = []
    for filename in os.listdir(inventory_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(inventory_dir, filename)
            df = pd.read_csv(filepath)
            inventory_data.append(df)

    if not inventory_data:
        return pd.DataFrame()

    inventory_df = pd.concat(inventory_data, ignore_index=True)
    inventory_df['card_number'] = inventory_df['card_number'].astype(str)
    
    # Aggregate Inventory Quantities
    inventory_cols = ['card_name', 'set_name', 'card_number', 'binder_number', 'binder_page_number']
    grouped_inventory = inventory_df.groupby(inventory_cols, as_index=False).size().rename(columns={'size': 'quantity'})
    
    return grouped_inventory

def _merge_and_calculate(grouped_inventory_df, lookup_df, output_file):
    """Merges inventory and lookup data, calculates total values, and writes to CSV."""
    if grouped_inventory_df.empty:
        print("No inventory data to process.", file=sys.stderr)
        return

    # Merge Inventory with Lookup Data
    merged_df = pd.merge(
        grouped_inventory_df, 
        lookup_df, 
        on=['card_name', 'set_name', 'card_number'], 
        how='left'
    )

    # Final Calculations
    merged_df['card_market_value'] = merged_df['card_market_value'].fillna(0.0)
    merged_df['total_value'] = merged_df['quantity'] * merged_df['card_market_value']
    merged_df['card_id'] = merged_df['card_id'].fillna('NOT_FOUND')
    merged_df['set_id'] = merged_df['set_id'].fillna('NOT_FOUND')

    # Select and Write to CSV
    final_cols = ['card_id', 'card_name', 'card_number', 'set_id', 'set_name', 
                  'binder_number', 'binder_page_number', 'card_market_value', 
                  'quantity', 'total_value']
    
    merged_df[final_cols].to_csv(output_file, index=False)
    print(f"Portfolio update complete. Data saved to {output_file}.")

def update_portfolio(inventory_dir, lookup_dir, output_file):
    """Main ETL orchestration function."""
    
    # 1. Extraction (JSON Lookup Data)
    lookup_df = _load_lookup_data(lookup_dir)
    
    # 2. Extraction & Aggregation (Inventory Data)
    grouped_inventory_df = _load_inventory_data(inventory_dir)
    
    # 3. Transformation and Loading
    _merge_and_calculate(grouped_inventory_df, lookup_df, output_file)


if __name__ == "__main__":
    # Use test data for the simple, repeatable test run
    TEST_OUTPUT_FILE = 'test_card_portfolio.csv'

    print("--- Running Update Portfolio with Test Data ---", file=sys.stderr)
    update_portfolio(
        inventory_dir='./card_inventory/', 
        lookup_dir='./card_set_lookup/', 
        output_file=TEST_OUTPUT_FILE
    )
    
    print("\nTest run complete. Output saved to test_card_portfolio.csv.", file=sys.stderr)
```



<br>

### `generate_summary.py` (Reporting)


```
#!/usr/bin/env python3

import os
import sys
import pandas as pd

def generate_summary(portfolio_file):
    """Reads the portfolio CSV and prints a summary to the console."""
    
    if not os.path.exists(portfolio_file):
        print(f"Error: Portfolio file '{portfolio_file}' not found. Run 'make Update_Portfolio' first.", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(portfolio_file)
            
    if df.empty:
        print("Portfolio is empty. Nothing to summarize.")
        return

    # Summary Calculations
    total_portfolio_value = df['total_value'].sum()
    binder_values = df.groupby('binder_number')['total_value'].sum().reset_index()
    
    page_values = df.groupby(['binder_number', 'binder_page_number'])['total_value'].sum().reset_index(name='page_total_value')
    most_valuable_page = page_values.loc[page_values['page_total_value'].idxmax()]
    
    # Most Valuable Card (based on per-card market value)
    most_valuable_card = df.loc[df['card_market_value'].idxmax()]

    # Print Summary Report
    print("\n" + "="*50)
    print("Portfolio Summary Report")
    print("="*50)
    
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}\n")
    
    print("Binder Totals:")
    for index, row in binder_values.iterrows():
        print(f"    Binder {row['binder_number']} Total Value: ${row['total_value']:,.2f}")
    
    print(f"\nMost Valuable Card: {most_valuable_card['card_name']} (${most_valuable_card['card_market_value']:,.2f})")
    
    print(f"\nMost Valuable Binder Page:")
    print(f"    - Binder: {most_valuable_page['binder_number']}, Page: {most_valuable_page['binder_page_number']}")
    print(f"    - Total Value: ${most_valuable_page['page_total_value']:,.2f}")
    
    print("="*50 + "\n")


if __name__ == "__main__":
    # If the live file doesn't exist, try the test file for debugging ease
    portfolio_file_to_use = 'card_portfolio.csv'
    
    if not os.path.exists(portfolio_file_to_use):
         portfolio_file_to_use = 'test_card_portfolio.csv'
         print(f"(Using test portfolio file: {portfolio_file_to_use})", file=sys.stderr)

    generate_summary(portfolio_file_to_use)
```

<br>

---

## Step 3: Orchestration with Makefile
The Makefile remains the central control for the pipeline.

```
# --- Variables ---
PORTFOLIO_CSV := card_portfolio.csv
TEST_PORTFOLIO_CSV := test_card_portfolio.csv
TEST_JSON := test_set.json
TEST_SET_ID := base1
TEST_LOOKUP_JSON := card_set_lookup/$(TEST_SET_ID).json

# --- Phony Targets ---
.PHONY: all Add_Set Refresh_Sets Update_Portfolio Generate_Summary Clean Test

# --- Default Target ---
all: Generate_Summary

# --- Utility Targets ---

Add_Set:
	@echo "--- Adding New Card Set ---"
	@./add_card_set.sh

Refresh_Sets:
	@echo "--- Refreshing All Card Sets ---"
	@./refresh_card_sets.sh

# --- Main Pipeline Targets ---

# Update_Portfolio: The core pipeline step.
Update_Portfolio: update_portfolio.py
	@echo "--- Starting Portfolio Update Pipeline ---"
	@echo "Do you want to add a NEW card set? (yes/no)"
	@read USER_ADD
	@if [ "$$USER_ADD" = "yes" ]; then \
		make Add_Set; \
		echo "Card set added. Add another? (yes/no)"; \
		read USER_ADD_AGAIN; \
		if [ "$$USER_ADD_AGAIN" = "yes" ]; then \
			make Add_Set; \
		fi; \
	fi

	@echo "Do you want to refresh ALL existing card sets? (yes/no)"
	@read USER_REFRESH
	@if [ "$$USER_REFRESH" = "yes" ]; then \
		make Refresh_Sets; \
	fi

	@echo "--- Running Data Merge and Calculation ---"
	@./update_portfolio.py

# Generate_Summary: Depends on the portfolio being updated.
Generate_Summary: $(PORTFOLIO_CSV) generate_summary.py
	@echo "--- Generating Portfolio Summary ---"
	@./generate_summary.py

# Test: Runs the pipeline with the small test data set.
Test: update_portfolio.py $(TEST_JSON)
	@echo "--- Running Test Portfolio Update Pipeline ---"
	@# 1. Prepare the test environment by copying the test JSON to the expected lookup path
	@cp $(TEST_JSON) $(TEST_LOOKUP_JSON)
	@# 2. Run the Python script (which uses the test output filename in its __main__ block)
	@./update_portfolio.py
	@# 3. Clean up the temporary test JSON file
	@rm -f $(TEST_LOOKUP_JSON)
	@echo "Test clean up complete."

# File Dependency: Ensures Generate_Summary runs Update_Portfolio if the CSV is missing.
$(PORTFOLIO_CSV): Update_Portfolio
	@touch $(PORTFOLIO_CSV)

# --- Clean Target ---
Clean:
	@echo "--- Cleaning Generated Files ---"
	# Remove generated CSV files
	@rm -f $(PORTFOLIO_CSV) $(TEST_PORTFOLIO_CSV)
	# Remove all dynamically fetched JSONs
	@rm -f card_set_lookup/*.json
	@echo "Clean complete."
```

<br>

---

## Step 4: Running the Pipeline
Use the Makefile targets to operate your new data pipeline.

1.  **Test the Pipeline**: Run the Test target to ensure your scripts work with the minimal test data.
```
make Test
```

2.  **Add Real Data**: Run the Add_Set target and provide the set IDs for the sets in your inventory (e.g., base1, base4).
```
make Add_Set
```

3.  **Run the Full Pipeline**: Run the all target. It will execute the full ETL process and print the final summary.
```
make all
```

4.  **Clean Up**: Remove all generated files (but keep your scripts and inventory files).
```
make Clean
```














