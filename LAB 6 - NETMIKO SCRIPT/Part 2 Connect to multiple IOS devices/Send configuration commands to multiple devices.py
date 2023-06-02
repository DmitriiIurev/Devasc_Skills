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
# Send configuration commands to multiple devices
def send_config_commands(devices, commands):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"\n==== Device: {device['ip']} ====")
        output = connection.send_config_set(commands)
        print(f"Configuration commands applied:\n{output}")
        connection.disconnect()


# Define configuration commands
config_commands = [
    'interface GigabitEthernet0/1',
    'shutdown',
]



# Execute the functions
send_config_commands(devices, config_commands)

