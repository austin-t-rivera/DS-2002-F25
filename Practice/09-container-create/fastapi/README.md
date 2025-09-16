# Header/info commands:
FROM - the base image upon which to build your container.
FROM centos/centos7:latest
FROM alpine/python-3.8.8

ENV - set arbitrary environment variables for the container when it is run.
ENV RUNTIME="1.0.13"

WORKDIR - sets a current directory for additional commands to use, like RUN, CMD, COPY, ADD, ENTRYPOINT.
WORKDIR /app

# Put things into the container
COPY - copies in source files/folders
COPY ./app .

ADD - copies in source files/folders with specific permissions, or remotely
ADD http://company.com/folder/file1.zip /app
ADD file1 /app/file1
ADD zimzam /app/config

# Executing things
RUN - run an arbitrary command. Allowed multiple times.
RUN pip install -r requirements.txt

CMD - run a single command. Only one allowed per Dockerfile
CMD /bin/bash /root/run-app.sh -c xxx -d xxx

ENTRYPOINT - allows you to configure a container that will run as an executable. OVERRIDES a CMD.
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE - tells Docker that this container listens on a specific port when run.
EXPOSE 3000

# Lesser commands:
ARG - a way of passing an argument or value in at build time.
ARG VERSION="1.13"
RUN /bin/bash installer.sh $VERSION

USER - specify the user the container should run as
LABEL - a way of adding metadata to the image.
VOLUME - marks a mountpoint held for externally mounted storage when run.
VOLUME /root/practice