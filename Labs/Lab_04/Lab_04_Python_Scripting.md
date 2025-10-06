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
card_name,set_id,card_number,binder_name,page_number,slot_number
Alakazam,base1,1,0,1,1
Charizard,base1,4,0,2,8
Pikachu,base1,58,0,3,4
Pikachu,base1,58,0,3,5
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
This script handles the full data pipeline: loading card details (JSON) and inventory (CSV), merging them, performing calculations, and outputting the final portfolio CSV.

<br>

#### NOTE about this file
The underscore prefix (`_`) before a function name in Python, like in `_load_lookup_data`, is not strictly necessary but is a widely adopted convention to indicate that the function is intended for internal use within the current module (script or class).
Here's a breakdown of why it's used:
- Convention (Good Practice): It signals to other programmers (and to you, later) that this function is a "helper" or "private" function. You're "discouraging" direct calls to it from outside the module.
- Encapsulation: It promotes better encapsulation in object-oriented programming (though Python doesn't enforce strict privacy). It tells users, "The module's public interface is `update_portfolio()`; please use that, as the behavior of `_load_lookup_data()` might change internally without notice."
- Behavior in `from module import *`: When you use the syntax `from script_name import *`, Python's interpreter will actually not import names that begin with a single underscore. This is the only place Python provides a small amount of "privacy" based on the underscore convention.
In short, it's a strong signal of intent to keep the function internal, making the public interface of your script cleaner. You could remove it, and the code would run exactly the same, but it would violate a common Python coding standard (PEP 8).

<br>

#### Function 1: `_load_lookup_data(lookup_dir)` (Load JSON Prices)

**What it does**: This function is responsible for the "E" (Extraction) and initial "T" (Transformation) of the JSON price data. It reads every JSON file, flattens the complex nested price structure, and isolates the single highest market price for each unique card ID.

**Why it's separate**: Isolating this logic makes the code robust. If the API changes its JSON format, you only need to update this one function. It keeps the data acquisition concerns separate from the inventory concerns.

1.  Initialize an empty list, `all_lookup_df`, to store DataFrames temporarily.
2.  Start a `for` loop to iterate over all files in the `lookup_dir`.
3.  Inside the loop, use an `if` statement to ensure you only process files that end with `.json`.
4.  Within the `if` block:
	- Construct the full `filepath`.
	- Open and load the JSON data into a variable named `data`.
	- Use `pd.json_normalize` on `data['data']` to flatten the JSON into a DataFrame (`df`).
	- Create a new column `df['card_market_value']` by filling missing `holofoil.market` values with `normal.market` values, and then filling any remaining missing values with `0.0`.
	- Use the `.rename()` method on `df` to simplify the column names (e.g., `'set.id'` to `'set_id'`, `'number'` to `'card_number'`, etc.).
	- Define a list of `required_cols` and append a copy of `df[required_cols]` to `all_lookup_df`.
5.  After the loop, use `pd.concat()` on `all_lookup_df` to create the final `lookup_df`.
6.  Ensure the `card_number` column in `lookup_df` is a string type.
7.  Return the `lookup_df` after sorting by value and removing duplicates using `drop_duplicates(subset=['card_name', 'set_id', 'card_number'], keep='first')`.

<br>

#### Function 2: `_load_inventory_data(inventory_dir)` (Load CSV Inventory)

**What it does**: This function handles the "E" (Extraction) of the local inventory CSV data. Critically, it then performs a necessary "T" (Transformation) step by synthesizing the unified `card_id` from the raw `set_id` and `card_number` columns.

**Why it's separate**: This isolates all file-reading and initial data manipulation for the local inventory. If you were to change from CSV to a database source, you would only have to modify this single function, not the merge or final output logic.

1.  Initialize an empty list, `inventory_data`.
2.  Start a `for` loop to iterate over all files in the `inventory_dir`.
3.  Inside the loop, use an `if` statement to ensure you only process files that end with `.csv`.
4.  Within the `if` block:
	- Construct the full `filepath`.
	- Use `pd.read_csv()` on the filepath and append the resulting DataFrame to `inventory_data`.
5.  Use an `if` statement to check if `inventory_data` is empty, returning an empty DataFrame if it is.
6.  Use `pd.concat()` on `inventory_data` to create the final `inventory_df`.
7.  Create a new column `inventory_df['card_id']` by concatenating the string versions of the `'set_id'`, a hyphen (`-`), and the `'card_number'`.
8.  Return the consolidated `inventory_df`.

<br>

#### Function 3: `update_portfolio(inventory_dir, lookup_dir, output_file)` (Main ETL/Loading Logic)

**What it does**: This is the main orchestration function. It gathers the two processed DataFrames, executes the final "T" (Transformation/Merge), and completes the "L" (Loading) by writing the final report CSV.

**Why it's separate**: This serves as the master controller, making the flow of the entire pipeline easy to follow: 1. Get prices, 2. Get inventory, 3. Merge and clean, 4. Output. It keeps the high-level logic clean and dependency-free.

1.  Call the two helper functions, `_load_lookup_data()` and `_load_inventory_data()`, storing the results in `lookup_df` and `inventory_df`.
2.  Use an `if` statement to check if `inventory_df` is empty; if so, print an error, create an empty portfolio CSV with the required headers, and `return`.
3.  Perform the data merge: Use `pd.merge()` to join `inventory_df` with the necessary columns from `lookup_df`.
	- The join must be on the `'card_id'` key.
	- Use the `how='left'` merge to keep all inventory items.
4.  Final Calculations and Cleaning:
	- Fill any missing `card_market_value` in `merged_df` with `0.0` (using `fillna(0.0)`).
	- Fill any missing `card_id` or `set_name` with the string `'NOT_FOUND'`.
5.  Index Creation: Create the final location index column, `'index'`, by concatenating the string versions of the location columns: `'binder_name'`, `'page_number'`, and `'slot_number'`.
6.  Define the `final_cols` list containing only the desired output columns.
7.  Write the final DataFrame to the `output_file` using `.to_csv()`, ensuring `index=False`.
8.  Print a success message indicating the data has been saved to the output file.

<br>

#### Main Block: if __name__ == "__main__":

**What it does**: This block ensures the code runs only when the script is executed directly (not when imported as a module). It defines the test environment for quick validation.

**Why it's separate**: This is a Python best practice. It provides a standard entry point and allows the entire script to be reused (imported) by other scripts without automatically running the test code.

1.  Define the `TEST_OUTPUT_FILE` variable.
2.  Print a message to standard error indicating the test run is starting.
3.  Call the main function, `update_portfolio()`, using the test directory paths and the test output file name.
4.  Print a final completion message to standard error.

<br>

### `generate_summary.py` (Reporting)
This script is purely a reporting tool. Its job is to ingest the single, final output file from the ETL pipeline (`update_portfolio.py`) and present key aggregated insights to the user.

#### Function 1: `generate_summary(portfolio_file)`

**What it does**: This is the core logic that reads the completed portfolio CSV, performs all required calculations (Total Value, Binder Values, Most Valuable Card), and prints the simplified report to the console.

**Why it's a function**: Keeping the logic inside a function makes the code reusable (it can be called by other scripts) and allows the script to easily handle both the main portfolio and the test portfolio files via the `__main__` block.

1.  Use an `if not os.path.exists()` check to verify the `portfolio_file exists`; if it doesn't, print an error message and exit the script.
2.  Read the CSV file into a DataFrame, `df`, using `pd.read_csv()`.
3.  Use an `if df.empty:` check to verify the file contains data; if empty, print a message and `return`.
4.  **Data Preparation**: Create a temporary column, `df['binder_name']`, by taking the first character of the new `index` column and converting it to an integer. This isolates the binder number for grouping.
5.  **Calculate Total Value**: Calculate the `total_portfolio_value` by summing the entire `card_market_value` column (since each row is a single card).
6.  **Calculate Binder Values**: Calculate `binder_values` by using `.groupby('binder_name')['card_market_value'].sum()` and resetting the index.
7.  **Find Most Valuable Card**: Find the row corresponding to the `most_valuable_card` by locating the index of the maximum value in the `card_market_value` column using `.idxmax()`.
8.  **Calculate Individual Binder Totals**: Explicitly extract the `binder_1_value` and `binder_2_value` from the `binder_values` DataFrame, defaulting to `0.0` if a binder isn't present in the data.
9.  **Print Report**: Print the final, simplified output strings for Total Value, Binder 1 Value, Binder 2 Value, and the Most Valuable Card details.

<br>

#### Main Block: if __name__ == "__main__":

**What it does**: This block sets up the script's execution. It first attempts to use the production file (`card_portfolio.csv`); if that file is missing (e.g., after running `make Clean`), it gracefully falls back to using the test file (`test_card_portfolio.csv`) for convenience and debugging.

**Why it's separate**: This Python standard practice provides a clean entry point. It handles the crucial logic of deciding which file to process without cluttering the main `generate_summary` function.

1.  Define the primary portfolio file name, `portfolio_file_to_use`.
2.  Use an `if not os.path.exists()` check to see if the main portfolio file is present.
3.  If the main file is missing, reassign `portfolio_file_to_use` to the test file name and print a message to standard error.
4.  Call the main function, `generate_summary()`, using the determined file path.

<br>

---

## Step 3: Orchestration with Makefile
The `Makefile` serves as the control center for the entire project, managing dependencies and providing a simple, consistent interface for running complex, multi-step tasks.


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














