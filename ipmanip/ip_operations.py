import socket
import struct
import ipaddress

class IPManipulator:

    @staticmethod
    def ip_to_binary(ip):
        return '.'.join(format(int(x), '08b') for x in ip.split('.'))

    @staticmethod
    def binary_to_ip(binary):
        return '.'.join(str(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

    @staticmethod
    def ip_to_int(ip):
        return struct.unpack("!I", socket.inet_aton(ip))[0]

    @staticmethod
    def int_to_ip(int_ip):
        return socket.inet_ntoa(struct.pack("!I", int_ip))

    @staticmethod
    def cidr_to_netmask(cidr):
        return str(ipaddress.IPv4Network(f'0.0.0.0/{cidr}', strict=False).netmask)

    @staticmethod
    def netmask_to_cidr(netmask):
        return sum(bin(int(x)).count('1') for x in netmask.split('.'))

    @staticmethod
    def get_network_address(ip, netmask):
        ip_int = IPManipulator.ip_to_int(ip)
        netmask_int = IPManipulator.ip_to_int(netmask)
        network_int = ip_int & netmask_int
        return IPManipulator.int_to_ip(network_int)

    @staticmethod
    def get_broadcast_address(ip, netmask):
        ip_int = IPManipulator.ip_to_int(ip)
        netmask_int = IPManipulator.ip_to_int(netmask)
        broadcast_int = ip_int | ~netmask_int & 0xFFFFFFFF
        return IPManipulator.int_to_ip(broadcast_int)

