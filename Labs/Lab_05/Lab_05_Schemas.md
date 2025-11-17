# Lab 5: Schema - The Data Contract Enforcer

---

<img width="400" height="250" alt="image" src="https://github.com/user-attachments/assets/6fd8c9ee-10ec-4ae5-9a64-09fb5b713644" />
<img width="330" height="250" alt="image" src="https://github.com/user-attachments/assets/4ff82e6a-c741-4660-b3c9-8d8f3d650b2d" />
<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/7a0ccd4f-0470-437d-927c-24300ee2b725" />

---

<br>

In this lab, you'll move from simply extracting and transforming data to the critical Data Management step of **Data Validation and Schema Enforcement**. You will create two separate synthetic datasets, enforce strict data typing on the resulting data, and formally document the final, clean schema for each.

The goal is to understand that clean data is not the default; it must be **enforced** via a schema, and that data structure (tabular vs. hierarchical) dictates how that enforcement works.

<br>

## Step 0. Setup

### Update your `main` branch and open up a new Codespace in GitHub

1.  Go to **your** forked `DS-2002-F25` repo in GitHub and make sure you are looking at your `main` branch.

2.  To open a Codespace, to the right, you can click on `<> Code`, then `Codespaces`, and lastly `Create codespace on main` or the `+` if this isn't your first rodeo since we did Activity_5.
    - NOTE: You are now in your VS Code Codespace! This is a container that is built for you to work in that has essentially all of the functionality of a high-powered IDE, in this case VS Code, but is also fully integrated into your GitHub!

4.  Within your Codespace, in the Terminal (bottom center), run the `update_repo.sh` file to update your `main` branch. (OPTIONAL: Follow the prompts in the script to update your other branches if you'd like!)

5.  Use `cd` to navigate to your `/Labs/Lab_05` directory, where you should see this file `Lab_05_Schemas.md` if everything is up-to-date.

6.  Create and move into a new branch called `Lab_5` by running `git checkout -b Lab_5`.

7.  Create a new directory for this project, within the `Labs/Lab_05/` directory, and navigate into it:
    ```bash
    mkdir Schema_Enforcer && cd Schema_Enforcer
    ```

<br>

### Install Dependencies and Create Script

1.  Create a new Python file (`.py`) or Jupyter Notebook (`.ipynb`) named **`lab_script`** (e.g., `lab_script.py` or `lab_script.ipynb`). All code for Parts 1 and 2 will go here.
2.  Install the `Python` and `Jupyter` extensions.

<br>

---

## Part 1: Acquisition and Flexible Formatting

**Goal:** Simulate receiving two different streams of data that intentionally have structural and data-type issues.

### Task 1: Create the Tabular CSV Data (Requires Cleaning)

1.  In your `lab_script`, use Python to create a list of data that is **tabular** but contains type inconsistencies. You can use the standard `csv` module or just Python's built-in file writing.

2.  **Data Requirements:** Create a dataset with at least five (5) records and **five (5) columns**:
    * `student_id` (Should be $\text{INT}$)
    * `major` (Should be $\text{STRING}$)
    * `GPA` (Should be $\text{FLOAT}$): **Intentionally save some values as integers (e.g., `3` instead of `3.0`).**
    * `is_cs_major` (Should be $\text{BOOL}$): **Intentionally use the strings 'Yes' or 'No'.**
    * `credits_taken` (Should be $\text{FLOAT}$): **Intentionally save the value as a string (e.g., `'10.5'`).**

3.  Write this data to a CSV file named **`raw_survey_data.csv`**.

    ```python
    # HINT: Use the 'csv' module with 'writer' or 'DictWriter', 
    # or just simple Python file I/O with .write() to save the data.
    # Be sure to include headers in your first row!
    ```

<br>

### Task 2: Create the Hierarchical JSON Data (Requires Normalization)

1.  In your `lab_script`, define a list of dictionaries that is **hierarchical** (nested) using the structure below.

2.  **Data Requirements:** Use the following structure to create a list of dictionaries for all of your courses this semester (at least two courses):
    ```json
    [
      {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
          {"name": "Austin Rivera", "role": "Primary"}, 
          {"name": "Heywood Williams-Tracy", "role": "TA"} 
        ]
      },
      {
        "course_id": "DS9999",
        "title": "Example Course Replace with One of yours",
        "level": 300,
        "instructors": [
          {"name": "Charlie Bucket", "role": "Primary"}
        ]
      },
      // ... include the rest of your courses here
    ]
    ```

3.  Write this structure to a JSON file named **`raw_course_catalog.json`**.

    ```python
    # HINT: Use the 'json' module's 'dump' function to write the data to the file.
    ```

<br>

---

## Part 2: Data Validation and Type Casting

**Goal:** Use Python and Pandas to enforce a clean, rigid schema, preparing the data for a database.

### Task 3: Clean and Validate the CSV Data

1.  In your `lab_script`, use `pandas` to load `raw_survey_data.csv` into a DataFrame.

    ```python
    # HINT: Use pd.read_csv()
    ```

2.  **Enforce Boolean Type:** Write a function or use a custom map/replace to convert the values in the `is_cs_major` column from the strings (`'Yes'`, `'No'`) to proper Python Boolean types (`True`, `False`).

    ```python
    # HINT: Use the .replace() or .apply() method on the DataFrame column.
    ```

3.  **Enforce Numeric Type:** Use the appropriate `pandas` function (e.g., `.astype()`) to explicitly ensure both the **`credits_taken`** and **`GPA`** columns are stored as a **float** type.

    ```python
    # HINT: Use the .astype() method on the columns and pass a dictionary 
    # like: {'column_name': 'float64'}
    ```

4.  Save the cleaned DataFrame to a new file named **`clean_survey_data.csv`**.

    ```python
    # HINT: Use the DataFrame's .to_csv() method.
    ```

<br>

### Task 4: Normalize the JSON Data

1.  In your `lab_script`, use the standard `json` module to load the `raw_course_catalog.json` file.

    ```python
    # HINT: Use the json.load() function.
    ```

2.  **Normalize:** Use **`pd.json_normalize`** to flatten the hierarchical data into a single, wide DataFrame.
    * **CRITICAL:** Use the **`record_path`** argument to specifically extract the nested **`instructors`** list. This will result in multiple rows for the courses that have multiple instructors (one row per instructor).

    ```python
    # HINT: pd.json_normalize(data, record_path=['instructors'], meta=['course_id', 'title', 'level'])
    ```

3.  Save the normalized DataFrame to a new file named **`clean_course_catalog.csv`**.

    ```python
    # HINT: Use the DataFrame's .to_csv() method.
    ```

<br>

---

## Part 3: The Schema Contract

**Goal:** Formally document the final, clean, and enforced schema for your data. This is what you would hand to a database administrator.

### Task 5: Document the Tabular Schema

1.  Examine the final, cleaned data in your `clean_survey_data.csv`.

2.  In a new markdown file named **`survey_schema.md`**, formally document the final, clean schema using the format below. Use the standard database types listed (INT, VARCHAR, BOOL, FLOAT).

**NOTE**: If a field is a VARCHAR (i.e. a STRING), you must define a reasonable size for the field by indicating a max number of characters, `VARCHAR(X)`. For example, if we have a table of fruit and we have set it to VARCHAR(8), that will work for many fruits like `apple`, `orange`, `banana`, etc. However, `Strawberry` is 10 characters long and would eeither fail or get truncated! We don't want to have to eat a `Strawber`! So then `VARCHAR(10)`? BUT WHAT ABOUT `dragonfruit`?! A good rule of thumb is to think of a reasonable max and then double it. So I think there is likely a 25 character multi-word fruit out there, so I will double 25 and choose `VARCHAR(50)`. Why not go for something like 100? Well because that's just wasteful and we still want to be mindful of the space we are taking up for efficiency, conservation, and we want to catch errors, we don't want anything being in there like `bananananananananananananananananananananananananananananananananananananananananananananananananana`!

Your table should look like the following, with the information filled out (I did the first one for you):
| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | `INT` | Unique identifier for the student. |
| `major` | `DataType` | Brief Description Goes Here. |
| `GPA` | `DataType` | Brief Description Goes Here. |
| `is_cs_major` | `DataType` | Brief Description Goes Here. |
| `credits_taken` | `DataType` | Brief Description Goes Here. |

And in the file itself, you will use this format to create the table. When you look at the preview markdown file in Codespace, it will pretty it up. Once pushed you will be able to see the preview more easily in GitHub.
```
| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | `INT` | Unique identifier for the student. |
| `major` | `DataType` | Brief Description Goes Here. |
| `GPA` | `DataType` | Brief Description Goes Here. |
| `is_cs_major` | `DataType` | Brief Description Goes Here. |
| `credits_taken` | `DataType` | Brief Description Goes Here. |
```

<br>

### Task 6: Document the Normalized Catalog Schema

1.  Examine the flattened data in your `clean_course_catalog.csv`. Note the column names created by the `json_normalize` function (e.g., `instructors.name` might become `instructors.name` or `name` depending on the arguments you used).

2.  In a markdown file named **`catalog_schema.md`**, document the schema for this **normalized** data. You must include **all** columns in your final DataFrame.

<br>

---

## Step 5: Add, Commit, Push, and Submit on Canvas!

1.  Stage all of your changes at once: `git add .`.
2.  Commit your staged changes to your local `Lab_5` branch **with a message**: `git commit -m "Completed Lab 5: Schema Contract Enforcer"`
3.  Push your local branch to your remote repository: `git push --set-upstream origin Lab_5`
4.  Exit your Codespace and navigate to your forked repository on GitHub.
5.  Switch to your `Lab_5` branch on GitHub.
6.  Navigate to your `Schema_Enforcer` directory.
7.  Copy the URL to your `Schema_Enforcer` directory on your `Lab_5` branch, and paste the URL into the Lab 5 assignment on Canvas.

**Expected Files in the `Schema_Enforcer` Directory:**

* **`lab_script.py`** or **`lab_script.ipynb`**
* `raw_survey_data.csv`
* `raw_course_catalog.json`
* **`clean_survey_data.csv`**
* **`clean_course_catalog.csv`**
* **`survey_schema.md`**
* **`catalog_schema.md`**
