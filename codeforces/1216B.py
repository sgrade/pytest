# B. Shooting

n = int(input())
a = list(map(int, input().split()))

a_sorted = list(zip(a, range(n)))
a_sorted.sort(reverse=True)

sm = 0
x = 0
output = list()
for item in a_sorted:
    sm += item[0] * x + 1
    x += 1
    output.append(item[1] + 1)

print(sm)
print(*output)
