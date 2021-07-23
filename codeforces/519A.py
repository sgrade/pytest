# A. A and B and Chess

weights = {
    'q': 9,
    'r': 5,
    'b': 3,
    'n': 3,
    'p': 1,
    'k': 0
}

white, black = 0, 0

for _ in range(8):
    row = input()
    for ch in row:
        if ch != '.':
            current = weights[ch.lower()]
            if ch.islower():
                black += current
            else:
                white += current

if white > black:
    print("White")
elif black > white:
    print("Black")
else:
    print("Draw")
