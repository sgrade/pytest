#!/usr/bin/env python

# https://realpython.com/python-practice-problems/

from string import ascii_lowercase

def caesar(s, n = 0):
    output = list()
    for ch in s:
        try:
            idx = (ascii_lowercase.index(ch) + n) % 26
            output.append(ascii_lowercase[idx])
        except:
            output.append(ch)
    return ''.join(output)

print(caesar("abcd xyz", 4))
