# B. Unique Bid Auction

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())

    ans = - 1

    v = list(map(int, input().split()))
    v_dict = dict()
    for i in range(n):
        try:
            v_dict[v[i]].append(i)
        except KeyError:
            v_dict[v[i]] = [i]
    for key, lst in sorted(v_dict.items()):
        if len(lst) == 1:
            ans = lst[0] + 1
            break

    print(ans)
