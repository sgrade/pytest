# Enter your code here. Read input from STDIN. Print output to STDOUT

class Error(Exception):
    """Base class for exceptions"""
    pass


class E1(Error):
    pass


class E2(Error):
    pass


class E3(Error):
    pass


class E4(Error):
    pass


class E5(Error):
    pass


def check_input(inp):
    inp_list = inp.split(' ')
    for element in inp_list:
        print(type(element))
        if type(element) != tuple:
            raise E1('Invalid Input Format')


inp = '(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)'
check_input(inp)

"""
class Error(Exception):
    """Base class for exceptions"""
    pass


class E1(Error):
    print("Invalid Input Format")


class E2(Error):
    print("Duplicate Pair")


class E3(Error):
    print("Parent Has More than Two Children")


class E4(Error):
    print("Tree Contains Cycle")


class E5(Error):
    print("Multiple Roots")
"""