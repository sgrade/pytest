# A. Spy Detected!

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    aa = Counter(a)
    for k, v in aa.items():
        if v == 1:
            print(a.index(k) + 1)
