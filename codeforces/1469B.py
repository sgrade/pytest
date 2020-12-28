# B. Red and Blue

for _ in range(int(input())):

    n = int(input())
    r = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))

    r_max = 0
    r_sum = 0
    for i in range(n):
        r_sum += r[i]
        r_max = max(r_max, r_sum)

    b_max = 0
    b_sum = 0
    for i in range(m):
        b_sum += b[i]
        b_max = max(b_max, b_sum)

    print(r_max + b_max)
