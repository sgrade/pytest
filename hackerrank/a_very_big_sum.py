# https://www.hackerrank.com/challenges/a-very-big-sum/problem


def aVeryBigSum(n, ar):
    #
    # Write your code here.
    #
    i, sum = 0, 0
    while i < n:
        sum += ar[i]
        i += 1
    return sum


inp = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(5, inp))
