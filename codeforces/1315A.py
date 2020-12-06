# A. Dead Pixel

for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    x = max(a-(x+1), x)
    y = max(b-(y+1), y)

    ans = max(x * b, y * a)
    print(ans)
