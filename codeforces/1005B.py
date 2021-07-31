# B. Delete from the Left

s = input()
t = input()

common = 0
i = len(s)
j = len(t)

while (i > 0 and j > 0) and s[i-1] == t[j-1]:
    i -= 1
    j -= 1

print(i + j)
