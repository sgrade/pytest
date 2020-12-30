# A. Sleuth

vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

ch = input().strip(' ?')[-1]
if ch.upper() in vowels:
    print("YES")
elif ch.upper() in consonants:
    print("NO")
