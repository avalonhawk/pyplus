from netmiko import ConnectHandler
from getpass import getpass

ios1 = {
        'device_type': 'cisco_ios',
        'host': 'cisco3.lasthop.io',
        'username': 'pyclass',
        'password': getpass("Enter router password"),
        'session_log': 'cisco3_log.txt'
        }
net_conn = ConnectHandler(**ios1)
f = open ('ios_version.txt', mode='w')
f.write(net_conn.send_command('show version'))
f.flush()
