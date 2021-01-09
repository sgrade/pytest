# A. Okabe and Future Gadget Laboratory

n = int(input())
a = list()

for i in range(n):
    a.append(list(map(int, input().split())))

found_bad = False
for i in range(n):
    if found_bad:
        break

    for j in range(n):

        target = a[i][j]

        if found_bad:
            break

        if target != 1:
            row = a[i].copy()
            del row[j]

            column = list()
            for k in range(n):
                if k != i:
                    column.append(a[k][j])

            found_target = False
            for x in row:
                if found_target:
                    break
                for y in column:
                    if x + y == target:
                        found_target = True
                        break
            if not found_target:
                found_bad = True

print("Yes" if not found_bad else "No")
