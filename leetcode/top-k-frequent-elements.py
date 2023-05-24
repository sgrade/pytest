# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = [(-cnt, el) for el, cnt in counter.items()]
        heapq.heapify(heap)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans
