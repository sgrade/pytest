# A. Rounding

n_str = input()
n = int(n_str)
last = int(n_str[-1])
if last == 0:
    print(n_str)
else:
    if last < 5:
        print(n - last)
    else:
        print(n + (10-last))
