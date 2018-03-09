# https://coderbyte.com/editor/guest:First%20Factorial:Python


def FirstFactorial(num):

    # code goes here
    fact = 1
    #print(fact)
    for number in range(1, num+1):
        fact = fact * number
        print(number)
    return fact

# keep this function call here
print(FirstFactorial(int(input())))
