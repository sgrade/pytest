# A. Reconnaissance

from collections import defaultdict

n, d = map(int, input().split())
inp = list(map(int, input().split()))

mp = defaultdict(int)
for h in inp:
    mp[h] += 1

ans = 0

if n == 1:
    ans = 1
else:
    for idx1 in mp.keys():
        ans += mp[idx1] * (mp[idx1] - 1)

        idx2 = 0
        for idx2 in mp.keys():
            if idx1 == idx2:
                idx2 += 1
                continue
            if abs(idx1 - idx2) <= d:
                ans += mp[idx1] * mp[idx2]
            idx2 += 1

        idx1 += 1

print(ans)
