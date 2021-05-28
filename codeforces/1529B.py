# B. Sifid and Strange Subsequences

import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mn = math.inf
    non_positives = list()
    ans = 0

    for i in range(n):
        if a[i] <= 0:
            ans += 1
            non_positives.append(a[i])
        else:
            mn = min(mn, a[i])
    
    if mn < math.inf:
        ans += 1
        non_positives.sort()
        for i in range(1, len(non_positives)):
            if abs(non_positives[i-1] - non_positives[i]) < mn:
                ans -= 1
                break
    
    print(ans)
