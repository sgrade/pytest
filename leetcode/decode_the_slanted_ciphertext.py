# 2075. Decode the Slanted Ciphertext
# https://leetcode.com/problems/decode-the-slanted-ciphertext/

# Based on https://leetcode.com/problems/decode-the-slanted-ciphertext/solutions/7770991/solution-of-the-day-0ms-runtime-9978-bea-2kyi
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        cols = len(encodedText) // rows
        res = []

        # Each diagonal starts at row 0, column c; follow it down-right.
        for c in range(cols):
            r, j = 0, c
            while r < rows and j < cols:
                res.append(encodedText[r * cols + j])
                r += 1
                j += 1

        return "".join(res).rstrip()
