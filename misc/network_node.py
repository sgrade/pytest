import subprocess
#import ipaddress
#import netifaces


class NetworkNode:

    @staticmethod
    def get_reachable_networks():
        ipr = subprocess.run(['ip', 'route'], stdout=subprocess.PIPE)
        # the following output is a string
        lst = ipr.stdout.decode()
        # I'll split it into list of strings
        lst = lst.split('\n')
        # Then create lists from lst strings (lst become list of lists)
        lst = [s.split(' ') for s in lst]
        for route in lst:
            print(route)


x = NetworkNode()
print(x.get_reachable_networks())
