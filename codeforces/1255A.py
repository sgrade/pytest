# A. Changing Volume

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if a < b:
        a, b = b, a

    ans = (a-b) // 5
    a = (a-b) % 5

    ans += a // 2
    a = a % 2

    ans += a // 1

    print(ans)
