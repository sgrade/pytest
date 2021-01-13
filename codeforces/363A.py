# A. Soroban

n = input()

output = list()

for c in n[::-1]:
    x = int(c)
    line = list()
    if x >= 5:
        line += ['-', 'O']
        x -= 5
    else:
        line += ['O', '-']
    line.append("|")
    while x > 0:
        line.append('O')
        x -= 1
    line.append('-')
    line += ['O'] * (8 - len(line))
    output.append(''.join(line))

print('\n'.join(output))
