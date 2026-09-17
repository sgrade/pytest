# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/


# Based on Editorial's Approach 2: Sliding Window + Dynamic Programming
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i]: shortest valid subarray lying entirely in arr[:i].
        min_len = [n] * (n + 1)
        ans = n + 1  # Sentinel: no pair found yet.
        window_sum = 0
        left = 0

        for right, num in enumerate(arr):
            # Values are positive, so shrink while the window overshoots.
            window_sum += num
            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            min_len[right + 1] = min_len[right]
            if window_sum == target:
                length = right - left + 1
                # Pair this window with the best one ending before it.
                ans = min(ans, length + min_len[left])
                min_len[right + 1] = min(min_len[right], length)

        return -1 if ans == n + 1 else ans
