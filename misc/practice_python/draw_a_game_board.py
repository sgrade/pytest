# http://www.practicepython.org/solution/2015/11/01/24-draw-a-game-board-solutions.html


def print_horizontal(dimension):
    print(' ---' * dimension)


def print_vertical(dimension):
    print('|   ' * (dimension + 1))


def main():
    dimension = int(input('Please provide game size: '))
    for index in range(dimension):
        print_horizontal(dimension)
        print_vertical(dimension)
    print_horizontal(dimension)


if __name__ == '__main__':
    main()