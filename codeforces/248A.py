# A. Cupboards

n = int(input())
l_open = 0
r_open = 0
for _ in range(n):
    li, ri = map(int, input().split())
    if li == 1:
        l_open += 1
    if ri == 1:
        r_open += 1
print(min(l_open, n - l_open) + min(r_open, n - r_open))
