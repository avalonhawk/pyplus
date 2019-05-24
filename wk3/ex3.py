import json
from pprint import pprint

# Open the datafile and read in the contents
filename = "nxos_intf.json"
with open(filename) as f:
    nxos_data = json.load(f)

# initilize blank lists for collecting IPv4 and IPv6 addresses
ipv4_list = []
ipv6_list = []

# iterate through the data and collect the addresses and prefixes
for intf, ip_info in nxos_data.items():
    for ipv4_or_ipv6, address_info in ip_info.items():
        for ip, prefix_info in address_info.items():
            prefix = prefix_info['prefix_length']
            if ipv4_or_ipv6 == 'ipv4':
                ipv4_list.append("{}/{}".format(ip, prefix))
            elif ipv4_or_ipv6 == 'ipv6':
                ipv6_list.append("{}/{}".format(ip, prefix))

# finally, print out the resulting lists
print("=" * 40)
print("IPv4 Addresses: {}".format(ipv4_list))
print("-" * 40)
print("IPv6 Addresses: {}".format(ipv6_list))
print("=" * 40)
