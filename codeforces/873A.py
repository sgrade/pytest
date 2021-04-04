# A. Chores

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

ans = sum(a[:n-k])
ans += k * x

print(ans)
