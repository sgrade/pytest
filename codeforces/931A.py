# A. Friends Meeting

x1 = int(input())
x2 = int(input())

diff = abs(x1 - x2)
n = diff // 2

ans = n * (n + 1)
if diff % 2 != 0:
    ans += n + 1

print(ans)
