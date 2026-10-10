# 2333. Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/


# Based on Editorial's Approach 2: Binary Search on the Answer
class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        # Changing nums1[i] by +-1 or nums2[i] by +-1 is equivalent, so only
        # the absolute differences and the total number of operations matter.
        diffs = [abs(a - b) for a, b in zip(nums1, nums2, strict=True)]
        total_ops = k1 + k2

        if sum(diffs) <= total_ops:
            return 0

        def ops_to_cap(cap: int) -> int:
            # Operations needed to lower every difference to at most `cap`.
            return sum(d - cap for d in diffs if d > cap)

        # Binary search for the smallest cap reachable within total_ops.
        low, high = 0, max(diffs)
        while low < high:
            mid = (low + high) // 2
            if ops_to_cap(mid) <= total_ops:
                high = mid
            else:
                low = mid + 1
        cap = low

        # Leftover operations are fewer than the number of differences equal
        # to cap, so each one lowers a distinct difference from cap to cap - 1.
        leftover_ops = total_ops - ops_to_cap(cap)
        capped_squares = sum(min(d, cap) ** 2 for d in diffs)
        return capped_squares - leftover_ops * (2 * cap - 1)
