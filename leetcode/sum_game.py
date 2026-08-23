# 1927. Sum Game
# https://leetcode.com/problems/sum-game/


# Based on Editorial's Approach: Guess + Mathematical Induction Verification
class Solution:
    def sumGame(self, num: str) -> bool:
        def half_score(half: str) -> tuple[int, int]:
            digit_sum = blanks = 0
            for char in half:
                if char == "?":
                    blanks += 1
                else:
                    digit_sum += int(char)
            return digit_sum, blanks

        mid = len(num) // 2
        left_sum, left_blanks = half_score(num[:mid])
        right_sum, right_blanks = half_score(num[mid:])

        # Odd blanks: Alice has a last unmatched move and can unbalance.
        # Even blanks: Bob can force a tie iff the 4.5-per-blank balance
        # point already equalizes the two halves.
        odd_blanks = (left_blanks + right_blanks) % 2 == 1
        bob_can_tie = (
            left_sum - right_sum == (right_blanks - left_blanks) * 9 // 2
        )
        return odd_blanks or not bob_can_tie
