# A2. Good Matrix Elements

n = int(input())

a = list()
for _ in range(n):
    a.append(list(map(int, input().split())))

ans = 0

for i in range(n):
    for j in range(n):
        if i == j:
            ans += a[i][j]

for i in range(n):
    for j in range(n):
        if n - i - 1 == j:
            ans += a[i][j]

i = n // 2
for j in range(n):
    ans += a[i][j]

j = n // 2
for i in range(n):
    ans += a[i][j]

ans -= 3 * a[n//2][n//2]

print(ans)
