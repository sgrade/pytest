# B. Saving the City

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    # The ideas are from https://codeforces.com/problemset/submission/1443/97516052
    s = input().strip('0')
    ans = len(s) and a + sum(min(a, b * len(x)) for x in s.split('1'))
    print(ans)
