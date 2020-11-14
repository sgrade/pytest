# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


print(fib(6))
