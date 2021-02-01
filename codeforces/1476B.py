# B. Inflation

for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    # Key ideas from - https://www.youtube.com/watch?v=vgxc1iXrAjo
    # His solution is - https://codeforces.com/contest/1476/submission/105869229
    ans = 0
    sm = p[0]
    for i in range(1, n):
        tmp = (100 * p[i] + k - 1) // k
        ans = max(ans, max(0, tmp - sm))
        sm += p[i]

    print(ans)
