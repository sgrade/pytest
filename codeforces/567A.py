# A. Lineland Mail

n = int(input())
x = list(map(int, input().split()))

ans = list()

ans.append(str(x[1]-x[0]) + ' ' + str(x[-1] - x[0]))

for i in range(1, n-1):
    mn = min(x[i] - x[i-1], x[i+1] - x[i])
    mx = max(x[i] - x[0], x[-1] - x[i])
    ans.append(str(mn) + ' ' + str(mx))

ans.append(str(x[-1] - x[-2]) + ' ' + str(x[-1] - x[0]))

print('\n'.join(ans))
