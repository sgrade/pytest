# 3736. Minimum Moves to Equal Array Elements III
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mx = max(nums)
        ans = 0
        for num in nums:
            ans += mx - num
        return ans
