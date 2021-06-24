# B. Friends and Candies

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    ans = -1 

    sm = sum(a)
    if (sm % n == 0):
        ans = 0
        
        # Editorial - https://codeforces.com/blog/entry/91637
        i = n - 1
        while (a[i] > sm // n):
            ans += 1
            i -= 1
        
    print(ans)
