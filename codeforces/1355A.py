# A. Sequence with Digits

from math import inf

for _ in range(int(input())):
    a, k = map(int, input().split())

    # Editorial - https://codeforces.com/blog/entry/77491

    for i in range(k):
        mn = inf
        mx = 0
        tmp = a
        while (tmp > 0):
            rem = tmp % 10
            mn = min(mn, rem)
            mx = max(mx, rem)
            tmp //= 10
        tmp = mn * mx
        if tmp == 0:
            break
        a += tmp

    print(a)
