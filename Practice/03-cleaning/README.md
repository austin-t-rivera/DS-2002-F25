# Cleaning data

## Convert Delimiters

To convert TSV to CSV, or vice versa, use a text search+replace function such as `awk`, `tr`, or a good IDE/text editor:

Use `tr`
```
tr '\t' ',' < file.tsv > file.csv
```

Use `sed`
```
sed 's/'$'\t''/,/g' file.tsv > file.csv
```

Use `awk`
```
awk 'BEGIN { FS="\t"; OFS="," } {$1=$1; print}' file.tsv > file.csv
```

This folder contains a CSV and TSV file. Try converting the format of one to another.

## Consuming Logs

[Parse/Filter Logs using Python](https://www.kaggle.com/nealmagee/parse-logs)

## Data Cleaning Exercises

Kaggle offers some data cleaning tutorials and exercises:

1. [Handing Missing Values](https://www.kaggle.com/alexisbcook/handling-missing-values)
2. [Scaling and Normalization](https://www.kaggle.com/alexisbcook/scaling-and-normalization)
3. [Parsing Dates](https://www.kaggle.com/alexisbcook/parsing-dates)
4. [Character Encoding](https://www.kaggle.com/alexisbcook/character-encodings)
5. [Inconsistent Data](https://www.kaggle.com/alexisbcook/inconsistent-data-entry)

