# C. Unique Number

for _ in range(int(input())):
    x = int(input())

    # Editorial - https://codeforces.com/blog/entry/85594
    lst = list()
    sm = 0
    i = 9

    while sm < x and i > 0:
        lst.append(min(x - sm, i))
        sm += i
        i -= 1

    if sm < x:
        print(-1)
    else:
        print(''.join([str(el) for el in lst[::-1]]))
