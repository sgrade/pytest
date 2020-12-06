# A. Vladik and Courtesy

a, b = map(int, input().split())

vladik = True
i = 1
while a > -1 and b > -1:
    if vladik:
        a -= i
    else:
        b -= i
    i += 1
    vladik = not vladik

if vladik:
    print("Valera")
else:
    print("Vladik")
