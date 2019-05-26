from netmiko import ConnectHandler
from pprint import pprint
from ciscoconfparse import CiscoConfParse
from os import path
import yaml

# setup import of connection details
home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    yaml_out = yaml.load(f, Loader=yaml.SafeLoader)

# connect to router 4 and pull down `show run`
cisco4 = yaml_out['cisco4']

net_conn = ConnectHandler(**cisco4)

output = net_conn.send_command('show run')

# set output as a list for ciscoconfparse to handle
sh_run = output.splitlines()

CiscoConfParse(sh_run)


