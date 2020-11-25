# A. Special Permutation

for _ in range(int(input())):
    n = int(input())
    lst = list()
    lst.append(str(n))
    lst += [str(x) for x in range(1, n)]
    print(' '.join(lst))
