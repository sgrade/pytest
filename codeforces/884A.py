# A. Book Reading

n, t = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    t -= 86400 - a[i]
    ans += 1
    if t <= 0:
        break

print(ans)
