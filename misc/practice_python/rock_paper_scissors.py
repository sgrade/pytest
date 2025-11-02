# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

while True:
    print('''\nPlease pick one:
                rock
                scissors
                paper
                ''')

    player1 = str(input('Player 1 choice: ')).lower()
    player2 = str(input('Player 2 choice: ')).lower()


    def check_inputs(inp):
        if inp == 'scissors' or inp == 'paper' or inp == 'rock':
            return True
        else:
            return False


    def who_wins(inp1, inp2):
        if inp1 == inp2:
            return 0
        elif inp1 == 'rock' and inp2 == 'scissors':
            return 1
        elif inp1 == 'scissors' and inp2 == 'rock':
            return 2
        elif inp1 == 'scissors' and inp2 == 'paper':
            return 1
        elif inp1 == 'paper' and inp2 == 'scissors':
            return 2
        elif inp1 == 'paper' and inp2 == 'rock':
            return 1
        elif inp1 == 'rock' and inp2 == 'paper':
            return 2


    def printing(number):
        if number == 0:
            print("It's a tie!")
        else:
            print('Player {0} wins. Congrats!'.format(number))


    player1_input = check_inputs(player1)
    player2_input = check_inputs(player2)

    if player1_input and player2_input:
        winner_number = who_wins(player1, player2)
        printing(winner_number)
    else:
        print('Wrong input')

    round_check = str(input('Do you want to continue y/n?'))
    if round_check == 'n':
        break
