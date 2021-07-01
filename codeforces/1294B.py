# B. Collecting Packages

for _ in range(int(input())):
    n = int(input())
    coords = list()
    for _ in range(n):
        coords.append(list(map(int, input().split())))
    coords.sort()

    ans = False
    output = list()
    
    cur_x, cur_y = 0, 0
    for i in range(n):
        x, y = coords[i]
        x_diff = x - cur_x
        y_diff = y - cur_y
        if x_diff < 0 or y_diff < 0:
            break
        else:
            output += 'R' * x_diff
            output += 'U' * y_diff
        cur_x, cur_y = x, y
    else:
        ans = True
    
    if ans:
        print("YES")
        print(''.join(output))
    else:
        print("NO")
