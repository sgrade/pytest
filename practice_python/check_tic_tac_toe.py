# http://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]


def check_horizontal(matrix):
    for lst in matrix:
        if lst[0] == lst[1] == lst[2]:
            return lst[0]


def check_vertical(matrix):
    for n in range(0, len(matrix)-1):
        if matrix[0][n] == matrix[1][n] == matrix[2][n]:
            return matrix[0][n]


def check_diagonal(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2] or \
            matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[1][1]


def main(matrix):
    h = check_horizontal(matrix)
    v = check_vertical(matrix)
    d = check_diagonal(matrix)
    result = [h, v, d]
    for item in result:
        if item:
            print('Player {0} won. Congrats!'.format(item))
            break
    else:
        print('No winner')


main(winner_is_2)
main(winner_is_1)
main(winner_is_also_1)
main(no_winner)
main(also_no_winner)