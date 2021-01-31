# A. Number of Apartments

for _ in range(int(input())):
    n = int(input())

    # Based on https://codeforces.com/contest/1430/submission/95634988
    if n in [1, 2, 4]:
        print(-1)
    elif n % 3 == 0:
        print(n // 3, '0', '0')
    elif n % 3 == 1:
        print(n // 3 - 2, '0', '1')
    # n % 3 == 2
    else:
        print(n // 3 - 1, '1', '0')
