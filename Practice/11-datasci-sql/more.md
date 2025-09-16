# Using SQL in Data Science

0. Sync your Repository

Change directories to your local clone of the course repository. Then synchronize your code by issuing:

```
git pull origin main
```

1. Interactively using Python3

Refer to the `manual-query.py` file and `fastapi-rds` folder for code examples, etc.

2. Interactively from a Notebook

To run the SciPy Jupyter Notebook locally, change directories to your local copy of the course container and:

```
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/scipy-notebook
```

Follow along with cells in the `ConnectToRds.ipynb` notebook.

3. Data-driven workflows/pipelines

