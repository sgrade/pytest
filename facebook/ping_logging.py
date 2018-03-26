import subprocess
import logging

logging.basicConfig(filename='ping.log', level=logging.DEBUG)

with open('ip_addresses.txt') as f:
    for address in f:
        x = subprocess.run(['ping', address, '-c2'], stdout=subprocess.PIPE)
        # print(x.stdout.decode().split(', '))
        if '100% packet loss' in x.stdout.decode().split(', '):
            logging.warning('{0} OFFLINE'.format(address.strip()))
        else:
            logging.info('{0} OK'.format(address.strip()))

