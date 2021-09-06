#!/bin/bash

IMAGE_SRC="./images/todo-app.tar"
IMAGE="todo-app:latest"

docker load -i $IMAGE_SRC
docker run -p "8080:4242" $IMAGE