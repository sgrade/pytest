# A. USB Flash Drives

n = int(input())
m = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)

ans = 0
tmp = 0
for el in a:
    tmp += el
    ans += 1
    if tmp >= m:
        break
print(ans)
