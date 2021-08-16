#!/usr/bin/python3

# Process the yaml configuration file, so we can regenerate it into something nagios understands.

import yaml

##############################################################    
from io import StringIO

class StringBuilder:

    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Add(self, str):
        self._file_str.write(str)

    def __str__(self):
        return self._file_str.getvalue()

##############################################################    
def process_instrument_config(i_data):

    instrument = i_data['instrument']
    group = i_data['group']

    hosts.Add("\ndefine host {\n")
    hosts.Add("\tuse stock\n")
    hosts.Add("\thost_name " + instrument + "\n")
    hosts.Add("\thostgroups " + group + "\n")
    hosts.Add("\taddress 127.0.0.1" + "\n")
    hosts.Add("\tregister 1" + "\n")
    hosts.Add("}\n")

    hostGroups.append(str(group))

    # Process the list of plugins,
    process_plugin_config(i_data['plugin'])


##############################################################    
# Process the plugins
def process_plugin_config(p_data):

    for plugin in p_data:

        # Get the standard arguments.
        plugins.Add(plugin['name'] + "\n")
        plugins.Add(plugin['desc'] + "\n")
        plugins.Add(plugin['group'] + "\n")
        plugins.Add(plugin['instrument'] + "\n")

        # Now process the additional arbitrary arguments.
        print (plugin[5:1])

##############################################################    
# Process the yaml file - main entry point.
hosts = StringBuilder();
hostGroups = []
plugins = StringBuilder();

with open ("trading-config.yml", "r") as f:

    # Load YAML data from the file

    data = yaml.safe_load(f)

    # Iterate the loop to read and print YAML data

    for i in range(len(data)):

        process_instrument_config(data[i])

##############################################################    
# Print the hosts group configuration.
sorted_host_groups = sorted(set(hostGroups))

for ig in sorted_host_groups:

    print ("\ndefine hostgroup {")
    print ("\thostgroup_name " + ig )
    print ("\talias " + ig )
    print ("}")

##############################################################    
# Print the hosts configuration.
print (hosts)


##############################################################    
# Print the plugin configuration
print (plugins)
