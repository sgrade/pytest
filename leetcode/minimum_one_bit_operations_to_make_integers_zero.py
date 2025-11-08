# 1611. Minimum One Bit Operations to Make Integers Zero
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

# Based on Editorial's Approach 3: Gray Code
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans
