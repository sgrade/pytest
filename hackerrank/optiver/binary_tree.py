# Enter your code here. Read input from STDIN. Print output to STDOUT

class Error(Exception):
    """Base class for exceptions"""
    pass

class E1(Error):
    # print("Invalid Input Format")
    pass


class E2(Error):
    # print("Duplicate Pair")
    pass


class E3(Error):
    # print("Parent Has More than Two Children")
    pass


class E4(Error):
    # print("Tree Contains Cycle")
    pass


class E5(Error):
    # print("Multiple Roots")
    pass


def check_input(inp):

    inp_list = inp.split(' ')

    input_is_valid = True
    for element in inp_list:
        if len(element) != 5:
            input_is_valid = False
        elif element[0] != '(' or element[-1] != ')':
            input_is_valid = False
        elif not element[1].isalpha() or not element[-2].isalpha():
            input_is_valid = False
        elif not element[1].isupper() or not element[-2].isupper():
            input_is_valid = False

    return input_is_valid


def check_for_duplicates(inp):
    inp_list = inp.split(' ')
    inp_hash = list()
    for item in inp_list:
        if item in inp_hash:
            return True
        else:
            inp_hash.append(item)

# inp = '(B,D) (D,E) (A,B) (C,F) (E,G) (A,C) "\n"'
# (A,B) (B,C) (A,B) (A,C)
inp = input()

if check_input(inp):
    if check_for_duplicates(inp):
        print('E2')
    else:
        pass
else:
    print('E1')
