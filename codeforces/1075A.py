# A. The King's Race

n = int(input())
x, y = map(int, input().split())

w = max(x, y) - 1
b = n - min(x, y)

print("Black" if b < w else "White")
