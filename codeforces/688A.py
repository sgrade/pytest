# A. Opponents

n, d = map(int, input().split())
days = [1] * d
for i in range(d):
    s = input()
    if '0' in s:
        days[i] = 0

ans = 0
cur = 0
for day in days:
    if day == 1:
        cur = 0
    else:
        cur += 1
        if cur > ans:
            ans = cur

print(ans)
