#!/usr/bin/env bash

if [ ! -f "deployment/scripts/local/.env" ]; then
    cp deployment/scripts/local/.env.docker deployment/scripts/local/.env
fi

source deployment/scripts/local/.env

./deployment/scripts/local/set-context.sh

kubectl apply -f deployment/kubernetes/local/load_balancer.yml
kubectl apply -f deployment/kubernetes/local/web.yml
kubectl apply -f deployment/kubernetes/local/worker.yml

minikube -p ${MINIKUBE_PROFILE} service web --url
