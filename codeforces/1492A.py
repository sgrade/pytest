# A. Three swimmers

p = 0


def check(x):
    return ((p + x - 1) // x) * x - p


for _ in range(int(input())):
    p, a, b, c = map(int, input().split())

    a = check(a)
    b = check(b)
    c = check(c)

    print(min([a, b, c]))
