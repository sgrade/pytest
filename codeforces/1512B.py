# B. Almost Rectangle

for _ in range(int(input())):
    n = int(input())
    coord = list()

    for i in range(n):
        s = input()
        try:
            idx1 = s.index('*')
            coord.append([i, idx1])
            try:
                idx2 = s.index('*', idx1 + 1)
                coord.append([i, idx2])
            except ValueError:
                continue
        except ValueError:
            continue

    mn_row = min(coord[0][0], coord[1][0])
    y = abs(coord[0][0] - coord[1][0])
    if y == 0:
        y = 1
        if mn_row == n - 1:
            mn_row = n - 2

    mn_col = min(coord[0][1], coord[1][1])
    x = abs(coord[0][1] - coord[1][1])
    if x == 0:
        x = 1
        if mn_col == n - 1:
            mn_col = n - 2

    output = []
    for i in range(n):
        output.append(['.'] * n)

    output[mn_row][mn_col] = '*'
    output[mn_row + y][mn_col] = '*'
    output[mn_row][mn_col + x] = '*'
    output[mn_row + y][mn_col + x] = '*'

    print('\n'.join(''.join(output[r]) for r in range(n)))
