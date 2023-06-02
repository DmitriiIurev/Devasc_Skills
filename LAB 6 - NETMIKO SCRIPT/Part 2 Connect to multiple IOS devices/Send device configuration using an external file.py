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
    
]
# Send device configuration using an external file
def send_config_file(devices, file_path):
    with open(file_path, 'r') as file:
        config_commands = file.read().splitlines()
    send_config_commands(devices, config_commands)
    
    

# Execute the functions
send_config_file(devices, 'device_config.txt')

