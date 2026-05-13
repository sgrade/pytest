# 1674. Minimum Moves to Make Array Complementary
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/


# Based on Editorial's Approach 1: Difference
class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo, hi = min(a, b), max(a, b)
            # cost drops from 2 to 1 on [lo+1, hi+limit]
            diff[lo + 1] -= 1
            diff[hi + limit + 1] += 1
            # cost drops further to 0 exactly at a+b
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        current = n              # baseline: 2 moves × n/2 pairs
        ans = n
        for t in range(2, 2 * limit + 1):
            current += diff[t]
            ans = min(ans, current)
        return ans
