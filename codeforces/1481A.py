# A. Space Navigation

for _ in range(int(input())):
    px, py = map(int, input().split())
    s = input()

    u = s.count('U')
    d = - s.count('D')
    r = s.count('R')
    l = - s.count('L')

    ans = False
    if px == 0 or (0 < px <= r) or (l <= px < 0):
        if py == 0 or (0 < py <= u) or (d <= py < 0):
            ans = True

    print("YES" if ans else "NO")
