# 3414. Maximum Score of Non-overlapping Intervals
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/


from bisect import bisect_left


# Based on Editorial's Approach: Dynamic Programming + Binary Search
class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        # Sort by right endpoint, keeping the original index for the answer.
        arr = sorted(
            (right, left, weight, i)
            for i, (left, right, weight) in enumerate(intervals)
        )

        # dp[i][j] = (best weight, chosen indices) for the first i intervals
        # picking at most j of them.
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i, (_, left, weight, idx) in enumerate(arr):
            # Intervals before k end before left, so they stay disjoint.
            k = bisect_left(arr, (left,), hi=i)
            for j in range(1, 5):
                skip_weight, skip_indices = dp[i][j]
                take_weight, take_indices = dp[k][j - 1]
                take = (take_weight + weight, sorted(take_indices + [idx]))
                # Maximize the weight, breaking ties lexicographically.
                better = take[0] > skip_weight or (
                    take[0] == skip_weight and take[1] < skip_indices
                )
                dp[i + 1][j] = take if better else dp[i][j]

        return dp[n][4][1]
