# 3488. Closest Equal Element Queries
# https://leetcode.com/problems/closest-equal-element-queries/


# Based on Editorial's Approach 2: Preprocessing Nearest Left and Right
class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        # Nearest same-value index to the left/right (circular).
        left = [0] * n
        right = [0] * n
        pos: dict[int, int] = {}

        # Sweep left → right over two copies to handle wrap-around.
        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i], -n)
            pos[nums[(i + n) % n]] = i

        pos.clear()
        # Sweep right → left.
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i], 2 * n)
            pos[nums[i % n]] = i

        # Answer each query using the precomputed nearest distances.
        for i, x in enumerate(queries):
            dist = min(x - left[x], right[x] - x)
            queries[i] = -1 if dist == n else dist

        return queries
