# 2574. Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/


class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        left_sum = 0
        for i in range(1, n):
            left_sum += nums[i - 1]
            ans[i] = left_sum
        right_sum = 0
        for i in range(n - 2, -1, -1):
            right_sum += nums[i + 1]
            ans[i] = abs(ans[i] - right_sum)
        return ans
