# A. Prime Minister

from math import ceil

n = int(input())
a = list(map(int, input().split()))

half = sum(a) // 2

k = 0
ans = [1]
sum_ans = a[0]
if sum_ans > half:
    k = 1
else:
    for ind, el in enumerate(a[1:], 2):
        if el > a[0] // 2:
            continue

        ans.append(ind)
        sum_ans += el
        if sum_ans > half:
            k = len(ans)
            break

print(k)
if k > 0:
    print(' '.join([str(x) for x in ans]))
