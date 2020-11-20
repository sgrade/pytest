# B. Toy Blocks

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # Editorial - https://codeforces.com/blog/entry/84847
    su = sum(a)
    max_el = max(a)
    k = max(max_el, (su + (n-1) - 1) // (n-1))
    ans = k * (n-1) - su

    print(ans)
