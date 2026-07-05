# 1301. Number of Paths with Max Score
# https://leetcode.com/problems/number-of-paths-with-max-score/

MOD = 10**9 + 7


class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        # dp[r][c] = [best score, number of paths] from (r, c) to 'S'.
        # score of -1 marks an unreachable cell.
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]

        # Fold a reachable neighbor's result into cell (r, c).
        def relax(r, c, nr, nc):
            if nr >= n or nc >= n or dp[nr][nc][0] == -1:
                return
            score, paths = dp[nr][nc]
            if score > dp[r][c][0]:
                dp[r][c] = [score, paths]
            elif score == dp[r][c][0]:
                dp[r][c][1] += paths

        # Fill from 'S' (bottom-right) back toward 'E' (top-left).
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r, c) == (n - 1, n - 1) or board[r][c] == "X":
                    continue
                relax(r, c, r + 1, c)
                relax(r, c, r, c + 1)
                relax(r, c, r + 1, c + 1)
                # Add the current cell's digit ('E' counts as 0).
                if dp[r][c][0] != -1 and board[r][c] != "E":
                    dp[r][c][0] += int(board[r][c])

        best, paths = dp[0][0]
        return [best, paths % MOD] if best != -1 else [0, 0]
