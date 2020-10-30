# A. Card Game

for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())

    max1 = 0
    tmp = map(int, input().split())
    for _ in tmp:
        if _ > max1:
            max1 = _

    max2 = 0
    tmp = map(int, input().split())
    for _ in tmp:
        if _ > max2:
            max2 = _

    print('NO') if max2 > max1 else print('YES')
