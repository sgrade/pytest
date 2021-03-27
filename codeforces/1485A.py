# A. Add and Divide

import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = math.inf

    b_is_one = False
    if b == 1:
        b += 1
        b_is_one = True

    # Explanation - https://www.youtube.com/watch?v=BzIc0ZwLvps
    for i in range(31):
        tmp = a
        current_ans = 1 if b_is_one else 0
        while tmp != 0:
            tmp //= b + i
            current_ans += 1

        ans = min(ans, current_ans + i)

    print(ans)
