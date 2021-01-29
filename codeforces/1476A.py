# A. K-divisible Sum

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = 2

    if k % n == 0:
        ans = k // n
    else:
        if k > n:
            ans = (k + n - 1) // n
        else:
            tmp = (n + k - 1) // k
            tmp *= k
            ans = (tmp + n - 1) // n

    print(ans)
