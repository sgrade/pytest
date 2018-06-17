# https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):
    leap = False

    # Write your logic here
    if 1900 <= year <= 100000:
        if year % 4 == 0 and year % 100 != 0:
            leap = True
        if year % 100 == 0 and year % 400 == 0:
            leap = True

    return leap


# year = int(input())
year = 2000
print(is_leap(year))    # expected True
year = 2400
print(is_leap(year))    # expected True
year = 1992
print(is_leap(year))    # expected True
print()

year = 1800
print(is_leap(year))    # expected False
year = 1900
print(is_leap(year))    # expected False
year = 2100
print(is_leap(year))    # expected False
year = 2200
print(is_leap(year))    # expected False
year = 2300
print(is_leap(year))    # expected False
year = 2500
print(is_leap(year))    # expected False
