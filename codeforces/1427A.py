# A. Avoiding Zero

for _ in range(int(input())):

    n = int(input())
    a = list(map(int, input().split()))

    sm = sum(a)

    ans = False if sm == 0 else True

    if sm > 0:
        a.sort(reverse= True)
    else:
        a.sort()
    
    print("YES" if ans else "NO")
    if ans:
        print(*a)
