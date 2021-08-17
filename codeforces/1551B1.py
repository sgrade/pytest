# B1. Wonderful Coloring - 1

from collections import Counter

for _ in range(int(input())):
    s = input()
    count = Counter(s)
    ans = 0
    for k, v in count.items():
        if v == 1:
            ans += 0.5
        else:
            ans += 1
    
    print(int(ans))
