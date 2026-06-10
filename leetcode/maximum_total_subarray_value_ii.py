# 3691. Maximum Total Subarray Value II
# https://leetcode.com/problems/maximum-total-subarray-value-ii/

import heapq


# Based on Editorial's Approach 1: Sparse Table + Max Heap
class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Sparse tables: st_max[j][i] / st_min[j][i] cover nums[i : i + 2**j].
        st_max = [list(nums)]
        st_min = [list(nums)]
        for j in range(1, n.bit_length()):
            step = 1 << (j - 1)
            prev_max, prev_min = st_max[-1], st_min[-1]
            st_max.append([
                max(prev_max[i], prev_max[i + step])
                for i in range(n - (1 << j) + 1)
            ])
            st_min.append([
                min(prev_min[i], prev_min[i + step])
                for i in range(n - (1 << j) + 1)
            ])

        # Value (max - min) of nums[left..r] via two
        # overlapping power-of-two ranges.
        def value(left: int, r: int) -> int:
            j = (r - left + 1).bit_length() - 1
            hi = max(st_max[j][left], st_max[j][r - (1 << j) + 1])
            lo = min(st_min[j][left], st_min[j][r - (1 << j) + 1])
            return hi - lo

        # For each left left the widest window nums[left..n-1] gives
        # its largest value;
        # repeatedly pop the best and push its next-shorter window to get top k.
        pq = [(-value(left, n - 1), left, n - 1) for left in range(n)]
        heapq.heapify(pq)
        ans = 0
        for _ in range(k):
            neg_val, left, r = heapq.heappop(pq)
            ans -= neg_val
            if r > left:
                heapq.heappush(pq, (-value(left, r - 1), left, r - 1))
        return ans
