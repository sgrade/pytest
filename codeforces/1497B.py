#  B. M-arrays

from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    ans = 0
    if n == 1:
        ans = 1
    else:
        #  Editorial - https://codeforces.com/blog/entry/88677
        cnt = defaultdict(int)
        for el in a:
            cnt[el % m] += 1

        if 0 in cnt.keys():
            ans += 1
            del cnt[0]
        if m % 2 == 0 and m // 2 in cnt.keys():
            ans += 1
            del cnt[m//2]

        for x in cnt.keys():
            y = m - x

            if y not in cnt.keys():
                ans += cnt[x]
                continue

            if 2 * x < m:
                ans += 1
                mn = min(cnt[x], cnt[y])
                mx = max(cnt[x], cnt[y])
                ans += max(0, mx - mn - 1)

    print(ans)
