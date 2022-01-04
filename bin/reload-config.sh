#!/usr/bin/bash

if ! $(which /usr/bin/ansible); then
 echo "Install ansible, and run again, exiting.."
 exit 1;
fi

ansible-playbook refresh_config/
