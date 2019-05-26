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

parser = CiscoConfParse(sh_run)

interfaces = parser.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

print()
print("=" * 80)

for obj in interfaces:
    print("Interface Line: {}".format(obj.text))
    ipaddr = obj.re_search_children(r"^\s+ip address")[0].text
    print("IP Address Line: {}".format(ipaddr))
    print("=" * 80)
    print()

