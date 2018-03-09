# http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

number = int(input('How many fibonacci numbers would you like to generate? '))
if number == 0:
    fib = []
else:
    fib = [0, 1]
    for i in range(1, number):
        fib.append(fib[i-1] + fib[i])
    fib.remove(0)

print(fib)



