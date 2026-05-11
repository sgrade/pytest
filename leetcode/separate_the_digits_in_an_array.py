# 2553. Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/


class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans: list[int] = []
        for num in nums:
            start = len(ans)
            while num:
                ans.append(num % 10)
                num //= 10
            ans[start:] = ans[start:][::-1]  # reverse digits to restore order
        return ans
