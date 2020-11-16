# A. Uniform String

import string

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = list()
    while n > 0:
        for i in range(min(k, n)):
            ans.append(string.ascii_lowercase[i])
            n -= 1

    print(''.join(ans))
