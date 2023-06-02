from netmiko import ConnectHandler
device = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.187',
    'username': 'admin',
    'password': 'pxl',
    'secret': 'cisco',
}
net_connect = ConnectHandler(**device)
net_connect.enable()
output = net_connect.send_command('show running-config')
filename = 'lab-ra08-a-sw03-confg'
with open(filename, 'w') as f:
    f.write(output)
print(f"Device configuration saved to {filename}")
net_connect.disconnect()
- Configure a subset of Interfaces
from netmiko import ConnectHandler
# Define the device information
device = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.187',
    'username': 'admin',
    'password': 'pxl',
    'secret': 'cisco',
}

# Define the interfaces to configure
interfaces = ['FastEthernet0/9', 'FastEthernet0/10', 'FastEthernet0/11']

# Define the configuration commands for the interfaces
interface_config_commands = [
    'description Configured by Netmiko',
    'ip address 10.125.100.187',
    'no shutdown',
]
# Establish an SSH connection to the device
net_connect = ConnectHandler(**device)
net_connect.enable()
# Configure each interface in the subset
for interface in interfaces:
    # Enter interface configuration mode
    config_commands = [f'interface {interface}']
    output = net_connect.send_config_set(config_commands)
    # Apply configuration commands for the interface
    output += net_connect.send_config_set(interface_config_commands)
    print(f"Configuration applied to interface {interface}:\n{output}")
# Disconnect from the device
net_connect.disconnect()
