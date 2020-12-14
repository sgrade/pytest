# A. Triangular numbers

n = int(input())

s = 0
i = 1
while s < n:
    s += i
    i += 1

print('YES' if s == n else 'NO')
