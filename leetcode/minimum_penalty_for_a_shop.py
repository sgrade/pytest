# 2483. Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/

# Based on Editorial's Approach 2: One Pass
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty, cur_penalty, closing_hour = 0, 0, 0
        for i, c in enumerate(customers):
            if c == "Y":
                cur_penalty -= 1
            else:
                cur_penalty += 1
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                closing_hour = i + 1
        return closing_hour
