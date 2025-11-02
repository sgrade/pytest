# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random


def guess():
    my_number = random.randint(1, 9)
    while True:
        user_input = input('Please a number in 1-9 range or type "quit" to quit: ')
        if str(user_input) == 'quit':
            break
        else:
            user_number = int(user_input)
            if user_number < 1 or user_number > 9:
                print('Wrong number!')
                continue
            elif user_number == my_number:
                print('Good job!')
                break
            elif user_number < my_number:
                print('too low')
            else:
                print('too high')


guess()