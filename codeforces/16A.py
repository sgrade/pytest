# A. Flag

n, m = map(int, input().split())

ans = True

tmp = list()

for i in range(n):
    x = set(input())
    if len(x) > 1:
        ans = False
        break
    else:
        tmp.append(x.pop())

if n > 1 and ans:
    for i in range(1, n):
        if tmp[i] == tmp[i-1]:
            ans = False
            break

print("YES" if ans else "NO")
