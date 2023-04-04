# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev, prev = 1, 1
        for i in range (n - 1):
            prev_prev, prev = prev, prev + prev_prev
        return prev