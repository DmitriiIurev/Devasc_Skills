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
def send_show_commands(devices, commands):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"\n==== Device: {device['ip']} ====")
        for command in commands:
            output = connection.send_command(command)
            print(f"Command: {command}\n{output}")
        connection.disconnect()

# Define show commands
show_commands = ['show interfaces', 'show ip route']

# Execute the functions
send_show_commands(devices, show_commands)
