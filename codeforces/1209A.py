# A. Paint the Numbers

from copy import deepcopy

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 1
while True:
    tmp = list()
    for el in a[1:]:
        if el % a[0] != 0:
            tmp.append(el)
    if len(tmp) < 1:
        break
    elif len(tmp) == 1:
        ans += 1
        break
    else:
        ans += 1
        a = deepcopy(tmp)

print(ans)
