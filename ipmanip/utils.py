class IPUtils:

    @staticmethod
    def get_ip_class(ip):
        first_octet = int(ip.split('.')[0])
        if 1 <= first_octet <= 126:
            return 'Class A'
        elif 128 <= first_octet <= 191:
            return 'Class B'
        elif 192 <= first_octet <= 223:
            return 'Class C'
        elif 224 <= first_octet <= 239:
            return 'Class D'
        else:
            return 'Class E'

    @staticmethod
    def validate_ip(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False

    @staticmethod
    def validate_netmask(netmask):
        try:
            ipaddress.IPv4Network(f'0.0.0.0/{netmask}', strict=False)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_cidr(cidr):
        try:
            ipaddress.IPv4Network(f'0.0.0.0/{cidr}', strict=False)
            return True
        except ValueError:
            return False

