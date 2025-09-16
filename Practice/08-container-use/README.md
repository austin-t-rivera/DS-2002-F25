# Running Containers

## Pulling Container Images

To pull a container image, find its location from Docker Hub or another registry. This should appear
something like:

```
docker pull ghcr.io/ds3002/course:latest
```

To view all the containers you have pulled to your computer,

```
docker images
```

To delete an image, use the `rmi` remove image command with either the container name:tag or ID.

```
docker rmi image_name
```

To delete all unused images:

```
docker system prune
```

## Running in Detached Mode

To run a container in detached mode, append the `-d` flag to the `docker run` command with the
container image name:

```
docker run -d nginx
```

## Running in Interactive Mode

To work with a container interactively, append the `-it` flag to the `docker run` command with
the container image name. Be sure to add a shell or some other executable program after the image
name:

```
docker run -it ubuntu /bin/bash
```

## View Running Containers

To see all containers running locally:

```
docker ps
```

Should give some results like this:

```
CONTAINER ID   IMAGE                          COMMAND       CREATED          STATUS          PORTS     NAMES
2ad2502e9600   ghcr.io/ds3002/course:latest   "/bin/bash"   36 minutes ago   Up 36 minutes             epic_hodgkin
```

You can now refer to any specific container by using either the FULL name `epic_hodgkin`, or the first few characters
of the Container ID, such as `2ad2`

## Stop a Running Container

To stop a container

```
docker stop epic_hodgkin
```

or

```
docker stop 21d2
```

## Add an Environment Variable

To inject ENV variables into a container, add the `-e` flag with a Key-Value mapping when you run the container:

```
docker run -it -e MYKEY=myvalue ubuntu:latest /bin/bash
```

## Attach a Local Port

To map a local port from a container to your workstation, use the `-p` flag with a mapping of
`HOST_PORT:CONTAINER_PORT`. This allows you to view/test a service listening on that port:

```
docker run -d -p 8080:80 nginx
```

## Mount Storage

To mount a directory from your local workstation into a container when launched, use the `-v` flag with
a mapping of `HOST_VOLUME:CONTAINER_VOLUME`:

```
docker run -it -v /home/user/project:/root/project ubuntu:latest /bin/bash
```

## Inspect Properties of a Container

To inspect all metadata attributes about a running container, such as IP address, or volume mounts, etc.
use the `inspect` command. This will return a JSON payload of fields:

```
docker inspect 2ad2
```

## Review Logs

To view the output logs from a running container:

```
docker logs 2ad2
```

## Shell into a Running Container

Finally, to "hop" into a running container that is running in detached mode, use the `exec -it` command
against the ID or name of the running container. Be sure to add a shell or other executable after the name
of the container.

```
docker exec -it 2ad2 /bin/bash
```
