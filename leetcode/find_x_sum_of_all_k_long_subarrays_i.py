# 3318. Find X-Sum of All K-Long Subarrays I
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        ans = []
        cntr = Counter(nums[: k - 1])
        for i in range(k - 1, n):
            cntr[nums[i]] += 1
            # Sort by count desc, then num desc to handle ties
            sorted_items = sorted(
                cntr.items(), key=lambda item: (item[1], item[0]), reverse=True
            )
            most_common = sorted_items[:x]
            sm = sum(num * cnt for num, cnt in most_common)
            ans.append(sm)
            if cntr[nums[i - k + 1]] == 1:
                del cntr[nums[i - k + 1]]
            else:
                cntr[nums[i - k + 1]] -= 1
        return ans
