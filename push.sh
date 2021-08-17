#!/usr/bin/bash

SHARK_DIR="/shark"
SHARK_CONF="${SHARK_DIR}/Shark-Config"

# Used to verify if the config file.

if [ ! `which yamllint` ]; then
  dnf install -y yamllint.noarch &&  echo "Installing yamllint, exiting..."
fi

if [ ! `/usr/bin/yamllint trading-config.yml` ]; then
  echo "Invalid YAML, exiting..."
  exit 1;
fi

# Pushes the shark config to the shark server.
cp -p ${SHARK_CONF}/trading-config.yml ${SHARK_DIR}/_sync/

# Convert the yaml into nagios code
${SHARK_CONF}/conf/_sync/convert_configuration.py > ${SHARK_CONF}/_sync/sync_role/files/conf.d/shark.cfg

ansible-playbook ${SHARK_CONF}/_sync/site.yml -i _sync/hosts 
