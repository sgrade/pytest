# C. Alternating Subsequence

from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    s = input()

    # Key idea is from https://codeforces.com/contest/1343/submission/93619455
    ans = 0
    for key, group in groupby(s.split(), str.isdigit):
        ans += max(map(int, group))
    print(ans)
