# Activity 5: Extract and Transform JSON to CVS

In this activity, you will use explore the fours primary methods of gathering data, parse and transform the data into a structured and human-readable dataframe using `requests`, `json`, `beautifulsoup`, and `pandas`. After extraction and transforming you will export the data to three `CSV` files.

The four primary methods of data extraction are:
- APIs
- Webscraping
- File Ingestion
- Streaming

For the purposes of this activity, we will be running Python Notebooks (`.ipynb`) that have been curated to follow along to get exposure to the process of extracting via APIs, Webscraping, and File Ingestion.

<br>

## Step 0. Setup 

### Navigate to your `DS-2002-F25` directory, update your `main` branch, and setup the Activity.
1. Open your Git Bash (Windows) or Terminal (macOS).

2. Navigate to your `DS-2002-F25` directory. For example: `cd ~/Documents/GitHub/DS-2002-F25/` (yours may differ)

3. Make sure that you do not have any unstaged or uncommitted stages by running `git status`. If you doo, `add` and `commit` them.

4. Switch to your `main` branch `git checkout main`.

5. Run `git remote -v`:
   - If your upstream lists my repo `austin-t-rivera/DS-2002-F25.git` and your origin list your repo `<your-github-id>/DS-2002-F25.git`, proceed to step 6.
   - If your upstream lists your repo or does not exist, set my repo by running `git remote add upstream git@github.com:austin-t-rivera/DS-2002-F25.git` and continue in step 5.
     - Run `git fetch upstream` and continue in step 5.
     - Run `git merge upstream/main main` and proceed to step 6.

6. Run the `update_repo.sh` file.

7. Use `cd` to further navigate to your `/Activities/Activity_05` directory to confirm your `main` branch is up to date.

<br>

### Open up a new Codespace in GitHub
1. Go to **your** `DS-2002-F25` repo in GitHuband make sure you are looking at your `main` branch.

2. Create a new branch named `Activity_5` by typing in "Activity_5" and clicking on "Create branch Activity_5 from main".
<img width="404" height="333" alt="image" src="https://github.com/user-attachments/assets/ae663f18-7930-4731-86e9-d52272c0df07" />

3. To open your first codespace, to the right, you can click on `<> Code`, then `Codespaces`, and lastly `Create codespace on Activity_5`.
<img width="507" height="539" alt="image" src="https://github.com/user-attachments/assets/74bd4a2b-0a7b-4a6c-8923-a47b1c26e4fb" />

4. NOTE: You are now in your VS Code Codespace! This is a container that is built for you to work in that has essentially all of the functionality of a high-powered IDE, in this case VS Code, but is also fully integrated into your GitHub!

5. Within your Codespace, in the Terminal (bottom center), use `cd` to navigate to your `/Activities/Activity_05` directory

6. Create a new directory for this project and navigate into it:
```
mkdir ET_activity && cd ET_activity
```

<br>

### Download from Canvas, Upload into GitHub
1. Within the Activity 5 assignment on Canvas, you should see 5 files to download. Download them.

2. Drag your newly downloaded files from your file system's Downloads folder and into your `ET_activity` directory
<img width="1322" height="464" alt="image" src="https://github.com/user-attachments/assets/667d4c0b-b772-4028-a9d5-d10f67816880" />

3. Click on "Extensions" all the way to the left and second from the bottom:
<img width="47" height="355" alt="image" src="https://github.com/user-attachments/assets/dad42615-19ed-48b6-a324-b1cc1b238d39" />

5. Click on the Extensions Filter icon and click on Recommendations:
<img width="508" height="458" alt="image" src="https://github.com/user-attachments/assets/dda90042-953a-458c-aeb2-f371ca104824" />

6. Install the `Python` and `Jupyter` extensions for this Activity:
<img width="345" height="253" alt="image" src="https://github.com/user-attachments/assets/588f7472-caa6-44f9-9444-a303da85066f" />
<img width="344" height="266" alt="image" src="https://github.com/user-attachments/assets/97517515-1948-4faa-a3c6-51542b9c6b67" />


---

## Step 1: Data From an Ingested File
1. Open `Ingesting_NBA_JSON_File.ipynb`.

2. Read through and run each cell to understand what we are doing.

3. Towards the end, it will create a CSV for you, I expect to see this in the directory as part of your submission.

4. Save `Ingesting_NBA_JSON_File.ipynb`.

<br>

---

## Step 2: Data From an API Call
1. In your `ET_activity` directory, create a file name `.env`.

2. Follow this link to the [NewsAPI](https://newsapi.org/) and click on "Get API Key" in the top right corner:
<img width="261" height="73" alt="image" src="https://github.com/user-attachments/assets/67910fd5-a920-4340-8131-31d756f3442d" />

3. Fill out the request form to get an access to the API:
<img width="523" height="689" alt="image" src="https://github.com/user-attachments/assets/e4702822-0e0a-4152-bb3b-9d19a16b3cd1" />

4. You should see something like the follow, where you can now copy your API Key:
<img width="511" height="379" alt="image" src="https://github.com/user-attachments/assets/ff4e8db4-92e9-43fe-86c1-63558209e7fe" />

5. Paste this key into your `.env` file, and assign it the variable name `newskey`, like so:
<img width="749" height="155" alt="image" src="https://github.com/user-attachments/assets/58009efd-1a92-445f-8684-dd9d00a92d00" />

6. Open `API_Calling_News.ipynb`.

7. Read through and run each cell to understand what we are doing.

8. Towards the end, it will create a CSV for you, I expect to see this in the directory as part of your submission. 

9. You will be asked to provide a topic after you run the last cell, please do so, it can be whatever you want to know about! It will prompt you up top, and can be hard to catch:
<img width="1250" height="738" alt="image" src="https://github.com/user-attachments/assets/8362af79-95c1-478d-90d6-8793ea1a587d" />
<img width="653" height="112" alt="image" src="https://github.com/user-attachments/assets/c1a2f6a8-2ddd-427e-b3c8-c549a008f6d5" />

10. Save `API_Calling_News.ipynb`.

<br>

---

## Step 3: Data From Webscraping

1. Open `Webscraping_Rotten_Tomatoes.ipynb`.

2. Read through and run each cell to understand what we are doing.

3. Note that towards the beggining, it will fail because you need to enter your UVA email. Please do so.

4. Towards the end, it will create a CSV for you, I expect to see this in the directory as part of your submission.

5. Save `Webscraping_Rotten_Tomatoes.ipynb`.

<br>

---

## Step 4: Data From a Stream

1. Open `Streaming_Bitcoin_trades.ipynb`.

2. Read through and run each cell to understand what we are doing.

3. Towards the end, it will create a CSV for you, I expect to see this in the directory as part of your submission.

4. Save `Streaming_Bitcoin_trades.ipynb`.

<br>

---

## Step 5: Add, Commit, Push, and Submit on Canvas!
1. Stage all of your changes at once: `git add .`.
2. Commit your staged changes to your local `Activity_5` branch **with a message**: `git commit -m ""`
3. Push your local branch to your remote repository: `git push --set-upstream origin Activity_5`
4. Exit your Codespace and navigate to your forked repository on GitHub.
5. Switch to your `Activity_5` branch on GitHub.
6. Navigate to your `ET_activity` directory.
7. Copy the URL to your `ET_activity` directory on your `Activity_5` branch, and paste the URL into the Activity 5 assignment on Canvas.
