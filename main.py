from cstcPack.getIP import getPublicIP
from cstcPack.IP2Bin import ip_to_binary

ip =  getPublicIP()
print(f"Public IP: {ip}")
binip = ip_to_binary(ip)
print(f"Binary IP: {binip}")
