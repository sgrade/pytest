# B. Balls of Steel

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list()
    for _ in range(n):
        a.append(tuple(map(int, input().split())))

    ans = -1
    #  Editorial - https://codeforces.com/blog/entry/85348
    for i in range(n):
        mx = 0
        for j in range(n):
            mx = max(mx, abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1]))
        if mx <= k:
            ans = 1
            break

    print(ans)
