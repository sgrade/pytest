import socket


def resolve_hostname_to_ip(file):
    with open(file, 'r') as f:
        for line in f:
            print(line.strip())
            print(socket.gethostbyname(line.strip()))
            print('\n')


filename = 'hostnames.txt'
resolve_hostname_to_ip(filename)
