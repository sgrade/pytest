# A. Split it!

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    ans = False
    if k == 0:
        ans = True
    else:
        # Editorial - https://codeforces.com/blog/entry/88533
        if 2 * k != n:
            if s[:k] == s[n-1:n-1-k:-1]:
                ans = True

    print("YES" if ans else "NO")
