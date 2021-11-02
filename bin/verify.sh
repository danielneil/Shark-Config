#!/usr/bin/bash

echo "Verifying Shark's config"

if [ ! `which yamllint` ]; then
  echo "Install yamllint please, exiting..."
  exit 1
fi

XMLLINT=`which yamllint`

$XMLLINT trading-config.yml

if [ $? -ne 0  ]; then
 echo "Invalid YAML, exiting..." && exit 1

echo "Shark's YAML config looks OK..."
exit 0
