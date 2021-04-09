# B. Balanced Remainders

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())
    mp = [0, 0, 0]
    for x in a:
        mp[x % 3] += 1

    ans = 0

    # Idea - https://codeforces.com/contest/1490/submission/108133578
    ans = max(ans, mp[0] - mp[2])
    ans = max(ans, mp[1] - mp[0])
    ans = max(ans, mp[2] - mp[1])

    print(ans)
