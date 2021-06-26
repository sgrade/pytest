# D. Same Differences

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())

    # Editorial - https://codeforces.com/blog/entry/90342
    ans = 0

    b = defaultdict(int)
    for i, el in enumerate(a):
        b_i = el - (i+1)
        ans += b[b_i]
        b[b_i] += 1
    
    print(ans)
