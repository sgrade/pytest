# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

# Просто́е число́ (др.-греч. πρώτος ἀριθμός) — натуральное (целое положительное) число,
# имеющее ровно два различных натуральных делителя — единицу и самого себя


from .divisors_solutions import get_divisor_from_user_input

d = get_divisor_from_user_input()
if len(d) == 2:
    print('Prime')
else:
    print('Not prime')
