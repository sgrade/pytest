# A. Find Square

n, m = map(int, input().split())

for i in range(n):
    s = input()
    left = s.find('B')
    if left != -1:
        right = s.rfind('B')
        c = (right - left) // 2 + 1
        print(i + c, left + c)
        break
