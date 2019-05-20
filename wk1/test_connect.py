from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
        'device_type': 'cisco_nxos',
        'host': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': getpass("Enter password for nxos1"),
        'session_log': 'nxos1_log.txt'
        }
net_conn = ConnectHandler(**nxos1)
print(net_conn.find_prompt())
