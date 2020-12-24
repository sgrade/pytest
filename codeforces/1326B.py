# B. Maximums

n = int(input())
b = list(map(int, input().split()))

a = [b[0]]
cur_max = b[0]
for i in range(1, n):
    a.append(b[i] + cur_max)
    if a[i] > cur_max:
        cur_max = a[i]

print(' '.join([str(x) for x in a]))
