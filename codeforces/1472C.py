# C. Long Jumps

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    max_score = 0

    # Editorial - https://codeforces.com/blog/entry/86406
    dp = [0 for i in range(n)]
    for j in range(n-1, -1, -1):
        dp[j] = a[j]
        if j + a[j] < n:
            dp[j] += dp[j + a[j]]
        max_score = max(max_score, dp[j])

    print(max_score)
