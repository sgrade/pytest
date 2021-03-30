# A. System Administrator

n = int(input())

a_reached = 0
a_total = 0
b_reached = 0
b_total = 0

for i in range(n):
    t, x, y = map(int, input().split())
    if t == 1:
        a_reached += x
        a_total += x + y
    else:
        b_reached += x
        b_total += x + y

print("LIVE" if a_reached * 2 >= a_total else "DEAD")
print("LIVE" if b_reached * 2 >= b_total else "DEAD")
