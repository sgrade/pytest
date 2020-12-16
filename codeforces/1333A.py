# A. Little Artem

for _ in range(int(input())):
    n, m = map(int, input().split())

    ans = [['W']]
    for i in range(m-1):
        ans[0].append('B')
    for j in range(n-1):
        ans.append(['B'] * m)

    for i in range(n):
        print(''.join(ans[i]))
