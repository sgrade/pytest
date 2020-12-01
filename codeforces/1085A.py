# A. Right-Left Cipher

s = input()
mid = len(s) // 2
if len(s) % 2 == 0:
    mid -= 1

ans = [s[mid]]
rng = 1
while True:
    try:
        ans.append(s[mid + rng])
        if mid - rng >= 0:
            ans.append(s[mid - rng])
        rng += 1
    except IndexError:
        break

print(''.join(ans))
