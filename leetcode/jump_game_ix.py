# 3660. Jump Game IX
# https://leetcode.com/problems/jump-game-ix/


# Based on Editorial's Approach 2: Monotonic Stack
class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        # Keep a non-decreasing stack of (max_value, left_index) per segment.
        # When nums[i] is smaller than the top, the popped segment can reach
        # i (and vice versa), so merge it and carry the running max value.
        stack = []
        for i, x in enumerate(nums):
            curr_val = x
            curr_left = i
            while stack and stack[-1][0] > x:
                top_val, top_left = stack.pop()
                curr_val = max(curr_val, top_val)
                curr_left = top_left
            stack.append((curr_val, curr_left))

        # Segments partition [0, n): segment k spans [left_k, left_{k+1}).
        n = len(nums)
        ans = [0] * n
        for k, (val, left) in enumerate(stack):
            right = stack[k + 1][1] if k + 1 < len(stack) else n
            for j in range(left, right):
                ans[j] = val
        return ans
