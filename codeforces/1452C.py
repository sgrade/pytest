# C. Two Brackets

for _ in range(int(input())):
    inp = input()
    ans = 0

    rnd = list()
    square = list()
    for ch in inp:
        if ch == '(':
            rnd.append(ch)
        elif ch == '[':
            square.append(ch)
        elif ch == ')' and len(rnd) != 0:
            rnd.pop()
            ans += 1
        elif ch == ']' and len(square) != 0:
            square.pop()
            ans += 1
    print(ans)
