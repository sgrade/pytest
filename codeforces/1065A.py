# A. Vasya and Chocolate

for _ in range(int(input())):
    s, a, b, c = map(int, input().split())
    buy = s // c
    get_for_free = (buy // a) * b
    print(buy + get_for_free)
