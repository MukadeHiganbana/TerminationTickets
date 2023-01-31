#!/usr/bin/env bash

if [ ! -f "deployment/scripts/local/.env" ]; then
    cp deployment/scripts/local/.env.docker deployment/scripts/local/.env
fi

source deployment/scripts/local/.env

minikube docker-env \
    -p "${MINIKUBE_PROFILE}" \
    --shell=bash

eval "$(minikube -p "${MINIKUBE_PROFILE}" docker-env)"