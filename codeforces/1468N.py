# N. Waste Sorting

for _ in range(int(input())):
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))

    ans = True

    c[0] -= a[0]
    c[1] -= a[1]
    c[2] -= a[2]

    tmp = min(max(0, c[0]), a[3])
    a[3] -= tmp
    c[0] -= tmp
    c[2] -= a[3]
    
    tmp = min(max(0, c[1]), a[4])
    a[4] -= tmp
    c[1] -= tmp
    c[2] -= a[4]

    for x in c:
        if x < 0:
            ans = False
    
    print("YES" if ans else "NO")
