#!/usr/bin/bash

SHARK_DIR="/shark"

# Used to verify if the config file.

if [ ! `which yamllint` ]; then
  dnf install -y yamllint.noarch
fi

/usr/bin/yamllint trading-config.yml

# Pushes the shark config to the shark server.
cp -p ${SHARK_DIR}/trading-config.yml ${SHARK_DIR}/_sync/

# Convert the yaml into nagios code
${SHARK_DIR}/conf/_sync/convert_configuration.py > ${SHARK_DIR}/_sync/sync_role/files/conf.d/shark.cfg

ansible-playbook ${SHARK_DIR}/conf/_sync/site.yml -i _sync/hosts 
