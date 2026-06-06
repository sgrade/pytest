# 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/


class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        ans = []
        left_sum = 0
        for x in nums:
            # Sum to the right is everything except the left part and x itself.
            right_sum = total - left_sum - x
            ans.append(abs(left_sum - right_sum))
            left_sum += x
        return ans
