import subprocess


def ping_devices(file):
    with open(file) as f:
        for address in f:
            output = subprocess.run(['ping', address, '-c2'], stdout=subprocess.PIPE)
            print(output.stdout.decode())


file = 'ip_addresses.txt'
ping_devices(file)