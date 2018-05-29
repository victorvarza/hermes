#!/usr/bin/env bash

DOCKER_HUB_USER="trainersontheweb"
VER="1.0"
APP_NAME="hermes"

[[ $# -gt 0 ]] && VER=$1

docker tag local/${APP_NAME}:${VER} ${DOCKER_HUB_USER}/${APP_NAME}:${VER}
docker push ${DOCKER_HUB_USER}/${APP_NAME}:${VER}