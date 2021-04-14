# A. Arena

for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    print(n - a.count(a[0]))
