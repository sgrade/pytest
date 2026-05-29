# 3300. Minimum Element After Replacement With Digit Sum
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/


class Solution:
    def minElement(self, nums: list[int]) -> int:
        ans = 1000000
        for num in nums:
            sm = sum(int(digit) for digit in str(num))
            ans = min(ans, sm)
        return ans
