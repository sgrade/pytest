# A. Nastya Is Reading a Book

n = int(input())
a = list()

for _ in range(n):
    x, y = map(int, input().split())
    a.append(y)

k = int(input())

for i, num in enumerate(a):
    if num >= k:
        print(n - i)
        break
