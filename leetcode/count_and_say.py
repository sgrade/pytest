# https://leetcode.com/problems/count-and-say/description/

"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def count_say_once(inp):
            # starting from reading off 1 (one 1)
            to_read = str(inp)
            # initialize a list of read off integers
            counted = []

            # internal structure to read off one integer
            # initialize counter
            count = 1
            # if I don't initialize i, the very last counted.append complains the i can be referenced before assignment
            i = 0
            for i in range(1, len(to_read)):
                # print('i:', i)
                # if an integer occurs again, we increase the counter
                if to_read[i - 1] == to_read[i]:
                    count += 1
                    # print('count: ', count)
                # if we find a different integer, write the number of the integer occurrences (count)
                # and the integer itself, then and reset the counter
                else:
                    # print('count:', count)
                    counted.append(str(count) + to_read[i - 1])
                    count = 1
                # print('counted:', counted)
            # the very last counter.append - required to count the last (i) element.
            # The one in the if/else counts (i-1) element
            counted.append(str(count) + to_read[i])
            inner_function_output = "".join(counted)
            return inner_function_output

        # Recursively going to the nth term of the count-and-say sequence
        j = 1
        output = "1"
        while j != n:
            output = count_say_once(output)
            j += 1

        return output


x = Solution()
print(type(x.countAndSay(1)))
print(type(x.countAndSay(2)))
#print(x.countAndSay(inp3))
#print(x.countAndSay(6))
#print(x.countAndSay(inp5))
