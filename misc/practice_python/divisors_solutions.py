

# First variant with user input
def get_divisor_from_user_input():
    number = int(input('number: '))
    divisor_list = list()
    numbers = list(range(1, number+1))
    for candidate in numbers:
        if number % candidate == 0:
            divisor_list.append(candidate)
    return divisor_list


# Second variant
def get_divisor_list(number):
    numbers = list(range(1, number + 1))
    l = [divisor for divisor in numbers if number % divisor == 0]
    return l


# 1.
#d = get_divisor_from_user_input()
#print(d)


# 2.
# print(get_divisor_list(40))