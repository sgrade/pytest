# A. Supermarket

n, m = map(int, input().split())
a, b = map(int, input().split())
ans = a * m / b
for _ in range(n - 1):
    a, b = map(int, input().split())
    if a * m / b < ans:
        ans = a * m / b
print(ans)
