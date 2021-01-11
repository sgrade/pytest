# A. Slime Combining

n = int(input())

ans = list()
for _ in range(n):
    ans.append(1)
    try:
        while ans[-1] == ans [-2]:
            ans[-2] += 1
            ans.pop()
    except IndexError:
        pass

print(' '.join([str(x) for x in ans]))
