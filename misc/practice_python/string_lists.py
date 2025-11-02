# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

s = str(input('String: '))
if s.lower() == s[::-1].lower():
    print('Yes')
else:
    print('no')

