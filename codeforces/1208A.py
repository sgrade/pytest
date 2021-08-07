# A. XORinacci

for _ in range(int(input())):
    a, b, n = map(int, input().split())

    # Editorial - https://codeforces.com/blog/entry/69357

    ans = 0

    x = n % 3
    if x == 0:
        ans = a
    elif x == 1:
        ans = b
    else:
        ans = a ^ b
    
    print(ans)
