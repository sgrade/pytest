# 800. Similar RGB Color
# https://leetcode.com/problems/similar-rgb-color/


# Based on Editorial's Approach 2: Rounding
class Solution:
    def similarRGB(self, color: str) -> str:
        def closest_channel(hex_code: str) -> str:
            # Shorthand channels "XX" correspond to multiples of 17 (0x11 = 17).
            # Rounding to the nearest multiple of 17 minimizes squared error.
            digit = round(int(hex_code, 16) / 17)
            return f"{digit:x}" * 2

        return "#" + "".join(
            closest_channel(color[i : i + 2]) for i in range(1, 6, 2)
        )
