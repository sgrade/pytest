# C. Boats Competition

from collections import Counter
from collections import defaultdict

for _ in range(int(input())):

    n = int(input())

    # Some ideas from https://codeforces.com/contest/1399/submission/102997535
    a = Counter(map(int, input().split()))

    ans = 0

    d = defaultdict(int)
    if n > 1:
        for i in a:
            for j in a:
                d[i + j] += min(a[i], a[j])
        ans = max(d.values()) // 2

    print(ans)
