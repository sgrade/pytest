# A. Dungeon

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    ans = False

    x = (a + b + c) // 9
    if min(a, b, c) >= x:
        y = (a + b + c) % 9
        if y == 0:
            ans = True

    print("YES" if ans else "NO")
