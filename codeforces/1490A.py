#  A. Dense Array

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(1, n):
        while a[i-1] * 2 < a[i]:
            a[i-1] *= 2
            ans += 1
        while (a[i-1] + 1) // 2 > a[i]:
            a[i-1] = (a[i-1] + 1) // 2
            ans += 1

    print(ans)
