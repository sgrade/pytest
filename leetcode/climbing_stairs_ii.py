# 3693. Climbing Stairs II
# https://leetcode.com/problems/climbing-stairs-ii/


# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        # Min total cost to reach the last 3 steps (3, 2 and 1 steps back).
        # Positions before step 0 are seeded with 0: they are never better
        # than step 0 itself, since jumping from step 0 is always cheaper.
        three_back = two_back = one_back = 0
        for cost in costs:
            # Jumping k steps costs k^2, plus the cost of the landing step.
            curr = min(three_back + 9, two_back + 4, one_back + 1) + cost
            three_back, two_back, one_back = two_back, one_back, curr
        return one_back
