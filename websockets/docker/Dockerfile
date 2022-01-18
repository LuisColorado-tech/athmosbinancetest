FROM python:3.8

WORKDIR /usr/src/websockets

RUN apt-get update && apt-get upgrade && pip install websocket-client

COPY . .
EXPOSE 80
