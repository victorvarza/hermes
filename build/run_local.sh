#!/bin/bash

DOCKER_HUB_USER="local"
VER="1.0"
APP_NAME="hermes"

[[ $# -gt 0 ]] && VER=$1

docker rm -f ${APP_NAME}
docker run -d -v /mnt/monitor:/monitor --name ${APP_NAME} ${DOCKER_HUB_USER}/${APP_NAME}:${VER}