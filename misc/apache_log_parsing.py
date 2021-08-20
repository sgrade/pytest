#!/usr/bin/env python3

""" Apache log parsing exercise
https://0xbharath.github.io/python-foundations/log_parsing/index.html
"""

import sys

def main():
    try:
        with open(sys.argv[2]) as f:

            lines = f.read().splitlines()

            if sys.argv[1] == '-u':
                unique_clients = {x.split()[0] for x in lines}
                print("Unique clients:", *unique_clients, sep="\n")

            if sys.argv[1] == '-t':
                lines.sort(key=lambda x: int(x.split()[2]))
                print("Sorted by requests: ")
                print("\n".join(lines))
    except:
        raise


if __name__ == '__main__':
    main()
