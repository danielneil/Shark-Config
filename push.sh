#!/usr/bin/bash

# Used to verify the yaml file.

if [ ! `which yamllint` ]; then
  dnf install -y yamllint.noarch
fi

yamllint trading-config.yml

# Pushes the shark config to the shark server.


