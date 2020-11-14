# List of Fibonacci numbers

def fib_numbers(n):
    f = [0]
    if n == 0:
        return [0]
    f.append(1)
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f


print(fib_numbers(6))
