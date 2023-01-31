#!/usr/bin/env bash

if [ ! -f "deployment/scripts/local/.env" ]; then
    cp deployment/scripts/local/.env.docker deployment/scripts/local/.env
fi

source deployment/scripts/local/.env

minikube -p "${MINIKUBE_PROFILE}" \
          image load "${DOCKER_IMAGE}" \
          --daemon=true