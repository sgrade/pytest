# B. Box Fitting

from collections import Counter, OrderedDict

for _ in range(int(input())):

    n, W = map(int, input().split())
    inp = list(map(int, input().split()))
    mp = OrderedDict(Counter(sorted(inp, reverse=True)))

    ans = 0
    while n > 0:
        w_left = W
        for w in mp:
            while w <= w_left and mp[w] > 0:
                w_left -= w
                mp[w] -= 1
                n -= 1
        ans += 1

    print(ans)
