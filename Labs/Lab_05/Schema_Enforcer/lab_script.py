#!/usr/bin/env python3
"""
lab_script.py

Creates messy raw data files (CSV, JSON), cleans/normalizes them with pandas,
and writes out cleaned CSVs and schema markdown files.

Outputs:
- raw_survey_data.csv
- raw_course_catalog.json
- clean_survey_data.csv
- clean_course_catalog.csv
- survey_schema.md
- catalog_schema.md
"""

import csv
import json
from pathlib import Path
import pandas as pd

DATA_DIR = Path(".")  # change if you want files somewhere else

def create_raw_survey_csv(path: Path):
    """
    Creates a tabular CSV with intentional type inconsistencies:
    - student_id should be INT
    - major should be STRING
    - GPA should be FLOAT but some values saved as integers
    - is_cs_major should be BOOL but stored as 'Yes'/'No'
    - credits_taken should be FLOAT but stored as strings
    """
    rows = [
        # headers: student_id, major, GPA, is_cs_major, credits_taken
        # Intentionally mixing types/formats
        {"student_id": 1001, "major": "Computer Science", "GPA": 3.8, "is_cs_major": "Yes", "credits_taken": "45.0"},
        {"student_id": 1002, "major": "Economics", "GPA": 3,   "is_cs_major": "No",  "credits_taken": "30"},
        {"student_id": 1003, "major": "Mathematics", "GPA": "3.5", "is_cs_major": "No", "credits_taken": "60.5"},
        {"student_id": "1004", "major": "Physics", "GPA": 4,    "is_cs_major": "Yes", "credits_taken": "15.0"},
        {"student_id": 1005, "major": "Data Science", "GPA": "3", "is_cs_major": "Yes", "credits_taken": "10.5"},
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["student_id", "major", "GPA", "is_cs_major", "credits_taken"])
        writer.writeheader()
        for r in rows:
            # write exactly as-is to preserve type inconsistencies (csv writes everything as text)
            writer.writerow(r)
    print(f"Created raw CSV at {path.resolve()}")

def create_raw_course_json(path: Path):
    """
    Creates hierarchical JSON for courses with nested 'instructors' lists.
    At least two courses and some with multiple instructors.
    """
    courses = [
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
            "course_id": "ECON3100",
            "section": "002",
            "title": "Econometrics I",
            "level": 300,
            "instructors": [
                {"name": "Patricia Gomez", "role": "Primary"}
            ]
        },
        {
            "course_id": "DS3001",
            "section": "001",
            "title": "Machine Learning Fundamentals",
            "level": 300,
            "instructors": [
                {"name": "Charlie Bucket", "role": "Primary"},
                {"name": "Zara White", "role": "TA"}
            ]
        }
        # add more courses if you like
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(courses, f, indent=2)
    print(f"Created raw JSON at {path.resolve()}")

def clean_survey_csv(raw_path: Path, clean_path: Path):
    """
    Loads raw CSV with pandas, enforces types:
    - student_id -> int
    - major -> string (VARCHAR-like)
    - GPA -> float
    - is_cs_major -> bool (map 'Yes'/'No' to True/False)
    - credits_taken -> float (some values were strings)
    Saves cleaned DataFrame to clean_path.
    """
    df = pd.read_csv(raw_path, dtype=str)  # read as strings first to be robust
    # Show what we got (optional)
    print("Raw survey CSV loaded with dtypes:")
    print(df.dtypes)
    # Trim whitespace
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # student_id -> int (some were strings)
    df["student_id"] = df["student_id"].astype(int)

    # major -> string (keep as object / string)
    df["major"] = df["major"].astype(str)

    # GPA -> float (some entries like '3' or 4)
    df["GPA"] = df["GPA"].astype(float)

    # is_cs_major -> bool (map 'Yes'/'No', case-insensitive)
    df["is_cs_major"] = df["is_cs_major"].str.strip().str.lower().map({"yes": True, "no": False})
    # If there were unexpected values, leave them as False or raise; here we coerce NaN -> False explicitly:
    df["is_cs_major"] = df["is_cs_major"].fillna(False).astype(bool)

    # credits_taken -> float (some were strings like '30' or '10.5')
    # remove possible commas, then convert
    df["credits_taken"] = df["credits_taken"].astype(float)

    # Reorder columns and save
    df = df[["student_id", "major", "GPA", "is_cs_major", "credits_taken"]]
    df.to_csv(clean_path, index=False)
    print(f"Saved cleaned survey CSV at {clean_path.resolve()}")
    print("Cleaned dtypes:")
    print(df.dtypes)
    return df

def normalize_course_json(raw_json_path: Path, clean_csv_path: Path):
    """
    Loads raw course JSON and normalizes 'instructors' using pd.json_normalize with record_path
    so that each instructor becomes a row, carrying meta fields course_id, section, title, level.
    """
    with raw_json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # Normalize instructors
    df = pd.json_normalize(data, record_path=["instructors"], meta=["course_id", "section", "title", "level"])
    # rename columns to be clear
    # json_normalize will typically create columns 'name', 'role', 'course_id', etc.
    df = df.rename(columns={"name": "instructor_name", "role": "instructor_role"})

    # Ensure types (e.g., level -> int)
    df["level"] = df["level"].astype(int)
    df["course_id"] = df["course_id"].astype(str)
    df["section"] = df["section"].astype(str)
    df["title"] = df["title"].astype(str)
    df["instructor_name"] = df["instructor_name"].astype(str)
    df["instructor_role"] = df["instructor_role"].astype(str)

    df.to_csv(clean_csv_path, index=False)
    print(f"Saved normalized course CSV at {clean_csv_path.resolve()}")
    print("Normalized course DataFrame head:")
    print(df.head())
    return df

def write_survey_schema_md(path: Path):
    """
    Writes survey_schema.md describing the final clean schema.
    Use standard DB types: INT, VARCHAR(X), BOOL, FLOAT
    """
    content = """# Survey Table Schema

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | `INT` | Unique identifier for the student. |
| `major` | `VARCHAR(100)` | Student's declared major. |
| `GPA` | `FLOAT` | Grade point average on a 4.0 scale. |
| `is_cs_major` | `BOOL` | Whether the student is a CS major (True/False). |
| `credits_taken` | `FLOAT` | Total credits the student has completed. |
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote survey schema markdown to {path.resolve()}")

def write_catalog_schema_md(path: Path, normalized_df: pd.DataFrame):
    """
    Writes catalog_schema.md describing the normalized catalog schema.
    Uses column names from normalized_df.
    """
    # Build table rows by iterating normalized_df columns and describing them
    rows = []
    # Decide types for expected columns
    col_type_map = {
        "course_id": "VARCHAR(20)",
        "section": "VARCHAR(10)",
        "title": "VARCHAR(200)",
        "level": "INT",
        "instructor_name": "VARCHAR(100)",
        "instructor_role": "VARCHAR(50)"
    }

    for col in normalized_df.columns:
        dtype = col_type_map.get(col, "VARCHAR(200)")
        description = ""
        if col == "course_id":
            description = "Course identifier (e.g., DS2002)."
        elif col == "section":
            description = "Course section identifier (e.g., 001)."
        elif col == "title":
            description = "Full course title."
        elif col == "level":
            description = "Course level as integer (e.g., 200, 300)."
        elif col == "instructor_name":
            description = "Instructor full name."
        elif col == "instructor_role":
            description = "Instructor role (e.g., Primary, TA)."
        else:
            description = "Field description goes here."

        rows.append(f"| `{col}` | `{dtype}` | {description} |")

    content = "# Catalog (Normalized) Table Schema\n\n"
    content += "| Column Name | Required Data Type | Brief Description |\n"
    content += "| :--- | :--- | :--- |\n"
    content += "\n".join(rows) + "\n"

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote catalog schema markdown to {path.resolve()}")

def main():
    raw_csv = DATA_DIR / "raw_survey_data.csv"
    raw_json = DATA_DIR / "raw_course_catalog.json"
    clean_csv = DATA_DIR / "clean_survey_data.csv"
    clean_courses_csv = DATA_DIR / "clean_course_catalog.csv"
    survey_md = DATA_DIR / "survey_schema.md"
    catalog_md = DATA_DIR / "catalog_schema.md"

    create_raw_survey_csv(raw_csv)
    create_raw_course_json(raw_json)

    cleaned_survey_df = clean_survey_csv(raw_csv, clean_csv)
    normalized_course_df = normalize_course_json(raw_json, clean_courses_csv)

    write_survey_schema_md(survey_md)
    write_catalog_schema_md(catalog_md, normalized_course_df)

    print("\nAll files created:")
    for p in [raw_csv, raw_json, clean_csv, clean_courses_csv, survey_md, catalog_md]:
        print(" -", p.resolve())

if __name__ == "__main__":
    main()
