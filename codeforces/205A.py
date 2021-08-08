# A. Little Elephant and Rozdil

from collections import Counter


n = int(input())
a = list(map(int, input().split()))
mn = min(a)

if a.count(mn) == 1:
    print(a.index(mn) + 1)
else:
    print("Still Rozdil")
