# A. Mean Inequality

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    b = [0] * (2 * n)
    j = 0
    for i in range(0, 2 * n - 1, 2):
        b[i] = a[j]
        j += 1
    for i in range(1, 2 * n, 2):
        b[i] = a[j]
        j += 1
    
    print(*b)
