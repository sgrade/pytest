# A. Subtractions

for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = 0
    while True:
        if y < x:
            y, x = x, y
        ans += y // x
        remainder = y % x
        if remainder > 0:
            y = x
            x = remainder
        else:
            break

    print(ans)
