# A. Chips

n, m = map(int, input().split())
rnd = (1 + n) * n // 2
if m > rnd:
    m %= rnd
for i in range (1, n+1):
    if m < i:
        break
    else:
        m -= i
print(m)
