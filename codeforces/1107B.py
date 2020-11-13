# B. Digital root

for _ in range(int(input())):
    k, x = map(int, input().split())
    # Editorial - https://codeforces.com/blog/entry/64847
    print((k - 1) * 9 + x)
