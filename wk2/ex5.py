from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass('Enter password for devices: ')

nxos1 = {
        'host': 'nxos1.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'device_type': 'cisco_nxos',
        }

nxos2 = {
        'host': 'nxos2.lasthop.io',
        'username': 'pyclass',
        'password': password,
        'device_type': 'cisco_nxos',
        }

devices = [nxos1, nxos2]

for device in devices:
    net_conn = ConnectHandler(**device)
    cfg_start = datetime.now()
    cfg_output = net_conn.send_config_from_file('nxos_vlans.txt')
    net_conn.save_config()
    cfg_end = datetime.now()
    cfg_time = cfg_end - cfg_start
    print(cfg_output)
    print('Configuration and save took: {}'.format(cfg_time))
    net_conn.disconnect()


