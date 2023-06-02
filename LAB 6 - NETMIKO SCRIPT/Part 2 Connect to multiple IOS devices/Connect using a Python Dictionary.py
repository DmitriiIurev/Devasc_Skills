from netmiko import ConnectHandler

# Connection details as a dictionary
device = {
    'device_type': 'cisco_ios',
    'ip': '10.125.100.187',
    'username': 'admin',
    'password': 'pxl',
}

try:
    # Establish an SSH connection to the device
    connection = ConnectHandler(**device)
    print(f"Connected to {device['ip']} successfully.")

    # Send commands or perform other operations
    # ...

    # Close the SSH connection
    connection.disconnect()
    print(f"Disconnected from {device['ip']}.\n")
