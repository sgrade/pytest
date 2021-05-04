# B. Card Deck
# NOT FINISHED

from collections import OrderedDict

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    mp = OrderedDict()
    for x in sorted(p, reverse=True):
        mp[x] = False

    ans = list()

    it = iter(mp)
    i, j = n, n
    while True:
        try:
            p = next(it)
            while True:
                i -= 1
                mp[p[i]] = True
                if p[i] == p:
                    break
            
            ans.append(p[i:j])
            j = i

            

        except StopIteration:
            break
