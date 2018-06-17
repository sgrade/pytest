# https://www.hackerrank.com/challenges/designer-door-mat/problem

# https://github.com/vinsonlee/hackerrank/blob/master/python/designer-door-mat/designer-door-mat.py

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))


