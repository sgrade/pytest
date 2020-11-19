# A. Shaass and Oskols

n = int(input())
a = list(map(int, input().split()))
for _ in range(int(input())):
    x, y = map(int, input().split())
    x -= 1
    if x - 1 >= 0:
        a[x-1] += max(0, y - 1)
    if x + 1 < n:
        a[x+1] += a[x] - y
    a[x] = 0
print('\n'.join([str(i) for i in a]))

