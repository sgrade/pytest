# A. Bad Ugly Numbers

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        # Editorial - https://codeforces.com/problemset/problem/1326/A
        print(2, end='')
        print(str(3)*(n-1))
