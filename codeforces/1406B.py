# B. Maximum Product

from math import prod, inf


for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))

    # Negative infinity
    ans = -inf

    # Key ideas from https://codeforces.com/contest/1406/submission/93622500
    for i in range(5):
        p = prod(a[:i] + a[i-5:])
        ans = max(ans, p)

    print(ans)
