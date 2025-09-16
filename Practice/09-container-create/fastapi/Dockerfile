FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8
COPY ./app /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt