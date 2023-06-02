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
# Execute a script with a function or classes
class CiscoDevice:
    def __init__(self, device_type, ip, username, password):
        self.device_type = device_type
        self.ip = ip
        self.username = admin
        self.password = pxl

    def connect(self):
        connection = ConnectHandler(
            device_type=self.device_type,
            ip=self.ip,
            username=self.username,
            password=self.password
        )
        print(f"Connected to {self.ip}")
        # Perform desired operations on the device
        connection.disconnect()
