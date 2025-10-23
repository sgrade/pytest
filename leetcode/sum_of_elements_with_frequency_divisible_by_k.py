# 3712. Sum of Elements With Frequency Divisible by K
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

from collections import defaultdict
from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        ans = 0
        for num, cnt in counter.items():
            if cnt % k == 0:
                ans += num * cnt
        return ans
