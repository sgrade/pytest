# C. Make It Good

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ind = n - 1
    for i in range(n-2, -1, -1):
        if a[i] >= a[ind]:
            ind = i
        else:
            break

    for i in range(ind-1, -1, -1):
        if a[i] <= a[ind]:
            ind = i
        else:
            break

    print(ind)
