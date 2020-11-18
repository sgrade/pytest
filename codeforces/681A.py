# A. A Good Contest

n = int(input())
ans = False
for _ in range(n):
    a, b, c = input().split()
    b = int(b)
    c = int(c)
    if 2400 <= b < c:
        ans = True
        break
print("YES") if ans else print("NO")
