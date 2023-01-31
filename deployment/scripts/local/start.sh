#!/usr/bin/env bash

if [ ! -f "deployment/scripts/local/.env" ]; then
    cp deployment/scripts/local/.env.docker deployment/scripts/local/.env
fi

source deployment/scripts/local/.env

LOCAL_PATH=`pwd`

minikube start \
    -p ${MINIKUBE_PROFILE} \
    --cpus=${MINIKUBE_CPUS} \
    --memory=${MINIKUBE_MEMORY} \
    --driver=${MINIKUBE_DRIVER} \
    --kubernetes-version=${MINIKUBE_KUBERNETES_VERSION} \
    --mount=true \
    --mount-string="${LOCAL_PATH}:/mount-termination-tickets"

