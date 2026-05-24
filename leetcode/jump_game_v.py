# 1340. Jump Game V
# https://leetcode.com/problems/jump-game-v/


# Based on Editorial's Approach: Memoization Search
class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        # visited[pos] = max indices reachable starting at pos.
        visited = {}

        def dfs(pos):
            if pos in visited:
                return
            visited[pos] = 1
            # Explore both directions; stop on out-of-range, distance > d,
            # or a height we can't jump down to.
            for step in (-1, 1):
                i = pos + step
                while 0 <= i < n and abs(i - pos) <= d and arr[i] < arr[pos]:
                    dfs(i)
                    # +1 counts pos itself prepended to i's chain.
                    visited[pos] = max(visited[pos], visited[i] + 1)
                    i += step

        for i in range(n):
            dfs(i)

        return max(visited.values())
