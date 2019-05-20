from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device = {
        'host': 'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type': 'cisco_ios',
        'fast_cli': True
        }


config = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
net_conn = ConnectHandler(**device)

cfg_start_time = datetime.now()
for items in config:
    output = net_conn.send_config_set(items)
    print('Command sent:\n {}'.format(output))
    print('-' * 80)
cfg_end_time = datetime.now()
cfg_time = cfg_end_time - cfg_start_time

output = net_conn.send_command('ping google.com')
print('Verifcation Command:\n {}'.format(output))

print('Configuration took: {}'.format(cfg_time))

'''
running without fast_cli config tasks take about 33 seconds
running *with* fast_cli config tasks take 5 seconds
'''
