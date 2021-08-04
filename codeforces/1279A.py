# A. New Year Garland

for _ in range(int(input())):
    rgb = list(map(int, input().split()))
    rgb.sort()
    if (rgb[0] + rgb[1] >= rgb[2] - 1):
        print("Yes")
    else:
        print("No")
