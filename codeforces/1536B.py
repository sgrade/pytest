# B. Prinzessin der Verurteilung

from string import ascii_lowercase

alphabet = list(ascii_lowercase)

dp = list()
# See in editorial why 3 levels only
# Editorial - https://codeforces.com/blog/entry/91520
for ch1 in alphabet:
    dp.append(ch1)
    for ch2 in alphabet:
        dp.append(ch1 + ch2)
        for ch3 in alphabet:
            dp.append(ch1 + ch2 + ch3)
dp.sort(key=len)


for _ in range(int(input())):
    n = int(input())
    s = input()

    for el in dp:
        if el not in s:
            print(el)
            break
