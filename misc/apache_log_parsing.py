""" Apache log parsing exercise
https://0xbharath.github.io/python-foundations/log_parsing/index.html
"""


with open("input.txt") as f:

    lines = f.read().splitlines()

    unique_clients = {x.split()[0] for x in lines}
    print("Unique clients:", *unique_clients, sep="\n")
    print()

    lines.sort(key=lambda x: int(x.split()[2]))
    print("Sorted by requests: ")
    print("\n".join(lines))
