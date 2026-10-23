# 3644. Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/


# Based on the Editorial's Approach: Traverse and Compute the Bitwise AND
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            ans &= nums[i]
        return 0 if ans == -1 else ans
