def ip_to_binary(ip):
    octets = ip.split('.')
    binary_ip = '.'.join(format(int(octet), '08b') for octet in octets)
    return binary_ip
