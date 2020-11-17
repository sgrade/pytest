# A. Coder

n = int(input())

ans = n // 2
if n % 2 == 0:
    ans *= n
else:
    ans *= n - 1
    ans += n
print(ans)

c = True
output = list()
for i in range(n):
    for j in range(n):
        if c:
            output.append('C')
        else:
            output.append('.')
        c = not c
    output.append('\n')
    if n % 2 == 0:
        c = not c
print(''.join(output))
