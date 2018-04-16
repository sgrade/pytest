# https://leetcode.com/problems/sqrtx/description/

"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
"""


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # https://stackoverflow.com/questions/3581528/how-is-the-square-root-function-implemented
        # Given x>0, find y such that y^2=x => y=x/y (this is the key step).

        lo, hi, mid = 0, x, 0
        i = 0

        while True:
            mid = (lo + hi) / 2
            #print(mid)
            if int(mid * mid) > x:
                hi = mid
            elif int(mid * mid) < x:
                lo = mid
            else:
                #print('FOUND', mid)
                return int(mid)

            i += 1
            if i > 100:
                break


        """
        # The below works, but time limit exceeded
        
        i = 0
        while True:
            if i*i >= x:
                return i
            else:
                if (i+1)*(i+1) > x:
                    return i
                else:
                    i += 1
        """

sol = Solution()
print(sol.mySqrt(8))
#print(sol.mySqrt(1594052380))

