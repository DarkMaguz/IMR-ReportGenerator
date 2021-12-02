#!/bin/bash

docker build -t darkmagus/flask .
docker run -it -p 5001:5001 darkmagus/flask
