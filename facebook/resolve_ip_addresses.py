import socket


class DnsHelper:

    @staticmethod
    def resolve_hostname_into_ip(file):
        """Reads a list of hostnames and resolves each IP address and print them"""

        with open(file, 'r') as f:
            for line in f:
                print(socket.gethostbyname(line.strip()))

    @staticmethod
    def resolve_ip_into_hostname(file):
        """Resolves IP address into hostname"""

        with open(file) as f:
            for line in f:
                print(socket.gethostbyaddr(line.strip()), sep=' ')


x = DnsHelper()
x.resolve_hostname_into_ip('hostnames.txt')
x.resolve_ip_into_hostname('ip_addresses.txt')
