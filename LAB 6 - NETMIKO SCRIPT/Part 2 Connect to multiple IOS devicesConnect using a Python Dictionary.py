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
# Connect using a Python dictionary
def connect_with_dictionary(device):
    connection = ConnectHandler(**device)
    print(f"Connected to {device['ip']}")
    # Perform desired operations on the device
    connection.disconnect()



