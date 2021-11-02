#!/usr/bin/bash

SHARK_DIR="/shark"
SHARK_CONF="${SHARK_DIR}/Shark-Config"

# Used to verify if the config file.

if [ ! `which yamllint` ]; then
  dnf install -y yamllint.noarch &&  echo "Installing yamllint, exiting..."
fi

/usr/bin/yamllint ${SHARK_CONF}/trading-config.yml  

if [ $? -ne 0  ]; then
 echo "Invalid YAML, exiting..." && exit 1
fi

# Pushes the shark config to the shark server.
cd ${SHARK_CONF} && cp -p trading-config.yml _sync/

# Convert the yaml into nagios code
cd ${SHARK_CONF} && _sync/convert_configuration.py > _sync/sync_role/files/conf.d/shark.cfg

cd ${SHARK_CONF}/_sync && ansible-playbook site.yml -i hosts 