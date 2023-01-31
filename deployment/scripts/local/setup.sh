#!/usr/bin/env bash

if [ ! -f "deployment/scripts/local/.env" ]; then
    cp deployment/scripts/local/.env.docker deployment/scripts/local/.env
fi

source deployment/scripts/local/.env

./deployment/scripts/local/start.sh

./deployment/scripts/local/build.sh

./deployment/scripts/local/init.sh

./deployment/scripts/local/deploy.sh
