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

# Specify the filename for the configuration file
config_file = 'config.txt'

# Read the configuration commands from the file
with open(config_file, 'r') as file:
    commands = file.read().splitlines()

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
