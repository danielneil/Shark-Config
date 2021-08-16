#!/usr/bin/bash

# used to verify the yaml file.

if [ $(which yamllint) -nq 0 ]:
  dnf install -y yamllint.noarch
fi

# Pushes the shark config to the shark server.


