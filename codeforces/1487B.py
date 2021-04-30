# B. Cat Cycle

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = 0

    # Editorial - https://codeforces.com/blog/entry/87873
    k -= 1

    if n % 2 == 0:
        ans = k % n + 1
    else:
        b_extra_steps = k // (n // 2)
        ans = (k + b_extra_steps) % n + 1
    
    print(ans)
