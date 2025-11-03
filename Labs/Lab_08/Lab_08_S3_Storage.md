# Lab 8: Amazon Simple Storage Service (S3)

---

<img width="1000" height="97" alt="image" src="https://github.com/user-attachments/assets/e5898d54-3fce-4448-b8e9-f9765e34de9f" />

<img width="271" height="97" alt="image" src="https://github.com/user-attachments/assets/0c09151e-cc47-47ba-8bac-d18265ab4fbc" />
<img width="385" height="97" alt="image" src="https://github.com/user-attachments/assets/e56e4000-dd7a-4d84-a081-e43764491052" />
<img width="335" height="97" alt="image" src="https://github.com/user-attachments/assets/3b0c39de-603a-45a8-a8cd-b701675dd974" />

<br>

---

Welcome to Lab 8 of the DS-2002 course! This lab will take you through the fundamentals of the three ways in which you can interact with S3:

## AWS CLI
The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

We will be accessing the AWS CLI in both our local environments and through the Sandbox Vocareum platform connected to our AWS Academy course.

## AWS Console
Everything you need to access and manage the AWS Cloud — in one web interface.

## boto3
You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.

<br>

---

## Part 0. Setup
Because Codespace does not seem to support `awscli` for AWS Academy, only for full access accounts, we will not be able to utilize Codespace for this lab. This will require you to ensure that you update your locally cloned fork of DS-2002-F25. This can come with some hiccups along the way, but I encourage all of you to persist and get it running!

<br>

### Install `awscli` and `boto3`

Complete both of the following within either Git Bash (Windows) or Terminal (macOS):

- `awscli` - Follow this guide to download and install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
 
- `boto3` - is a simple `pip` command in your terminal:
```bash
python3 -m pip install boto3
```

<br>

### Navigate to your `DS-2002-F25` directory, update your `main` branch, and setup the `Lab_8` branch.
1. Open your Git Bash (Windows) or Terminal (macOS).

2. Navigate to your `DS-2002-F25` directory. For example: `cd ~/Documents/GitHub/DS-2002-F25/` (yours may differ)

3. Switch to your `main` branch `git checkout main`.

4. Make sure that you do not have any unstaged or uncommitted stages by running `git status`. Add and commit any changes if there are some lingering.

5. Run `git remote -v`:
   - If your upstream lists my repo `austin-t-rivera/DS-2002-F25.git` and your origin list your repo `<your-github-id>/DS-2002-F25.git`, proceed to step 6.
   - If your upstream lists your repo or does not exist, set my repo by running `git remote add upstream git@github.com:austin-t-rivera/DS-2002-F25.git` and continue in step 5.
     - Run `git fetch upstream` and continue in step 5.
     - Run `git merge upstream/main main` and proceed to step 6.

6. Run the `update_repo.sh` file to update just your `main` branch.

7. Use `cd` to navigate to your `/Labs/Lab_08/` directory.

9. Create and move into a new branch called `Lab_8` by running `git checkout -b Lab_8`.

10. Create a new directory for this project, within the `Labs/Lab_08/` directory, and navigate into it:
```bash
mkdir s3_bucket_lab && cd s3_bucket_lab
```

<br>

### Start up your AWS Academy Sandbox, Console, and Find your Credentials
1. Go to our [Cloud Foundations course](https://awsacademy.instructure.com/courses/144192) in AWS Academy.

2. Click into `Modules` and then into the `Sandbox` module.
<img width="1038" height="619" alt="image" src="https://github.com/user-attachments/assets/31ba5d9c-b864-45fb-b8d5-51f3409c5bfa" />

3. Click the thing that says to load it in a new window, which will open Vocareum.
<img width="1536" height="401" alt="image" src="https://github.com/user-attachments/assets/6d62385e-b704-4795-bffa-e7beeab5e7b6" />

4. You should now see the following:
<img width="1920" height="467" alt="image" src="https://github.com/user-attachments/assets/263becb1-aab1-4fe2-9831-d83af69a92c7" />

5. Click on "Start Lab". **This will bring up a popup window that you will wait until it tells you the lab is started before hitting "X" to exit the popup window.**
<img width="159" height="83" alt="image" src="https://github.com/user-attachments/assets/937bc18b-726d-4d02-9f23-04fc55414761" />

6. Click on "AWS" to open the AWS Console in another tab. **We will use this later.**
<img width="128" height="92" alt="image" src="https://github.com/user-attachments/assets/afacb3e0-d6ca-4bc9-8aac-89833e620513" />

7. Back in Vocareum, click on "Details", which will **show you the AWS Credentials for ONLY THIS LAB SESSION. You will need to update credentials if you stop the lab or if the time expires.**
<img width="1920" height="1063" alt="image" src="https://github.com/user-attachments/assets/4ed6448f-e22d-4fa2-bb57-cabaa0cc8833" />

8. Only for "AWS CLI" click on "Show" and follow the next steps to copy all of what it shows you into the correct AWS `credentials` file.
<img width="2305" height="1274" alt="image" src="https://github.com/user-attachments/assets/bd09ff61-5b33-4a69-bc5a-ed71140aaa55" />

### Configure your Lab Session Credentials
When we downloaded and installed AWS CLI, it automatically created a `config` and a `credentials` file within a directory at our root called `.aws/`. We will be copy and pasting the entire set of credentials from the Vocareum into the credentials file.

1. Within your CLI, you should be able to access the print out the contents of the `credentials` file by running `cat ~/.aws/credntials`. It is okay if there is nothing in there at the moment.
2. Open the `credentials` file in the `nano` editor by running `nano ~/.aws/credntials`. Alternatively, you can navigate into in your Finder/File Explorer and open it in Notepad, VS Code, or whatever.
3. Delete anything in there and paste your entire set of credentials from Vocareum, including the part that says "[default]".
4. Save and close it.
5. Open the `config` file in the `nano` editor by running `nano ~/.aws/config`. Alternatively, you can navigate into in your Finder/File Explorer and open it in Notepad, VS Code, or whatever.
6. Delete anything in there and paste the following:
```
[default]
region = us-east-1
output = json
```
7. Everything should be set up, so now in your `s3_bucket_lab` directory, run the following to list all buckets in S3:
```
aws s3 ls
```
8. If you get an error, head to "Troubleshooting Setup" below. If you get either nothing or a list of buckets, you are all set!

<br>

### Troubleshooting Setup
-  If you get this error: `An error occurred (ExpiredToken) when calling the ListBuckets operation: The provided token has expired.`, it means your Lab Session was either stopped or it expired, meaning you just need to start up your Sandbox Lab again and copy and paste in the new credentials into `~/.aws/credentials`, but no need to do anything to `~/.aws/config`.
-  If you get any other error, it means you have not set this up properly. Read back through the instructions and try them again, if the issue persists, please come to office hours.

<br>

---

## Objectives and Preamble

In this lab you will:

1. Using the AWS CLI, create a bucket in S3.
2. Upload a file into the bucket.
3. Verify the file is in the bucket.
4. Verify the file is not publicly accessible.
5. Create an expiring URL for the file and verify access.
6. Modify the bucket ACL to allow for public access.
7. Upload a new file with public access enabled, and verify access.
8. Upload a file and delete it.
9. Finally, write Python3 snippets using the `boto3` library to upload a private file, a public file, and to presign an object in S3.

### S3 Security and HTTP Access by URL

S3 buckets are PRIVATE by default. No files/objects uploaded to a plain, unaltered bucket are ever publicly-accessible. In this lab you will learn more about public/private buckets and objects.

AWS operates many `regions` of infrastructure around the world. We will be using the `us-east-1` region, the first and one of their largest regions. To get the web URL to any public file in `us-east-1` this is the syntax:
```
https://s3.amazonaws.com/ + BUCKET_NAME + / file/path.sfx
```

For example, this URL is to a publicly-accessible file within a publicly-accessible bucket:
[`https://s3.amazonaws.com/ds2002-resources/vuelta.jpg`](https://s3.amazonaws.com/ds2002-resources/vuelta.jpg)

<br>

---

## Part 1 (AWS CLI - Vocareum) (Instructional): Create and Configure an S3 Bucket, Then Load a File

This part is just instructional and should be done within the AWS CLI found in Vocareum:
<img width="1920" height="467" alt="image" src="https://github.com/user-attachments/assets/9e6b0071-2e2c-4535-93c1-3dc7972dacac" />

1. List any existing buckets (there should be none):

    ```
    aws s3 ls
    ```

2. Create a new bucket using the `mb` S3 subcommand. Add **your computing ID** to the name of the bucket, i.e. `ds2002-f25-atr8ec` and so on. Note the use of the `s3://` protocol before the bucket name.

    ```
    aws s3 mb s3://ds2002-f25-atr8ec
    ```

3. Grab an image file. Using the `curl` command below you can retrieve any image from the Internet you want to use for this lab. Once you have the URL copied for the image, use this command syntax:

    ```
    curl URL > file
    ```
    For example, to fetch the [Google logo](https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png). You can output the image to a new file name.
    ```
    curl https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png > google_logo.png
    ```

4. So now you have a local file. Imagine you want to upload the file to your new S3 bucket. Use the AWS CLI to do this. The syntax is:
    ```
    aws s3 cp FILE s3://BUCKET/
    ```

    For example, to upload the Google logo:

    ```
    aws s3 cp google_logo.png s3://ds2002-f25-atr8ec/
    ```

5. Go ahead and upload your file. List the contents of your bucket to verify it is there. Notice it is the same `ls` command, but specifying the bucket to list the contents of:

    ```
    aws s3 ls s3://ds2002-f25-atr8ec/
    ```
    which should return something like:
    ```
    $ aws s3 ls s3://ds2002-f25-atr8ec/
    2025-11-02 12:59:52      13504 google_logo.png
    ```

6. Take the bucket and file path and assemble a public URL to your file as described at the start of this lab:
    ```
    # https://s3.amazonaws.com/ + BUCKET_NAME + / FILE_PATH
    
    https://s3.amazonaws.com/ds2002-f25-atr8ec/google_logo.png
    ```
    Test that URL using your web browser. What do you see?

7. You cannot retrieve the file using a plain HTTPS address because anonymous web access is not allowed to your bucket or your file. Let's do a special trick S3 is capable of by creating an "expiring" URL that allows access to your file for a specified amount of time.

    The syntax for the command is:
    ```
    aws s3 presign --expires-in 30 s3://ds2002-f25-atr8ec/google_logo.png

    # The --expires-in flag is how many seconds the file should be public.
    # The s3:// is the BUCKET+FILE path to your specific file.
    ```

    Once you issue this command, it will return a long URL with signature:
    
    ```
    https://ds2002-f25-atr8ec.s3.us-east-1.amazonaws.com/google_logo.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIARSH3E2VEKJX3JBMC%2F20251102%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251102T210238Z&X-Amz-Expires=30&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDmBfzwoH44VZFLB36ehfW9ImIZPciBXrHt8EvGwq%2Fc%2BgIhAMbcaZeFeY35x7fYnO85TTs1ittKv4yjJ8h31PPaF34IKqcCCE4QARoMMTA3OTAwODg0Mjk2IgwNNPWmrIkh5LdhWU0qhALcpI2TTYpPQtb%2BFYpBFP5DS6Zc8ynJ7mOt86X47XXySOtCIwK8BXK1zdZpLM9fwSOwzO9whyBjQle8jlYYikKwZNFzUVNkp4sLe4Jp8h8YZQdMHiYCehdWPtQ9n%2Blo45D5phvMEC06%2FEYf082f2ehhlkImYhwjljI10Kptj9Cf2NnyVRzWVXciQHt0U%2F8A%2BU8yIoiMa%2BYPqlW1if2YJgbdQMAmbJt2ebsP7pr2ryJdnU7xkTXUiqIRwRrtaqo9F1Fwmb221qBOjC6Nb%2Fg6KI7Ch%2BJg9I1zzsuy1HH%2BVGYJLKjG%2FetF0FnOTGTnjyxWsNijwlZQPqsQM8nLHqLJzNtHBjhA6DDohJ%2FIBjqcAVKtZdqqcdZs%2BhMQrdbIw3zQj7nUBYhNuzJhy3%2FNt0Bs6gA8kIK2j%2Fj7Ho75pYIVOlCQOOqHG36JIi9s76sKLJ47fHrmDfBE5FT%2BI4rBFouIGUZL6Cd5MpuzzkyOg4WsWg%2FeGIfVbMA4Qasb87QXVKzrVjFtbSHlm%2FBW7mVTxdPDiUotrI3MAABJY2CWij%2FjDDbGWw7PBWrzo8JVTA%3D%3D&X-Amz-Signature=a5ff8bb7b28d20221c0cf3ca8791da197310e917d8ca064731345d7daceff242
    ```
    
    Open that link in a browser - you should be able to see your file.

    If you refresh the browser after the expiration period has elapsed, what do you see then?

<br>

---

## Part 2 (Local Terminal Using AWS CLI): Write a Bash Script (1 of 2)

In this part of the lab we are going to switch over to our Git Bash/Terminal to develop our scripts. Sure we could write our scripts in the Vocareum AWS CLI, however, we would need to set up our SSH and clone to that environment, which will just take unnecessary time. If we were not bound by the time limits of the Sandbox, and were working with full AWS accounts, it may be more advantageous to develop in AWS, but not this time.

Given what was covered above, and what we have covered this semester so far, the following should be relatively quick. Please follow the steps below:

1. Write a simple `bash` script that can performs two actions:
   - Uploads a file (image, PDF, etc.) to a private bucket.
   - Presigns a URL to that file with an expiration of `604800` (7 days).
   - Write the script so that it takes three positional arguments: The name of the local file to upload, the name of the bucket in your account, and the length of expiration in seconds.

**NOTE**: Test your script a few times, with enough of a short expiration that you can observe it timing out.

<br>

---

## Part 3 (AWS Console) (Instructional): Update Your bucket's ACL (Access Control List)

1. Open the [AWS Management Console](https://console.aws.amazon.com/) to perform this task. Either click the link or "AWS" in Vocareum, either should work so long as you are logged in and the Lab is active.
2. Within the AWS Management Console, open the S3 service and find your bucket.
3. Click the name of the bucket to get detailed settings.
4. Select the Permissions tab within your bucket settings.
5. Click "Edit" within the "Block public access (bucket settings)" section.
6. Uncheck all boxes and save your settings. Confirm the change.
7. Scroll down and click "Edit" within the "Object Ownership" section.
8. Enable ACLs by checking the right-hand radio button. Confirm your changes by checking the box. Leave "Bucket owner preferred" selected. Save your changes.

    These changes have not made your bucket or any of its contents public. However, they have now allowed you the option to specifically make any contents public if you choose to do so. (Without the above changes this would not be possible.)

    S3 also allows you to set a bucket policy to allow public access to ALL objects, or only objects of certain types, among many other policy options if needed.

10. Now that your bucket allows you to grant public access to specific files, fetch another image file from the Internet (`.gif`, `.png`, `.jpg`, etc.) and upload it with this syntax to make it public. Note the `--acl public-read` option:

    ```
    aws s3 cp --acl public-read IMAGE s3://BUCKET_NAME/
    ```

    For example:
    ```
    aws s3 cp --acl public-read vuelta.jpg s3://ds2002-f25-atr8ec/
    ```

11. Test access

    Using the `bucket/file` path structure, construct the URL for your file like this: 
    [`https://s3.amazonaws.com/ds2002-f25-atr8ec/vuelta.jpg`](https://s3.amazonaws.com/ds2002-f25-atr8ec/vuelta.jpg)

12. Delete a file in your bucket. Using the AWS CLI, upload another image file to the bucket. List the bucket contents to confirm it has been uploaded. And, finallly, delete the file using this syntax:

    ```
    aws s3 rm s3://BUCKET_NAME/FILE_NAME
    ```
    For example
    ```
    aws s3 rm s3://ds2002-f25-atr8ec/vuelta.jpg
    ```
    And confirm the file has been deleted:
    ```
    aws s3 ls s3://ds2002-f25-atr8ec/
    ```

13. To empty a bucket completely, a `--recursive` option is available:

    ```
    aws s3 rm s3://BUCKET_NAME/FILE_NAME --recursive
    ```
    You can only delete empty buckets. Once empty, to delete:
    ```
    aws s3 rb s3://BUCKET_NAME
    ```

<br>

---

## Part 4 (AWS SDK) (Instructional): Use the `boto3` library with Python3

Developers should keep in mind that S3 is a web service, or API, which means that in addition to using the AWS Management Console or CLI tools you can work with any AWS service using the language of your choice.

In this section of the lab you will perform basic S3 operations using Python3 and the `boto3` library.

Complete documentation for `boto3` is available:

* `boto3` - https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
* `s3` - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

<br>

### 1. Install and Import `boto3`

Should have been completed in Step 0 already, but just in case. To work with `boto3` you must first make sure it is installed, so that you can import it. From a terminal:
```
python3 -m pip install boto3
```

You can confirm that `boto3` is installed if you create a quick `test.py` file with the following code:
```python
import boto3
print("A successful import should result in no errors/warnings above. :)")
```

You can go ahead and delete the `test.py` file now.

<br>

### 2. Upload a file to S3 and keep it private
The following tasks assume you are able to import `boto3` successfully.

1. Each AWS service you connect to via `boto3` needs a `client` or `resource` or some other reusable connection. Let's create a simple client for the S3 service:

    ```
    import boto3

    s3 = boto3.client('s3', region_name='us-east-1')
    ```
    
    The variable `s3` populated with an instance of the `boto3.client` class can be named anything you like. Once a class object it can be reused for other calls to that specific service.


2. Once you have created a client you are now ready to use it. In your command prompt (in a local terminal or VSCode, etc.), upon invoking the `s3` class object you just created, you will notice many new options:

    You can only do this if you are working in a python3 session on the command line, which Git Bash tends to struggle with. So you can run this in the VS Code, maybe Terminal (macOS), if you want to see it or you can just see my screenshot below.
    ```python3
    s3.<TAB>
    ```
    
    May need to do:
    ```python3
    s3.<TAB><TAB>
    ```

    My screenshot showing all of the s3 options to choose from:
   <img width="1660" height="1305" alt="image" src="https://github.com/user-attachments/assets/70569f6e-fc91-42f9-84cb-fa3a4659a69b" />


4. For instance, list all your buckets:

    ```
    import boto3

    # create client
    s3 = boto3.client('s3', region_name="us-east-1")

    # make request
    response = s3.list_buckets()

    # now iterate through the response:
    for r in response['Buckets']:
      print(r['Name'])
    ```

    This will return the name(s) of any bucket(s) in your account in a full JSON payload, with all results nested a single array. Note that above, a variable named `response` was created and populated with the results of the `list_buckets()` method. This is an arbitrary variable name - you can always use your own.

5. To upload a file to your bucket:

    ```
    import boto3

    s3 = boto3.client('s3', region_name="us-east-1")
    bucket = 'ds2002-f25-atr8ec'
    local_file = 'project/vuelta.jpg'

    # 1. Open the file in binary read mode ('rb')
    with open(local_file, 'rb') as data:
        resp = s3.put_object(
            Body=data,        # PASS THE OPEN FILE OBJECT HERE
            Bucket=bucket,
            Key=local_file    # This is the destination key/path in S3
    )
    ```

    Some explanation:
      - `bucket` is an S3 bucket that already exists.
      - `local_file` is the path/file you want to upload.
      - `Key` within the `put_object()` method is the destination path you want for the uploaded path.
      - These three parameters are the minimum required for a `put_object` call. There are many other options.
  
6. Alternatively, you can upload an object using `upload_file()`:
    ```python3
    import boto3

    s3 = boto3.client('s3', region_name="us-east-1")
    bucket = 'ds2002-f25-atr8ec'
    local_file_path = 'project/vuelta.jpg'
    s3_key = 'vuelta/2024.jpg' # Example of a different key

    s3.upload_file(
        Filename=local_file_path,  # The local file path on your system
        Bucket=bucket,             # The S3 bucket name
        Key=s3_key                 # The destination object key in S3
    )

7. Write your own upload script and test for success. Try getting the file using a public URL. You should get `Permission Denied`.

<br>

### 3. Upload a file to S3 and make it public

Upload a new file to S3 with public visibility. The request will be like the one above, but add the following parameter:

    ACL = 'public-read',

Test your file upload using a public URL to see if you can access it.

<br>

---

## Part 5. (AWS SDK): Write a Python Script using `boto3` (2 of 2)

Like the `bash` script you wrote above, now write a simple Python script that performs a similar task. Your script should:

  - Fetch and save a file from the internet using `urllib`, [`requests`](https://gist.github.com/nmagee/e43265d988c10a0bde79aabf7f6d97fe) or some other simple method. A simple gif would be a good file to work with, but your code should pull the file, not a human manually saving it.
  - Upload the file to a bucket in S3.
  - Presign the file with an expiration time. Documentation for that method is [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html)
  - Output the presigned URL.
  - Test your script and be sure it works without error.
  - BONUS: If you'd like to learn a new skill, try using the [`argparse`](https://docs.python.org/3/library/argparse.html) library to customize command-line arguments with a Python script. 

Here is a snippet for generating a presigned URL:

```python
# vars needed
bucket_name = str
object_name = str
expires_in = int

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)
```

<br>

---

## Step 6: Add, Commit, Push, and Submit on Canvas!

1.  Stage all of your changes at once: `git add .`.
2.  Commit your staged changes to your local `Lab_8` branch **with a message**: `git commit -m "Completed Lab 8: S3 Storage"`
3.  Push your local branch to your remote repository: `git push --set-upstream origin Lab_8`
4.  Navigate to your forked repository on GitHub.
5.  Switch to your `Lab_8` branch on GitHub.
6.  Navigate to your `s3_bucket_lab` directory.
7.  Copy the URL to your `s3_bucket_lab` directory on your `Lab_8` branch, and paste the URL into the Lab 8 assignment on Canvas.
