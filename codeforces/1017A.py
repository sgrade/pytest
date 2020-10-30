# A. The Rank

# https://codeforces.com/blog/entry/61081

ans = 1

n = int(input())

s = map(int, input().split())
s = sum(s)

for _ in range(n-1):
    tmp = map(int, input().split())
    tmp = sum(tmp)
    if tmp > s:
        ans += 1

print(ans)
