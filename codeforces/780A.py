# A. Andryusha and Socks

n = int(input())
max_socks = 0
table = set()
for sock in input().split():
    if sock in table:
        table.remove(sock)
    else:
        table.add(sock)
        max_socks = max(max_socks, len(table))

print(max_socks)
