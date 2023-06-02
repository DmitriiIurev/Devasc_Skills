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
# Backup device configurations
def backup_configurations(devices):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"\n==== Device: {device['ip']} ====")
        output = connection.send_command('show running-config')
        filename = f"{device['ip']}_config.txt"
        with open(filename, 'w') as file:
            file.write(output)
        print(f"Configuration saved to {filename}")
        connection.disconnect()


# Execute the functions
backup_configurations(devices)
