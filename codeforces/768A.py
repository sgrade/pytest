# A. Oath of the Night's Watch

from collections import Counter


n = int(input())
a = Counter(map(int, input().split()))
a_sorted = sorted(a.items())

ans = max(0, n - (a_sorted[0][1] + a_sorted[-1][1]))
print(ans)
