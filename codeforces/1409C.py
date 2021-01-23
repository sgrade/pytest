# C. Yet Another Array Restoration

def check(n, x, y, diff):
    candidate = y - diff
    output = [y]
    while candidate > 0 and len(output) < n:
        output.append(candidate)
        candidate -= diff

    candidate = y + diff
    while len(output) < n:
        output.append(candidate)
        candidate += diff

    output.sort()

    return output


for _ in range(int(input())):
    n, x, y = map(int, input().split())

    output = [x, y]

    if n > 2:
        diff = y - x
        output = check(n, x, y, diff)

        diff -= 1
        while diff >= ((y - x) + (n - 1) - 1) // (n - 1):
            if (y - x) % diff == 0:
                tmp = check(n, x, y, diff)
                if tmp[n-1] < output[n-1]:
                    output = tmp
            diff -= 1

    print(' '.join([str(x) for x in output]))
