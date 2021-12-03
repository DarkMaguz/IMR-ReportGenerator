#!/bin/bash -e

# Create network if it does not already exist
docker network inspect imr-network >/dev/null 2>&1 || \
  docker network create imr-network

docker-compose up -d
