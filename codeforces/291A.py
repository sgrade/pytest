# A. Spyke Talks

from typing import Counter


n = int(input())
ids = Counter(map(int, input().split()))

ans = 0
for key, value in ids.items():
    if key == 0:
        continue
    if value > 2:
        ans = -1
        break
    elif value == 2:
        ans += 1
        
print(ans)
