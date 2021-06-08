# A. Donut Shops

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    price_b = c / b

    ans = [-1, -1]

    if a <= price_b:
        ans[0] = b - 1
    else:
        ans[0] = 1 if c / a > 1 else -1
        ans[1] = b
    
    print(*ans)
