# A. Payment Without Change

from math import ceil

for _ in range(int(input())):
    a, b, n, S = map(int, input().split())

    rem = S % n
    
    ans = False
    if rem <= b and n * a + b >= S:
        ans = True
    
    print("YES" if ans else "NO")
