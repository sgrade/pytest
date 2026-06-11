# 3558. Number of Ways to Assign Edge Weights I
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/


class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS level by level from the root (node 1) to find the max depth.
        seen = [False] * (n + 1)
        seen[1] = True
        level, max_depth = [1], 0
        while level:
            nxt = []
            for node in level:
                for child in adj[node]:
                    if not seen[child]:
                        seen[child] = True
                        nxt.append(child)
            if nxt:
                max_depth += 1
            level = nxt

        # Only parity matters: along the deepest path an odd number of
        # weight-1 edges makes the cost odd, giving 2^(max_depth-1) ways.
        return pow(2, max_depth - 1, self.MOD)
