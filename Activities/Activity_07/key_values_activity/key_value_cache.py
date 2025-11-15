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
# SETTING Data: Storing our user data using a unique key
# The key is designed for fast access: 'user_session:UID'
session_cache['user_session:9001'] = USER_A_DATA
session_cache['user_session:9002'] = USER_B_DATA

# Check the contents of our cache
print("--- Current Cache Status ---")
print(session_cache)

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

# Update the activity for user 9001
new_activity = USER_A_DATA['recent_activity']
new_activity.append("submitted_lab_4") # New activity

# Overwrite the old value with the new value
session_cache['user_session:9001']['recent_activity'] = new_activity

print("\n--- Updated Data ---")
print(session_cache['user_session:9001']['recent_activity'])

# Note: The database doesn't care about the structure of the value,
# it just overwrites the entire stored object associated with the key.
