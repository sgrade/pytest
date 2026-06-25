# 3737. Count Subarrays With Majority Element I
# https://leetcode.com/problems/count-subarrays-with-majority-element-i/


# Based on Editorial's Approach: Enumeration
class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        ans = 0
        # For each start i, extend the subarray and track a running balance:
        # +1 for target, -1 otherwise. target is the majority iff balance > 0.
        for i in range(len(nums)):
            balance = 0
            for j in range(i, len(nums)):
                balance += 1 if nums[j] == target else -1
                if balance > 0:
                    ans += 1
        return ans
