# A. Ehab and another construction problem

x = int(input())
found = False
for b in range(x, 0, -1):
    if not found:
        for a in range(b, 0, -1):
            if b % a == 0 and a / b < x < a * b:
                print(a, b)
                found = True
                break
if not found:
    print(-1)
