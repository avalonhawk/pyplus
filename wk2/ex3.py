from netmiko import ConnectHandler
from getpass import getpass

device = {
        'host': 'cisco4.lasthop.io',
        'username': 'pyclass',
        'password': getpass(),
        'device_type': 'cisco_ios',
        }

net_conn = ConnectHandler(**device)
print(net_conn.find_prompt())
print( '-' * 30)

# sh_ver = net_conn.send_command('show version', use_textfsm=True)
# sh_lldp = net_conn.send_command('show lldp nei', use_textfsm=True)
cmds = ['show version', 'show lldp neighbors']

for cmd in cmds:
    output = net_conn.send_command(cmd, use_textfsm=True)
    print( '-' * 30)
    print(cmd)
    print( '-' * 30)
    print(output)
    print( '-' * 30)

    if cmd == 'show lldp neighbors':
        print("LLDP Data Type: {}".format(type(output)))
        print("HPE Switch Port: {}".format(output[0]["neighbor_interface"]))

net_conn.disconnect()

'''
print(sh_ver)
print( '-' * 30)
print(sh_lldp)
print( '-' * 30)
net_conn.disconnect()
'''

