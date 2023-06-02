# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        prev_prev = 0
        prev = 1
        ans = 0
        for i in range(n - 1):
            ans = prev_prev + prev
            prev_prev = prev
            prev = ans
        return ans
