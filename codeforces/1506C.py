# C. Double-ended Strings

for _ in range(int(input())):
    a = input()
    b = input()

    ans = len(a) + len(b)
    for i in range(1, min(len(a), len(b)) * 2):
        l = 0
        while l + i <= len(a):
            tmp = a[l: l+i]
            if b.find(tmp) != -1:
                candidate = len(a) + len(b) - len(tmp) * 2
                ans = min(ans, candidate)
            l += 1

    print(ans)
