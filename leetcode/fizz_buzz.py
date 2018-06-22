# https://leetcode.com/problems/fizz-buzz/description/

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # Runtime: 60 ms
        # Your runtime beats 77.61 % of python3 submissions.

        output = list()

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append('FizzBuzz')
            elif i % 3 == 0:
                output.append('Fizz')
            elif i % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))

        return output


sol = Solution()
inp = 15
print(sol.fizzBuzz(inp))
