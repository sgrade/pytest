# A. Lunch Rush

from sys import maxsize

n, k = map(int, input().split())

max_joy = -maxsize
for _ in range(n):
    f, t = map(int, input().split())
    current_joy = f if t <= k else f - (t - k)
    max_joy = max(max_joy, current_joy)

print(max_joy)
