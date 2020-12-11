# A. String Generation

for _ in range(int(input())):
    n, k = map(int, input().split())

    source = ['a', 'b', 'c']

    ans = list()
    ans += source * (n // 3)
    i = n % 3
    ans += source[:i]

    print(''.join(ans))
