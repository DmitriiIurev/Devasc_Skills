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
def execute_with_statements(device):
    connection = ConnectHandler(**device)
    print(f"Connected to {device['ip']}")
    if device['ip'] == '10.125.100.187':
        output = connection.send_command('show interfaces')
        print(f"Output from {device['ip']}:\n{output}\n")
    elif device['ip'] == '10.125.100.181':
        output = connection.send_command('show ip route')
        print(f"Output from {device['ip']}:\n{output}\n")
    else:
        print(f"No specific operation defined for {device['ip']}")
    connection.disconnect()


for device in devices:
    connect_with_dictionary(device)

device1 = CiscoDevice('cisco_ios', '10.125.100.181', 'admin', 'pxl')
device1.connect()

execute_with_statements(devices[0])
execute_with_statements(devices[1])
