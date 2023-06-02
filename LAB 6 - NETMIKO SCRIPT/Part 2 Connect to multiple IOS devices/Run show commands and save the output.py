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

# Show commands to be executed on the devices
commands = [
    'show version',
    'show interfaces',
    # Add more show commands as needed
]

# Iterate over the devices and execute show commands
for device in devices:
    try:
        # Establish an SSH connection to the device
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']} successfully.")

        # Create a filename for the output based on the device IP
        filename = f"{device['ip']}_output.txt"

        # Open the file in write mode
        with open(filename, 'w') as file:
            # Iterate over the show commands
            for command in commands:
                # Execute the command and write the output to the file
                output = connection.send_command(command)
                file.write(f"Command: {command}\n")
                file.write(output)
                file.write('\n')

        print(f"Output from {device['ip']} saved to {filename}.\n")

        # Close the SSH connection
        connection.disconnect()
        print(f"Disconnected from {device['ip']}.\n")
