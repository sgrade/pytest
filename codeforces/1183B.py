# B. Equalize Prices

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = set(map(int, input().split()))
    a = sorted(a)

    ans = a[0] + k
    if abs(a[-1] - ans) > k:
        print(-1)
    else:
        print(ans)
