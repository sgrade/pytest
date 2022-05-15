# B. Array Cloning Technique

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sa = sorted(set(a))

    ans = 0

    if len(sa) > 1:

        cnt = {}
        for x in sa:
            cnt[x] = 0
        for x in a:
            cnt[x] += 1

        mx = max(cnt.values())

        others = n - mx
        while True:
            d = min(others, mx)
            others -= d
            ans += 1 + d
            if others == 0:
                break
            mx *= 2

    print(ans)
