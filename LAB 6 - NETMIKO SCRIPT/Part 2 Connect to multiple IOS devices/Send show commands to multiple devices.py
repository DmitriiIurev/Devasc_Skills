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

# Iterate over the devices and send show commands
for device in devices:
    try:
        # Establish an SSH connection to the device
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']} successfully.")

        # Send show commands
        output = connection.send_command('show version')
        print(f"Output from {device['ip']}:")
        print(output)

        # Close the SSH connection
        connection.disconnect()
        print(f"Disconnected from {device['ip']}.\n")
