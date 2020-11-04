# A. Nauuo and Votes

x, y, z = map(int, input().split())
if x - y > z:
    print('+')
elif y - x > z:
    print('-')
elif x - y == 0 and z == 0:
    print('0')
else:
    print('?')
