# A. Kids Seating

from math import gcd

for _ in range(int(input())):
    n = int(input())
    ans = list()
    for i in range(4 * n, 0, -1):
        for j in ans:
            if i % j == 0 or j % i == 0 or gcd(i, j) == 1:
                break
        else:
            ans.append(i)
    print(*ans)
