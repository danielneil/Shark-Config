#!/usr/bin/bash

if ! $(which ansible-playbook > /dev/null); then
 echo "Install ansible, and run again, exiting.."
 exit 1;
fi

ansible-playbook ./site.yml 
