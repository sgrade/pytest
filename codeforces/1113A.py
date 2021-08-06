# A. Sasha and His Trip

n, v = map(int, input().split())

ans = 0

if v >= n - 1:
    ans = n - 1

else:
    for i in range(1, n-v+1):
        ans += i
    ans += v - 1

print(ans)
