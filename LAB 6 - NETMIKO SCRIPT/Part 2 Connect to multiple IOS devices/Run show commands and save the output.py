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
# Run show commands and save the output
def run_show_commands_save_output(devices, commands):
    for device in devices:
        connection = ConnectHandler(**device)
        print(f"\n==== Device: {device['ip']} ====")
        for command in commands:
            output = connection.send_command(command)
            filename = f"{device['ip']}_output.txt"
            with open(filename, 'a') as file:
                file.write(f"Command: {command}\n{output}\n\n")
            print(f"Command: {command}\nOutput saved to {filename}")
        connection.disconnect()


# Define show commands
show_commands = ['show interfaces', 'show ip route']

# Execute the functions
run_show_commands_save_output(devices, show_commands)

