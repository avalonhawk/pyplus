from pprint import pprint
from netmiko import ConnectHandler
import yaml

# read in connection file
filename = input("Enter connection filename: ")

with open(filenmae) as f:
    connections = yaml.load(f)

net_conn = ConnectHandler(**connections['cisco3'])
print(net_conn.find_prompt())


