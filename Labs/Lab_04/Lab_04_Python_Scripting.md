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

### Scenario
Building off of what we did in Activity 4, you still want to understand the value of your inheretance, a binder (or two?!) of Pokémon cards from your older cousin Austin! Because you want to simplify and automate this process, you are building an application to track the market prices of your new Pokémon cards. Your first task is to create a reliable and repeatable data pipeline that can pull card data from an API, process it, and output the results to a CSV file.

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

1.2 `refresh_card_sets.sh` (Batch Fetch)
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












