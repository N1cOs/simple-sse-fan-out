FROM python:3.8-slim

WORKDIR /opt/scanner

RUN apt-get update && apt-get install -y gcc

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir \
    --requirement requirements.txt

COPY . /opt/scanner
