# A. Memory and Crow
# TLE: Time limit exceeded on test 5

n = int(input())
a = list(map(int, input().split()))

ans = [a[n-1]]
for i in range(n-2, -1, -1):
    ans.append(a[i] + a[i+1])

print(' '.join([str(x) for x in ans[::-1]]))
