# API Assignment

## Clone this repository

```
git clone https://github.com/ds3002/fastapi.git
```

You may build upon the code in `app/main.py` or create a new `.py` file from scratch.

Next, create a virtual environment in Python3
```
virtualenv venv
```
and activate it
```. venv/bin/activate
```
and run your pip installations
```
python3 -m pip install -r requirements.txt
```

## Customize Your API

Use `FastAPI` (to run locally) that achieves the following four goals:

1. Create a GET endpoint `http://127.0.0.1:8000/test`
That takes FOUR query string parameters (parameters appended to the URL such as http://127.0.0.1:8000/test?one=xxx&two=yyy&three=zzz&four=aaa) and displays them back. Two of these must be strings and two must be integers.

2. Create a POST endpoint `http://127.0.0.1:8000/items/{item_id}`
That takes an "item_id" as a path parameter and a "description" in a data payload and appends them both to a text file.

3. Create a GET endpoint `http://127.0.0.1:8000/quotes/{row_number}`
That takes a "row_number" parameter and returns the corresponding row (1-10) from the "quotes.txt" file included here. --> Helpful reference on extracting lines: https://www.computerhope.com/issues/ch001721.htm

4. Create a GET endpoint `http://127.0.0.1:8000/github/{username}` 
That retrieves and returns the URL of the specified user's Github profile picture and returns it. --> Github User API reference: https://docs.github.com/en/rest/reference/users

FastAPI Documentation: https://fastapi.tiangolo.com/

## Run and Test your API

To run your local `uvicorn` web server, run this command from within the `app` directory of the project:

```
uvicorn app:main --reload
```
Where `app` is the name of the `FastAPI` instance declared in your Python file, and `main` is the filename.

To view your local API, open a browser or Postman to http://127.0.0.1:8000/
