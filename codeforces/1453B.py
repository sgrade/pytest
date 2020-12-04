# B. Suffix Operations

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # Editorial - https://codeforces.com/blog/entry/85288

    ans = 0
    for i in range(1, n):
        ans += abs(a[i] - a[i-1])

    # Corner cases
    mx = max(abs(a[0]-a[1]), abs(a[n-1]-a[n-2]))

    # The rest
    for i in range(1, n-1):
        mx = max(mx, abs(a[i] - a[i-1]) + abs(a[i] - a[i+1]) - abs(a[i-1] - a[i+1]))

    ans -= mx
    print(ans)
