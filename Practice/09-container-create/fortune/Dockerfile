FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
        fortune fortunes-min && \
    rm -rf /var/lib/apt/lists/*

ENV PATH=/usr/games:${PATH}

ENTRYPOINT ["fortune"]
