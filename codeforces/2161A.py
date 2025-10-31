# A. Round Trip
# https://codeforces.com/contest/2161/problem/A

for _ in range(int(input())):
    r, x, d, n = map(int, input().split())
    rounds = input()
    ans = 0
    for i in range(n):
        round = rounds[i]
        if round == "1":
            ans += 1
            r = max(0, r - d)
        elif round == "2":
            if r < x:
                ans += 1
                r = max(0, r - d)
    print(ans)
