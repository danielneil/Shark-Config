#!/usr/bin/bash

# Used to verify if the config file.

if [ ! `which yamllint` ]; then
  dnf install -y yamllint.noarch
fi

/usr/bin/yamllint trading-config.yml

# Pushes the shark config to the shark server.
