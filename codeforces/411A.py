# A. Password Check

from string import ascii_lowercase
from string import ascii_uppercase

ans = False

s = input()

is_len = True if len(s) >= 5 else False

if is_len:
    is_lower = False
    is_upper = False
    is_digit = False

    for ch in s:
        if ch.lower() and ch in ascii_lowercase:
            is_lower = True
        if ch.upper() and ch in ascii_uppercase:
            is_upper = True
        if ch.isdigit():
            is_digit = True

    if is_lower and is_upper and is_digit:
        ans = True

if ans:
    print("Correct")
else:
    print("Too weak")
