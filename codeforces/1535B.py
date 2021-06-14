# B. Array Reodering

from math import gcd


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # Editorial - https://codeforces.com/blog/entry/91481
    a.sort(key = lambda x: x % 2)

    ans = 0

    for i in range(n):
        for j in range(i+1, n):
            if gcd(a[i], a[j] * 2) > 1:
                ans += 1
    
    print(ans)
