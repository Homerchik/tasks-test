#!/bin/bash

IMAGE_SRC="./images/todo-app.tar"
IMAGE="todo-app:latest"

docker load -i $IMAGE_SRC
docker pull direvius/yandex-tank

docker run -e VERBOSE=1 --name "todo"  -d --rm -p "8080:4242" $IMAGE
docker run --name "ytank" --rm -v "$(pwd)":/var/loadtest --net host -it direvius/yandex-tank -c configs/tank.yaml
docker stop "todo"
