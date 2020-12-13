# A. Blackjack

n = int(input())

if n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 23, 24, 25]:
    print(0)
elif n == 20:
    print(15)
else:
    print(4)
