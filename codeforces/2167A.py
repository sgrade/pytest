# A. Square?
# https://codeforces.com/contest/2167/problem/A


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == b and b == c and c == d:
        print("YES")
    else:
        print("NO")
