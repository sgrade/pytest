# C. Divisibility by Eight

s = input()

ans = False

# Editorial - https://codeforces.com/blog/entry/18329
tmp = 0
output = ""
while not ans and tmp < 1000:
    output = str(tmp)
    idx = 0
    offset = 0
    for i in range(len(output)):
        try:
            idx = s.index(output[i], offset)
            offset = idx + 1
        except ValueError:
            break
    else:
        ans = True
    tmp += 8

print("YES\n" + output if ans else "NO")
