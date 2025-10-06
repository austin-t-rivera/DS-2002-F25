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
2.  Within `pokemon_lab`, create four directories where you will be storing data.
	```bash
	mkdir card_set_lookup card_inventory card_set_lookup_test card_inventory_test
	```

<br>

### Store Data

Create the following test files. The `base0.json` file should be placed in the `root card_set_lookup_test` directory, and the `binder_0.csv` should go into the `card_inventory_test/` directory.

1.  `card_set_lookup_test/base0.json` (Root Directory). This file simulates the JSON response from the Pokemon TCG API for a small set of cards.
```JSON
{
  "data": [
    {
      "id": "base0-1",
      "name": "Alakazam",
      "number": "1",
      "set": { "id": "base1", "name": "Base Set" },
      "tcgplayer": { "prices": { "holofoil": { "market": 65.50 } } }
    },
    {
      "id": "base0-4",
      "name": "Charizard",
      "number": "4",
      "set": { "id": "base1", "name": "Base Set" },
      "tcgplayer": { "prices": { "holofoil": { "market": 250.75 } } }
    },
    {
      "id": "base0-58",
      "name": "Pikachu",
      "number": "58",
      "set": { "id": "base1", "name": "Base Set" },
      "tcgplayer": { "prices": { "normal": { "market": 5.15 } } }
    }
  ]
}
```

2.  `card_inventory_test/binder_0.csv` (Test Inventory Directory). This CSV file represents a small sample of your inventory.
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
```bash
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

## Step 2: Python Script for Data ETL - `update_portfolio.py`

This script handles the full **Extract, Transform, and Load (ETL)** data pipeline: loading card details (JSON) and inventory (CSV), merging them, performing calculations, and outputting the final portfolio CSV.

### NOTE about the Underscore Prefix
The underscore prefix (`_`) before a function name in Python, like in `_load_lookup_data`, is a convention to indicate that the function is intended for **internal use** within the current module. It signals that this is a "helper" or "private" function and should not be called directly, promoting a cleaner public interface.

<br>

### Function 1: `_load_lookup_data(lookup_dir)` (Load JSON Prices)

**What it does**: This function is responsible for the "E" (Extraction) and initial "T" (Transformation) of the JSON price data. It reads every JSON file, flattens the complex nested price structure, and isolates the single highest market price for each unique card ID.

**Why it's separate**: Isolating this logic makes the code robust. If the API changes its JSON format, you only need to update this one function.

1.  Initialize an empty list, `all_lookup_df`, to store DataFrames temporarily.
2.  Start a `for` loop to iterate over all files in the `lookup_dir`, processing only files that end with `.json`.
3.  Within the loop:
    - Construct the full `filepath` and load the JSON data into a variable named `data`.
    - Use **`pd.json_normalize`** on `data['data']` to flatten the JSON into a DataFrame (`df`).
    - **Price Calculation**: Create a new column `df['card_market_value']` by prioritizing `tcgplayer.prices.holofoil.market` and filling missing values with `tcgplayer.prices.normal.market`, finally filling any remaining missing values with `0.0`.
    - **Rename Columns**: Use the `.rename()` method to standardize the column names (e.g., `'id'` to `'card_id'`, `'set.id'` to `'set_id'`).
    - Define a list of `required_cols` and append a copy of the new `df` to `all_lookup_df`.
4.  After the loop, use **`pd.concat()`** on `all_lookup_df` to create the final `lookup_df`.
5.  **Clean Duplicates**: Return the `lookup_df` after sorting by value and removing duplicates using **`drop_duplicates(subset=['card_id'], keep='first')`**.

<br>

### Function 2: `_load_inventory_data(inventory_dir)` (Load CSV Inventory)

**What it does**: This function handles the "E" (Extraction) of the local inventory CSV data. It then performs a necessary "T" (Transformation) step by synthesizing the unified `card_id` key.

**Why it's separate**: This isolates all file-reading and initial data manipulation for the local inventory.

1.  Initialize an empty list, `inventory_data`.
2.  Start a `for` loop to iterate over all files in the `inventory_dir`, processing only files that end with `.csv`.
3.  Within the loop, read the CSV using `pd.read_csv()` and append the resulting DataFrame to `inventory_data`.
4.  Use an `if` statement to check if `inventory_data` is empty, returning an empty DataFrame if it is.
5.  Use **`pd.concat()`** on `inventory_data` to create the final `inventory_df`.
6.  **Create Unified Key**: Create a new column **`inventory_df['card_id']`** by concatenating the string versions of the `'set_id'`, a hyphen (`-`), and the `'card_number'`. This is the common key used for merging.
7.  Return the consolidated `inventory_df`.

<br>

### Function 3: `update_portfolio(inventory_dir, lookup_dir, output_file)` (Main ETL/Loading Logic)

**What it does**: This is the main **orchestration function**. It executes the final "T" (Transformation/Merge) and completes the "L" (Loading) by writing the final portfolio CSV.

**Why it's separate**: This serves as the master controller, keeping the high-level logic clean and dependency-free.

1.  Call the two helper functions, `_load_lookup_data()` and `_load_inventory_data()`.
2.  **Handle Empty Inventory**: Check if `inventory_df` is empty; if so, print an error to `sys.stderr`, create an empty portfolio CSV with the required headers, and `return`.
3.  **Data Merge**: Use **`pd.merge()`** to join `inventory_df` with the necessary columns from `lookup_df`.
    - Join on the **`'card_id'`** key using the **`how='left'`** method to keep all inventory items.
4.  **Final Cleaning**:
    - Fill any missing `card_market_value` with `0.0`.
    - Fill any missing `set_name` with the string `'NOT_FOUND'`.
5.  **Index Creation**: Create the final location index column, **`'index'`**, by concatenating the string versions of the location columns: `'binder_name'`, `'page_number'`, and `'slot_number'`.
6.  Define the `final_cols` list containing only the desired output columns.
7.  Write the final DataFrame to the `output_file` using **`.to_csv()`**, ensuring `index=False`.
8.  Print a success message.

<br>

### Public Interface and Execution Block

The script now uses defined public functions to clearly define the file paths and output names for both production and testing environments.

#### Function 4: `main()`
- **Purpose**: A public function that calls `update_portfolio` using the **production** directory paths (`./card_inventory/` and `./card_set_lookup/`) and the production output file (`card_portfolio.csv`).

#### Function 5: `test()`
- **Purpose**: A public function that calls `update_portfolio` using the **test** directory paths (`./card_inventory_test/` and `./card_set_lookup_test/`) and the test output file (`test_card_portfolio.csv`).

<br>

### Main Block: `if __name__ == "__main__":`

**What it does**: This block runs when the script is executed directly, setting the default execution mode.

1.  Print a message to `sys.stderr` indicating that the script is starting in **Test Mode**.
2.  Call the **`test()`** function.
3.  **Default Action**: The script's default behavior is to run the pipeline using the dedicated test directories and outputting the data to the test CSV file.

<br>

---

## Step 3: Python Script for Data Reporting - `generate_summary.py`
This script is purely a **reporting tool**. Its job is to ingest the single, final output file from the ETL pipeline and present key aggregated insights to the user.

<br>

### Function 1: `generate_summary(portfolio_file)`

**What it does**: This is the core logic that reads the completed portfolio CSV, performs the required summary calculations, and prints the simplified report to the console.

**Why it's a function**: Keeping the logic inside a function makes the code reusable (it can be called by other scripts) and allows the script to easily handle both the main portfolio and the test portfolio files via the public interface functions (`main()` and `test()`).

1.  Use an `if not os.path.exists()` check to verify the `portfolio_file` exists. If it doesn't, print an error message to `sys.stderr` and **exit the script** using `sys.exit(1)`.
2.  Read the CSV file into a DataFrame, `df`, using `pd.read_csv()`.
3.  Use an `if df.empty:` check to verify the file contains data. If the DataFrame is empty, print a message and **`return`** from the function.
4.  **Calculate Total Value**: Calculate the `total_portfolio_value` by summing the entire `card_market_value` column.
5.  **Find Most Valuable Card**: Find the entire row corresponding to the `most_valuable_card` by locating the index of the maximum value in the `card_market_value` column using `.idxmax()` and then using `.loc[]` to extract the row.
6.  **Print Report**: Print the final, simplified output strings for **Total Portfolio Value** and the **Most Valuable Card's** details (Name, ID, and Value). Use f-string formatting (e.g., `f"{variable:,.2f}"`) to format the currency values.

<br>

### Public Interface Functions

The script now uses defined public functions (`main()` and `test()`) to clearly define which portfolio file is used.

#### Function 2: `main()`
- **Purpose**: A public function that calls `generate_summary` using the **production portfolio file: `'card_portfolio.csv'`**.

#### Function 3: `test()`
- **Purpose**: A public function that calls `generate_summary` using the **test portfolio file: `'test_card_portfolio.csv'`**.

<br>

### Main Block: `if __name__ == "__main__":`

**What it does**: This block sets up the script's execution when it is called directly from the command line.

**Why it's separate**: This Python standard practice provides a clean entry point. It contains the logic for the script's default behavior, which is now to run in test mode for easy debugging.

1.  When the script is executed directly, this block simply calls the **`test()`** function.
2.  **Default Action**: The script's default behavior is now to use the **test file** (`test_card_portfolio.csv`). This is in alignment with the `Makefile`'s new `Test` target, where the script is expected to run a self-contained test without external API calls or production data.

<br>

---

## Step 4: One Python File to Rule Them All - `pipeline.py`

This script is the **master orchestration file** for the entire data workflow. Its sole purpose is to import and sequentially call the production functions from the two main components of your system: `update_portfolio.py` (the ETL step) and `generate_summary.py` (the reporting step). By centralizing the execution flow here, the `Makefile` becomes much simpler.

### Function 1: `run_production_pipeline()`

**What it does**: This function defines the exact sequence of steps for a full, production-ready data run.

**Why it's a function**: It encapsulates the full workflow logic, making the main execution block clean and easy to read.

1.  Print a starting message to standard error (`sys.stderr`) for logging clarity.
2.  **ETL Step**: Print a message for the update step, then call the **`update_portfolio.main()`** function. This executes the full data merge and writes the production CSV (`card_portfolio.csv`).
3.  **Reporting Step**: Print a message for the reporting step, then call the **`generate_summary.main()`** function. This reads the newly created production CSV and prints the final report to the console.
4.  Print a completion message to standard error.

<br>

### Main Block: `if __name__ == "__main__":`

**What it does**: This block serves as the single entry point for the entire pipeline when the script is executed directly (e.g., when `make Portfolio_Build` runs).

1.  This block simply calls the master function, **`run_production_pipeline()`**.
2.  **Default Action**: Running this script executes the entire production workflow from start to finish.

<br>

---

## Step 5: Orchestration with Makefile
The `Makefile` serves as the control center for the entire project, managing dependencies and providing a simple, consistent interface for running complex, multi-step tasks.

Because this pipeline requires a `Makefile` that is more complex than you need to know for the purposes of this class, I am going to provide all of the code for you to copy and paste but with explanations to go along with it. All you need to do is create a new file called `Makefile` in your `pokemon_lab/` directory.

### Variables Section
This section uses variables to define key file paths and names.
```Makefile
# --- Variables ---
PORTFOLIO_CSV := card_portfolio.csv
TEST_PORTFOLIO_CSV := test_card_portfolio.csv
```
Explanation:
- **Purpose**: Defining variables prevents repeating file names throughout the file. This makes the code easier to read and allows you to change a file name in one place (at the top) without breaking every target that uses it.
- **Syntax**: `VAR_NAME := value` assigns the value. You reference the variable later using `$(VAR_NAME)`.

<br>

### Phony and Default Targets
This section defines special non-file targets and the command that runs by default.
```Makefile
# --- Phony Targets ---
.PHONY: all Add_Set Refresh_Sets Portfolio_Build Clean Test

# --- Default Target ---
all: Portfolio_Build
```
Explanation:
- `.PHONY`: This is crucial. It tells Make that these targets (like `Clean` or `Portfolio_Build`) are not actual files to be built. If you didn't use `.PHONY`, and a file named `Clean` existed, `make Clean` would do nothing because Make would assume the "target" (the file) is already up-to-date.
- `all`: This is the default target. If a user simply types `make`, this target runs. We set it to run `Portfolio_Build`, as the user's primary goal is to execute the full data pipeline.

<br>

### Utility Targets
These are simple wrappers for our Bash scripts, providing a clean way to call them from the `Makefile`.
```Makefile
# --- Utility Targets ---

Add_Set:
    @echo "--- Adding New Card Set ---"
    @./add_card_set.sh

Refresh_Sets:
    @echo "--- Refreshing All Card Sets ---"
    @./refresh_card_sets.sh
```
Explanation:
- **`@` Symbol**: The `@` before a command prevents the command itself from being printed to the console (e.g., it prints "--- Adding New Card Set ---" but not `./add_card_set.sh`), keeping the output clean for the user.
- **Direct Execution**: These targets simply execute the corresponding shell scripts (`.sh`).

<br>

### Main Pipeline Targets
This is the core of the data pipeline, which consolidates all major steps into one comprehensive target.
```Makefile
# --- Main Pipeline Target ---

# Portfolio_Build: Executes interactive setup, runs the full production pipeline (update + summary).
Portfolio_Build: update_portfolio.py generate_summary.py pipeline.py
    @echo "--- Starting Portfolio Build Workflow ---"
    @echo "Do you want to add a NEW card set? (yes/no)"
    @read USER_ADD; \
    if [ "$$USER_ADD" = "yes" ]; then \
        $(MAKE) Add_Set; \
        echo "Card set added. Add another? (yes/no)"; \
        read USER_ADD_AGAIN; \
        if [ "$$USER_ADD_AGAIN" = "yes" ]; then \
            $(MAKE) Add_Set; \
        fi; \
    fi

    @echo "Do you want to refresh ALL existing card sets? (yes/no)"
    @read USER_REFRESH; \
    if [ "$$USER_REFRESH" = "yes" ]; then \
        $(MAKE) Refresh_Sets; \
    fi

    @# Execute the centralized pipeline (Update + Summary)
    @python ./pipeline.py
```
Explanation:
- **Dependencies**: The target lists the three main Python scripts (`update_portfolio.py`, `generate_summary.py`, and `pipeline.py`) as dependencies. This ensures they exist before running the target's commands.
- **User Interaction**: This section uses shell logic to prompt the user for input:
  - The `read` command captures user input into a variable (e.g., `USER_ADD`).
  - The `if [ "$$USER_ADD" = "yes" ]` logic executes based on that input.
- **Double Dollar Sign `($$USER_ADD)`**: This is essential. `make` itself substitutes variables starting with `$`, so you must escape one dollar sign (`$`) so the remaining one (`$`) is passed to the shell script for variable evaluation.
- **Calling Other Targets**: `$(MAKE) Add_Set` is the standard and most robust way to execute another target defined within the `Makefile`.
- **Final Step**: The entire ETL and reporting process is triggered by the single command: `@python ./pipeline.py`. This indicates the logic for merging, updating, and summarizing has been centralized into that script.

<br>

### Test and Clean Targets
These provide quick ways to run internal checks and wipe generated files.
```Makefile
# --- Testing Target ---

# Test: Runs the full process using built-in test modes and test data.
Test: update_portfolio.py generate_summary.py card_set_lookup_test/*.json
    @echo "--- Running Test Pipeline (Built-in Test Modes) ---"
    # 1. Run the update script (triggers test() function by default)
    @python ./update_portfolio.py
    # 2. Run the summary script (triggers test() function by default)
    @python ./generate_summary.py
    @echo "Test complete."

# --- Clean Target ---
Clean:
    @echo "--- Cleaning Generated Files ---"
    @rm -f $(PORTFOLIO_CSV) $(TEST_PORTFOLIO_CSV)
    @rm -f card_set_lookup/*.json
    @echo "Clean complete."
```
Explanation:
- **`Test` Dependencies**: This target lists the Python scripts and the test JSON files (in the `card_set_lookup_test/` directory) as dependencies, ensuring everything needed for testing exists.
- **Built-in Test Mode**: The `Test` target relies on the Python scripts (`update_portfolio.py` and `generate_summary.py`) having built-in testing logic. Running these scripts without special arguments triggers a `test()` function that uses the dedicated test data and outputs to the test CSV file (`$(TEST_PORTFOLIO_CSV)`). This keeps the `Makefile` clean by avoiding manual file management.
- **`Clean` Target**: This target simply uses the `rm -f` command to safely remove all files that were generated by the pipeline (`.csv` files and dynamically fetched `.json` files), leaving the source code intact. The `-f` flag ensures it doesn't fail if a file doesn't exist.

<br>

---

## Step 5: Running the Pipeline
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

## Step 6: Add, Commit, Push, and Submit on Canvas!

1.  Stage all of your changes at once: `git add .`.
2.  Commit your staged changes to your local `Lab_4` branch **with a message**: `git commit -m "Completed Lab 4"`
3.  Push your local branch to your remote repository: `git push --set-upstream origin Lab_4`
4.  Exit your Codespace and navigate to your forked repository on GitHub.
5.  Switch to your `Lab_4` branch on GitHub.
6.  Navigate to your `pokemon_lab` directory.
7.  Copy the URL to your `pokemon_lab` directory on your `Lab_4` branch, and paste the URL into the Lab 4 assignment on Canvas.
