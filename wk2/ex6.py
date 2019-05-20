from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
import time

password = getpass('Enter password for devices: ')

device = {
        'host': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'secret': password,
        'device_type': 'cisco_nxos',
        'session_log': 'ex6_session.txt',
        }

net_conn = ConnectHandler(**device)

print(net_conn.find_prompt())
print('Entering config mode')
print('-' * 80)
net_conn.config_mode()
print(net_conn.find_prompt())

print('Exiting config mode')
print('-' * 80)
net_conn.exit_config_mode()
print(net_conn.find_prompt())

print('Exiting enable mode')
print('-' * 80)
net_conn.write_channel('disable\n')
time.sleep(2)
print(net_conn.read_channel())

print('Entering enable mode')
print('-' * 80)
net_conn.enable()
print(net_conn.find_prompt())

