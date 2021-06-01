#  B. Maximal Continuous Rest

n = int(input())
a = list(input().split())
a += a

ans = 0

cnt = 0
for i in range(n * 2):
    cnt = cnt + 1 if a[i] == '1' else 0
    ans = max(ans, cnt)

print(ans)
