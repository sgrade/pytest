# A. Juicer

from collections import Counter

n, b, d = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

sm = 0
for orange in a:
    if orange <= b:
        sm += orange
        if sm > d:
            ans += 1
            sm = 0

print(ans)
