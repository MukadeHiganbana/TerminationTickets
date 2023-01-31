#!/usr/bin/env bash

set -a

CIRCLE_BRANCH="$(git symbolic-ref HEAD 2>/dev/null)" ||
CIRCLE_BRANCH="(no_value)"
CIRCLE_BRANCH=${CIRCLE_BRANCH##refs/heads/}

CREDENTIALS_PASSWORD=no_value

if [ -f .credentials_password  ]; then
    CREDENTIALS_PASSWORD=$(cat .credentials_password)
else
  echo "Please create and fill credentials into .credentials_password file"
  exit 1
fi

circleci local execute --branch $CIRCLE_BRANCH --job "deploy_to_gcloud" --env CREDENTIALS_PASSWORD=$CREDENTIALS_PASSWORD
