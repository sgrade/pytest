# A. Party

# Editorial - https://codeforces.com/blog/entry/2584
# Solution based on https://codeforces.com/contest/115/submission/57934041

n = int(input())
p = [int(input()) for i in range(n)]

ans = 0
for i in range(n):
    current = 0
    while i >= 0:
        i = p[i] - 1
        current += 1
    ans = max(ans, current)

print(ans)
