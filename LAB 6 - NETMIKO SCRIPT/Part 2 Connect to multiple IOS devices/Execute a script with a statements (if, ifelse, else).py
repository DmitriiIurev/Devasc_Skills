from netmiko import ConnectHandler

def main():
    device = {
        'device_type': 'cisco_ios',
        'ip': '10.125.100.187',
        'username': 'admin',
        'password': 'pxl',
    }

    try:
        connection = ConnectHandler(**device)
        print(f"Connected to {device['ip']} successfully.")

        # Send show command to retrieve interface status
        output = connection.send_command('show interface GigabitEthernet0/1')
        if 'GigabitEthernet0/1 is up' in output:
            print("Interface GigabitEthernet0/1 is up and operational.")
        else:
            print("Interface GigabitEthernet0/1 is down or not operational.")

        # Send show command to retrieve interface speed
        output = connection.send_command('show interface GigabitEthernet0/1 | include BW')
        speed = int(output.split()[2])
        if speed > 1000:
            print("Interface speed is greater than 1000 Mbps.")
        else:
            print("Interface speed is less than or equal to 1000 Mbps.")

        connection.disconnect()
        print(f"Disconnected from {device['ip']}.\n")

    except Exception as e:
        print(f"Failed to connect to {device['ip']}. Error: {str(e)}\n")

if __name__ == '__main__':
    main()
