# 3568. Minimum Moves to Clean the Classroom
# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

from collections import deque


# Based on Editorial's Approach: Breadth-First Search
class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        litter_mask = [[0] * cols for _ in range(rows)]
        start_row = start_col = 0
        litter_count = 0

        # Assign a unique bitmask to each litter cell and locate the start.
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == "S":
                    start_row, start_col = r, c
                elif classroom[r][c] == "L":
                    litter_mask[r][c] = 1 << litter_count
                    litter_count += 1

        target_mask = (1 << litter_count) - 1
        # best_energy[r][c][mask] tracks the max remaining energy at each state.
        best_energy = [
            [[-1] * (1 << litter_count) for _ in range(cols)]
            for _ in range(rows)
        ]
        best_energy[start_row][start_col][0] = energy

        queue = deque([(start_row, start_col, 0, energy, 0)])

        while queue:
            r, c, mask, curr_energy, moves = queue.popleft()
            if mask == target_mask:
                return moves
            if curr_energy == 0:
                continue

            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and classroom[nr][nc] != "X"
                ):
                    next_energy = (
                        energy if classroom[nr][nc] == "R" else curr_energy - 1
                    )
                    next_mask = mask | litter_mask[nr][nc]
                    if next_energy > best_energy[nr][nc][next_mask]:
                        best_energy[nr][nc][next_mask] = next_energy
                        queue.append((
                            nr,
                            nc,
                            next_mask,
                            next_energy,
                            moves + 1,
                        ))

        return -1
