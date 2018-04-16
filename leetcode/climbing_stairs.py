# https://leetcode.com/problems/climbing-stairs/description/

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Solution - https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
        # It can be optimized: more advanced versions are at the same place


        # "The expression is actually the expression for Fibonacci numbers, but there is one thing to notice,
        # the value of ways(n) is equal to fibonacci(n+1)."
        # "Recursive program to find n'th fibonacci number"
        """
        # TIME LIMIT EXCEEDED
        def fib(x):
            if x <= 1:
                return x
            return fib(x-1) + fib(x-2)

        # returns no. of ways to reach s'th stair
        return fib(n+1)
        """

        """
        # Optimized, but still TIME LIMIT EXCEEDED
        def count_ways_until(x, m):
            if x <= 1:
                return x
            res = 0
            i = 1
            while i <= m and i <= x:
                res = res + count_ways_until(x-i, m)
                i = i + 1
            return res

        return count_ways_until(n+1, 2)
        """

        # Optimized #2
        # The time complexity of above solution is exponential. It can be optimized to O(mn) by using dynamic
        # programming. Following is dynamic programming based solution. We build a table res[] in bottom up manner.
        def count_ways_until(x, m):
            res = [0 for x in range(x)]  # Creates list res with all elements 0
            res[0], res[1] = 1, 1

            for i in range(2, x):
                # print('Outer cycle (for)')
                j = 1
                while j <= m and j <= i:
                    # print('Inner cycle (while)')
                    # print('i', i, 'j', j, 'res[i]', res[i])
                    res[i] = res[i] + res[i-j]
                    j = j+1

            return res[x-1]

        return count_ways_until(n+1, 2)


sol = Solution()
inp = 4
print(sol.climbStairs(inp))