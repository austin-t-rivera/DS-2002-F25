# In-Class Activity: GitHub Class Log
Welcome to the version control activity! We're going to collectively build a single file that contains a fun fact from everyone in the class. This will give you hands-on experience with the core workflow of collaborative development.

**The Objective**: Your goal is to add a single line to the 'class_log.txt' file in this repository in the Activity_2 folder.

<br>

## Step 1: Fork the Repository
First, you need to create your own copy of this repository. This is called forking. A fork is a personal sandbox where you can make changes without affecting the original project.
1. Open the repository in your web browser: `https://github.com/austin-t-rivera/DS-2002-F25`
2. In the top-right corner, click the "**Fork**" button.
3. A pop-up will ask you to confirm. Just click "**Create fork.**"
4. You will now have a copy of the repository under your own GitHub account.

<br>

## Step 2: Clone Your Fork
Now you need to get the code from your personal GitHub copy onto your local computer. This is called cloning.
1. On your new forked repository page, click the green "**Code**" button.
2. Make sure the **SSH** tab is selected.
3. Copy the URL to your clipboard. It will look like `git@github.com:YOUR-USERNAME/DS-2002-F25.git`.
4. Open your **Terminal** (or Git Bash/WSL) and run the `git clone` command followed by the URL you copied:
```
git clone [paste your copied URL here]
```
5. Use `ls` to confirm that a new folder named DS-2002-F25 has been created.
6. Change into that new directory:
```
cd DS-2002-F25
```

<br>

## Step 3: Add Your Contribution
Now that you have the repository on your computer, it's time to add your contribution.

1. Figure out what you want to put after your name for your fun fact and favorite Bash command, following this format:
```
[Your Name], [A Fun Fact About You], [Your Favorite Bash Command]
```
For example:
```
Jane Doe, I can play the ukulele, ls
```
2. NAVIGATE TO THE `Activity_2` DIRECTORY!
2. Choose one of the following methods to edit the `class_log.txt` file:
  - Open the file from the command line using the `nano` command:
```
nano class_log.txt
```
  - Use the `echo` command and the `>>` operator to append your message into the file:
```
echo 'Jane Doe, I can play the ukulele, ls' >> class_log.txt
```
  - Open the file in your favorite text editor.

3. Make sure the file is saved!

<br>

## Step 4: Add, Commit, and Push
You've made a change, but Git doesn't know about it yet. This is where the core Git workflow comes in.

1. Stage your change with `git add`, either implicitly or explicitly:
- **Implicitly**: this will stage any files you have added, deleted, or modified and saved on this branch.
```
git add .
```

- **Explicitly**: this will stage only files you explicitly name that you have added, deleted, or modified and saved on this branch.
```
git add class_log.txt
```

2. Commit your change to your local branch with a brief but descriptive message. The -m stands for "message".
```
git commit -m "Add my contribution to the class log."
```

3. Push your committed changes from your local computer back to your forked repository on GitHub.
```
git push origin main
```

<br>

## Step 5: Submit a Pull Request
Now you'll request that your changes be pulled into the original repository.

1. Go back to your forked repository page on GitHub.
2. You should see a yellow banner at the top that says, "This branch is 1 commit ahead of austin-t-rivera:main." Click the "Contribute" button.
3. Click "**Open pull request.**"
4. Give your pull request a clear title like "Adds [Your Name] to class log" and write a short description explaining what you did.
5. Click the "**Create pull request**" button.

Congratulations! Your pull request has been submitted. The repository owner (your instructor) will then review and merge your changes.

## Step 6: Submit a Pull Request
1. Go to your pull request on GitHub and copy the URL.
2. Paste the URL of your PR into the submission box for Activity 2 on Canvas.

<br>

## Bonus Skill: Update Your Repository
Now that your contribution is merged, you're ready to see everyone else's. In your Terminal, run the `git pull` command to get the latest changes from the original repository:
```
git pull origin main
```
The `class_log.txt` file on your computer will now be updated with everyone else's contributions.
