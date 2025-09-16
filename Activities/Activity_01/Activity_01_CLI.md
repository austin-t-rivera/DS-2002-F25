# In-Class Activity: Introduction to Command Line
Course: DS-2002, Section 001, Data Science Systems
Time Allotted: 20 minutes

**Instructions**: The goal of this activity is to get you comfortable with the most fundamental commands used in Unix-like environments (Linux and macOS). These commands are essential for navigating, managing, and manipulating data. Follow the steps below in your terminal. For those with prior experience, challenge yourself to complete the activity as quickly as possible without referring to the instructions.

## Part 1: Navigation & File Creation
1. Print your current location.
```
pwd
```
<br>

2. Create a new directory for this activity called `ds_activity`.
```
mkdir ds_activity
```
<br>

3. Change into the newly created directory.
```
cd ds_activity
```
<br>

4. Create a file named `notes.txt`.
```
touch notes.txt
```
<br>

5. Create a file named `project_plan.txt`.
```
touch project_plan.txt
```
<br>

6. List all files in the current directory to confirm they were created.
```
ls
```
<br>

## Part 2: File Content & Manipulation
1. Add a single line of text to `notes.txt` using the `cat` command and output redirection. The line should say "My first command line note."
```
cat > notes.txt
```
(Type the line and then press **Ctrl+D** to save and exit.)
<br>

2. View the contents of `notes.txt` to confirm the text was added.
```
cat notes.txt
```
<br>

3. Copy `notes.txt` and name the new file `notes_backup.txt`.
```
cp notes.txt notes_backup.txt
```
<br>

4. Rename `project_plan.txt` to `final_project_plan.txt`.
```
mv project_plan.txt final_project_plan.txt
```
<br>

5. List the contents of the directory again to see the changes.
```
ls
```
<br>

## Part 3: Permissions & Cleanup
1. Change the permissions of `notes.txt` so that the owner can read and write the file.
```
chmod u+rw notes.txt
```
<br>

2. View the detailed list of files to see the permission changes.
```
ls -l
```
<br>

3. Remove the `notes_backup.txt` file.
```
rm notes_backup.txt
```
<br>

4. Remove the `final_project_plan.txt` file.
```
rm final_project_plan.txt
```
<br>

5. View the list of files one last time to confirm you only have `notes.txt`.
```
ls
```
<br>

## Part 4: Submission
1. View your command history using the `history` command. This is a very useful command to view your past commands.
```
history
```
<br>

2. Create your submission file. Now, use the `history` command to create a new file named `submission.txt`. We will use a pipe (`|`) to send the output of one command to the input of another. Then use the `tail` command to get the last 10 commands from your history.
```
history | tail -n 10 > submission.txt
```
<br>

3. Add your name and UVA computing ID to the top of your `submission`.txt file. We can do this with the `echo` command.
```
echo "Name: [Your Name] | ID: [Your ID]" >> submission.txt
```
<br>

4. Append the contents of your `notes.txt` file to the end of `submission.txt`. We can do this with the `cat` command using output redirection.
```
cat notes.txt >> submission.txt
```
<br>

5. View the final contents of your `submission.txt` file to ensure everything is correct.
```
cat submission.txt
```
<br>

## Activity Submission
Upload the `submission.txt` file to Canvas for grading. Congratulations, you've successfully completed the activity!

<br>

## Final Cleanup
1. Navigate up to the parent directory.
```
cd ..
```
<br>

2. Remove the entire `ds_activity` directory and all of its contents now that you have your submission file ready.
```
rm -r ds_activity
```
