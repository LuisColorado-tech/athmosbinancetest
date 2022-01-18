#!/bin/bash
docker-compose -f binance_coin_app/docker/docker-compose.yml up --build -d
docker-compose -f websockets/docker/docker-compose.yml up --build
