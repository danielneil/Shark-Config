#!/usr/bin/bash

# Used to verify if the config file.

if [ ! `which yamllint` ]; then
  dnf install -y yamllint.noarch
fi

/usr/bin/yamllint trading-config.yml

# Convert the yaml into nagios code
_sync/convert_configuration.py > _sync/sync_role/files/nagios_config/shark.cfg

# Pushes the shark config to the shark server.
cp -p trading-config.yml _sync/

ansible-playbook _sync/site.yml -i _sync/hosts 
