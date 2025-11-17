# Lab 7 - NoSQL Databases (7 Families Edition)

Welcome to Lab 7 of the DS-2002 course! This lab will take you through the fundamentals of three of the seven primary families of NoSQL Databases we have covered in class, giving you brief exposure to real-world systems like MongoDB and Neo4j.

To keep the lab a reasonable length, there are only three (3) parts that are required and that count for credit, however, I have provided instructions for one optional part that is not for credit, but for your own exploration if you are interested.

### NOTE
While this iteration of this lab lists Part 4 as optional, it is important to note that Redis is an incredibly powerful and ubiquitous tool that goes well beyond Key-Value databases and would be a powerful addition to your toolkit.

| Assignment | NoSQL Family | Database Management System (DBMS) | Exposure Type | Goal |
| :--- | :--- | :--- | :--- | :--- |
| `Required` | Document | MongoDB Atlas | Hands-on querying with sample data. | Use MongoDB to explore Movie data to answer a few questions and practice querying. |
| `Required` | Graph | Neo4j GraphAcademy | Guided hands-on with the first few lessons. | Complete the Neo4j fundamentals certification and add it to your LinkedIn! |
| `Required` | Vector | Python/NumPy (From Scratch) | Guided Python notebook exercise. | Follow along some code where we build a basic Patient Disease Diagnosis tool from scratch! |
| `Optional` | Key-Value | Redis | Hands-on via a free cloud console. |

<br>

---

## Part 0. Setting Up and What to Submit
**Create**:
- Create a LinkedIn profile if you have not already.
- Create a new GitHub Gist, the URL of which is what will be submitted to Canvas for this lab.

**Submit to Canvas**:
- URL to your GitHub Gist, which will contain the following information (please copy and paste the example below and then add the information to your gist as you go):

```
Part 1 (Document - MongoDB):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 2 (Graph - Neo4j):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 3 (Vector - From Scratch):
<You will copy and paste additional formatting here as dictated by the section below.>
```

<br>

---

<img width="250" height="64" alt="image" src="https://github.com/user-attachments/assets/db1f71c8-175e-4002-bd7d-383fc8890b93" />

## Part 1. Document Databases using MongoDB:
### MongoDB Atlas Free Tier:
- MongoDB Atlas offers a free tier that allows you to create a small cluster. While it's a cloud-hosted service, it's very easy to set up.
- You can find many public datasets that can be easily imported into your free cluster.
- MongoDB also provides interactive tutorials and documentation with sample data.
- If you have not already done so, please watch [this video](https://www.youtube.com/watch?v=9DbZ2ii01ew&ab_channel=NealMagee) to set up your account.

### Quick Help for MongoDB:
1. Open your free cluster, navigate to your `sample_mflix` database, and see your six (6) collections, each of which containing many documents:
   - comments, embedded_movies, movies, sessions, theaters, users
2. Click on your `movies` collection and use `Find` to query your movies documents
3. Open the [query documentation](https://www.mongodb.com/docs/manual/tutorial/query-documents/) for help for how to query using MongoDB.
   - (NOTE: The documentation allows you to select a language. By default it will use `Node.js`, switch this to `Compass`.)
4. Copy and paste this query and hit `Apply`:
```
{
"year": { $gt: 1990 },
"cast": "Tom Hanks",
"genres": "Comedy",
"imdb.rating": { $gt: 7.5 },
"metacritic": {$gt: 80}
}
```
  - This should return three documents which consist of the first three Toy Story Movies.
  - With this query, we are searching for any movies that meets these criteria, i.e. All Tom Hanks comedies made after 1990 with critical acclaim on both IMDB (>7.5) and MetaCritic (>80).
  - You may be wondering, "Hey, there were four Toy Stories! Does this mean there is no Toy Story 4 in this collection or did it not do as well, critically?"
5. Try running this:
```
{
"year": { $gt: 1990 },
"cast": "Tom Hanks",
"genres": "Comedy",
"title": { $regex: '^Toy' }
}
```
  - Here we introduce the use of `regex` or Regular Expression, to enhance our search to find all of the Comedic "Toy" movies Tom Hanks has been in since 1990.
  - There are many other ways we could look to prove this, maybe even by getting rid of the genre or year, but we can rest easy knowing that Toy Story 4 is simply not in this dataset.

### Instructions for MongoDB
Please use my natural language sentences to create a Compass query to search within the sample_mflix database. You will need to paste your query as well as provide the answer to the thing I am trying to find.

0. **FOR EXAMPLE**: If I were asking for "All Tom Hanks comedies made after 1990 with critical acclaim on both IMDB (>7.5) and MetaCritic (>80).", I would expect to see the following in your Gist (I will be lenient on formatting, but try to get it close, at least so it is easy to read.):
```
Part 1 (Documents - MongoDB):
  - Query 0:
            {
            "year": { $gt: 1990 },
            "cast": "Tom Hanks",
            "genres": "Comedy",
            "imdb.rating": { $gt: 7.5 },
            "metacritic": {$gt: 80}
            }
  - Answer 0: Toy Story, Toy Story 2, Toy Story 3
```
1. An award winning R-rated Sci-Fi movie starring Arnold Schwarzenegger consisting of a "hunt" in the full plot description that IMDB (>6) found favorable, and MetaCritic hated (<40).
2. A G-rated movie, exactly 100 minutes long that came out either after 1980 or before 1940 with at least one "dog" being part of the full plotline.
3. The theaterId of the most northern theater in Charlottesville.

Copy the formatting below and paste into your Gist:
```
Part 1 (Document - MongoDB):
  - Query 1: 
  - Answer 1: 
  - Query 2: 
  - Answer 2: 
  - Query 3: 
  - Answer 3:
```

<br>

---

<br>

<img width="250" height="89" alt="image" src="https://github.com/user-attachments/assets/065815f5-cd63-45e0-8243-7dbd70572615" />


## Part 2. Graph Databases using neoj4
1. Go to the [Neo4j GraphAcademy](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/) and enroll in the the Neo4j Fundamentals course.
2. You can make a free account using your UVA email.
3. Complete the course (Estimated 1 hour):
   - 9 lessons
   - 5 videos
   - 8 "quizzes"
   - Ability to use their sandbox
4. Upon completion, add the certification to your LinkedIn profile page. There will be a button that will take you to login and do so.
5. Add the URL to your LinkedIn to your Gist like so:
```
Part 2 (Graph - Neo4j):
LinkedIn URL: <your LinkedIn profile page URL>
```

<br>

---

<br>

## Part 3. Vector Databases from Scratch
1. Download the `Lab_7_Vector_Database.ipynb` file from the Lab 7 Assignment page on Canvas.
2. Go to [Google Collab](https://colab.research.google.com/) and sign in or open a Codespace on GitHub.
3. Open the notebook you just downloaded.
4. Read through and run each cell in the notebook.
5. Answer the questions at the bottom.
6. Add your answers to your Gist file, like so:
```
Part 3 (Vector - From Scratch)

1. How many patients are diagnosed with:
  - Flu: <your answer>
  - Common Cold: <your answer>
  - Pneumonia: <your answer>
  - Migraine: <your answer>
  - Asthma: <your answer>
  - Undiagnosed: <your answer>

2. <your answer>

3. <your answer>

4a. <your answer>

4b. <your answer>

5. <your answer>
```

<br>

---

<img width="200" height="64" alt="image" src="https://github.com/user-attachments/assets/00f0cb6f-13c0-4bfb-b926-24d05926db4f" />

## (`Optional`) Part 4. Key-Value Databases using Redis

**Goal**: Understand the simplicity and utility of Key-Value stores, especially for caching and temporary data.

<br>

### Redis Cloud Free Tier:
We will use the Redis Cloud free tier or a browser-based console to quickly interact with the system.
1. Go to [Redis Cloud](https://redis.io/cloud/) and click `Try for free`. Create an account using your UVA email and put "University of Virginia" for the "Company".
   - It may take a few minutes for the email to login after creating your account.

2. Once logged in, click on `Databases` and create a new database.

3. You should select the "Free" plan:
<img width="865" height="786" alt="image" src="https://github.com/user-attachments/assets/04ea910d-ed76-4438-84a4-4c54a8864e2c" />

4. Name your database `<your UVA computing id>-lab7-redis`, version 7.4, and keep `AWS` and `us-east-1` selected:
<img width="1143" height="532" alt="image" src="https://github.com/user-attachments/assets/8bfb29ac-e51e-40a0-8330-f90af7c07300" />

5. Click `Create database`

6. you should be able to create a free subscription and then a new database. Choose the "Fixed" (Free) plan.

7. Once the database is created, `Connect to database`, then under "Redis Insight", click `Launch Redis Insight web`.
<img width="514" height="134" alt="image" src="https://github.com/user-attachments/assets/f7243e49-f1e0-4ac8-adaa-7e6dfcfe50ad" />
<img width="484" height="594" alt="image" src="https://github.com/user-attachments/assets/6f17bf08-09ab-459a-9ac8-199665b35f6b" />

8. Click into the "Workbench" at the top, or the "CLI: at the bottom and run the following commands one at a time:
<img width="1863" height="256" alt="image" src="https://github.com/user-attachments/assets/b32d79b7-423a-46c5-9e3f-3ca7ec9e7381" />

| Command | Purpose |
| :--- | :--- |
| `SET user:42 "Jane Doe"` | Store a simple string value with a key. |
| `GET user:42` | Retrieve the value. |
| `INCR views:homepage` | Increment a counter key. |
| `GET views:homepage` | Check the new counter value. |
| `SETEX temp:token 60 "secret_value"` | Set a key that expires in 60 seconds (demonstrates caching). |
| `TTL temp:token` | Check the remaining time-to-live (TTL). |


### Instructions for Redis
After running the commands above, answer the following questions based on the output you saw in the console.
1. What was the output after running `INCR views:homepage` for the first time?
2. What does `SETEX` allow you to do that a regular `SET` command does not? Why is this feature important for a Key-Value store used as a cache?
3. Explore the tutorials to better understand the power of Redis!
