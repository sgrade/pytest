# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar):
    #
    # Write your code here.
    #
    sum = 0
    for i in ar:
        sum += i
    return(sum)


ar = [1, 2, 3, 4, 10, 11]
print(simpleArraySum(ar))
