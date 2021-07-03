# A. Odd Set

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odd = 0
    for x in a:
        if x % 2 != 0:
            odd += 1

    ans = False

    if odd == n:
        ans = True
    
    print("Yes" if ans else "No")
