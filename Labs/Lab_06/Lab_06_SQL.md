# Lab 6 - Structured Query Language (SQL)

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/108deaed-0886-4a45-a19a-6b1903581642" />
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/fb2cfcb8-925a-4316-9eb6-85e030bacdf4" />

<br>

<br>

Historically, SQL keywords were capitalized to visually distinguish them from table and column names because early computer terminals lacked syntax highlighting.

Today, modern SQL tools and IDEs like DBeaver automatically color-code keywords, making the uppercase convention no longer strictly necessary for readability or function, as SQL is generally case-insensitive. While many style guides maintain the practice for tradition and visual contrast, writing keywords in lowercase is now widely accepted.

<br>

---

## Objective
This lab will take you through two (2) exercises, will be more involved than the last couple of labs, but will give you a wide range and wealth of experience using SQL.
  - Part 1 will consist of guiding you through making your own table and then querying that table to get some results.
  - Part 2 will have you ingest a database and explore it, testing your SQL skills with increasing complexity.
The Relational Database Management System (RDBMS) we will be using is SQLite. As the name suggests, SQLite is a lightweight RDBMS that is incredibly useful for working with local data. So we have talked about RDBMSs like MySQL, Oracle, PostgreSQL, etc., which are server-based. To simply things and get you exposure to SQL and querying, we will not worry about setting up and configuring the appropriate configurations that are needed for a server-based RDBMS.

<br>

---

## SUBMITTING WORK
  - You will create one (1) GitHub Gist.
  - Please use the template below as a means of filling out the Gist:
    - For some problems, I will just want the SQL query, for some I will want the result from running the query. Make sure you read carefully, so you know which to put.
  - PART 1 only requires you to copy and past the query and output from the directions under the section "Your Turn".
    - Formatting for the results is very lenient, I just want to see them there.

```Markdown
################################################
#################### PART 1 ####################
################################################
QUERY:
<paste query here>

RESULT:
<paste/type result here>

################################################
#################### PART 2 ####################
################################################

#### Basic Queries
1. QUERY:
<paste query here>

2. QUERY:
<paste query here>

3. RESULT: <paste/type result here>

4. RESULT: <paste/type result here>

5. QUERY:
<paste query here>

#### Intermediate Queries
6. QUERY:
<paste query here>

7. QUERY:
<paste query here>

8. QUERY:
<paste query here>

9. RESULT: <paste/type result here>

10. QUERY:
<paste query here>

#### Advanced Queries
11. RESULT: <paste/type result here>

12. QUERY:
<paste query here>

13. RESULT: <paste/type result here>

14. QUERY:
<paste query here>

15. QUERY:
<paste query here>


```

<br>

---

## Setting Up Your IDE (DBeaver)
NOTE: You may use any IDE that supports SQLite if you have a preference.

1. Download and Install: Download [**DBeaver Community Edition**](https://dbeaver.io/download/) (it's free and open-source) from the DBeaver website and install it by opening the downloaded file and following the install instructions.

2. Create a New Connection:
  - Open DBeaver.
  - In the top right, click "New Database Connection" (plug with the +), either by using the drop down arrow or directly on the button.
      - <img width="262" height="123" alt="image" src="https://github.com/user-attachments/assets/325f811f-1747-47f0-a91d-f96b6cea9ccc" />
  - Select SQLite and hit "Next >"
      - <img width="298" height="335" alt="image" src="https://github.com/user-attachments/assets/016b0a24-b491-4b1d-bf3b-bf66f1f062e8" />
  - Connect by: Host
  - Click "Create ..."
    - <img width="596" height="244" alt="image" src="https://github.com/user-attachments/assets/a3580d93-c87d-4b3c-a038-0b719af6843d" />
    - Navigate to a path in your local directory that you would like to save this data base (.db) that we will create and name it your computing ID
    - My example: atr8ec
  - Click "Save"
      - <img width="699" height="466" alt="image" src="https://github.com/user-attachments/assets/23d32b86-09bd-4eee-b503-987511bbf19c" />
  - Click "Finish"
      - <img width="170" height="68" alt="image" src="https://github.com/user-attachments/assets/252bbf92-d117-45df-b918-95cefedfce79" />
  - You should see your newly created and completely empty database on the left-hand side in DBeaver under Database Navigator.
      - <img width="157" height="121" alt="image" src="https://github.com/user-attachments/assets/96691386-4a8d-499c-820b-8fc52023ede3" />
  - Click into your database on the left-hand navigation and then the SQL tab at the top of the page. This will give you a text field to insert SQL queries.
      - <img width="99" height="70" alt="image" src="https://github.com/user-attachments/assets/1ebddbab-d355-4ed7-9d68-61a1ec80afd8" />
      - <img width="570" height="386" alt="image" src="https://github.com/user-attachments/assets/7d6ee872-f5c4-4498-810e-b1855f56e677" />
   
<br>

---

<br>

# Part 1 - Creating Tables From Scratch and Querying Them (15 out of 30 Points)

## Create a new table

You will create a simple database to track inventory and progress on processing datasets. Imagine there are 100 data files that must go through a multi-stage process and this DB is designed to keep a clear inventory of each file and where each one stands in the process.

1. Having clicked on your new DB, now click on the "SQL" tool dropdown and click "Open SQL Script"
2. Then, in the editor window, create the table:
```
CREATE TABLE `tracking` (
    `id` INTEGER PRIMARY KEY,  -- Changed to INTEGER PRIMARY KEY
    `file` VARCHAR(50) NULL,
    `owner` VARCHAR(30) NULL,
    `updated` DATE NULL,
    `step` INT NULL,
    `source` VARCHAR(30) NULL
);
```
3. If you did not get an error, it means your table was created! That said, it may not immediately show up and you will need to refresh the tables for your DB for it to show up. To do this:
  - Click on the drop down for your DB on the left-hand side and then double-click on tables.
  - Click "Refresh" found in the bottom left of the window that popped up and your `tracking` table should appear. 
  - Run the `PRAGMA table_info(tracking);` command back in your SQL script window to see the schema:

```
+---------+-------------+---------+------------+----+
| name   | type         | notnull | dflt_value | pk |
+---------+-------------+---------+------------+----+
| id      | INTEGER     | 0       | NULL       | 1  |
| file    | VARCHAR(50) | 0       | NULL       | 0  |
| owner   | VARCHAR(30) | 0       | NULL       | 0  |
| updated | DATE        | 0       | NULL       | 0  |
| step    | INT         | 0       | NULL       | 0  |
| source  | VARCHAR(30) | 0       | NULL       | 0  |
+---------+-------------+---------+------------+----+
```
For purposes of inserting mock data, here are some suggestions:

- `file` - A simple file name. Imagine these are `.csv` files.
- `owner` - The user ID of the researcher who is working with the data.
- `updated` - A date for when the last step occurred with this data. This takes `YYYY-MM-DD` format.
- `step` - An integer indicating which step of the workflow was completed most recently (e.g. 1-7).
- `source` - The name of the data source.

<br>

## Insert data

Using the SQL Editor, add data to your new table. Here is a sample entry you can use:

```
INSERT INTO `tracking` (`id`, `file`, `owner`, `updated`, `step`, `source`) VALUES (NULL, 'BkJrynaRf4gu.csv', 'mst3k', '2024-02-08', '4', 'NSF')
```
**Repeat this process and create at least 20 entries in your table.** Be sure to vary your `owner` field to use 3-4 different owners, a few different sources, and a few different dates.

Here's an example of data:

```
+----+------------------------+-------+------------+------+--------+
| id | file                   | owner | updated    | step | source |
+----+------------------------+-------+------------+------+--------+
|  1 | BkJrynaRf4gu.csv       | nem2p | 2024-02-08 |    4 | NSF    |
|  2 | 6gN5rc9z4YVx.csv       | mst3k | 2022-08-31 |    7 | NIH    |
|  3 | tc1pZ6EPPsxgtc1pZ6.csv | mst3k | 2023-03-13 |    6 | NSF    |
|  4 | 4vCTppoBU.csv          | nem2p | 2024-01-30 |    4 | NOAA   |
|  5 | sofowror23542.csv      | nem2p | 2024-03-28 |    1 | USGS   |
|  6 | 1a2b3c4d5e.csv         | nem2p | 2024-03-28 |    1 | USGS   |
|  7 | 2b3c4d5e6f.csv         | nem2p | 2024-03-28 |    1 | USGS   |
|  8 | 3c4d5e6f7g.csv         | nem2p | 2024-03-24 |    2 | USGS   |
|  9 | aa3c4d5e6f7g.csv       | jaj   | 2024-03-21 |    2 | NSF    |
| 10 | zz3c4d5e6f7g.csv       | jaj   | 2024-03-04 |    3 | NSF    |
| 11 | qq3c4d5e6f7g.csv       | jaj   | 2024-03-14 |    2 | NSF    |
| 12 | wrelktjyl3k45j.csv     | jaj   | 2024-01-12 |    5 | NSF    |
| 13 | 634yl3k45j.csv         | atr8ec| 2024-01-12 |    5 | NSF    |
| 14 | th634bbyla3k4.csv      | atr8ec| 2024-01-12 |    4 | USGS   |
| 15 | 1824absdfs.csv         | atr8ec| 2024-09-13 |    6 | NIH    |
| 16 | 23942fweorif.csv       | atr8ec| 2024-09-13 |    6 | NIH    |
| 17 | alfkwerljweflksd.csv   | nem2p | 2022-09-13 |    5 | NIH    |
| 18 | 41bafa.csv             | nem2p | 2021-09-11 |    5 | NSF    |
| 19 | 1j9flwer.csv           | mst3k | 2021-09-11 |    5 | NSF    |
| 20 | 2345lkjwlfkjwsfl.csv   | mst3k | 2023-10-14 |    5 | NIH    |
+----+------------------------+-------+------------+------+--------+
```

<br>

## Query your table

Now practice some SQL queries:

Select all records but put them in date order:
```
SELECT * FROM tracking ORDER BY updated ASC;
```

Select all columns and records for a specific owner:
```
SELECT * FROM tracking WHERE owner = 'jaj';
```

Select just `id` and `file` for a specific year:
```
SELECT id, file FROM tracking WHERE updated LIKE '2021%';
```

Select all columns for a range of values and order by the owner and then the updated date:
```
SELECT * FROM tracking WHERE id < 12 AND id > 7 ORDER BY owner, updated;
```

Select just the first 5 records of a query:
```
SELECT * FROM tracking LIMIT 5;
```

Update a record. Let's change the owner of a specific row, using the `id` to specify which row. This `SET`s the new value, based on a `WHERE` condition:

```
UPDATE tracking SET owner='jaj' WHERE id=4;
```
Delete a record. Let's delete a record based on a specific row `id`:

```
DELETE FROM tracking WHERE id=19;
```

Take some time to practice more SELECT, INSERT, DELETE, and UPDATE queries.

<br>

## Create a second table and add data

Since you are using unique user IDs for the `owner` field, you already have a key you can use to relate to a second table. Create a new table named `owners` using this query:

```
CREATE TABLE owners (
    owner VARCHAR(8) NULL,
    name VARCHAR(30) NULL,
    joined DATE NULL,
    training INTEGER NULL  -- BOOLEAN type is not directly supported in SQLite
);
```
Run this command and then `PRAGMA table_info(owners);` to see the schema of the new table:

```
+----------+-------------+---------+------------+-----+
| name     | type        | nonnull | dflt_value | pk  |
+----------+-------------+---------+------------+-----+
| owner    | VARCHAR(8)  | YES     | NULL       | 0   |
| name     | VARCHAR(30) | YES     | NULL       | 0   |
| joined   | DATE        | YES     | NULL       | 0   |
| training | INTEGER     | YES     | NULL       | 0   |
+----------+-------------+---------+------------+-----+
```

Here are the fields:

- `owner` - is the computing ID of the owner, which you have been using in the `tracking` table.
- `name` - is their real name, first and last.
- `joined` - is a date for when the owner joined the research group.
- `training` - is a boolean for whether they have completed required training. Values should be 0 (no) or 1 (yes).

Now insert a new record into `owners` for each of the fictitious owners you added to the `tracking` table. To retrieve a list of all the unique owners in your `tracking` table, there is a SQL query for that!

```
SELECT DISTINCT owner FROM tracking;
```

Using those values, insert a record into `owners` for each:

```
INSERT INTO `owners` (`owner`, `name`, `joined`, `training`) VALUES ('jaj', 'Jim Jokl', '1991-12-01', '1');
```

Complete one entry per owner, so that you have a completed `owners` table. Be sure some of your researchers have completed the training and some have not:
```
select * from owners;
+-------+-----------------+------------+----------+
| owner | name            | joined     | training |
+-------+-----------------+------------+----------+
| nem2p | Neal Magee      | 2016-12-01 |        1 |
| jaj   | Jim Jokl        | 1991-12-01 |        1 |
| mst3k | Mystery Science | 2021-04-13 |        0 |
| atr8ec| Austin Rivera   | 2023-01-18 |        0 |
+-------+-----------------+------------+----------+
```

<br>

## Query using JOIN statements

Finally, let's write a JOIN statement that relates both the `tracking` and `owners` tables. Imagine we simply want a list of data files, with the real name of the owner for each.

To get a full `JOIN` of both tables joined, this is a first step:
```
SELECT * FROM tracking JOIN owners ON tracking.owner=owners.owner;
```

But the results are repetitive with regards to the `owners` data on the right-hand side (results are not exactly what you will see, do not worry):
```
sqlite> SELECT * FROM tracking JOIN owners ON tracking.owner=owners.owner;
+----+------------------------+-------+------------+------+--------+-------+-----------------+------------+----------+
| id | file                   | owner | updated    | step | source | owner | name            | joined     | training |
+----+------------------------+-------+------------+------+--------+-------+-----------------+------------+----------+
|  1 | BkJrynaRf4gu.csv       | nem2p | 2024-02-08 |    4 | NSF    | nem2p | Neal Magee      | 2016-12-01 |        1 |
|  2 | 6gN5rc9z4YVx.csv       | mst3k | 2022-08-31 |    7 | NIH    | mst3k | Mystery Science | 2021-04-13 |        0 |
|  3 | tc1pZ6EPPsxgtc1pZ6.csv | mst3k | 2023-03-13 |    6 | NSF    | mst3k | Mystery Science | 2021-04-13 |        0 |
|  4 | 4vCTppoBU.csv          | jaj   | 2024-01-30 |    4 | NOAA   | jaj   | Jim Jokl        | 1991-12-01 |        1 |
|  5 | sofowror23542.csv      | nem2p | 2024-03-28 |    1 | USGS   | nem2p | Neal Magee      | 2016-12-01 |        1 |
|  6 | 1a2b3c4d5e.csv         | nem2p | 2024-03-28 |    1 | USGS   | nem2p | Neal Magee      | 2016-12-01 |        1 |
|  7 | 2b3c4d5e6f.csv         | nem2p | 2024-03-28 |    1 | USGS   | nem2p | Neal Magee      | 2016-12-01 |        1 |
|  8 | 3c4d5e6f7g.csv         | nem2p | 2024-03-24 |    2 | USGS   | nem2p | Neal Magee      | 2016-12-01 |        1 |
. . .
```

But we want to narrow our results by selecting fewer columns. To do this we need a special join called a `LEFT JOIN`. The best way to visualize this is to think of your "primary" table (which would be `tracking` in this case) on the left, and your `owners` reference list on the right.

Here is the query broken into multiple lines with line numbers:
```
1    SELECT 
2      tracking.file, owners.name
3    FROM tracking 
4    LEFT JOIN owners
5      ON tracking.owner=owners.owner;
```

Some notes:
- Line 2 - select specific columns from each of your two tables with `table_name.column_name`
- Line 3 - you still select `FROM` a primary table, but then follow it with 
- Line 4 - a join of the secondary table, which will serve as a resource to populate the query.
- Line 5 - finally, you must map the "relation", i.e. the column from one table that matches up with a value in the other table.

<br>

## Your Turn

Now write a query that lists the `file`, `step`, and owner `name` for researchers who have NOT yet completed the training. Order the results by ascending order from the `updated` column.

Run the query to test or debug your results.

<br>

---

<br>

# Part 2 - Using an Existing Database to Explore Movie Data (15 out of 30 Points)
1. Download the DB from the Lab 4 assignment page on Canvas.
2. Save the data to a location on your local directory that makes sense, like the place where you put the DB from Part 1. Please do not just save it to your downloads... I beg you!
3. Create a New Connection:
  - Open DBeaver.
  - Click "New Connection."
  - Choose SQLite.
  - Connect by: Host
  - Click "Open ..."
    - Navigate to the path in your local directory where the DB file lives and select it.
    - Should be called: `2024_imdb_movies`
  - Click "Open"
  - Click "Finish"
  - You should see your newly created DB that I cureated for you all on the left-hand side in DBeaver under Database Navigator.

<br>

### About the Data
In this part of the lab, you'll be using SQL to explore a simplified version of the Internet Movie Database (IMDB).  Your goal is to write queries to answer the questions below.  Don't be afraid to experiment, and remember to use the DBeaver SQL editor to test your queries.

<br>

### Database Schema:
- You'll be working with four tables:
  - `crew`: Information about who worked on each title (directors, writers, etc.).
  - `people`: Details about the people involved in movies (actors, directors, etc.).
  - `ratings`: Ratings and vote counts for each title.
  - `titles`: Information about the movies themselves.

<br>

### Important Tip:
Before you start, take a few minutes to familiarize yourself with the schema.  Understanding the relationships between the tables is key to writing effective queries.

<br>

### Getting Unstuck:
- **Review the schema**: Make sure you understand which tables contain the information you need.
- **Start simple**: Break down complex questions into smaller steps.
- **Use DBeaver's help**: DBeaver has documentation and code completion features that can be helpful.
- **Experiment**: Try different queries and see what results you get. Don't be afraid to make mistakes – that's how you learn!

<br>

## Questions
Below you will find 15 questions that you will need to answer about this database, where you will add either the SQL query or the result into your Gist for submission:

### Quick Note
- **Titles** - Please use `primary_title` as the title when I ask you to name a movie or title or query for movies.

### Basic Queries (5 Questions) (1 point each)
1. `**QUERY**` List all movie titles. (**Hint**: Which table contains the movie titles?)
2. `**QUERY**` Find the names of all people in the database: (**Hint**: Which table stores people's names?)
3. `**RESULT**` How many movies were **at least** 100 minutes long?. (**Hint**: Which table has the runtime? How do you filter by INTEGER?)
4. `**RESULT**` What movie has the highest rating: (**Hint**: Which table stores ratings? How do you find the maximum value?)
5. `**QUERY**` List the names of all directors: (**Hint**: The crew table holds category information. How do you filter for directors?)

<br>

### Intermediate Queries (5 Questions) (1 point each)
6. `**QUERY**` List the titles and ratings of all movies. (**Hint**: You'll need to combine data from two tables. What kind of join is appropriate?)
7. `**QUERY**` Find the names of all actors who were born before 1980. (**Hint**: You'll need to join the people and crew tables and filter by birth year and category.)
8. `**QUERY**` List the titles of all movies with a rating greater than 8. (**Hint**: Combine data from the titles and ratings tables.)
9. `**RESULT**` Find the average rating of all movies. (**Hint**: Use an aggregate function.)
10. `**QUERY**` List the names of all people who have worked as both directors and actors. (**Hint**: This requires checking the crew table for both categories for the same person. You might need to use subqueries or self-joins.)

<br>

### Advanced Queries (5 Questions) (1 point each)
11. `**RESULT**` Name the movie with the most votes: (**Hint**: Look in the ratings table.)
12. `**QUERY**` List the names of all actors who have appeared in more than 5 movies: (**Hint**: Use GROUP BY and HAVING.)
13. `**RESULT**` Name the titles of the top 3 highest-rated movies taht received at least 10,000 votes. (**Hint**: Use ORDER BY, JOIN, and LIMIT.)
14. `**QUERY**` For each of **your** three most favorite genres, find the number of movies in that genre. (**Hint**: The titles table has a genres column. GROUP BY will be useful. You may also want to look at all of the genres to pick your three favorite.)
15. `**QUERY**` Find the names of all people who have worked on a movie with a rating greater than 9. (**Hint**: This requires joining multiple tables.)

<br>

# Submit the URL to your Gist in Canvas.
