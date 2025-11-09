# 2169. Count Operations to Obtain Zero
# https://leetcode.com/problems/count-operations-to-obtain-zero/


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while True:
            if num1 == 0 or num2 == 0:
                break
            if num1 < num2:
                num1, num2 = num2, num1
            num1 -= num2
            ans += 1
        return ans
