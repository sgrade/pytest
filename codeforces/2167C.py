# C. Isamatdin and His Magic Wand!
# https://codeforces.com/contest/2167/problem/C

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even, odd = False, False
    for el in a:
        if el % 2 == 0:
            even = True
        else:
            odd = True
    
    if even and odd:
        a.sort()
    print(*a)
