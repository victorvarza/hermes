#!/usr/bin/env bash

VER=1.0
APP_NAME="hermes"

[[ $# -gt 0 ]] && VER=$1

docker build -t local/${APP_NAME}:${VER} .
