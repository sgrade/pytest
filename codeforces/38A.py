# A. Army

n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1
b -= 1
ans = 0
for i in range(a, b):
    ans += d[i]
print(ans)
