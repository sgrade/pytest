# A. Find Extra One

cnt_positive = 0
cnt_negative = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > 0:
        cnt_positive += 1
    elif x < 0:
        cnt_negative += 1

if (cnt_positive == 0 or cnt_positive == 1) or \
        (cnt_negative == 0 or cnt_negative == 1):
    print('Yes')
else:
    print('No')
