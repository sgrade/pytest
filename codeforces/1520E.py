#  E. Arranging The Sheep

for _ in range(int(input())):
    n = int(input())
    s = input().strip('.')
    n = len(s)

    ans = 0

    # Key ideas from https://codeforces.com/contest/1520/submission/118467369
    cnt = s.count('*')
    if 0 < cnt < n:
        stars_passed = 0
        for ch in s:
            if ch == '*':
                stars_passed += 1
            else:
                # Editorial - https://codeforces.com/blog/entry/90342
                # min shows if we passed mid star or not
                ans += min(stars_passed, cnt - stars_passed)

    print(ans)
