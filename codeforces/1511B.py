# B. GCD Length

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    # Very elegant solution is given in the editorial - not even sure what I can optimize
    # https://codeforces.com/blog/entry/89634

    x = ("1" + "0" * (a - 1))
    y = ("1" * (b - c + 1) + "0" * (c - 1))
    print(x, y)
