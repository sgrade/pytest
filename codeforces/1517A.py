# A. Sum of 2050

for _ in range(int(input())):
    # idea from https://codeforces.com/contest/1517/submission/113986084
    n = int(input())
    if n % 2050:
        print(-1)
    else:
        n //= 2050
        print(sum(map(int, str(n))))
