#!/usr/bin/env bash

if [ ! -f "deployment/scripts/local/.env" ]; then
    cp deployment/scripts/local/.env.docker deployment/scripts/local/.env
fi

source deployment/scripts/local/.env

docker build -f "${DOCKER_DOCKERFILE}" -t "${DOCKER_IMAGE}" .

source deployment/scripts/local/image-load.sh