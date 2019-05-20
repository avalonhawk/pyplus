import yaml

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

# init a blank list
lab_list = []

# iterate through the device list and generate lab info
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

filename = "lab_info.yml"
with open(filename, "wt") as f:
    yaml.dump(lab_list, f, default_flow_style=False)

