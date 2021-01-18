# A. Zoning Restrictions Again

n, h, m = map(int, input().split())

limits = [h] * n
for _ in range(m):
    l, r, x = map(int, input().split())
    for i in range(l-1, r):
        limits[i] = min(limits[i], x)

profit = 0
for x in limits:
    profit += x * x

print(profit)
