from netmiko import ConnectHandler

def connect_to_device(device):
    try:
        # Establish an SSH connection to the device
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']} successfully.")

        # Send commands or perform other operations
        # ...

        # Close the SSH connection
        connection.disconnect()
        print(f"Disconnected from {device['ip']}.\n")

    except Exception as e:
        print(f"Failed to connect to {device['ip']}. Error: {str(e)}\n")

def main():
    # Connection details as a dictionary
    device = {
        'device_type': 'cisco_ios',
        'ip': '10.125.100.187',
        'username': 'admin',
        'password': 'pxl',
    }

    connect_to_device(device)

if __name__ == '__main__':
    main()
