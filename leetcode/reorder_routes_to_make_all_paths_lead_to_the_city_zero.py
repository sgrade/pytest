# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/


# Based on Editorial's Approach 1: Depth First Search
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # Bidirectional graph: 1 if the original road points this way.
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for src, dst in connections:
            adj[src].append((dst, 1))
            adj[dst].append((src, 0))

        def dfs(node: int, parent: int) -> int:
            # Count roads pointing away from 0 on the unique path to 0.
            reorder = 0
            for neighbor, direction in adj[node]:
                if neighbor == parent:
                    continue
                reorder += direction + dfs(neighbor, node)
            return reorder

        return dfs(0, -1)
