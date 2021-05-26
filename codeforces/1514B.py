# B. AND 0, Sum Big

mod = 1000000000 + 7

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = 1

    # Editorial - https://codeforces.com/blog/entry/89810

    for _ in range(k):
        ans = (ans * n) % mod
    
    print(ans)
