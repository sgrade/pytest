# D. Decrease the Sum of Digits

def n_sum(n):
    sm = 0
    while n > 0:
        sm += n % 10
        n //= 10
    return sm


for _ in range(int(input())):
    n, s = map(int, input().split())

    ans = 0

    # Editorial - https://codeforces.com/blog/entry/82284

    tens = 1
    while n_sum(n) > s:
        rem = n % (tens * 10)

        x = 10 * tens - rem

        n += x
        ans += x
            
        tens *= 10
    
    print(ans)
