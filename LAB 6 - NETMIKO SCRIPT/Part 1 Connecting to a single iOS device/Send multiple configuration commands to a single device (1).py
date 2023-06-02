pfrom netmiko import ConnectHandler

cisco_Switch = {
    "device_type": "cisco_ios",
    "host": "10.125.100.187,
    "username": "admin",
    "password": "pxl",
    "secret": "cisco"}

with ConnectHandler(**cisco_Switch) as net_connect:
    
    net_connect.enable()
    output - net_connect.send_config_from_file('iosv_l3_config.txt')

    print (output)
    net_connect.disconnect()

from netmiko import ConnectHandler
# Define the device information
device = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.187',
    'username': 'admin',
    'password': 'pxl',
    'secret': 'cisco',
}

# Define the configuration commands
config_commands = [
    'interface FastEthernet0/10',
    'description Netmiko Example',
    'ip address 192.168.1.1 255.255.255.0',
    'no shutdown',
    'exit',
    'interface FastEthernet0/11',
    'ip address 10.0.0.1 255.255.255.0',
    'exit',
]

# Establish an SSH connection to the device
net_connect = ConnectHandler(**device)
net_connect.enable()

# Send configuration commands
output = net_connect.send_config_set(config_commands)

# Print the output
print(output)

# Disconnect from the device
net_connect.disconnect()

