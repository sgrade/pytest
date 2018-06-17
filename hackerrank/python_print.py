# https://www.hackerrank.com/challenges/python-print/problem


def py_print(inp):
    i = 1
    while i <= inp:
        print(i, end="")
        i += 1


if __name__ == '__main__':
    n = int(input())
    py_print(n)