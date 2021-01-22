# A. Wizard of Orz

for _ in range(int(input())):
    n = int(input())
    output = list()
    output.append(9)

    # Editorial - https://codeforces.com/blog/entry/86566
    if n >= 2:
        output.append(8)
        if n > 2:
            n -= 2
            i = 9
            while n > 0:
                output.append(i)
                i += 1
                if i == 10:
                    i = 0
                n -= 1
    print(''.join([str(x) for x in output]))
