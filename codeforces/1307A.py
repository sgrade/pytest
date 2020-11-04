# A. Cow and Haybales

for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(1, len(a)):
        x = min(d//i, a[i])
        d -= x * i
        a[0] += x
    print(a[0])
