from netmiko import ConnectHandler

# Create a list of devices with their connection details
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

# Configuration commands to be sent to the devices
commands = [
    'interface GigabitEthernet0/1',
    'description Connected to Server',
    'no shutdown',
    'exit',
    'interface GigabitEthernet0/2',
    'description Connected to Switch',
    'no shutdown',
    'exit',
    # Add more commands as needed
]

# Iterate over the devices and send configuration commands
for device in devices:
    try:
        # Establish an SSH connection to the device
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']} successfully.")

        # Send configuration commands
        output = connection.send_config_set(commands)
        print(f"Output from {device['ip']}:")
        print(output)

        # Save the configuration (optional)
        connection.send_command('write memory')
        print(f"Configuration saved on {device['ip']}.\n")

        # Close the SSH connection
        connection.disconnect()
        print(f"Disconnected from {device['ip']}.\n")
