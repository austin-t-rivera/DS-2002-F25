# Lab 4: Building a Data Pipeline with Bash and Python

**Objective:** In this lab, you will build a sophisticated, multi-stage data pipeline using `curl`, Bash scripts, Python scripts, and `Makefile` automation. The lab is divided into three progressive versions, each introducing new concepts in data processing and orchestration.

---

<img width="250" height="342" alt="image" src="https://github.com/user-attachments/assets/ae3823f6-c73b-4f0e-a761-32c68d4e3caf" />
<img width="250" height="342" alt="image" src="https://github.com/user-attachments/assets/35d56fc3-35c1-41c4-b29a-095aa643aa42" />
<img width="250" height="342" alt="image" src="https://github.com/user-attachments/assets/194cfb72-a392-4e19-9cd5-d0d3a9238afc" />

---

Before starting the lab, I encourage you to spend a few minutes exploring the data so you know what you will be looking at:
- [Sample JSON](https://docs.pokemontcg.io/api-reference/cards/card-object#sample-json)
- [Sample CURL Code](https://docs.pokemontcg.io/api-reference/sets/search-sets#code-samples)
- [Sample End Product on Trading Site](https://www.tcgplayer.com/product/42346/pokemon-base-set-alakazam?page=1&Language=English)

<br>

---

## Step 0. Setup 

### Follow these directions to ensure you have `Python` and `PIP` installed and working in your environment:
- [Windows Users](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/Windows_Users/)
- [macOS Users](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/macOS_Users/)

<br>

### Navigate to your `DS-2002-F25` directory, update your `main` branch, and setup the Lab.
1. Open your Git Bash (Windows) or Terminal (macOS).

2. Navigate to your `DS-2002-F25` directory. For example: `cd ~/Documents/GitHub/DS-2002-F25/` (yours may differ)

3. Make sure that you do not have any unstaged or uncommitted stages by running `git status`. If you do, `add` and `commit` them.

4. Switch to your `main` branch `git checkout main`.

5. Run `git remote -v`:
   - If your upstream lists my repo `austin-t-rivera/DS-2002-F25.git` and your origin list your repo `<your-github-id>/DS-2002-F25.git`, proceed to step 6.
   - If your upstream lists your repo or does not exist, set my repo by running `git remote add upstream git@github.com:austin-t-rivera/DS-2002-F25.git` and continue in step 5.
     - Run `git fetch upstream` and continue in step 5.
     - Run `git merge upstream/main main` and proceed to step 6.

6. Run the `update_repo.sh` file and update at least your main branch.

7. Use `cd` to further navigate to your `/Labs/Lab_04` directory. If you do not have this directory, return to step 5 above.

8. Run `git checkout -b Lab_4_Branch` to create and move to a new branch named "Lab_4_Branch".

9. Create a new directory for this project and navigate into it by running:
```
mkdir pokemon_lab && cd pokemon_lab
```

<br>

---

## Step 1: The Foundational Pipeline 🚀

### Scenario
Building off of what we did in Activity 4, you still want to understand the value of your inheretance, a binder of Pokémon cards from your older cousin Austin! Because you want to simplify and automate this process, you are building an application to track the market prices of your new Pokémon cards. Your first task is to create a reliable and repeatable data pipeline that can pull card data from an API, process it, and output the results to a CSV file.

### 1.1 Create Your Test Data
Before you dive in and start developing, you know that you will first want some simple reliable data to work with, so you put together a JSON file that has a few cards and their information that you pulled by manually searching on TCG Player. You do this by creating a small, local JSON file named `test_cards.json` with the following content. (NOTE: This will serve as a mock API response, allowing you to test your Python script in isolation.)

```
{
  "data": [
    {
      "id": "base1-1",
      "name": "Alakazam",
      "set": { "name": "Base Set" },
      "rarity": "Rare Holo",
      "tcgplayer": { "prices": { "holofoil": { "market": 65.50 } } }
    },
    {
      "id": "base1-4",
      "name": "Charizard",
      "set": { "name": "Base Set" },
      "rarity": "Rare Holo",
      "tcgplayer": { "prices": { "holofoil": { "market": 250.75 } } }
    },
    {
      "id": "base1-10",
      "name": "Pikachu",
      "set": { "name": "Base Set" },
      "rarity": "Common"
      "tcgplayer": { "prices": { "holofoil": { "market": 50.15 } } }
    }
  ]
}
```

### 1.2 Create Your Processing Script (`process_cards.py`)

This Python script will read JSON from standard input, parse it, and write a CSV to standard output. The use of a `main` function and a `__main__` block allows you to test it easily.

**Local Testing with a `__main__` Block:** A key practice in professional software development is making your scripts modular and testable. The `if __name__ == __main__`: block allows you to write code that only runs when the script is executed directly, which is perfect for local testing.

1. Create a file named `process_cards.py` and make it executable.

2. Add the appropriate `shebang` at the top of your file.

3. Import the following libraries: `sys`, `json`, `csv`

4. Different than Activity_4, we will be using an `input_stream` instead of `sys.stdin` to process the data as it comes in, rather than as a batch.
```
def process_data(input_stream):
    """
    Reads JSON from an input stream, processes it, and writes a CSV to stdout.
    """
    try:
        data = json.loads(input_stream.read())
    except json.JSONDecodeError:
        print("Error: Invalid JSON received.", file=sys.stderr)
        sys.exit(1)
```

5. Just like we did in Activity_4, define the `fieldnames` we care about and create a `writer` object that will write the `stdout`.

6. Set a `cards` variable to extract the actual data from the file using `cards = data.get('data', [])` or `cards = data['data']`.

7. Just like we did in Activity_4, create a `for` loop to write the data into our CSV format.

8. Lastly, have this script which contains a `main()` function, which we called "`process_data(f)`", that handles the processing, and a `__main__` block that calls it, allowing you to test it with your local JSON file. You can just copy and paste this code at the bottom of your script:
```
if __name__ == "__main__":
    # This block of code runs only when the script is executed directly, not when imported.
    # It allows for local testing with a static file without a live API call.
    with open('test_cards.json', 'r') as f:
        process_data(f)
    print("\nTest run complete. Check your terminal for the CSV output.", file=sys.stderr)
```

### 1.2 The Makefile (Version 1)
This is the **first version** of your Makefile. It defines a single target, `cards.csv`, which runs the full pipeline. It uses the `read` command to make the API call interactive.

1. Create a file named `Makefile`.

2. Copy and paste the following into the file. The `@` symbol at the beginning of a line prevents `make` from echoing the command before it is executed, keeping the output clean.
```
.PHONY: all clean

all: test_cards

# This target prompts the user for API parameters and builds the URL dynamically.
test_cards:
	@echo "Enter the Card Set ID (e.g., base1, swsh1): "
	@read SET_ID
	@echo "Enter the page number (e.g., 1): "
	@read PAGE_NUM
	@echo "Enter the page size (e.g., 20): "
	@read PAGE_SIZE
	@curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$(SET_ID)&page=$(PAGE_NUM)&pageSize=$(PAGE_SIZE)" | python ./process_cards.py > test_cards.csv

# This target cleans up generated files.
clean:
	@rm -f test_cards.csv
```

3. Run the pipeline with `make`.
```bash
make
```

---

### Version 2: Processing a Local Dataset 📁

In this version, you will simulate a different scenario: processing a large, pre-existing JSON file that contains your "binder of cards." This requires a new Bash script and a new `Makefile` target.

### 2.1 The Binder Data (`binder.json`)
First, create the large dataset you will work with. This JSON file contains a sample of a few card IDs. This file simulates a local inventory of cards.

1. Create a file named `binder.json`.

2. Copy and paste the following content into the file.
` ` `json
[
    "base1-1",
    "base1-4",
    "base1-10",
    "base1-15",
    "base1-1",
    "base1-1"
]
` ` `

### 2.2 The Makefile (Version 2)
This is the **second version** of your Makefile. It includes the new target `inventory.csv`. This target will create a list of your card inventory.

1. Replace the contents of your `Makefile` with the following.
` ` `Makefile
.PHONY: all clean

all: cards.csv inventory.csv

cards.csv:
	@echo "Enter the Card Set ID (e.g., base1, swsh1): "
	@read SET_ID
	@echo "Enter the page number (e.g., 1): "
	@read PAGE_NUM
	@echo "Enter the page size (e.g., 20): "
	@read PAGE_SIZE
	@curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$(SET_ID)&page=$(PAGE_NUM)&pageSize=$(PAGE_SIZE)" | ./process_cards.py > cards.csv

# This target creates a clean inventory list from the local binder data.
inventory.csv: binder.json
	@echo "Creating inventory list..."
	@cat binder.json | jq -r '.[]' > inventory.csv

# This target cleans up generated files.
clean:
	@rm -f test_cards.json cards.csv inventory.csv
` ` `

2. Run the full pipeline with `make`.
` ` `bash
make
` ` `

---

### Version 3: The Portfolio Pipeline 📈

In this final version, you'll create a second pipeline to enrich your `inventory.csv` with live pricing data from the API and calculate your portfolio's total value. This demonstrates chaining pipelines and performing advanced calculations within a script.

### 3.1 The Portfolio Script (`update_portfolio.py`)
This new Python script will use the `requests` library to make API calls to get live pricing data. It will first read your inventory list, count the number of each card, and then perform API calls to get the most up-to-date market price.

1. Create a new Python file named `update_portfolio.py` and make it executable.
2. Install the necessary library: `pip install requests`
3. Copy and paste the following code into the file.
` ` `python
#!/usr/bin/env python3

import sys
import csv
import requests
from collections import Counter

def get_live_price(card_id):
    """Fetches a single card's market price from the API using the requests library."""
    api_url = f"https://api.pokemontcg.io/v2/cards/{card_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data.get('data', {}).get('tcgplayer', {}).get('prices', {}).get('holofoil', {}).get('market', 0)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price for card ID {card_id}: {e}", file=sys.stderr)
        return 0

def calculate_portfolio():
    """Reads inventory, fetches prices, and calculates portfolio value."""
    # Count the number of each card in the inventory
    with open('inventory.csv', 'r') as infile:
        card_counts = Counter(line.strip() for line in infile)
        
    total_portfolio_value = 0
    
    # Open the new portfolio CSV for writing
    with open('portfolio.csv', 'w', newline='') as outfile:
        fieldnames = ['card_id', 'count', 'price_per_card', 'total_value']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Process each unique card in the inventory
        for card_id, count in card_counts.items():
            price = get_live_price(card_id)
            total_value = price * count
            total_portfolio_value += total_value
            
            # Write to the new portfolio CSV
            writer.writerow({
                'card_id': card_id,
                'count': count,
                'price_per_card': f"{price:.2f}",
                'total_value': f"{total_value:.2f}"
            })
    
    print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")

if __name__ == "__main__":
    calculate_portfolio()
` ` `

### 3.2 The Portfolio Script with `subprocess` (`update_portfolio_curl.py`)
This script accomplishes the same task as the previous one, but it leverages `curl` via a `subprocess`. This demonstrates how to combine the power of an external command-line tool with Python's data processing capabilities.

1. Create a new Python file named `update_portfolio_curl.py` and make it executable.

2. Copy and paste the following code into the file.
` ` `python
#!/usr/bin/env python3

import sys
import csv
import json
import subprocess
from collections import Counter

def get_live_price_curl(card_id):
    """Fetches a single card's market price using a subprocess to run curl."""
    api_url = f"https://api.pokemontcg.io/v2/cards/{card_id}"
    try:
        result = subprocess.run(
            ['curl', '-s', api_url],
            capture_output=True,
            text=True,
            check=True
        )
        data = json.loads(result.stdout)
        return data.get('data', {}).get('tcgplayer', {}).get('prices', {}).get('holofoil', {}).get('market', 0)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        print(f"Error fetching price with curl for card ID {card_id}: {e}", file=sys.stderr)
        return 0

def calculate_portfolio_curl():
    """Reads inventory, fetches prices with curl, and calculates portfolio value."""
    # Count the number of each card in the inventory
    with open('inventory.csv', 'r') as infile:
        card_counts = Counter(line.strip() for line in infile)
        
    total_portfolio_value = 0
    
    # Open the new portfolio CSV for writing
    with open('portfolio_curl.csv', 'w', newline='') as outfile:
        fieldnames = ['card_id', 'count', 'price_per_card', 'total_value']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Process each unique card in the inventory
        for card_id, count in card_counts.items():
            price = get_live_price_curl(card_id)
            total_value = price * count
            total_portfolio_value += total_value
            
            # Write to the new portfolio CSV
            writer.writerow({
                'card_id': card_id,
                'count': count,
                'price_per_card': f"{price:.2f}",
                'total_value': f"{total_value:.2f}"
            })
    
    print(f"Total Portfolio Value: ${total_portfolio_value:.2f}")

if __name__ == "__main__":
    calculate_portfolio_curl()
` ` `

### 3.3 The Makefile (Version 3)
This is the **final version** of your Makefile. The `all` target now depends on two portfolio files, and the `clean` target is updated to remove them.

1. Replace the contents of your `Makefile` with the following.
` ` `Makefile
.PHONY: all clean

all: cards.csv portfolio.csv portfolio_curl.csv

cards.csv:
	@echo "Enter the Card Set ID (e.g., base1, swsh1): "
	@read SET_ID
	@echo "Enter the page number (e.g., 1): "
	@read PAGE_NUM
	@echo "Enter the page size (e.g., 20): "
	@read PAGE_SIZE
	@curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$(SET_ID)&page=$(PAGE_NUM)&pageSize=$(PAGE_SIZE)" | ./process_cards.py > cards.csv

inventory.csv: binder.json
	@echo "Creating inventory list..."
	@cat binder.json | jq -r '.[]' > inventory.csv

portfolio.csv: inventory.csv
	@echo "Updating portfolio with live prices using requests..."
	@./update_portfolio.py

portfolio_curl.csv: inventory.csv
	@echo "Updating portfolio with live prices using curl and subprocess..."
	@./update_portfolio_curl.py

# This target cleans up generated files.
clean:
	@rm -f test_cards.json cards.csv inventory.csv portfolio.csv portfolio_curl.csv
` ` `

---

### Step 4: Add, Commit, Push, and Submit on Canvas!
1. Stage all of your changes at once: `git add .`.
2. Commit your staged changes to your local `Lab_4` branch **with a message**: `git commit -m "Complete Lab 4"`
3. Push your local branch to your remote repository: `git push --set-upstream origin Lab_4`
4. Navigate to your forked repository on GitHub.
5. Switch to your `Lab_4` branch on GitHub.
6. Navigate to your `pokemon_lab` directory.
7. Copy the URL to your `pokemon_lab` directory on your `Lab_4` branch, and paste the URL into the Lab 4 assignment on Canvas.
