# A. Letter

n, m = map(int, input().split())

left, right = 51, 0
top, bottom = 51, 0

a = list()

for i in range(n):
    s = input()
    a.append(s)

    tmp = s.find('*')
    if tmp != -1:
        left = min(left, tmp)
        right = max(right, s.rfind('*'))

        top = min(top, i)
        bottom = max(bottom, i)

for i in range(n):
    if top <= i <= bottom:
        print(a[i][left:right + 1])
