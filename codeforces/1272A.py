# A. Three Friends

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    lst.sort()

    a = lst[0]
    b = lst[1]
    c = lst[2]

    ans = c - a
    ans = max(ans - 2, 0)

    if ans > 0:
        ans += (b - (a + 1)) + ((c - 1) - b)
    
    print(ans)
