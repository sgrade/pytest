# A. Little Pony and Crystal Mine

n = int(input())

num_of_d = -1
for i in range(1, n+1):
    if i <= (n + 2 - 1) // 2:
        num_of_d += 2
    else:
        num_of_d -= 2
    stars = (n - num_of_d) // 2
    print(''.join([stars * '*', num_of_d * 'D', stars * '*']))
