# https://leetcode.com/problems/count-primes/description/

"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # https://stackoverflow.com/questions/45395600/need-help-count-primes-using-python
        sieve = [True] * n

        if n > 0:
            sieve[0] = False
            if n > 1:
                sieve[1] = False

        # print(sieve)

        def mark_sieve(prime):
            for i in range(prime + prime, n, prime):
                sieve[i] = False

        for number in range(2, int(n ** 0.5) + 1):
            # print(number)
            # print(sieve[number])
            if sieve[number]:
                mark_sieve(number)

        return sum(sieve)


sol = Solution()
inp = 10
print(sol.countPrimes(inp))
