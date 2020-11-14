# A. New Year and Counting Cards

vowels = ['a', 'e', 'i', 'o', 'u']
even = ['0', '2', '4', '6', '8']
s = input()
ans = 0
for i in s:
    if i in vowels or (i.isdigit() and (i not in even)):
        ans += 1
print(ans)
