# Activity 3: Bash Scripting
This activity guides you through creating a simple data pipeline using Bash scripts and a `Makefile`. You will use `curl` to fetch data from a public API, process it with `jq`, and perform a simple calculation.

<br>

### Follow these directions to ensure you have `chocolatey` (Windows) or `homebrew` (macOS) installed:
- [Windows Users](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/Windows_Users.md)
- [macOS Users](https://github.com/austin-t-rivera/DS-2002-F25/blob/main/Setup/macOS_Users.md)

<br>

### Make sure you have both `jq` and `make` installed:

**Windows Users**
- First confirm whether you have them installed by running `jq --version` and `make --version` in Git Bash.
- If you do not have one or both, run the following commands to install them:
```
choco install jq
```
```
choco install make
```

**macOS Users**
- First confirm whether you have them installed by running `jq --version` and `make --version` in Terminal.
- If you do not have one or both, run the following commands to install them:
```
brew install jq
```
```
brew install make
```

<br>

## Step 0. Setup
### Setup a logical file system:
1. Open your Git Bash (Windows) or Terminal (macOS).
2. Run `cd ~` to ensure you are in your home directory.
3. Use `cd` to navigate to your preferred `Documents` directory. (mine is here `/c/Users/atr8e/OneDrive/Documents/` for example)
4. Run `mkdir GitHub && cd GitHub` to create and enter into a directory named "GitHub".
5. In your web browser, pull up YOUR FORK of the class repository DS-2002-F25.
6. Click "Code", Select "SSH", Click "Copy url to clipboard"
7. Back in your terminal, type `git clone ` on your command line, paste the URL from GitHub, and hit Enter.
8. Run the following to ensure your repository is up-to-date:
```
git remote add upstream git@github.com:austin-t-rivera/DS-2002-F25.git
```
```
git fetch upstream
```
```
git merge upstream/main main
```

<br>

## Step 1: Set Up Your Project
1. If not already, open your Git Bash (Windows) or Terminal (macOS).
2. Use `cd` to navigate to your `DS-2002-F25` repository.
3. Use `cd` to further navigate to your `/Activities/Activity_03` directory.
4. Run `git checkout -b Activity_3` to create and move to a new branch named "Activity_3".
5. Create a new directory for this project and navigate into it:
```
mkdir bash_pipeline && cd bash_pipeline
```

## Step 2: Create the `fetch_data.sh` Script
This script will fetch a list of all dog breeds from the Dog CEO API and save the JSON output to a file.
1. Create a new file named `fetch_data.sh` using a text editor, `nano` or the `touch` command.
2. Add the following code to the file:

<br>

- A shebang, a special line that tells the operating system to execute this file using the `/bin/bash` interpreter.
```
#!/bin/bash
```

<br>

- The core command for this script, `curl`, which is used to make a web request. The `-s` flag means "silent," which suppresses `curl`'s progress bar. The `>` is a redirection operator that sends `curl`'s output (the JSON data) to a file named `breeds.json`.
```
# Fetch data from the Dog CEO API and save it to a file.
# We redirect standard output (1) to a file.
echo "Fetching all dog breeds..."
curl -s 'https://dog.ceo/api/breeds/list/all' > breeds.json
```

<br>

- A basic **conditional IF statement**. It checks the exit status of the previous command (`curl`). `$?` is a special variable that holds the exit status of the most recently executed command. An exit status of `0` means the command was successful.
```
if [ $? -eq 0 ]; then
    echo "Data fetched successfully and saved to breeds.json"
else
    echo "Error: Failed to fetch data." >&2
fi
```

3. Make the script executable `chmod +x fetch_data.sh`.

4. Test the script: `./fetch_data.sh`. You should see a file named `breeds.json` in your directory if you run `ls`.

<br>

## Step 3: Create the `process_data.sh` Script
This script will read the JSON file, use `jq` to extract the number of breeds, and print the result.

1. Create a new file named `process_data.sh`.

2. Add the following code to the file.

<br>

- Again, a shebang
```
#!/bin/bash
```

<br>

- This is a variable assignment. It stores the file name `breeds.json` in a variable named `DATA_FILE`. Using a variable makes the script more readable and easier to modify.
```
# A variable to store the name of our input file
DATA_FILE="breeds.json"
```

<br>

- This is a conditional statement that checks if a file exists. `! -f` checks for the negative: if the file (`-f`) does not (`!`) exist, an error message is printed to standard error (`>&2`), and the script exits with a non-zero status (`exit 1`), which signals a failure.
```
# Check if the data file exists
if [ ! -f "$DATA_FILE" ]; then
    echo "Error: Data file '$DATA_FILE' not found. Please run fetch_data.sh first." >&2
    exit 1
fi
```

<br>

- `NUM_BREEDS` is a command substitution. The entire command inside the `$(...)` is executed, and its standard output is captured and assigned to the variable `NUM_BREEDS`.
- Inside the `$(...)` is a `jq` command that performs the data processing. It takes the `message` field from the JSON, extracts its keys (which are the breed names), and then counts the number of keys using `length`. The output is the final number.
```
# Use jq to count the number of top-level keys in the 'message' field
# The output of jq is piped to wc -l to get the line count
echo "Processing data from '$DATA_FILE'..."
NUM_BREEDS=$(jq '.message | keys | length' "$DATA_FILE")
```

<br>

- This command prints the final result to the terminal, using the value stored in the `NUM_BREEDS` variable.
```
echo "Total number of unique dog breeds: $NUM_BREEDS"
```

<br>

3. Make the script executable: `chmod +x process_data.sh`.

4. Test the script: `./process_data.sh`. You should see the count of dog breeds.

## Step 4: Create a Makefile to Automate the Pipeline
The Makefile is a configuration file for the `make` utility. It orchestrates the execution of the other two scripts in the correct order.

1. Create a new file named `Makefile`.

2. Add the following code to the file. Note: The indentation for the recipe lines (e.g., `bash ./fetch_data.sh`) must be a tab, not spaces:

<br>

- This defines the default target for `make`. When you run `make` without any arguments, it will try to build `all`. `process_data` is a prerequisite, so `make` will first ensure `process_data` is up to date.
```
all: process_data
```

<br>

- This defines a target named `fetch_data`. It has no prerequisites, so it can be run directly. The indented lines below it are the recipe—the shell commands `make` will execute to fulfill this target.
```
# A rule to fetch the data
fetch_data:
	@echo "--- Fetching data ---"
	bash ./fetch_data.sh
```

<br>

- This defines the `process_data` target. It lists `fetch_data` as a prerequisite, which is critical. `make` will see this dependency and automatically run `fetch_data` before executing the `process_data` recipe. This ensures the data is downloaded before the processing script tries to read it.
```
# A rule to process the data, which depends on 'fetch_data'
process_data: fetch_data
	@echo "--- Processing data ---"
	bash ./process_data.sh
	@echo "--- Pipeline complete ---"
```

<br>

- This is a user-defined, conventional target. It's not part of the primary pipeline but provides a convenient way to remove all the generated files to reset the project. This target is often called a phony target because it doesn't create a file. The recipe uses the `rm -f` command to forcefully remove the `breeds.json` file.
```
# A rule to clean up the generated files
clean:
	@echo "--- Cleaning up ---"
	rm -f breeds.json
```

<br>

3. Run the full pipeline with a single command: `make`.

4. Clean up your workspace: `make clean`.

<br>

## Step 5: Add, Commit, Push, and Submit on Canvas!
1. Stage all of your changes at once: `git add .`.
2. Commit your staged changes to your local `Activity_3` branch **with a message**: `git commit -m ""`
3. Push your local branch to your remote repository: `git push --set-upstream origin Activity_3`
4. Navigate to your forked repository on GitHub.
5. Switch to your `Activity_3` branch on GitHub.
6. Navigate to your `bash_pipeline` directory.
7. Copy the URL to your `bash_pipeline` directory on your `Activity_3` branch, and paste the URL into the Activity 3 assignment on Canvas.
