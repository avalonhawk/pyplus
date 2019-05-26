from netmiko import ConnectHandler
from pprint import pprint
from ciscoconfparse import CiscoConfParse
from os import path
import yaml

home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    yaml_out = yaml.load(f, Loader=yaml.SafeLoader)

cisco4 = yaml_out['cisco4']

net_conn = ConnectHandler(**cisco4)

output = net_conn.send_command("show run")


