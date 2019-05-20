from netmiko import ConnectHandler
from getpass import getpass

device = {
        'host': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type': 'cisco_nxos',
        'global_delay_factor': 2,
        }

net_conn = ConnectHandler(**device)
output = net_conn.find_prompt()

print('-' * 30)

output = net_conn.send_command('show lldp nei detail', delay_factor=8)
print(output)
print('-' * 30)
net_conn.disconnect()
