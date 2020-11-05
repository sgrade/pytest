# A. Yet Another Tetris Problem

for _ in range(int(input())):
    n = int(input())
    ans = "YES"

    lst = list(map(int, input().split()))

    if n > 1:
        parity = lst[0] % 2
        for el in lst:
            if el % 2 != parity:
                ans = "NO"
                break

    print(ans)
