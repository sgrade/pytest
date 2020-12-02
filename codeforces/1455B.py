# Based on https://codeforces.com/contest/1455/submission/100058627

n = int(input())
for _ in range(n):
    x = int(input())
    k = 0
    while x > 0:
        k += 1
        x -= k
    # Why "x == -1" is explained here
    # https://codeforces.com/blog/entry/85186?#comment-728523
    print(k + (x == -1))
