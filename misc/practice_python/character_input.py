# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
years_to_100 = 100 - age

now = datetime.datetime.now()
year_of_100_anniversary = int(now.year) + years_to_100

multiplier = int(input('How many times should I repeat: '))


print(multiplier * ('\n{0}, you will turn 100 years in {1}'.format(name, year_of_100_anniversary)))
