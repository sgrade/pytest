# A. Coins

n, S = map(int, input().split())
ans = S//n
if S % n != 0:
    ans += 1
print(ans)

