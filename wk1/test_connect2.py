from netmiko import ConnectHandler
from getpass import getpass

password = getpass("Enter Lab Device Password:")

nxos1 = {
        'device_type': 'cisco_nxos',
        'host': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'session_log': 'nxos1_log.txt'
        }
nxos2 = {
        'device_type': 'cisco_nxos',
        'host': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'session_log': 'nxos2_log.txt'
        }

for device in (nxos1, nxos2):
    conn = ConnectHandler(**device)
    print(conn.find_prompt())
