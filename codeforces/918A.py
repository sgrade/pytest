# A. Eleven

def fib_numbers(n):
    if n == 0:
        return 0
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f


n = int(input())
f_nums = fib_numbers(n+1)
output = ['O' if i in f_nums else 'o' for i in range(1, n+1)]
print(''.join(output))
