# A. Professor GukiZ's Robot

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

x_diff = abs(x1 - x2)
y_diff = abs(y1 - y2)

ans = min(x_diff, y_diff) + abs(x_diff - y_diff)
print(ans)
