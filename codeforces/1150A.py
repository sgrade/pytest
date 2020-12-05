# A. Stock Arbitraging

n, m, r = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(int, input().split()))

s.sort()
b.sort()

ans = r // s[0] * b[-1] + r % s[0]
if ans < r:
    ans = r
print(ans)
