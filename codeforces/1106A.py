# A. Lunar New Year and Cross Counting

n = int(input())
m = list()
for _ in range(n):
    m.append(input())

ans = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if m[i][j] == '.':
            continue
        elif m[i][j] == m[i-1][j-1] and m[i][j] == m[i-1][j+1] and \
                m[i][j] == m[i+1][j-1] and m[i][j] == m[i+1][j+1]:
            ans += 1

print(ans)
