import json
from pprint import pprint

# Open the datafile and read in the contents
filename = "arp.json"
with open(filename) as f:
    arp_data = json.load(f)

# extract the arp item we want to work with
ip_info = arp_data['ipV4Neighbors']

# initalize a blank dictionary
arp_dict = {}

# extract and map ip -> mac
for i in ip_info:
    mac = i['hwAddress']
    ip = i['address']
    arp_dict[ip] = mac

# print the resulting dictionary
pprint(arp_dict)

