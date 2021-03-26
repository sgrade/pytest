# A. Strange Table

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    column = (x + n - 1) // n
    row = x - (column - 1) * n
    y = (row - 1) * m + column
    print(y)
