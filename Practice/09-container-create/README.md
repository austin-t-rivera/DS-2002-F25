# Creating Containers

This directory contains four container projects of varying complexity.
Take the time to examine each directory separately, paying careful attention
to the `Dockerfile` for each build, as well as any accompanying code or 
supporting files.

## `fortune`

This is a statically loaded quote/fortune generator. All data is contained within
the container and, when run, it returns one of them to the user. To build, cd into
this directory:

```
docker build -t fortune .
```
To run the container:
```
docker run fortune
```

## `whalesay`

This is a famous demo container created by Docker to demonstrate an interactive
container image that takes input from a user. To build it, cd into this directory:

```
docker build -t whalesay` .
```
To run it, simply append a command or quote or joke at the end of the `run` command:
```
docker run whalesay Hello everyone!
```

## `fastapi`

This is the FastAPI demonstration package covered earlier in the semester. This
will run a local API over an arbitrary port.

To build, cd into this directory:
```
docker build -t fastapi .
```
Then to run it, map a local host port to port 80 of the container:
```
docker run -d -p 8080:80 fastapi
```

## `convert`

This is the Python3 ETL pipeline segment demonstrated in the lecture. You can build
it locally by changing into its directory and running:

```
docker build -t converter .
```
To try running it on your own, just map a directory to the `/data` path of the directory and pass the
fictional ID `0987654321` in as a parameter:

```
docker run -v ${PWD}:/data converter -i 0987654321
```
