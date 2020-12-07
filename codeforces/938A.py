# A. Word Correction
# NOT FINISHED

vowels = ['a', 'e', 'i', 'o', 'u']

n = int(input())
s = list(input())

stop = False
i = 0
while True:
    try:
        if s[i] in vowels:
            for j in range(i+1, len(s)):
                if s[j] in vowels:
                    del(s[j])
                    break
            else:
                i = n
        else:
            i += 1
    except IndexError:
        break

print(''.join(s))
