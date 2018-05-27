#!/usr/bin/env bash

VER=1.0
APP_NAME="hermes"

docker build -t local/${APP_NAME}:${VER} .
