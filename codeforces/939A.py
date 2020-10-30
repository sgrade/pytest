# A. Love Triangle

n = int(input())
lst = map(int, input().split())
lst = [i-1 for i in lst]

ans = False
first, second, third = [], [], []

for i in range(len(lst)):
    first = [i, lst[i]]
    second = [first[1], lst[first[1]]]
    third = [second[1], lst[second[1]]]
    if third[1] == first[0]:
        ans = True
        break

print('YES\n') if ans else print('NO\n')
