# 198. House Robber
# https:#leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums) -> int:
        prev, ans = 0, 0
        for num in nums:
            tmp = ans
            ans = max(ans, prev + num)
            prev = tmp
        return ans
