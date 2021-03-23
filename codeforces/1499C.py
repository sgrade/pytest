# C. Minimum Grid Path

import math

for _ in range(int(input())):
    n = int(input())

    tmp = 0
    nx, ny = n, n
    min_x = math.inf
    min_y = math.inf
    cost = 0
    ans = math.inf

    c = list(map(int, input().split()))
    for i in range(1, n+1):
        tmp = c[i-1]
        if i & 1:
            min_x = min(min_x, tmp)
            nx -= 1
        else:
            min_y = min(min_y, tmp)
            ny -= 1

        cost += tmp
        if i > 1:
            ans = min(ans, cost + nx * min_x + ny * min_y)

    print(ans)
