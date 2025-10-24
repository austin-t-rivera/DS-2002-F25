# Lab 7 - NoSQL Databases (7 Families Edition)

Welcome to Lab 6 of the DS-2002 course! This lab will take you through the fundamentals of the seven primary types of NoSQL Databases we have covered in class, giving you brief exposure to real-world systems like Redis, MongoDB, Cassandra, and InfluxDB.

| NoSQL Family | Database Management System (DBMS) | Exposure Type |
| :--- | :--- | :--- |
| Key-Value | Redis | Hands-on via a free cloud console. |
| Document | MongoDB Atlas | Hands-on querying with sample data. |
| Wide-Column | DataStax Astra DB (Cassandra) | Hands-on via a free cloud console. |
| Time-Series | InfluxDB | Guided conceptual review and questions. |
| Ledger | Amazon QLDB (Conceptual) | Video review and conceptual questions. |
| Graph | Neo4j GraphAcademy | Guided hands-on with the first few lessons. |
| Vector | Python/NumPy (From Scratch) | Guided Python notebook exercise. |

<br>

---

## Part 0. Setting Up and What to Submit
**Create**:
- Create a LinkedIn profile if you have not already.
- Create a new GitHub Gist, the URL of which is what will be submitted to Canvas for this lab.

**Submit to Canvas**:
- URL to your GitHub Gist, which will contain the following information (please copy and paste the example below and then add the information to your gist as you go):

```
Part 1 (Key-Value - Redis):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 2 (Document - MongoDB):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 3 (Wide-Column - Cassandra):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 4 (Time-Series - InfluxDB):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 5 (Ledger - Conceptual):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 6 (Graph - Neo4j):
<You will copy and paste additional formatting here as dictated by the section below.>

------------------------------------------
Part 7 (Vector - From Scratch):
<You will copy and paste additional formatting here as dictated by the section below.>
```

<br>

---

## Part 1. Key-Value Databases using Redis
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
3. Run `DEL views:homepage`. Now run `INCR views:homepage` again. What is the output and why? (Hint: How does Redis treat a key that doesn't exist when an operation like `INCR` is run?)

Add your responses to your Gist like so:
```
Part 1 (Key-Value - Redis):
- Answer 1: <your output>
- Answer 2: <your answer>
- Answer 3: <your output> and <your explanation>
```












