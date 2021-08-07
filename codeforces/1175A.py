# A. From Hero to Zero

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = 0
    while n > 0:
        if n % k == 0:
            n //= k
            ans += 1
        else:
            reminder = n % k
            n -= reminder
            ans += reminder

    print(ans)
