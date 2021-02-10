from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    output = list()
    max_gcd = 0

    # Idea from - https://codeforces.com/contest/1407/submission/92313307
    while a:
        v = list((gcd(max_gcd, x), x) for x in a)
        m = max(v)
        max_gcd = m[0]
        output.append(str(m[1]))
        a.remove(m[1])

    print(' '.join(output))
