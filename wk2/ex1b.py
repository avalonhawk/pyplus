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

output = net_conn.send_command(command, expect_string="ip]:", strip_prompt=False, strip_command=False)
output += net_conn.send_command("\n", expect_string="ress:", strip_prompt=False, strip_command=False)
output += net_conn.send_command("8.8.8.8\n", expect_string="]:", strip_prompt=False, strip_command=False)
for i in range(1,5):
    output += net_conn.send_command("\n", expect_string="]:", strip_prompt=False, strip_command=False)

output += net_conn.send_command("\n", expect_string="#", strip_prompt=False, strip_command=False)
print(output)
net_conn.disconnect()
