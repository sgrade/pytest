# A. Reconnaissance 2

n = int(input())
a = list(map(int, input().split()))
diff = abs(a[-1] - a[0])
indexes = [n - 1, 0]

if n > 2:
    for i in range(1, n):
        if abs(a[i] - a[i-1]) < diff:
            diff = abs(a[i] - a[i-1])
            indexes[0] = i - 1
            indexes[1] = i

print(indexes[0] + 1, indexes[1] + 1)
