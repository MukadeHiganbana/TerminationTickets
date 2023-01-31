#!/usr/bin/env bash

CREDENTIALS_PASSWORD=no_value

if [ -f .credentials_password  ]; then
    CREDENTIALS_PASSWORD=$(cat .credentials_password)
else
  echo "Please create and fill credentials into .credentials_password file"
  exit 1
fi

rm -rf credentials.zip

zip -r -e credentials.zip deployment/credentials/ -P $CREDENTIALS_PASSWORD
