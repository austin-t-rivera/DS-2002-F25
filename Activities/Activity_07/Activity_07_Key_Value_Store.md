# Activity 7: Simulating a Key-Value Cache in Python

In this activity, you will apply the concepts of NoSQL Key-Value stores by building a simple, in-memory cache using a Python dictionary. This will demonstrate the speed and efficiency of direct key lookups, which is the foundational advantage of databases like Redis and Memcached.

<br>

---

## Step 0. Setup

### Open Your Codespace in GitHub

1. Go to your `DS-2002-F25` repo in GitHub and make sure you are looking at your `main` branch.

2. Open your codespace for `main`.

### Sync Your Main and Setup Your Activity

1. Within your codespace terminal, run the `update_repo.sh` file to update at least your main branch.

2. Once up-to-date, create a new branch for this activity and move into by running `git checkout -b Activity_7`.

3. Navigate to your `Activities/Activities_07` directory and create a new directory called `key_values_activity` and move into it.

4. Create a file name `key_value_cache.py`

<br>

---

## Step 1. Initilize the "Database"
In a Key-Value store, everything is a key pointing to a value. In Python, this is a simple dictionary. We will simulate a cache for common user data.

**Action**: Copy the Python code block below into your `key_value_cache.py` file.
```Python
# Our Key-Value "Database" (In-Memory Cache)
session_cache = {}

# We define some complex user data that would normally be slow to retrieve
USER_A_DATA = {
    "user_id": 9001,
    "username": "ds_student_uva",
    "last_login": "2025-10-20T10:30:00Z",
    "recent_activity": ["viewed_lab_4", "checked_forum"]
}
USER_B_DATA = {
    "user_id": 9002,
    "username": "nosql_fan",
    "last_login": "2025-10-20T10:45:00Z",
    "recent_activity": ["downloaded_slides"]
}
```

<br>

---

## Step 2. Write (SET) Data
In Key-Value terminology, storing data is often called a "SET" operation. We use a key that is easy to look up.

**Action**: Append the Python code block below to your `key_value_cache.py` file and run the script (`python key_value_cache.py`).
```Python
# SETTING Data: Storing our user data using a unique key
# The key is designed for fast access: 'user_session:UID'
session_cache['user_session:9001'] = USER_A_DATA
session_cache['user_session:9002'] = USER_B_DATA

# Check the contents of our cache
print("--- Current Cache Status ---")
print(session_cache)
```

<br>

---

## Step 3. Read (GET) Data and Check Performance
Retrieving data is called a "GET" operation. This is where the Key-Value model shines.

**Action**: Append the Python code block below to your `key_value_cache.py` file and run the script. Note the speed difference between the direct key lookup and the simulated "slow search."
```Python
import time

# GETTING Data: Retrieving a session by its key
key_to_find = 'user_session:9001'

start_time = time.perf_counter()
# Direct lookup by key (the speed of a hashmap)
data = session_cache.get(key_to_find)
end_time = time.perf_counter()

print("\n--- Retrieval Results ---")
print(f"Retrieved data for {key_to_find}: {data['username']}")
print(f"Time taken for retrieval: {((end_time - start_time) * 1000):.6f} milliseconds")

# Now, imagine if we had to search through all the values:
# This is what relational DBs sometimes have to do (a full table scan)
slow_start = time.perf_counter()
found_slow = next((v for k, v in session_cache.items() if v['username'] == 'nosql_fan'), None)
slow_end = time.perf_counter()

print(f"\nTime taken for SLOW search: {((slow_end - slow_start) * 1000):.6f} milliseconds")
```

<br>

---

## Step 4. Update/Overwrite Data
Key-Value updates are simple: you just "SET" the new value to the existing key. The new value completely overwrites the old value associated with that key.

**Action**: Append the Python code block below to your `key_value_cache.py` file and run the script.
```Python
# Update the activity for user 9001
new_activity = USER_A_DATA['recent_activity']
new_activity.append("submitted_lab_4") # New activity

# Overwrite the old value with the new value
session_cache['user_session:9001']['recent_activity'] = new_activity

print("\n--- Updated Data ---")
print(session_cache['user_session:9001']['recent_activity'])

# Note: The database doesn't care about the structure of the value,
# it just overwrites the entire stored object associated with the key.
```

<br>

---

## Step 5: Add, Commit, Push, and Submit on Canvas!

1. Stage your changes: `git add .`
2. Commit your staged changes to your local `Activity_7` branch with a message: `git commit -m "Complete Activity 7: Key Value Cache Simulation"`
3. Push your local branch to your remote repository: `git push --set-upstream origin Activity_7`
4. Exit your Codespace and navigate to your forked repository on GitHub.
5. Switch to your `Activity_7` branch on GitHub.
6. Navigate to your `/Activities/Activity_07/key_values_activity` directory.
7. Copy the URL to your `key_values_activity` directory and paste the URL into the Activity 7 assignment on Canvas.


