print("Connecting via SSH => show interface status (brief)")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="10.125.100.187",
    port="22",
    username="admin",
    password="pxl",
    secret="cisco",
    )
output1=sshCli.send_command("show ip interface brief")
output2=sshCli.send_command("show version")
print(output1 + "\n\n" + output2)

