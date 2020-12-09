# A. Word Correction

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

n = int(input())
s = list(input())

stop = False
i = 0
while True:
    try:
        if s[i] in vowels:
            if s[i+1] in vowels:
                del(s[i+1])
            else:
                i += 2
        else:
            i += 1
    except IndexError:
        break

print(''.join(s))
