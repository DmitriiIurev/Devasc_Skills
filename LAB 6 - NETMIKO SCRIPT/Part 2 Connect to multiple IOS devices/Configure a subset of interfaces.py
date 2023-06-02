from netmiko import ConnectHandler

# Define the device information
devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '10.125.100.187',
        'username': 'admin',
        'password': 'pxl',
    },
    {
        'device_type': 'cisco_ios',
        'ip': '10.125.100.181',
        'username': 'admin',
        'password': 'pxl',
    },
    # Add more devices as needed
]
# Configure a subset of interfaces
def configure_subset_interfaces(devices, interface_commands):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"\n==== Device: {device['ip']} ====")
        output = connection.send_config_set(interface_commands)
        print(f"Interface configuration applied:\n{output}")
        connection.disconnect()

# Define interface configuration commands
interface_commands = [
    'interface GigabitEthernet0/1',
    'shutdown',
    'interface GigabitEthernet0/2',
    'shutdown',
]

# Execute the functions
configure_subset_interfaces(devices, interface_commands)
