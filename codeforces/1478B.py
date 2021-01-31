# B. Nezzar and Lucky Number

for _ in range(int(input())):
    q, d = map(int, input().split())
    a = list(map(int, input().split()))

    # Key ideas - https://codeforces.com/contest/1478/submission/105769747
    for num in a:
        if num > 10 * d:
            print('YES')
            continue

        while str(d) not in str(num):
            num -= d

        if num >= 0:
            print('YES')
        else:
            print('NO')
