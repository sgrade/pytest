# A. Finding Sasuke

t = int(input())

while t > 0:

    n = int(input())

    ans = [1 for i in range(n)]

    a = list(map(int, input().split()))
    sm = sum(a)

    if sm != 0:

        a.reverse()
        ans = [-1 * i for i in a[:int(n/2)]]
        ans += [i for i in a[int(n/2):]]

    for i in ans:
        print(i, end=' ')
    print()

    t -= 1


