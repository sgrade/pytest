# 3524. Find X Value of Array I
# https://leetcode.com/problems/find-x-value-of-array-i/

# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        # Subarrays ending at the previous index, counted by product % k.
        prev_counts = [0] * k

        for num in nums:
            curr_counts = [0] * k
            # New subarray that starts (and ends) at num.
            curr_counts[num % k] += 1
            for remainder, count in enumerate(prev_counts):
                # Extend each previous subarray by multiplying by num.
                curr_counts[(remainder * num) % k] += count

            prev_counts = curr_counts
            for remainder, count in enumerate(curr_counts):
                ans[remainder] += count

        return ans
