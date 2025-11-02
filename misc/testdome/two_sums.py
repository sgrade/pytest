"""
Write a function that, given a list and a target sum, returns zero-based indices of any two
distinct elements whose sum is equal to the target sum. If there are no such elements,
the function should return (-1, -1).

For example, find_two_sum([1, 3, 5, 7, 9], 12) should return a tuple containing any of the following pairs of indices:

1 and 4 (3 + 9 = 12)
2 and 3 (5 + 7 = 12)
3 and 2 (7 + 5 = 12)
4 and 1 (9 + 3 = 12)
"""

class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """

        """
        # Do it with generators
        # It works, but only gets 25% marks (1 of 4 tests pass)
        def gen_tuple(num_list, target_s):
            for item in num_list:
                complement = target_s - item
                if complement in numbers:
                    target_t = (numbers.index(item), numbers.index(complement))
                    yield target_t
            yield (-1, -1)

        return next(gen_tuple(numbers, target_sum))
        """


        # Below works, but not perfect: 3 of 4 tests pass, only performance test fails
        '''for number in numbers:
            supplement = target_sum - number
            if supplement in numbers:
                index1 = numbers.index(number)
                if supplement != number:
                    index2 = numbers.index(supplement)
                    return index1, index2
                else:
                    if numbers.count(number) >= 2:
                        numbers.pop(index1)
                        index2 = (numbers.index(supplement))+1
                        return index1, index2
        else:
            return -1, -1
        '''

        # same - little performance
        # changed  but not finished
        """
        for index1 in range(len(numbers)):
            number = numbers[index1]
            supplement = target_sum - number
            for index2 in range(len(numbers)):
                return (index1, index2) if number and supplement in numbers
            if supplement in numbers:
                if supplement != number:
                    return index1, numbers.index(supplement)
                else:
                    if numbers.count(number) >= 2:
                        numbers.pop(index1)
                        index2 = (numbers.index(supplement)) + 1
                        return index1, index2
        else:
            return -1, -1
        """

print('First run')
print(TwoSum.find_two_sum([1, 3, 5, 7, 9], 12))
print('Second run')
print(TwoSum.find_two_sum([9, 2, 12, 100, 100], 200))
print('Third run')
print(TwoSum.find_two_sum([1, 23, 54, 97, 19, 12, 234, 23423, 67, 789, 23, 234, 23423, 666, 3], 669))
print('Fourth run')
print(TwoSum.find_two_sum([1, 3, 5, 7, 9], 120))
