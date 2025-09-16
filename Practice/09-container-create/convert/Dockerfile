FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update && apt-get install -y \
    python3 python3-dev gcc \
    python3-pip musl-dev g++ \
    libffi-dev openssl

COPY requirements.txt /root/requirements.txt
RUN python3 -m pip install -r /root/requirements.txt

COPY convert /usr/local/bin/convert

WORKDIR /data
ENTRYPOINT ["convert"]
