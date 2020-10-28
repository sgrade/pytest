# B. A New Technique
# TLE (Time limit exceeded)

from sys import stdin, stdout

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    rows = [0] * n

    a_column = list()

    for r in range(n):
        tmp = list(input().split())
        rows[r] = tmp
        a_column.append(tmp[0])
    sorted_a_column = sorted(a_column)

    found = False
    for c in range(m):
        if not found:
            tmp_c = list(input().split())
            if sorted(tmp_c) == sorted_a_column:
                found = True
                output = str()
                for num in tmp_c:
                    index = a_column.index(num)
                    output += ' '.join(rows[index])
                    output += '\n'
                print(output, end='')
        else:
            stdin.__next__()
