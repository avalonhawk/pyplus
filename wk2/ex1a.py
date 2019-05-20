from netmiko import ConnectHandler
from getpass import getpass

device1 = {
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
        }

net_conn = ConnectHandler(**device1)
print(net_conn.find_prompt())

command = "ping"

output = net_conn.send_command_timing(command, strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing("8.8.8.8\n", strip_prompt=False, strip_command=False)
for i in range(1,4):
    output += net_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)

print(output)
net_conn.disconnect()
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
        }

net_conn = ConnectHandler(**device1)
print(net_conn.find_prompt())

command = "ping"

output = net_conn.send_command_timing(command, strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_conn.send_command_timing("8.8.8.8\n", strip_prompt=False, strip_command=False)
for i in range(1,5):
    output += net_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)

print(output)
net_conn.disconnect()
