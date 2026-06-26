# 3739. Count Subarrays With Majority Element II
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/


# Based on Editorial's Approach: Prefix Sum
class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # balance = (#target - #others) in a prefix; target is the majority of
        # subarray (j, i] iff balance[i] > balance[j]. So for each i we count
        # earlier prefixes with a strictly smaller balance.
        #
        # pre: histogram of seen prefix balances (offset by n so index >= 0).
        # balance: current balance (offset by n). presum: number of earlier
        # prefixes whose balance is strictly below balance.
        pre = [0] * (2 * n + 1)
        balance = n
        pre[balance] = 1  # empty prefix, balance 0
        ans = presum = 0
        for num in nums:
            if num == target:
                # old-balance prefixes are now below balance
                presum += pre[balance]
                balance += 1
            else:
                balance -= 1
                # prefixes at new balance no longer count
                presum -= pre[balance]
            pre[balance] += 1
            ans += presum
        return ans
