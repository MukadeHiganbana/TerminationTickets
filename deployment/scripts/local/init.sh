#!/usr/bin/env bash

if [ ! -f "deployment/scripts/local/.env" ]; then
    cp deployment/scripts/local/.env.docker deployment/scripts/local/.env
fi

source deployment/scripts/local/.env

./deployment/scripts/local/set-context.sh

kubectl create secret generic ssh-keys --from-file=id_rsa=${SSH_ID_RSA} \
  --from-file=id_rsa.pub=${SSH_ID_RSA_PUB} \
  --from-file=known_hosts=${SSH_KNOWN_HOSTS} \
  --from-file=config=${SSH_CONFIG}

kubectl apply -f deployment/kubernetes/local/init.yml
