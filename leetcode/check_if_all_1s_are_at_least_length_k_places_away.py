# 1437. Check If All 1's Are at Least Length K Places Away
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = nums.index(1) if 1 in nums else -1
        for cur in range(prev + 1, len(nums)):
            if nums[cur] == 1:
                dist = cur - prev - 1
                if dist < k:
                    return False
                prev = cur
        return True
