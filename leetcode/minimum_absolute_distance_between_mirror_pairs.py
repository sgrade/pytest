# Approach: One-time Traversal
# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/


class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        ans = len(nums)
        # Map each reversed number to its latest index.
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                ans = min(ans, i - seen[num])
            # Reverse digits of nums[i].
            cur_reversed = 0
            while nums[i]:
                cur_reversed = cur_reversed * 10 + nums[i] % 10
                nums[i] //= 10
            seen[cur_reversed] = i
        return -1 if ans == len(nums) else ans
