# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/


# Based on Editorial's Approach 1: Depth First Search
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append([connection[1], 1])
            adj[connection[1]].append([connection[0], 0])

        reorder = 0

        def dfs(node, parent):
            nonlocal reorder
            nonlocal adj
            for neighbor, direction in adj[node]:
                if neighbor != parent:
                    reorder += direction
                    dfs(neighbor, node)

        dfs(0, n)
        return reorder
