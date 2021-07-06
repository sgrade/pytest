# B. Neighbor Grid

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list()
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    ans = True
    output = list()
    
    for i in range(n):
        current_row = list()

        for j in range(m):
            # Below formula is based on https://codeforces.com/contest/1375/submission/86113396
            num_of_neighbors = (i > 0) + (i < n-1) + (j > 0) + (j < m-1)

            # Editorial - https://codeforces.com/blog/entry/79731
            if a[i][j] > num_of_neighbors:
                ans = False
                break

            current_row.append(num_of_neighbors)
        
        if ans:
            output.append(current_row)
        else:
            break
    
    print("YES" if ans else "NO")
    
    if ans:
        for lst in output:
            print(*lst)
