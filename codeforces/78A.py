# A. Haiku

syl = ["a", "e", "i", "o", "u"]

ans = True
for i in range(3):
    line = input()
    syl_in_line = 0
    for ch in syl:
        syl_in_line += line.count(ch)
    if i == 0 or i == 2:
        if syl_in_line != 5:
            ans = False
    elif i == 1:
        if syl_in_line != 7:
            ans = False

print("YES" if ans else "NO")
