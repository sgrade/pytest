# B. Card Deck

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
    current_max = next(it)
    while True:
        try:
            while True:
                i -= 1
                mp[p[i]] = True
                if p[i] == current_max:
                    break
            
            ans += p[i:j]
            j = i

            while mp[current_max] != False:
                current_max = next(it)

        except StopIteration:
            break

    print(*ans)
