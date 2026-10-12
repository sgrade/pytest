# 2897. Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/


# Based on Editorial's Approach: Greedy
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        # The operations only move bits between numbers, so all that matters
        # is how many numbers have each bit set.
        cnt = [sum(num >> i & 1 for num in nums) for i in range(30)]

        ans = 0
        # Greedily build the k largest numbers: each takes one of every
        # still-available bit.
        for _ in range(k):
            cur = 0
            for i in range(30):
                if cnt[i]:
                    cur |= 1 << i
                    cnt[i] -= 1
            ans = (ans + cur * cur) % mod
        return ans
