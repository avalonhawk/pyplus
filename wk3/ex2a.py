from pprint import pprint

# define list of devices as a string
devices = '''
arista1
arista2
arista3
arista4
'''

# domain name for devices
domain = "lasthop.io"

# provide filler for username and password
username = "nouser"
password = "notpassword"

# convert devices string into a list
devices = devices.strip()
device_list = devices.splitlines()

# Init a blank list
lab_list = []

for device in device_list:
    device_name = device
    host = device+"."+domain
    device_dict = {
        "device_name": device_name,
        "host": host,
        "username": username,
        "password": password,
        }
    lab_list.append(device_dict)

print()
pprint(lab_list)
print()
