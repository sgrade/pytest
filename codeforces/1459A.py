# A. Red-Blue Shuffle

for _ in range(int(input())):
    n = int(input())
    r = input()
    b = input()

    rans = 0
    bans = 0
    for i in range(n):
        if r[i] > b[i]:
            rans += 1
        elif r[i] < b[i]:
            bans += 1

    if rans > bans:
        print("RED")
    elif rans < bans:
        print("BLUE")
    else:
        print("EQUAL")
