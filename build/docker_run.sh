#!/bin/bash

DOCKER_HUB_USER="trainersontheweb"
VER="1.0"
APP_NAME="hermes"

docker rm -f ${APP_NAME}
docker run -d -v /mnt/monitor:/monitor --name ${APP_NAME} local/${APP_NAME}:${VER}