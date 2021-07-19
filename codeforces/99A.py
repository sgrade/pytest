# A. Help Far Away Kingdom

int_part, frac_part = input().split('.')

if int_part.endswith('9'):
    print("GOTO Vasilisa.")

else:
    first = int(frac_part[0])
    if first < 5:
        print(int_part)
    else:
        print(int_part[:-1], end="")
        print(int(int_part[-1]) + 1)
