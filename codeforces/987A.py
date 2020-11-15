# A. Infinity Gauntlet

colors = {
    'purple': 'Power',
    'green': 'Time',
    'blue': 'Space',
    'orange': 'Soul',
    'red': 'Reality',
    'yellow': 'Mind'
}

n = int(input())

present = list()
for _ in range(n):
    present.append(input())

ans = list()
for color in colors.keys():
    if color not in present:
        ans.append(colors[color])

print(len(ans))
print('\n'.join(ans))
