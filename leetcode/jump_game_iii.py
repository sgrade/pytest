# 1306. Jump Game III
# https://leetcode.com/problems/jump-game-iii/


# Based on Editorial's Approach: DFS
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            arr[start] = -arr[start]  # mark visited
            return self.canReach(arr, start + arr[start]) or self.canReach(
                arr, start - arr[start]
            )

        return False
