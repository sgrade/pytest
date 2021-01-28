# A. Nezzar and Colorful Balls

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = Counter(map(int, input().split()))
    print(max(a.values()))
